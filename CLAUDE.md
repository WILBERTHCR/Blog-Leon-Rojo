# Blog León Rojo — instrucciones para publicar artículos

Este repositorio publica el blog de https://quimicasarji.com/blog/ (Químicas Arji WGAC S.A., marca León Rojo, Costa Rica).
El servidor (cPanel) hace `git pull` cada hora y copia `blog/`, `redes/`, `productos/`, `site/index.html` y `sitemap.xml` a `public_html`. Todo lo que se sube a `main` queda publicado en máximo una hora.

## Estructura
- `posts.json` — lista de artículos (slug, title, desc, img, date AAAA-MM-DD, cta [img, nombre, texto], kw).
- `posts/<slug>.html` — cuerpo del artículo (HTML simple: `<p class="lead">`, `<h2>`, `<h3>`, `<ul>`, `<ol>`, `<p>`, y avisos `<div class="warn"><b>⚠ Seguridad:</b> …</div>`).
- `tools/build.py` — genera `blog/` y `sitemap.xml`. **Siempre correrlo antes de hacer commit.**
- `productos.md` — productos, imágenes disponibles y presentaciones reales. Usar SOLO estos datos.
- `blog/` y `sitemap.xml` — salida generada (no editar a mano). `blog/latest.json` alimenta la sección "Guías prácticas" de la página principal.
- `site/data.js` — catálogo y reseñas de la página principal (window.GOOGLE = calificación; window.REVIEWS = reseñas reales copiadas de Google, sin inventar).
- `site/index.html` — página principal de quimicasarji.com (el servidor la copia a public_html). Editar solo si se pide un cambio en la web.
- `productos/` — páginas de producto (quimicasarji.com/productos/<slug>/), generadas con `python3 tools/build_products.py` desde `catalogo.json` + `fichas/<id>.json` (fuente: `tools/fichas_src.py`). Fotos limpias en `productos_img/` (`tools/clean_imgs.py`). Correr build_products antes de build.py para que el sitemap las incluya. No editar `productos/` a mano.
- `redes/` — imágenes de las publicaciones de Facebook/Instagram, publicadas en quimicasarji.com/redes/.

## Cómo publicar un artículo nuevo
1. Elegir un tema que la gente busque en Google en Costa Rica y que se resuelva con un producto de `productos.md`. No repetir temas ya publicados en `posts.json`.
2. Escribir `posts/<slug>.html` (600–900 palabras) y agregar su entrada en `posts.json` con la fecha de hoy.
3. `python3 tools/build.py`
4. `git add -A && git commit -m "Artículo: <título>" && git push`

## Reglas de contenido (obligatorias)
- Español de Costa Rica con voseo ("podés", "escribinos"), tono práctico y cercano.
- Productos químicos: incluir siempre un aviso de seguridad. Nunca mezclar ácidos, cloro, vinagre ni desatoradores entre sí. Recomendar guantes, lentes y ventilación.
- **No inventar dosis, tiempos ni concentraciones** que no estén en `productos.md`: remitir siempre a "lo que indica la etiqueta".
- No inventar propiedades, certificaciones, precios ni reseñas. Presentaciones: solo las de `productos.md`. En publicidad se dice "litro" y "galón" (no ml).
- Productos marcados como uso profesional (Formalina, Bicromato) no se promocionan en el blog.
- Contacto: WhatsApp 8994-4763, tel. 2250-2064.
