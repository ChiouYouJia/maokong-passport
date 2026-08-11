#!/usr/bin/env python3
"""把 Artifact 格式的 maokong-passport-demo.html 包成可獨立部署的 index.html"""
import re, pathlib

src = pathlib.Path("maokong-passport-demo.html").read_text(encoding="utf-8")
title = re.search(r"<title>(.*?)</title>", src, re.S).group(1).strip()
body  = re.sub(r"<title>.*?</title>\s*", "", src, count=1, flags=re.S)

pathlib.Path("index.html").write_text(f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="給貓空茶行的合作提案：捷運站掃碼進場、路線設計、店家給碼集章、集滿換青農聯名禮盒。">
<meta property="og:title" content="{title}">
<meta property="og:description" content="一張數位護照，把纜車人潮走進茶園。">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><text y='26' font-size='26'>%F0%9F%8D%B5</text></svg>">
<style>*,*::before,*::after{{box-sizing:border-box}}body,h1,h2,h3,h4,p,dl,dd,figure{{margin:0}}button,input{{font:inherit;color:inherit}}</style>
</head>
<body>
{body}
</body>
</html>
""", encoding="utf-8")
print("已產生 index.html")
