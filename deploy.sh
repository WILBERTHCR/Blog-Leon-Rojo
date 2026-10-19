#!/bin/sh
# Lo ejecuta el Cron Job de cPanel cada hora: trae los artículos nuevos y los publica.
cd "$HOME/blog-leon-rojo" || exit 1
git pull -q origin main || exit 1
mkdir -p "$HOME/public_html/blog"
cp -rf blog/. "$HOME/public_html/blog/"
cp -f sitemap.xml "$HOME/public_html/sitemap.xml"
