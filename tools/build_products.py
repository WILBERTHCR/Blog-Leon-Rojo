"""Genera una página por producto en productos/<slug>/index.html a partir de catalogo.json y fichas/<id>.json.
Uso: python3 tools/build_products.py [id1 id2 ...]   (sin ids: todos los productos que tienen ficha)"""
import json, os, re, sys, html, shutil, unicodedata, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'productos')
CAT = json.load(open(os.path.join(ROOT, 'catalogo.json'), encoding='utf-8'))
P = CAT['products']; CATS = CAT['cats']
BYID = {p['id']: p for p in P}
WA = 'https://wa.me/50689944763?text='
e = html.escape


def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s


def wa(t):
    return WA + urllib.parse.quote(t)


def ficha(pid):
    f = os.path.join(ROOT, 'fichas', pid + '.json')
    return json.load(open(f, encoding='utf-8')) if os.path.exists(f) else None


def pres_text(pres):
    p = [x[0].lower() + x[1:] if not x[0].isdigit() else x for x in pres]
    return p[0] if len(p) == 1 else ', '.join(p[:-1]) + ' y ' + p[-1]


CSS = '''
.crumbs{font-family:var(--f-label);font-size:.85rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding-top:22px}
.crumbs a{color:var(--muted);text-decoration:none}.crumbs a:hover{color:var(--fg)}
.phero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:36px;padding-block:22px 10px;align-items:start}
.gal{display:grid;gap:10px}
.gal .main{background:#F2F2F0;border-radius:12px;overflow:hidden;display:grid;place-items:center;aspect-ratio:4/5}
.gal .main img{width:100%;height:100%;object-fit:contain}
.thumbs{display:flex;gap:8px;flex-wrap:wrap}
.thumbs button{border:2px solid transparent;background:#F2F2F0;border-radius:8px;padding:0;width:64px;height:80px;overflow:hidden;cursor:pointer}
.thumbs button[aria-current=true]{border-color:var(--red)}
.thumbs img{width:100%;height:100%;object-fit:cover}
.pinfo h1{margin:6px 0 8px}
.sub{font-size:1.2rem;color:var(--muted);margin:0 0 18px}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 18px}
.tag{font-family:var(--f-label);font-weight:600;font-size:.95rem;letter-spacing:.04em;border:1px solid var(--line);border-radius:999px;padding:6px 12px;background:var(--panel)}
.lbl{font-family:var(--f-label);font-weight:700;text-transform:uppercase;letter-spacing:.12em;font-size:.8rem;color:var(--muted);margin:0}
.ctas{display:flex;flex-wrap:wrap;gap:10px;margin:8px 0 14px}
.note{font-size:.95rem;color:var(--muted);margin:0}
.uses{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin:12px 0}
.use{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px;font-family:var(--f-label);font-weight:700;font-size:1.1rem;text-transform:uppercase;letter-spacing:.03em}
.steps{counter-reset:s;list-style:none;padding:0;display:grid;gap:10px}
.steps li{counter-increment:s;display:grid;grid-template-columns:36px 1fr;gap:12px;align-items:start;margin:0}
.steps li::before{content:counter(s);width:32px;height:32px;border-radius:50%;background:var(--red);color:#fff;display:grid;place-items:center;font-family:var(--f-label);font-weight:700}
details{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:10px 0}
summary{cursor:pointer;font-weight:600;font-size:1.05rem}
details p{margin:10px 0 0;color:#E4DCD6}
.rel{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.rel a{background:var(--panel);border:1px solid var(--line);border-radius:10px;overflow:hidden;text-decoration:none;color:inherit}
.rel a:hover{border-color:var(--red)}
.rel img{width:100%;aspect-ratio:4/5;object-fit:cover;background:#F2F2F0;display:block}
.rel span{display:block;padding:10px 12px;font-family:var(--f-label);font-weight:700;text-transform:uppercase;font-size:.95rem;letter-spacing:.02em;line-height:1.2}
.guide{display:block;background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--red);border-radius:10px;padding:14px 16px;text-decoration:none;margin:12px 0}
.guide b{display:block;font-family:var(--f-label);text-transform:uppercase;letter-spacing:.04em;font-size:1.1rem}
.guide small{color:var(--muted)}
main.prod{max-width:67.5rem}
@media (max-width:760px){.phero{grid-template-columns:1fr;gap:18px}.rel{grid-template-columns:repeat(2,minmax(0,1fr))}}
'''


def head(title, desc, canon, img, ld):
    return f'''<!doctype html><html lang="es-CR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{canon}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:image" content="https://quimicasarji.com/img/p/{img}.jpg"><meta property="og:type" content="website"><meta property="og:locale" content="es_CR">
<link rel="icon" href="/redes/icons/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="192x192" href="/redes/icons/icon-192.png"><link rel="apple-touch-icon" href="/redes/icons/apple-touch-icon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600;700&family=Barlow+Condensed:wght@500;600;700&display=swap"><link rel="stylesheet" href="/blog/blog.css"><style>{CSS}</style>{ld}<script async src="https://www.googletagmanager.com/gtag/js?id=G-HB5PXSGNYF"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-HB5PXSGNYF');document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a[href*="wa.me"]');if(a)gtag('event',a.id==='tsend'?'pedido_whatsapp':'whatsapp_click',{{link_url:a.href.split('?')[0],page_path:location.pathname}})}},true)</script></head><body>
<header><div class="wrap"><a class="brand" href="/"><img src="/img/logo.png" alt=""><span><b>QUÍMICAS ARJI</b><small>León Rojo</small></span></a><nav class="navl"><a href="/#productos">Productos</a><a href="/blog/">Blog</a><a href="/#contacto">Contacto</a></nav><a class="btn btn-wa" href="{wa('Hola Químicas Arji, quiero hacer un pedido.')}" target="_blank" rel="noopener">Pedir</a></div></header>'''


FOOT = '''<footer><div class="wrap">© 2026 Químicas Arji WGAC S.A. · Fabricantes de León Rojo desde hace 29 años · Desamparados, San José · Tel. 2250-2064 · WhatsApp 8994-4763 · <a href="/">quimicasarji.com</a></div></footer>
<script>document.querySelectorAll('.thumbs button').forEach(b=>b.addEventListener('click',()=>{document.querySelector('.gal .main img').src=b.dataset.src;document.querySelectorAll('.thumbs button').forEach(x=>x.setAttribute('aria-current',x===b))}))</script></body></html>'''


def page(p, f, posts):
    s = slug(p['n']); url = f'https://quimicasarji.com/productos/{s}/'
    cat = CATS.get(p['c'], '')
    imgs = p['img']
    desc = (f['intro'] if f else p['d'])[:155].rsplit(' ', 1)[0] + '…' if len((f['intro'] if f else p['d'])) > 155 else (f['intro'] if f else p['d'])
    title = f"{p['n']} León Rojo | {p['s']} · Costa Rica"
    faq = list((f or {}).get('faq', []))
    if not any('Dónde' in q for q, a in faq):
        faq.append(['¿Dónde lo compro?', 'En ferreterías de todo el país que venden la marca León Rojo, o pedilo directo por WhatsApp al 8994-4763.'])
    # Sin "Product": Google exige precio (offers) o reseñas para ese tipo, y no publicamos precios ni inventamos reseñas.
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": p['n'] + ' León Rojo', "description": p['d'], "url": url,
           "inLanguage": "es-CR", "primaryImageOfPage": f"https://quimicasarji.com/productos/img/{imgs[0]}.jpg",
           "publisher": {"@type": "Organization", "name": "Químicas Arji WGAC S.A.", "url": "https://quimicasarji.com/"}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://quimicasarji.com/"},
              {"@type": "ListItem", "position": 2, "name": "Productos", "item": "https://quimicasarji.com/productos/"},
              {"@type": "ListItem", "position": 3, "name": p['n'], "item": url}]}]
    if faq:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    ldh = ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>' for x in ld)
    thumbs = ''.join(f'<button type="button" data-src="/productos/img/{i}.jpg" aria-current="{str(k == 0).lower()}" aria-label="Foto {k + 1}"><img src="/productos/img/{i}.jpg" alt="" loading="lazy"></button>' for k, i in enumerate(imgs)) if len(imgs) > 1 else ''
    pres = ''.join(f'<span class="tag">{e(x)}</span>' for x in p.get('pres', []))
    vars_ = ''.join(f'<span class="tag">{e(x)}</span>' for x in p.get('vars', []))
    msg = f"Hola Químicas Arji, quiero pedir {p['n']} León Rojo."
    body = f'''<main class="wrap prod"><nav class="crumbs" aria-label="Ruta"><a href="/">Inicio</a> › <a href="/productos/">Productos</a> › {e(cat)}</nav>
<section class="phero"><div class="gal"><div class="main"><img src="/productos/img/{imgs[0]}.jpg" alt="{e(p['n'])} León Rojo"></div><div class="thumbs">{thumbs}</div></div>
<div class="pinfo"><span class="eyebrow">León Rojo · {e(cat)}</span><h1>{e(p['n'])} León Rojo</h1><p class="sub">{e(p['s'])}</p>
<p class="lbl">Presentaciones</p><div class="tags">{pres}</div>{f'<p class="lbl">Aromas / variantes</p><div class="tags">{vars_}</div>' if vars_ else ''}
<div class="ctas"><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener">Pedir por WhatsApp</a>{'' if p['c'] == 'envases' else f'<a class="btn btn-red" href="{wa('Hola Químicas Arji, necesito la ficha técnica de ' + p['n'] + '.')}" target="_blank" rel="noopener">Ficha técnica</a>'}</div>
<p class="note">🏪 También lo encontrás en ferreterías de todo el país: pedí la marca León Rojo en tu ferretería de confianza.</p></div></section>
<article style="padding-top:10px">
<h2>¿Para qué sirve?</h2><p>{e(f['intro'] if f else p['d'])}</p>
<div class="uses">{''.join(f'<div class="use">{e(u)}</div>' for u in p.get('u', []))}</div>
{('<h2>' + ('Cómo pedirlos' if p['c'] == 'envases' else 'Cómo se usa') + '</h2><ol class="steps">' + ''.join(f'<li>{e(x)}</li>' for x in f['pasos']) + '</ol>' + ('<p class="note">Seguí siempre las indicaciones y cantidades de la etiqueta.</p>' if p['c'] != 'envases' else '')) if f and f.get('pasos') else ''}
{f'<div class="warn"><b>⚠ Seguridad:</b> {e(f["seguridad"])}</div>' if f and f.get('seguridad') else ('<div class="warn"><b>⚠ Seguridad:</b> Leé la etiqueta antes de usar. Usá guantes y lentes de protección y no lo mezclés con otros productos.</div>' if p.get('haz') else '')}
{''.join(f'<a class="guide" href="/productos/{h["slug"]}/"><small>Guía completa · cuál elegir, usos y seguridad</small><b>{e(h["h1"])}</b></a>' for h in HUBS if p['id'] in h['ids'])}
{''.join(f'<a class="guide" href="/blog/{g["slug"]}/"><small>Guía paso a paso</small><b>{e(g["title"])}</b></a>' for g in posts if f and f.get('blog') == g['slug'])}
{('<h2>Preguntas frecuentes</h2>' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faq)) if faq else ''}
<h2>También te puede servir</h2><div class="rel">{''.join(f'<a href="/productos/{slug(r["n"])}/"><img src="/productos/img/{r["img"][0]}.jpg" alt="" loading="lazy"><span>{e(r["n"])}</span></a>' for r in [x for x in P if x['c'] == p['c'] and x['id'] != p['id'] and not x.get('pro')][:4])}</div>
</article></main>'''
    os.makedirs(os.path.join(OUT, s), exist_ok=True)
    open(os.path.join(OUT, s, 'index.html'), 'w', encoding='utf-8').write(head(title, desc, url, imgs[0], ldh) + body + FOOT)
    return s


HUBS = [json.load(open(os.path.join(ROOT, 'temas', x), encoding='utf-8')) for x in sorted(os.listdir(os.path.join(ROOT, 'temas')))] if os.path.isdir(os.path.join(ROOT, 'temas')) else []


for _h in HUBS: _h.setdefault('img', BYID[_h['ids'][0]]['img'][0])


def auto_body(h, prods):
    b = h['intro']
    b += '<h2>¿Cuál elijo?</h2><ul>' + ''.join(f'<li>{e(t)}</li>' for t in h['tips']) + '</ul>'
    b += '<h2>Los productos</h2>' + ''.join(f'<h3><a href="/productos/{slug(r["n"])}/">{e(r["n"])}</a></h3><p>{e(r["d"])}</p>' for r in prods)
    if h.get('seguridad'): b += f'<div class="warn"><b>⚠ Seguridad:</b> {e(h["seguridad"])}</div>'
    b += '<h2>Presentaciones</h2><ul>' + ''.join(f'<li><b>{e(r["n"])}:</b> {e(", ".join(r["pres"]))}</li>' for r in prods) + '</ul>'
    b += '<h2>¿Dónde comprar?</h2><p>Encontrá los productos León Rojo en ferreterías de todo el país: pedilos en tu ferretería de confianza. Si sos ferretería, distribuidor o empresa, escribinos al WhatsApp 8994-4763 o llamá al 2250-2064.</p>'
    return b


def hub(h, posts):
    url = f"https://quimicasarji.com/productos/{h['slug']}/"
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": h['title'], "description": h['desc'], "url": url, "inLanguage": "es-CR",
           "primaryImageOfPage": f"https://quimicasarji.com/productos/img/{h['img']}.jpg",
           "publisher": {"@type": "Organization", "name": "Químicas Arji WGAC S.A.", "url": "https://quimicasarji.com/"}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://quimicasarji.com/"},
              {"@type": "ListItem", "position": 2, "name": "Productos", "item": "https://quimicasarji.com/productos/"},
              {"@type": "ListItem", "position": 3, "name": h.get('label', h['h1']), "item": url}]},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in h['faq']]}]
    ldh = ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>' for x in ld)
    prods = [BYID[i] for i in h['ids']]
    cards = ''.join(f'<a href="/productos/{slug(r["n"])}/"><img src="/productos/img/{r["img"][0]}.jpg" alt="{e(r["n"])} León Rojo" loading="lazy"><span>{e(r["n"])}</span></a>' for r in prods)
    guide = ''.join(f'<a class="guide" href="/blog/{g["slug"]}/"><small>Guía paso a paso</small><b>{e(g["title"])}</b></a>' for g in posts if g['slug'] in [h.get('blog')] + h.get('blogs', []))
    body = f'''<main class="wrap prod"><nav class="crumbs" aria-label="Ruta"><a href="/">Inicio</a> › <a href="/productos/">Productos</a> › {e(h.get('label', h['h1']))}</nav>
<section class="phero"><div class="gal"><div class="main"><img src="/productos/img/{h['img']}.jpg" alt="{e(h['h1'])} León Rojo"></div></div>
<div class="pinfo"><span class="eyebrow">León Rojo · Fabricado en Costa Rica</span><h1>{e(h['h1'])}</h1><p class="sub">{e(h['sub'])}</p>
<div class="ctas"><a class="btn btn-wa" href="{wa('Hola Químicas Arji, quiero información de ' + h.get('label', h['h1']).lower() + ' León Rojo.')}" target="_blank" rel="noopener">Consultar por WhatsApp</a></div>
<p class="note">🏪 Pedilo en tu ferretería de confianza: buscá la marca León Rojo.</p>
<p class="lbl" style="margin-top:18px">Elegí tu producto</p><div class="rel" style="grid-template-columns:repeat(2,minmax(0,1fr))">{cards}</div></div></section>
<article style="padding-top:10px">{h.get('body') or auto_body(h, prods)}{guide}
<h2>Preguntas frecuentes</h2>{''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in h['faq'])}
</article></main>'''
    os.makedirs(os.path.join(OUT, h['slug']), exist_ok=True)
    open(os.path.join(OUT, h['slug'], 'index.html'), 'w', encoding='utf-8').write(head(h['title'], h['desc'], url, h['img'], ldh) + body + FOOT)
    return h['slug']


def index(built):
    cards = ''
    for c, name in CATS.items():
        items = [p for p in P if p['c'] == c and p['id'] in built]
        if not items: continue
        cards += f'<h2>{e(name)}</h2><div class="rel">' + ''.join(f'<a href="/productos/{slug(p["n"])}/"><img src="/productos/img/{p["img"][0]}.jpg" alt="" loading="lazy"><span>{e(p["n"])}</span></a>' for p in items) + '</div>'
    h = head('Productos León Rojo · Catálogo completo | Químicas Arji', 'Catálogo de productos químicos León Rojo hechos en Costa Rica: limpieza, taller y autos, construcción, madera y piscinas.', 'https://quimicasarji.com/productos/', 'b1_14', '')
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(h + f'<main class="wrap prod"><nav class="crumbs"><a href="/">Inicio</a> › Productos</nav><section style="padding-top:16px"><span class="eyebrow">Catálogo León Rojo</span><h1>Nuestros productos</h1><img src="/productos/img/linea_completa_1.jpg" alt="Línea completa de productos León Rojo" style="width:100%;border-radius:12px;margin:8px 0 18px;background:#F2F2F0"><p class="lead">Fabricados en Costa Rica desde hace 29 años. Tocá un producto para ver presentaciones, usos y precauciones.</p></section><h2>Guías por tema</h2><div class="uses">{''.join(f'<a class="use" style="text-decoration:none" href="/productos/{h["slug"]}/">{e(h.get("label", h["h1"]))}</a>' for h in HUBS)}</div>{cards}<p style="padding-bottom:40px"></p></main>' + FOOT)


if __name__ == '__main__':
    posts = json.load(open(os.path.join(ROOT, 'posts.json'), encoding='utf-8'))
    ids = sys.argv[1:] or [p['id'] for p in P if not p.get('pro') and os.path.exists(os.path.join(ROOT, 'fichas', p['id'] + '.json'))]
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(ROOT, 'productos_img'), os.path.join(OUT, 'img'))
    built = {}
    for pid in ids:
        built[pid] = page(BYID[pid], ficha(pid), posts)
    index(built)
    hubs = [hub(h, posts) for h in HUBS]
    json.dump([f'https://quimicasarji.com/productos/{s}/' for s in hubs + list(built.values())], open(os.path.join(OUT, 'urls.json'), 'w'))
    print('ok', len(built), list(built.values()))
