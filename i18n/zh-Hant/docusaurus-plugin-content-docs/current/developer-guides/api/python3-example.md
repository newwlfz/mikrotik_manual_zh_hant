---
sidebar_key: "developer-guides/api/python3-example"
sidebar_position: 1
title: "Python3 示例"
sidebar_label: "Python3 示例"
description: "本頁提供了一個 Python3 示例用戶端，用於透過 RouterOS 的 API 與其互動，演示 sentence 交換、明文和舊版挑戰-響應登入，以及透過 API 和 API-SSL 服務進行套接字通訊。"
tags:
  - 'api'
  - 'management'
source: https://manual.mikrotik.com/docs/developer-guides/api/python3-example
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

一個簡單的 Python3 API 用戶端。

- 用法：`api.py <ip-address> <username> <password> <secure(True|False)>`，
  例如：`api.py 10.0.0.1 admin Badpassword123 False`（空密碼也可以）
- 啟動指令碼後，逐行輸入 API 語句中的單詞，每行一個單詞；每輸入一個單詞後按 Enter
- 空行會終止該語句並將其傳送到路由器——在最後一個單詞後按 **兩次** Enter
- 在空行上按 `Ctrl-D` 退出
- 在輸出中，`<<<` 標記客戶端傳送的單詞，`>>>` 標記從路由器接收的單詞

用戶端首先嚐試 plain-text 登入方法。如果路由器用質詢（`=ret=`）來應答登入，用戶端則改為完成舊版 challenge-response 交換。secure 選項連線到 API-SSL 服務（埠 8729）；路由器必須為 api-ssl 服務配置證書，並且用戶端必須信任該證書（請參閱 [API 參考](./index.md)）。

對於舊版交換，空密碼和質詢 `93b438ec9b80057c06dd9fe67d56aa9a` 的響應是 `00e134102a9d330dd7b1849fedfea3cb57`——這對你自己的實現來說是一個有用的測試向量。

示例輸出：

```bash
$ ./api.py 10.0.0.1 admin '' False
<<< /login
<<< =name=admin
<<< =password=
<<<
>>> !done
>>>
/system/identity/print

<<< /system/identity/print
<<<
>>> !re
>>> =name=MyRouter
>>>
>>> !done
>>>
```

```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ApiRos:
    """Client for the RouterOS binary API protocol."""

    def __init__(self, sk):
        self.sk = sk

    def login(self, username, pwd):
        # Plain-text login method first.
        for repl, attrs in self.talk(
            ["/login", "=name=" + username, "=password=" + pwd]
        ):
            if repl == "!trap":
                return False
            if "=ret" in attrs:
                # The router asked for the legacy challenge-response method.
                return self._login_legacy(username, pwd, attrs["=ret"])
        return True

    def _login_legacy(self, username, pwd, challenge):
        # The response is the MD5 digest of 0x00, the password and the
        # received challenge, prefixed with "00".
        chal = binascii.unhexlify(challenge)
        md = hashlib.md5()
        md.update(b"\x00")
        md.update(pwd.encode("utf-8"))
        md.update(chal)
        response = "00" + binascii.hexlify(md.digest()).decode("ascii")
        for repl, _attrs in self.talk(
            ["/login", "=name=" + username, "=response=" + response]
        ):
            if repl == "!trap":
                return False
        return True

    def talk(self, words):
        if self.write_sentence(words) == 0:
            return
        replies = []
        while True:
            i = self.read_sentence()
            if len(i) == 0:
                continue
            reply = i[0]
            attrs = {}
            for w in i[1:]:
                j = w.find("=", 1)
                if j == -1:
                    attrs[w] = ""
                else:
                    attrs[w[:j]] = w[j + 1:]
            replies.append((reply, attrs))
            if reply == "!done":
                return replies

    def write_sentence(self, words):
        count = 0
        for w in words:
            self.write_word(w)
            count += 1
        self.write_word("")
        return count

    def read_sentence(self):
        words = []
        while True:
            w = self.read_word()
            if w == "":
                return words
            words.append(w)

    def write_word(self, w):
        print("<<< " + w, flush=True)
        data = w.encode("utf-8")
        self.write_len(len(data))
        self.write_bytes(data)

    def read_word(self):
        w = self.read_bytes(self.read_len()).decode("utf-8", "replace")
        print(">>> " + w, flush=True)
        return w

    def write_len(self, l):
        if l < 0x80:
            self.write_bytes(bytes([l]))
        elif l < 0x4000:
            l |= 0x8000
            self.write_bytes(l.to_bytes(2, "big"))
        elif l < 0x200000:
            l |= 0xC00000
            self.write_bytes(l.to_bytes(3, "big"))
        elif l < 0x10000000:
            l |= 0xE0000000
            self.write_bytes(l.to_bytes(4, "big"))
        else:
            self.write_bytes(bytes([0xF0]) + l.to_bytes(4, "big"))

    def read_len(self):
        c = self.read_bytes(1)[0]
        if (c & 0x80) == 0x00:
            return c
        if (c & 0xC0) == 0x80:
            return ((c & ~0xC0) << 8) + self.read_bytes(1)[0]
        if (c & 0xE0) == 0xC0:
            b = self.read_bytes(2)
            return ((c & ~0xE0) << 16) + (b[0] << 8) + b[1]
        if (c & 0xF0) == 0xE0:
            b = self.read_bytes(3)
            return ((c & ~0xF0) << 24) + (b[0] << 16) + (b[1] << 8) + b[2]
        if (c & 0xF8) == 0xF0:
            return int.from_bytes(self.read_bytes(4), "big")
        # Any other first byte is a reserved control byte; the stream cannot
        # be decoded further.
        raise RuntimeError("received reserved control byte 0x%02x" % c)

    def write_bytes(self, b):
        n = 0
        while n < len(b):
            r = self.sk.send(b[n:])
            if r == 0:
                raise RuntimeError("connection closed by remote end")
            n += r

    def read_bytes(self, length):
        data = b""
        while len(data) < length:
            s = self.sk.recv(length - len(data))
            if s == b"":
                raise RuntimeError("connection closed by remote end")
            data += s
        return data

def open_socket(dst, port, secure=False):
    res = socket.getaddrinfo(dst, port, socket.AF_UNSPEC, socket.SOCK_STREAM)
    af, socktype, proto, _canonname, sockaddr = res[0]
    skt = socket.socket(af, socktype, proto)
    if secure:
        # The router's api-ssl service needs a certificate, and the client
        # must trust it. The name used here must match the certificate; to
        # connect by IP address, the certificate needs a matching IP address
        # entry.
        context = ssl.create_default_context()
        s = context.wrap_socket(skt, server_hostname=dst)
    else:
        s = skt
    s.connect(sockaddr)
    return s

def main():
    dst = sys.argv[1]
    user = "admin"
    passw = ""
    secure = False

    if len(sys.argv) > 2:
        user = sys.argv[2]
    if len(sys.argv) > 3:
        passw = sys.argv[3]
    if len(sys.argv) > 4:
        secure = sys.argv[4].lower() == "true"

    port = 8729 if secure else 8728
    s = open_socket(dst, port, secure)
    apiros = ApiRos(s)

    if not apiros.login(user, passw):
        print("login failed")
        s.close()
        return

    inputsentence = []
    while True:
        r = select.select([s, sys.stdin], [], [], None)
        if s in r[0]:
            apiros.read_sentence()
        if sys.stdin in r[0]:
            line = sys.stdin.readline()
            # Ctrl-D (EOF) on an empty line quits the client.
            if line == "":
                if inputsentence:
                    apiros.write_sentence(inputsentence)
                break
            line = line.rstrip("\r\n")
            if line == "":
                apiros.write_sentence(inputsentence)
                inputsentence = []
            else:
                inputsentence.append(line)

    # Best effort: read out replies that are still pending before closing the
    # connection (a listen command may still have updates in flight).
    s.settimeout(0.5)
    try:
        while True:
            apiros.read_sentence()
    except socket.timeout:
        pass
    s.close()

if __name__ == "__main__":
    main()
```

## 從指令碼中使用用戶端 {#use-the-client-from-a-script}

上面的示例是互動式的。要將其用於指令碼，請直接使用用戶端類：

```python

from api import ApiRos, open_socket  # the client above, saved as api.py

s = open_socket("10.0.0.1", 8728)
api = ApiRos(s)
if not api.login("admin", "S3cret"):
    sys.exit("login failed")
for repl, attrs in api.talk(["/system/resource/print", "=.proplist=uptime,cpu-load"]):
    if repl == "!re":
        print(attrs)
s.close()
```

`talk()` 返回一個由 `(reply, attributes)` 對組成的列表，直到幷包括 `!done` 回覆。返回資料的命令（例如 `print` 和 `getall`）會為每個專案產生一個 `!re` 對；無資料的命令只產生 `!done` 對；沒有匹配項的 `print` 會產生一個 `!empty` 對。
