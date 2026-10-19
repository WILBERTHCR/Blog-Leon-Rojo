"""Crea fotos limpias (fondo uniforme 242,242,240, sin bordes visibles) en productos_img/<img>.jpg"""
import sys, os, numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__)); from prep import flat_bbox, T
SRC = sys.argv[1]; OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'productos_img'); os.makedirs(OUT, exist_ok=True)
for name in sys.argv[2:]:
    dst = os.path.join(OUT, name + '.jpg')
    if os.path.exists(dst): continue
    src = Image.open(os.path.join(SRC, name + '.jpg')).convert('RGB'); g = np.asarray(src.convert('L')).astype(int)
    pad = g[2, 2]; rows = np.where((np.abs(g - pad) <= 2).mean(1) < .97)[0]; cols = np.where((np.abs(g - pad) <= 2).mean(0) < .97)[0]
    if len(rows) and len(cols) and (rows[-1] - rows[0] < g.shape[0] * .97 or cols[-1] - cols[0] < g.shape[1] * .97):
        src = src.crop((cols[0] + 3, rows[0] + 3, cols[-1] - 3, rows[-1] - 3))
    tmp = os.path.join(OUT, '_tmp.png'); src.save(tmp)
    try: a, (x0, y0, x1, y1) = flat_bbox(tmp)
    except Exception: a, (x0, y0, x1, y1) = flat_bbox(os.path.join(SRC, name + '.jpg'))
    os.remove(tmp)
    mg = int(max(y1 - y0, x1 - x0) * .08); h, w = a.shape[:2]
    p = Image.fromarray(a[max(0, y0 - mg):min(h, y1 + mg), max(0, x0 - mg):min(w, x1 + mg)].astype(np.uint8))
    W, H = 800, 1000; sc = min((W * .86) / p.width, (H * .86) / p.height); p = p.resize((int(p.width * sc), int(p.height * sc)), Image.LANCZOS)
    pw, ph = p.size; yy, xx = np.mgrid[0:ph, 0:pw]; d = np.minimum(np.minimum(xx, pw - 1 - xx), np.minimum(yy, ph - 1 - yy)).astype(float)
    t = np.clip(d / (min(pw, ph) * .07), 0, 1); al = Image.fromarray((t * t * (3 - 2 * t) * 255).astype(np.uint8))
    c = Image.new('RGB', (W, H), tuple(int(v) for v in T)); c.paste(p, ((W - pw) // 2, (H - ph) // 2), al); c.save(dst, quality=88)
    print(name)
