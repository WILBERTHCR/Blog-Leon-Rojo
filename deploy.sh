#!/bin/sh
# Lo ejecuta el Cron Job de cPanel cada hora: trae los artículos nuevos y los publica.
cd "$HOME/blog-leon-rojo" || exit 1
git pull -q origin main || exit 1
mkdir -p "$HOME/public_html/blog" "$HOME/public_html/redes"
cp -rf blog/. "$HOME/public_html/blog/"
cp -rf redes/. "$HOME/public_html/redes/"
[ -d productos ] && mkdir -p "$HOME/public_html/productos" && cp -rf productos/. "$HOME/public_html/productos/"
cp -f sitemap.xml "$HOME/public_html/sitemap.xml"
[ -f site/index.html ] && cp -f site/index.html "$HOME/public_html/index.html"
[ -d site/audio ] && mkdir -p "$HOME/public_html/audio" && cp -rf site/audio/. "$HOME/public_html/audio/"
[ -f site/data.js ] && cp -f site/data.js "$HOME/public_html/data.js"
