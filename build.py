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
<meta name="description" content="走進貓空六間茶行，完成任務集章，集滿六個章換一盒青農聯名小茶禮盒。">
<meta property="og:title" content="{title}">
<meta property="og:description" content="走一趟山上的茶行，把六個章蓋滿。">
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
