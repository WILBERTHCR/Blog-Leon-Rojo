import json,html,os,urllib.parse,shutil
import sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'blog')
WA='https://wa.me/50689944763?text='
def wa(t): return WA+urllib.parse.quote(t)
HEAD='''<!doctype html><html lang="es-CR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="https://quimicasarji.com/blog/{slug}">
<meta property="og:title" content="{ogt}"><meta property="og:description" content="{desc}"><meta property="og:image" content="https://quimicasarji.com/img/p/{img}.jpg"><meta property="og:type" content="{ogtype}"><meta property="og:locale" content="es_CR">
<link rel="icon" href="/img/logo.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600;700&family=Barlow+Condensed:wght@500;600;700&display=swap"><link rel="stylesheet" href="/blog/blog.css">{ld}<script async src="https://www.googletagmanager.com/gtag/js?id=G-HB5PXSGNYF"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-HB5PXSGNYF');document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a[href*="wa.me"]');if(a)gtag('event',a.id==='tsend'?'pedido_whatsapp':'whatsapp_click',{{link_url:a.href.split('?')[0],page_path:location.pathname}})}},true)</script></head><body>
<header><div class="wrap"><a class="brand" href="/"><img src="/img/logo.png" alt=""><span><b>QUÍMICAS ARJI</b><small>León Rojo</small></span></a><nav class="navl"><a href="/#productos">Productos</a><a href="/blog/">Blog</a><a href="/#contacto">Contacto</a></nav><a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">Pedir</a></div></header>'''
FOOT='''<footer><div class="wrap">© 2026 Químicas Arji WGAC S.A. · Fabricantes de León Rojo desde hace 29 años · Desamparados, San José · Tel. 2250-2064 · WhatsApp 8994-4763 · <a href="/">quimicasarji.com</a></div></footer></body></html>'''
CAT=json.load(open(os.path.join(ROOT,'catalogo.json'),encoding='utf-8'))['products']
import unicodedata,re as _re
def _slug(t): return _re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',t).encode('ascii','ignore').decode().lower()).strip('-')
PSLUG={p['img'][0]:_slug(p['n']) for p in CAT if not p.get('pro')}
def cta(img,name,txt):
    return f'''<div class="cta"><img src="/img/p/{img}.jpg" alt="{name} León Rojo"><div><h3>{name}</h3><p>{txt}</p><div class="row"><a class="btn btn-wa" target="_blank" rel="noopener" href="{wa('Hola Químicas Arji, quiero pedir '+name+'.')}">Pedir por WhatsApp</a><a class="btn btn-red" href="{'/productos/'+PSLUG[img]+'/' if img in PSLUG else '/productos/'}">Ver ficha del producto</a></div></div></div>'''

POSTS=json.load(open(os.path.join(ROOT,'posts.json'),encoding='utf-8'))
POSTS.sort(key=lambda p:p['date'],reverse=True)
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
shutil.copy(os.path.join(ROOT,'blog.css'),os.path.join(OUT,'blog.css'))
for p in POSTS:
    slug=p['slug'];title=p['title'];desc=p['desc'];img=p['img'];date=p['date'];kw=p.get('kw','')
    body=open(os.path.join(ROOT,'posts',slug+'.html'),encoding='utf-8').read()
    ld='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"image":f"https://quimicasarji.com/img/p/{img}.jpg","datePublished":date,"dateModified":date,"inLanguage":"es-CR","author":{"@type":"Organization","name":"Químicas Arji WGAC S.A."},"publisher":{"@type":"Organization","name":"Químicas Arji WGAC S.A.","logo":{"@type":"ImageObject","url":"https://quimicasarji.com/img/logo.png"}},"mainEntityOfPage":f"https://quimicasarji.com/blog/{slug}/","keywords":kw},ensure_ascii=False)+'</script>'
    h=HEAD.format(title=html.escape(title)+' | Químicas Arji',desc=html.escape(desc),slug=slug+'/',ogt=html.escape(title),img=img,ogtype='article',ld=ld,wa=wa('Hola Químicas Arji, quiero hacer un pedido.'))
    art=f'<main class="wrap"><article><a class="eyebrow" href="/blog/" style="text-decoration:none">Blog León Rojo</a><h1>{title}</h1><p class="meta">Químicas Arji · {date[8:10]}/{date[5:7]}/{date[:4]}</p><div class="hero"><img src="/img/p/{img}.jpg" alt="{html.escape(title)}"></div>{body}{cta(*p["cta"])}<p><a href="/blog/">← Más artículos</a></p></article></main>'
    os.makedirs(os.path.join(OUT,slug),exist_ok=True)
    open(os.path.join(OUT,slug,'index.html'),'w',encoding='utf-8').write(h+art+FOOT)
cards=''.join(f'<a class="post" href="/blog/{p["slug"]}/"><img src="/img/p/{p["img"]}.jpg" alt="" loading="lazy"><div><span class="eyebrow">Guía práctica</span><h2>{p["title"]}</h2><p>{p["desc"]}</p></div></a>' for p in POSTS)
h=HEAD.format(title='Blog León Rojo · Guías de limpieza y mantenimiento | Químicas Arji',desc='Guías prácticas para limpiar, destapar, desengrasar y mantener tu casa, taller o piscina con productos León Rojo.',slug='',ogt='Blog León Rojo',img='b1_14',ogtype='website',ld='',wa=wa('Hola Químicas Arji, quiero hacer un pedido.'))
open(os.path.join(OUT,'index.html'),'w',encoding='utf-8').write(h+f'<main class="wrap"><section style="padding-top:40px"><span class="eyebrow">Blog León Rojo</span><h1>Guías prácticas</h1><p class="lead">Cómo resolver los problemas de limpieza y mantenimiento más comunes, con seguridad y sin desperdiciar producto.</p></section><div class="list">{cards}</div></main>'+FOOT)
json.dump([{k:p[k] for k in ('slug','title','desc','img','date')} for p in POSTS[:6]],open(os.path.join(OUT,'latest.json'),'w',encoding='utf-8'),ensure_ascii=False)
last=max(p['date'] for p in POSTS)
u=[f'  <url><loc>https://quimicasarji.com/</loc><lastmod>{last}</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>',f'  <url><loc>https://quimicasarji.com/blog/</loc><lastmod>{last}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>']
u+=[f'  <url><loc>https://quimicasarji.com/blog/{p["slug"]}/</loc><lastmod>{p["date"]}</lastmod><priority>0.7</priority></url>' for p in POSTS]
pu=os.path.join(ROOT,'productos','urls.json')
if os.path.exists(pu):
    u.append(f'  <url><loc>https://quimicasarji.com/productos/</loc><lastmod>{last}</lastmod><priority>0.8</priority></url>')
    u+=[f'  <url><loc>{x}</loc><priority>0.7</priority></url>' for x in json.load(open(pu))]
open(os.path.join(ROOT,'sitemap.xml'),'w',encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+'\n'.join(u)+'\n</urlset>\n')
print('ok',len(POSTS))
