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


LICENSE = 'https://quimicasarji.com/productos/uso-de-imagenes/'
# Productos controlados por el ICD (requieren licencia para comprarlos y venderlos) y su alternativa sin licencia
CTRL = {'muriatico36': ('el Ácido Muriático 29% NC', 'acido-muriatico-29'),
        'superdesatorador': ('el Desatorador de Cañerías NC', 'desatorador-de-canerias-nc'),
        'potasa': ('el Desatorador de Cañerías NC', 'desatorador-de-canerias-nc')}


def ctrl_note(p):
    if p['id'] not in CTRL: return ''
    alt, sl = CTRL[p['id']]
    return (f'<div class="warn"><b>⚠ Producto controlado por el ICD:</b> para comprarlo y venderlo se necesita licencia del '
            f'Instituto Costarricense sobre Drogas. Si no tenés licencia, usá <a href="/productos/{sl}/">{e(alt)}</a>, que no la requiere.</div>')


IMGMAP = {}  # (product id, k) -> nombre descriptivo del archivo (sin .jpg)
IMAGES = {}  # url de página -> [(url de imagen, título)] para el mapa de imágenes
# Qué muestra cada foto adicional (revisado a ojo); las demás quedan como "foto N".
IMGLBL = {('muriatico29', 0): '1/2 litro, litro y galón', ('muriatico36', 0): '1/2 litro, litro y galón',
          ('muriatico29', 1): 'galón', ('muriatico29', 2): 'litro', ('muriatico29', 3): '1/2 litro',
          ('muriatico36', 1): 'galón', ('muriatico36', 2): 'litro', ('muriatico36', 3): '1/2 litro'}


def iname(p, k=0):
    """Nombre de archivo descriptivo para Google Imágenes, ej. acido-muriatico-29-leon-rojo-2."""
    lb = IMGLBL.get((p['id'], k))
    n = slug(p['n']) + '-leon-rojo' + (('-' + slug(lb.replace('1/2', 'medio'))) if lb and k else (f'-{k + 1}' if k else ''))
    IMGMAP[(p['id'], k)] = n
    return n


def isrc(p, k=0, thumb=False):
    return f"/productos/img/{'t/' if thumb else ''}{iname(p, k)}.jpg"


def ialt(p, k=0):
    base = f"{p['n']} León Rojo"
    if IMGLBL.get((p['id'], k)): base += ' en ' + IMGLBL[(p['id'], k)]
    elif k == 0 and p.get('s'): base += ' · ' + p['s']
    elif k: base += f' – foto {k + 1}'
    return base


def img_ld(p, url):
    """Datos de las fotos para Google (sin Product: no publicamos precios)."""
    imgs = []
    for k in range(len(p['img'])):
        u = 'https://quimicasarji.com' + isrc(p, k)
        imgs.append({"@type": "ImageObject", "contentUrl": u, "url": u, "name": ialt(p, k), "caption": ialt(p, k),
                     "creditText": "León Rojo · Químicas Arji", "creator": {"@type": "Organization", "name": "Químicas Arji WGAC S.A."},
                     "copyrightNotice": "Químicas Arji WGAC S.A.", "license": LICENSE, "acquireLicensePage": LICENSE})
        IMAGES.setdefault(url, []).append((u, ialt(p, k)))
    return imgs


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
.steps li::before{content:counter(s);box-sizing:border-box;width:32px;height:32px;min-width:32px;border-radius:50%;background:var(--red);color:#fff;display:flex;align-items:center;justify-content:center;line-height:1;padding:0;font-family:Arial,Helvetica,sans-serif;font-size:15px;font-weight:700;font-variant-numeric:tabular-nums}
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
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:image" content="{img if img.startswith('http') else 'https://quimicasarji.com/img/p/' + img + '.jpg'}"><meta property="og:type" content="website"><meta property="og:locale" content="es_CR">
<link rel="icon" href="/redes/icons/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="192x192" href="/redes/icons/icon-192.png"><link rel="apple-touch-icon" href="/redes/icons/apple-touch-icon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow:wght@400;500;600;700&family=Barlow+Condensed:wght@500;600;700&display=swap"><link rel="stylesheet" href="/blog/blog.css"><style>{CSS}</style>{ld}<script async src="https://www.googletagmanager.com/gtag/js?id=G-HB5PXSGNYF"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-HB5PXSGNYF');document.addEventListener('click',function(e){{var a=e.target.closest&&e.target.closest('a[href*="wa.me"]');if(a)gtag('event',a.id==='tsend'?'pedido_whatsapp':'whatsapp_click',{{link_url:a.href.split('?')[0],page_path:location.pathname}})}},true)</script></head><body>
<header><div class="wrap"><a class="brand" href="/"><img src="/img/logo.png" alt=""><span><b>QUÍMICAS ARJI</b><small>León Rojo</small></span></a><nav class="navl"><a href="/#productos">Productos</a><a href="/blog/">Blog</a><a href="/#contacto">Contacto</a></nav><a class="btn btn-wa" href="{wa('Hola Químicas Arji, quiero hacer un pedido.')}" target="_blank" rel="noopener">Pedir</a></div></header>'''


FOOT = '''<footer><div class="wrap">© 2026 Químicas Arji WGAC S.A. · Fabricantes de León Rojo desde hace 29 años · Desamparados, San José · Tel. 2250-2064 · WhatsApp 8994-4763 · <a href="/">quimicasarji.com</a></div></footer>
<script>document.querySelectorAll('.thumbs button').forEach(b=>b.addEventListener('click',()=>{document.querySelector('.gal .main img').src=b.dataset.src;document.querySelectorAll('.thumbs button').forEach(x=>x.setAttribute('aria-current',x===b))}))</script></body></html>'''


REVIEWS_BLOCK = r'''<section class="resenas" id="resenas" data-pid="{ID}">
<style>
.resenas{margin:34px 0 10px}.resenas h2{margin-bottom:6px}
.res-top{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:6px 0 14px}
.stars{--n:0;display:inline-block;font-size:22px;line-height:1;position:relative;color:#d9d9d9;letter-spacing:2px}
.stars::before{content:"★★★★★"}
.stars>i{position:absolute;left:0;top:0;width:calc(var(--n)/5*100%);overflow:hidden;color:#f5a623;white-space:nowrap}
.stars>i::before{content:"★★★★★"}
.res-avg{font-size:1.4em;font-weight:700}.res-count{opacity:.7}
.res-list{display:grid;gap:12px;margin:10px 0 22px}
.res-item{border:1px solid #eee;border-radius:12px;padding:12px 14px;background:#fff}
.res-item .stars{font-size:16px}.res-head{display:flex;justify-content:space-between;gap:8px;align-items:center;flex-wrap:wrap}
.res-name{font-weight:600}.res-date{font-size:.82em;opacity:.6}.res-text{margin-top:6px}
.res-form{border:1px solid #eee;border-radius:14px;padding:16px;background:#FAFAF8;max-width:560px}
.res-form h3{margin:0 0 10px}
.res-pick{display:flex;gap:4px;margin-bottom:10px}
.res-pick button{font-size:30px;line-height:1;background:none;border:none;cursor:pointer;color:#d9d9d9;padding:0 2px}
.res-pick button.on{color:#f5a623}
.res-form input[type=text]:not(.res-hp),.res-form input[name=author],.res-form textarea{width:100%;box-sizing:border-box;border:1px solid #ccc;border-radius:9px;padding:10px;font:inherit;margin-bottom:10px}
.res-form textarea{min-height:84px;resize:vertical}
.res-hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}
.res-msg{margin:8px 0 0;font-weight:600;min-height:1em}.res-msg.ok{color:#1a8f3c}.res-msg.err{color:#c0392b}
</style>
<h2>Opiniones de clientes</h2>
<div class="res-top"><span class="stars" id="resStars"><i></i></span><span class="res-avg" id="resAvg">—</span><span class="res-count" id="resCount">Sé el primero en opinar</span></div>
<div class="res-list" id="resList"></div>
<form class="res-form" id="resForm" autocomplete="off">
<h3>Calificá este producto</h3>
<div class="res-pick" id="resPick" role="radiogroup" aria-label="Estrellas">
<button type="button" data-v="1" aria-label="1 estrella">★</button><button type="button" data-v="2" aria-label="2 estrellas">★</button><button type="button" data-v="3" aria-label="3 estrellas">★</button><button type="button" data-v="4" aria-label="4 estrellas">★</button><button type="button" data-v="5" aria-label="5 estrellas">★</button>
</div>
<input type="hidden" name="rating" id="resRating" value="0">
<input name="author" maxlength="40" placeholder="Tu nombre" required>
<textarea name="text" maxlength="600" placeholder="Contanos qué te pareció el producto" required></textarea>
<input type="text" name="website" class="res-hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<button type="submit" class="btn btn-red">Enviar mi opinión</button>
<p class="res-msg" id="resMsg" aria-live="polite"></p>
</form>
<script>
(function(){
var S=document.getElementById('resenas'),PID=S.dataset.pid,API='/productos/resenas.php';
function esc(t){var d=document.createElement('div');d.textContent=t;return d.innerHTML;}
function starHTML(n){return '<span class="stars" style="--n:'+n+'"><i></i></span>';}
function render(d){
 var n=d.count||0,a=d.average||0;
 document.getElementById('resStars').style.setProperty('--n',a);
 document.getElementById('resAvg').textContent=n?a.toFixed(1):'—';
 document.getElementById('resCount').textContent=n?('· '+n+(n==1?' opinión':' opiniones')):'Sé el primero en opinar';
 var L=document.getElementById('resList');L.innerHTML='';
 (d.reviews||[]).forEach(function(r){
  var el=document.createElement('div');el.className='res-item';
  el.innerHTML='<div class="res-head"><span class="res-name">'+esc(r.author)+'</span><span class="res-date">'+esc(r.date||'')+'</span></div>'+starHTML(r.rating)+'<div class="res-text">'+esc(r.text)+'</div>';
  L.appendChild(el);
 });
 if(n){var ld={"@context":"https://schema.org","@type":"AggregateRating","ratingValue":a,"reviewCount":n};
  document.querySelectorAll('script[type="application/ld+json"]').forEach(function(sc){
   try{var j=JSON.parse(sc.textContent);if(j && j["@type"]==="Product"){j.aggregateRating={"@type":"AggregateRating","ratingValue":a,"reviewCount":n,"bestRating":5,"worstRating":1};
    j.review=(d.reviews||[]).slice(0,10).map(function(r){return {"@type":"Review","reviewRating":{"@type":"Rating","ratingValue":r.rating,"bestRating":5,"worstRating":1},"author":{"@type":"Person","name":r.author},"datePublished":r.date,"reviewBody":r.text};});
    sc.textContent=JSON.stringify(j);}}catch(e){}
  });
 }
}
fetch(API+'?id='+encodeURIComponent(PID)).then(function(r){return r.json();}).then(render).catch(function(){});
var pick=document.getElementById('resPick'),rating=document.getElementById('resRating');
pick.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var v=+b.dataset.v;rating.value=v;[].forEach.call(pick.children,function(x,i){x.classList.toggle('on',i<v);});});
document.getElementById('resForm').addEventListener('submit',function(e){
 e.preventDefault();var m=document.getElementById('resMsg');m.className='res-msg';
 if(!(+rating.value)){m.textContent='Elegí cuántas estrellas.';m.className='res-msg err';return;}
 var fd=new FormData(e.target);fd.append('id',PID);
 var btn=e.target.querySelector('button[type=submit]');btn.disabled=true;
 fetch(API,{method:'POST',body:fd}).then(function(r){return r.json().then(function(j){return {s:r.status,j:j};});}).then(function(o){
  btn.disabled=false;
  if(o.j&&o.j.ok){e.target.reset();[].forEach.call(pick.children,function(x){x.classList.remove('on');});rating.value=0;m.textContent='¡Gracias por tu opinión!';m.className='res-msg ok';render(o.j);}
  else if(o.s===429){m.textContent='Ya dejaste una opinión de este producto. ¡Gracias!';m.className='res-msg err';}
  else{m.textContent='Revisá tu nombre y comentario e intentá de nuevo.';m.className='res-msg err';}
 }).catch(function(){btn.disabled=false;m.textContent='No se pudo enviar. Probá más tarde.';m.className='res-msg err';});
});
})();
</script>
</section>
'''


def page(p, f, posts):
    s = slug(p['n']); url = f'https://quimicasarji.com/productos/{s}/'
    cat = CATS.get(p['c'], '')
    imgs = p['img']
    desc = f['intro'] if f else p['d']
    if len(desc) < 140 and p.get('pres'): desc += ' Presentaciones: ' + ', '.join(p['pres']) + '.'
    if len(desc) < 140: desc += ' Hecho en Costa Rica por Químicas Arji.'
    if len(desc) > 160: desc = desc[:157].rsplit(' ', 1)[0].rstrip(',.:') + '…'
    _c = [f"{p['n']} León Rojo | {p['s']} · Costa Rica", f"{p['n']} León Rojo | {p['s']}", f"{p['n']} León Rojo en Costa Rica | Usos y presentaciones", f"{p['n']} León Rojo | Usos y presentaciones"]
    title = next((t for t in _c if len(t) <= 65), _c[-1])
    faq = list((f or {}).get('faq', []))
    if p['id'] in CTRL and not any('licencia' in q.lower() for q, a in faq):
        faq.insert(0, ['¿Se necesita licencia para comprarlo?', f"Sí. Es un precursor controlado: para comprarlo y venderlo se necesita licencia del Instituto Costarricense sobre Drogas (ICD). Si no tenés licencia, usá {CTRL[p['id']][0]}, que no la requiere."])
    if not any('Dónde' in q for q, a in faq):
        faq.append(['¿Dónde lo compro?', 'En ferreterías de todo el país que venden la marca León Rojo, o pedilo directo por WhatsApp al 8994-4763.'])
    # Sin "Product": Google exige precio (offers) o reseñas para ese tipo, y no publicamos precios ni inventamos reseñas.
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": p['n'] + ' León Rojo', "description": p['d'], "url": url,
           "inLanguage": "es-CR", "primaryImageOfPage": img_ld(p, url)[0], "image": [x["contentUrl"] for x in img_ld(p, '_')],
           "publisher": {"@type": "Organization", "name": "Químicas Arji WGAC S.A.", "url": "https://quimicasarji.com/"}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://quimicasarji.com/"},
              {"@type": "ListItem", "position": 2, "name": "Productos", "item": "https://quimicasarji.com/productos/"},
              {"@type": "ListItem", "position": 3, "name": p['n'], "item": url}]}]
    precios = (f or {}).get('precios') or []
    if precios:  # precio sugerido al público (IVA incluido), dado por la empresa
        ld.append({"@context": "https://schema.org", "@type": "Product", "name": p['n'] + ' León Rojo', "description": desc, "url": url,
                   "image": [x["contentUrl"] for x in img_ld(p, '_')], "brand": {"@type": "Brand", "name": "León Rojo"},
                   "manufacturer": {"@type": "Organization", "name": "Químicas Arji WGAC S.A."},
                   "offers": {"@type": "AggregateOffer", "priceCurrency": "CRC", "lowPrice": min(v for _, v in precios), "highPrice": max(v for _, v in precios), "offerCount": len(precios),
                              "offers": [{"@type": "Offer", "name": f"{p['n']} León Rojo · {n}", "price": v, "priceCurrency": "CRC", "availability": "https://schema.org/InStock", "itemCondition": "https://schema.org/NewCondition", "url": url,
                                          **({"priceValidUntil": f['precios_hasta']} if f.get('precios_hasta') else {}),
                                          "seller": {"@type": "Organization", "name": "Químicas Arji WGAC S.A."}} for n, v in precios]}})
    if faq:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    ldh = ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>' for x in ld)
    thumbs = ''.join(f'<button type="button" data-src="{isrc(p, k)}" aria-current="{str(k == 0).lower()}" aria-label="Foto {k + 1}"><img src="{isrc(p, k, True)}" alt="{e(ialt(p, k))}" loading="lazy"></button>' for k, i in enumerate(imgs)) if len(imgs) > 1 else ''
    pres = ''.join(f'<span class="tag">{e(x)}</span>' for x in p.get('pres', []))
    vars_ = ''.join(f'<span class="tag">{e(x)}</span>' for x in p.get('vars', []))
    msg = f"Hola Químicas Arji, quiero pedir {p['n']} León Rojo."
    reviews_html = REVIEWS_BLOCK.replace('{ID}', p['id']) if (f and f.get('resenas')) else ''
    body = f'''<main class="wrap prod"><nav class="crumbs" aria-label="Ruta"><a href="/">Inicio</a> › <a href="/productos/">Productos</a> › {e(cat)}</nav>
<section class="phero"><div class="gal"><div class="main"><img src="{isrc(p)}" alt="{e(ialt(p))}" width="800" height="1000"></div><div class="thumbs">{thumbs}</div></div>
<div class="pinfo"><span class="eyebrow">León Rojo · {e(cat)}</span><h1>{e(p['n'])} León Rojo</h1><p class="sub">{e(p['s'])}</p>
<p class="lbl">Presentaciones</p><div class="tags">{pres}</div>{('<p class="lbl">Precio sugerido al público</p><div class="tags">' + ''.join(f'<span class="tag">{e(n)}: <b>₡{v:,}</b></span>'.replace(',', '.') for n, v in precios) + '</div><p class="note" style="margin-top:4px">IVA incluido · <b>Disponible</b> en ferreterías de todo el país y en planta. El precio puede variar en cada ferretería.</p>') if precios else ''}{f'<p class="lbl">Aromas / variantes</p><div class="tags">{vars_}</div>' if vars_ else ''}
<div class="ctas"><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener">Pedir por WhatsApp</a>{'' if p['c'] == 'envases' else (''.join(f'<a class="btn btn-red" href="/fichas-tecnicas/pdf/{x["file"]}" target="_blank" rel="noopener">⬇ Ficha técnica{(" " + e(x["label"].replace("Cloro ", ""))) if x["label"] else ""} (PDF)</a>' for x in FTBY.get(p['id'], [])) or f'<a class="btn btn-red" href="{wa('Hola Químicas Arji, necesito la ficha técnica de ' + p['n'] + '.')}" target="_blank" rel="noopener">Ficha técnica</a>')}</div>
<p class="note">🏪 También lo encontrás en ferreterías de todo el país: pedí la marca León Rojo en tu ferretería de confianza.</p></div></section>
<article style="padding-top:10px">
<h2>¿Para qué sirve?</h2><p>{e(f['intro'] if f else p['d'])}</p>{ctrl_note(p)}
<div class="uses">{''.join(f'<div class="use">{e(u)}</div>' for u in p.get('u', []))}</div>
{('<h2>' + ('Cómo pedirlos' if p['c'] == 'envases' else 'Cómo se usa') + '</h2><ol class="steps">' + ''.join(f'<li>{e(x)}</li>' for x in f['pasos']) + '</ol>' + ('<p class="note">Seguí siempre las indicaciones y cantidades de la etiqueta.</p>' if p['c'] != 'envases' else '')) if f and f.get('pasos') else ''}
{f'<div class="warn"><b>⚠ Seguridad:</b> {e(f["seguridad"])}</div>' if f and f.get('seguridad') else ('<div class="warn"><b>⚠ Seguridad:</b> Leé la etiqueta antes de usar. Usá guantes y lentes de protección y no lo mezclés con otros productos.</div>' if p.get('haz') else '')}
{''.join(f'<a class="guide" href="{hurl(h)}"><small>Guía completa · cuál elegir, usos y seguridad</small><b>{e(h["h1"])}</b></a>' for h in HUBS if p['id'] in h['ids'])}
{''.join(f'<a class="guide" href="/blog/{g["slug"]}/"><small>Guía paso a paso</small><b>{e(g["title"])}</b></a>' for g in posts if f and f.get('blog') == g['slug'])}
{('<h2>Preguntas frecuentes</h2>' + ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faq)) if faq else ''}
{reviews_html}<h2>También te puede servir</h2><div class="rel">{''.join(f'<a href="/productos/{slug(r["n"])}/"><img src="{isrc(r, 0, True)}" alt="{e(r["n"])} León Rojo" loading="lazy"><span>{e(r["n"])}</span></a>' for r in [x for x in P if x['c'] == p['c'] and x['id'] != p['id'] and not x.get('pro')][:4])}</div>
</article></main>'''
    os.makedirs(os.path.join(OUT, s), exist_ok=True)
    open(os.path.join(OUT, s, 'index.html'), 'w', encoding='utf-8').write(head(title, desc, url, 'https://quimicasarji.com' + isrc(p), ldh) + body + FOOT)
    return s


FT = json.load(open(os.path.join(ROOT, 'site', 'fichas-tecnicas', 'fichas.json'), encoding='utf-8')) if os.path.exists(os.path.join(ROOT, 'site', 'fichas-tecnicas', 'fichas.json')) else []
FTBY = {}
for _x in FT: FTBY.setdefault(_x['id'], []).append(_x)

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


def hurl(h):
    """URL pública de una guía: si se unió a otra página, apunta al destino."""
    return h.get('redirect') or f"/productos/{h['slug']}/"


def redirect_page(h):
    """Guía unida a otra página: 301 por .htaccess y, de respaldo, canonical + meta refresh."""
    dst = 'https://quimicasarji.com' + h['redirect']
    d = os.path.join(OUT, h['slug']); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, '.htaccess'), 'w').write(f'RedirectMatch 301 ^/productos/{h["slug"]}/?(index\\.html)?$ {dst}\n')
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{e(h.get("label", h["h1"]))} | León Rojo</title><link rel="canonical" href="{dst}"><meta http-equiv="refresh" content="0;url={dst}"></head><body><p>Esta guía ahora está en <a href="{dst}">{dst}</a>.</p><script>location.replace({json.dumps(dst)})</script></body></html>')
    return None


def hub(h, posts):
    if h.get('redirect'): return redirect_page(h)
    url = f"https://quimicasarji.com/productos/{h['slug']}/"
    _m = next(((BYID[i], BYID[i]['img'].index(h['img'])) for i in h['ids'] if h['img'] in BYID[i]['img']), None)
    hsrc, halt = (isrc(*_m), ialt(*_m)) if _m else (f"/productos/img/{h['img']}.jpg", h.get('label', h['h1']) + ' León Rojo')
    for i in h['ids']:
        IMAGES.setdefault(url, []).append(('https://quimicasarji.com' + isrc(BYID[i]), ialt(BYID[i])))
    ld = [{"@context": "https://schema.org", "@type": "WebPage", "name": h['title'], "description": h['desc'], "url": url, "inLanguage": "es-CR",
           "primaryImageOfPage": {"@type": "ImageObject", "contentUrl": "https://quimicasarji.com" + hsrc, "url": "https://quimicasarji.com" + hsrc, "name": halt, "caption": halt, "creditText": "León Rojo · Químicas Arji", "creator": {"@type": "Organization", "name": "Químicas Arji WGAC S.A."}, "copyrightNotice": "Químicas Arji WGAC S.A.", "license": LICENSE, "acquireLicensePage": LICENSE},
           "publisher": {"@type": "Organization", "name": "Químicas Arji WGAC S.A.", "url": "https://quimicasarji.com/"}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://quimicasarji.com/"},
              {"@type": "ListItem", "position": 2, "name": "Productos", "item": "https://quimicasarji.com/productos/"},
              {"@type": "ListItem", "position": 3, "name": h.get('label', h['h1']), "item": url}]},
          {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in h['faq']]}]
    ldh = ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + '</script>' for x in ld)
    prods = [BYID[i] for i in h['ids']]
    cards = ''.join(f'<a href="/productos/{slug(r["n"])}/"><img src="{isrc(r, 0, True)}" alt="{e(r["n"])} León Rojo" loading="lazy"><span>{e(r["n"])}</span></a>' for r in prods)
    guide = ''.join(f'<a class="guide" href="/blog/{g["slug"]}/"><small>Guía paso a paso</small><b>{e(g["title"])}</b></a>' for g in posts if g['slug'] in [h.get('blog')] + h.get('blogs', []))
    body = f'''<main class="wrap prod"><nav class="crumbs" aria-label="Ruta"><a href="/">Inicio</a> › <a href="/productos/">Productos</a> › {e(h.get('label', h['h1']))}</nav>
<section class="phero"><div class="gal"><div class="main"><img src="{hsrc}" alt="{e(halt)}" width="800" height="1000"></div></div>
<div class="pinfo"><span class="eyebrow">León Rojo · Fabricado en Costa Rica</span><h1>{e(h['h1'])}</h1><p class="sub">{e(h['sub'])}</p>
<div class="ctas"><a class="btn btn-wa" href="{wa('Hola Químicas Arji, quiero información de ' + h.get('label', h['h1']).lower() + ' León Rojo.')}" target="_blank" rel="noopener">Consultar por WhatsApp</a></div>
<p class="note">🏪 Pedilo en tu ferretería de confianza: buscá la marca León Rojo.</p>
<p class="lbl" style="margin-top:18px">Elegí tu producto</p><div class="rel" style="grid-template-columns:repeat(2,minmax(0,1fr))">{cards}</div></div></section>
<article style="padding-top:10px">{h.get('body') or auto_body(h, prods)}{guide}
<h2>Preguntas frecuentes</h2>{''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in h['faq'])}
</article></main>'''
    os.makedirs(os.path.join(OUT, h['slug']), exist_ok=True)
    open(os.path.join(OUT, h['slug'], 'index.html'), 'w', encoding='utf-8').write(head(h['title'], (h['desc'] if len(h['desc']) >= 140 or len(h['desc']) + 44 > 160 else h['desc'] + ' Fabricados en Costa Rica por Químicas Arji.'), url, 'https://quimicasarji.com' + hsrc, ldh) + body + FOOT)
    return h['slug']



def thumbs_dir():
    """Miniaturas livianas (360 px) para tarjetas y galerías pequeñas."""
    src = os.path.join(ROOT, 'productos_img'); dst = os.path.join(src, 't')
    os.makedirs(dst, exist_ok=True)
    try:
        from PIL import Image
    except ImportError:
        import shutil
        for f in os.listdir(src):
            if f.endswith('.jpg') and not os.path.exists(os.path.join(dst, f)): shutil.copy(os.path.join(src, f), os.path.join(dst, f))
        return
    for f in os.listdir(src):
        if not f.endswith('.jpg'): continue
        o = os.path.join(dst, f)
        if os.path.exists(o) and os.path.getmtime(o) >= os.path.getmtime(os.path.join(src, f)): continue
        im = Image.open(os.path.join(src, f)).convert('RGB'); im.thumbnail((360, 360))
        im.save(o, quality=78, optimize=True, progressive=True)

def index(built):
    cards = ''
    for c, name in CATS.items():
        items = [p for p in P if p['c'] == c and p['id'] in built]
        if not items: continue
        cards += f'<h2>{e(name)}</h2><div class="rel">' + ''.join(f'<a href="/productos/{slug(p["n"])}/"><img src="{isrc(p, 0, True)}" alt="{e(p["n"])} León Rojo" loading="lazy"><span>{e(p["n"])}</span></a>' for p in items) + '</div>'
    h = head('Productos León Rojo · Catálogo completo | Químicas Arji', 'Catálogo de productos químicos León Rojo hechos en Costa Rica: limpieza, taller y autos, construcción, madera y piscinas. Presentaciones, usos y seguridad.', 'https://quimicasarji.com/productos/', 'b1_14', '')
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(h + f'<main class="wrap prod"><nav class="crumbs"><a href="/">Inicio</a> › Productos</nav><section style="padding-top:16px"><span class="eyebrow">Catálogo León Rojo</span><h1>Nuestros productos</h1><img src="/productos/img/linea_completa_1.jpg" alt="Línea completa de productos León Rojo" style="width:100%;border-radius:12px;margin:8px 0 18px;background:#F2F2F0"><p class="lead">Fabricados en Costa Rica desde hace 29 años. Tocá un producto para ver presentaciones, usos y precauciones.</p></section><p><a class="btn btn-red" href="/fichas-tecnicas/">⬇ Fichas técnicas en PDF</a></p><h2>Guías por tema</h2><div class="uses">{''.join(f'<a class="use" style="text-decoration:none" href="{hurl(h)}">{e(h.get("label", h["h1"]))}</a>' for h in HUBS)}</div>{cards}<p style="padding-bottom:40px"></p></main>' + FOOT)


def fichas_index(built):
    d = os.path.join(OUT, 'fichas-tecnicas'); os.makedirs(d, exist_ok=True)
    for x in FT: shutil.copy(os.path.join(ROOT, 'fichas_pdf', x['file']), os.path.join(d, x['file']))
    url = 'https://quimicasarji.com/productos/fichas-tecnicas/'
    cards = ''
    for c, name in CATS.items():
        items = [x for x in FT if BYID.get(x['id'], {}).get('c') == c]
        if not items: continue
        rows = ''
        for x in items:
            p = BYID[x['id']]; nm = x['label'] or p['n']
            link = f'<a href="/productos/{built[x["id"]]}/">{e(nm)}</a>' if x['id'] in built else e(nm)
            rows += (f'<div class="ft"><img src="{isrc(p, 0, True)}" alt="{e(p["n"])} León Rojo" loading="lazy"><div><b>{link}</b>'
                     f'<small>{e(", ".join(p.get("pres", [])))}{" · Solo uso profesional" if p.get("pro") else ""}</small></div>'
                     f'<a class="btn btn-red" href="/productos/fichas-tecnicas/{x["file"]}" target="_blank" rel="noopener" download>⬇ PDF</a></div>')
        cards += f'<h2>{e(name)}</h2>{rows}'
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Fichas técnicas León Rojo", "url": url, "inLanguage": "es-CR", "publisher": {"@type": "Organization", "name": "Químicas Arji WGAC S.A."}}, ensure_ascii=False) + '</script>'
    h = head('Fichas técnicas León Rojo (PDF) | Químicas Arji · Costa Rica', 'Descargá las fichas técnicas de los productos León Rojo en PDF: modo de uso, diluciones, precauciones, datos técnicos, registro sanitario y presentaciones.', url, 'b1_14', ld)
    css = '<style>.ft{display:flex;align-items:center;gap:12px;padding:10px 0;border-bottom:1px solid #e5e5e2}.ft img{width:56px;height:56px;object-fit:contain;border-radius:8px;background:#F2F2F0}.ft div{flex:1;min-width:0}.ft b{display:block}.ft b a{color:inherit}.ft small{color:#666;font-size:.85rem}.ft .btn{white-space:nowrap;padding:8px 14px}</style>'
    body = (f'{css}<main class="wrap prod"><nav class="crumbs"><a href="/">Inicio</a> › <a href="/productos/">Productos</a> › Fichas técnicas</nav>'
            f'<section style="padding-top:16px"><span class="eyebrow">Para clientes, ferreterías e instituciones</span><h1>Fichas técnicas León Rojo</h1>'
            f'<p class="lead">Cada ficha trae el modo de uso, las diluciones, las precauciones, los primeros auxilios, los datos técnicos, el registro del Ministerio de Salud y las presentaciones. Descargalas en PDF o pedí las fichas de datos de seguridad por WhatsApp al 8994-4763.</p></section>'
            f'{cards}<p class="note" style="margin:24px 0 40px">¿Sos ferretería, distribuidor, cadena o institución? <a href="{wa("Hola Químicas Arji, tengo un negocio y quiero información de distribución de León Rojo.")}" target="_blank" rel="noopener">Pedí condiciones por WhatsApp</a>.</p></main>')
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(h + body + FOOT)
    return 'fichas-tecnicas'


if __name__ == '__main__':
    posts = json.load(open(os.path.join(ROOT, 'posts.json'), encoding='utf-8'))
    ids = sys.argv[1:] or [p['id'] for p in P if not p.get('pro') and os.path.exists(os.path.join(ROOT, 'fichas', p['id'] + '.json'))]
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    thumbs_dir()
    shutil.copytree(os.path.join(ROOT, 'productos_img'), os.path.join(OUT, 'img'))
    built = {}
    for pid in ids:
        built[pid] = page(BYID[pid], ficha(pid), posts)
    index(built)
    hubs = [x for x in (hub(h, posts) for h in HUBS) if x]
    for p in P:  # asegurar nombres para todas las fotos de productos publicados
        if p['id'] in built:
            for k in range(len(p['img'])): iname(p, k)
    for (pid, k), n in IMGMAP.items():
        src = BYID[pid]['img'][k]
        for sub in ('', 't'):
            a_ = os.path.join(OUT, 'img', sub, src + '.jpg')
            if os.path.exists(a_): shutil.copy(a_, os.path.join(OUT, 'img', sub, n + '.jpg'))
    lic_url = LICENSE
    os.makedirs(os.path.join(OUT, 'uso-de-imagenes'), exist_ok=True)
    lic_body = f'''<main class="wrap" style="max-width:760px;padding:40px 16px">
<nav class="crumbs"><a href="/">Inicio</a> › <a href="/productos/">Productos</a> › Uso de imágenes</nav>
<h1>Uso de las fotos de productos León Rojo</h1>
<p>Las fotos de productos publicadas en quimicasarji.com son propiedad de <b>Químicas Arji WGAC S.A.</b>, fabricante de los productos León Rojo en Costa Rica. Todos los derechos reservados.</p>
<p>Si sos ferretería, distribuidor o medio de comunicación y querés usar alguna de estas fotos, escribinos y te respondemos con gusto:</p>
<ul><li>WhatsApp: <a href="{wa('Hola Químicas Arji, quiero usar fotos de productos León Rojo.')}" target="_blank" rel="noopener">8994-4763</a></li><li>Teléfono: 2250-2064</li><li>Correo: qarjisa@hotmail.com</li></ul>
<p><a href="/productos/">Ver todos los productos León Rojo</a></p>
</main>'''
    open(os.path.join(OUT, 'uso-de-imagenes', 'index.html'), 'w', encoding='utf-8').write(head('Uso de las fotos de productos León Rojo | Químicas Arji', 'Las fotos de productos León Rojo son propiedad de Químicas Arji WGAC S.A. Si querés usar alguna para vender o publicar nuestros productos, escribinos por WhatsApp.', lic_url, 'https://quimicasarji.com/productos/img/acido-muriatico-29-leon-rojo.jpg', '') + lic_body + FOOT)
    _php = open(os.path.join(ROOT, 'productos_resenas_php.tmpl'), encoding='utf-8').read()
    open(os.path.join(OUT, 'resenas.php'), 'w', encoding='utf-8').write(_php)
    json.dump({u: v for u, v in IMAGES.items() if u != '_'}, open(os.path.join(OUT, 'images.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    json.dump([f'https://quimicasarji.com/productos/{s}/' for s in hubs + list(built.values())], open(os.path.join(OUT, 'urls.json'), 'w'))
    print('ok', len(built), list(built.values()))
