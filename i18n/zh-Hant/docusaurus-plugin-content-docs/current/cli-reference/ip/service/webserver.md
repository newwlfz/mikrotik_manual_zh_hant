---
sidebar_key: "cli-reference/ip/service/webserver"
sidebar_position: 1
title: "webserver"
sidebar_label: 'webserver'
source: https://manual.mikrotik.com/docs/cli-reference/ip/service/webserver
captured_at: '2026-11-09T11:35:47.715Z'
translated_at: "2026-11-11T16:56:16.529Z"
translation_provider: "opencode-go"
translation_model: "deepseek-v4.1-flash"
---

-----------

## ip/service/webserver {#ipservicewebserver}
**型別：** 設定目錄

用於分別針對 HTTP（即 `-plain` 相關設定，由 `www` 服務提供）和 HTTPS（即 `-secure` 相關設定，由 `www-ssl` 服務提供）開啟或關閉路由器 Web 伺服器的各個部分。所有部分預設均為啟用狀態。被停用的部分會返回 `403 Forbidden`，而其他部分仍可正常工作，因此你可以例如在 HTTPS 上提供 REST API 而不啟用 WebFig。Web 伺服器的埠、允許的地址和證書在 [`/ip/service`](./index.md) 中設定。有關 REST API 的資訊，請參閱 [REST API](../../../developer-guides/rest-api.md)。

<ArgTable c1="引數" c2="型別" c3="描述">
<ArgTableRow arg="index-plain" typ="bool">透過 HTTP 提供首頁（登入頁）以及諸如 `/favicon.png` 之類的靜態檔案。僅當 `webfig-plain` 和 `graphs-plain` 也均為 `no` 時才會生效；此時首頁、靜態檔案和未知路徑會透過 HTTP 返回 403，而 REST API 仍可正常工作。預設值：yes。</ArgTableRow>
<ArgTableRow arg="webfig-plain" typ="bool">透過 HTTP 在 `/webfig/` 提供 WebFig。預設值：yes。</ArgTableRow>
<ArgTableRow arg="graphs-plain" typ="bool">透過 HTTP 在 `/graphs/` 提供圖表。預設值：yes。</ArgTableRow>
<ArgTableRow arg="rest-plain" typ="bool">透過 HTTP 在 `/rest` 提供 [REST API](../../../developer-guides/rest-api.md)。設為 `no` 時，透過 HTTP 的 REST 請求會返回 403，而 HTTPS 不受影響。預設值：yes。</ArgTableRow>
<ArgTableRow arg="crl-plain" typ="bool">透過 HTTP 在 `/crl/` 提供證書吊銷列表下載。預設值：yes。</ArgTableRow>
<ArgTableRow arg="scep-plain" typ="bool">透過 HTTP 在 `/scep/` 提供 SCEP 伺服器。預設值：yes。</ArgTableRow>
<ArgTableRow arg="acme-plain" typ="bool">透過 HTTP 在 `/.well-known/acme-challenge/` 響應 ACME HTTP-01 質詢請求。預設值：yes。</ArgTableRow>
<ArgTableRow arg="index-secure" typ="bool">透過 HTTPS 提供首頁（登入頁）以及諸如 `/favicon.png` 之類的靜態檔案。僅當 `webfig-secure` 和 `graphs-secure` 也均為 `no` 時才會生效；此時首頁和靜態檔案會透過 HTTPS 返回 403，而 REST API 仍可正常工作。預設值：yes。</ArgTableRow>
<ArgTableRow arg="webfig-secure" typ="bool">透過 HTTPS 在 `/webfig/` 提供 WebFig。預設值：yes。</ArgTableRow>
<ArgTableRow arg="graphs-secure" typ="bool">透過 HTTPS 在 `/graphs/` 提供圖表。預設值：yes。</ArgTableRow>
<ArgTableRow arg="rest-secure" typ="bool">透過 HTTPS 在 `/rest` 提供 [REST API](../../../developer-guides/rest-api.md)。設為 `no` 時，透過 HTTPS 的 REST 請求會返回 403，而 HTTP 不受影響。預設值：yes。</ArgTableRow>
</ArgTable>
