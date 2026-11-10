"""Génère presplash.png (écran de démarrage Android) et icon.png (icône de l'appli) si absents.
Utilise les images déjà intégrées dans assets_data.py. Lancé automatiquement par la compilation."""
import base64
import io
import os

from PIL import Image

from assets_data import DATA


def img(n):
    return Image.open(io.BytesIO(base64.b64decode(DATA[n]))).convert('RGBA')


def vgrad(w, h, top, bot):
    g = Image.new('RGB', (1, h))
    for y in range(h):
        t = y / max(1, h - 1)
        g.putpixel((0, y), tuple(int(top[i] * (1 - t) + bot[i] * t) for i in range(3)))
    return g.resize((w, h)).convert('RGBA')


if not os.path.exists('presplash.png'):
    W, H = 1280, 720
    bg = vgrad(W, H, (12, 18, 40), (6, 8, 16))
    logo = img('logo')
    k = 0.85
    logo = logo.resize((int(logo.width * k), int(logo.height * k)), Image.LANCZOS)
    bg.alpha_composite(logo, ((W - logo.width) // 2, (H - logo.height) // 2 - 40))
    for i, n in enumerate(('em_kingdom', 'em_horde', 'em_sylvan')):
        e = img(n).resize((84, 84), Image.LANCZOS)
        bg.alpha_composite(e, (W // 2 - 140 + i * 98, H // 2 + 150))
    bg.convert('RGB').save('presplash.png')
if not os.path.exists('icon.png'):
    S = 512
    ic = vgrad(S, S, (40, 60, 120), (14, 22, 52))
    e = img('em_kingdom').resize((380, 380), Image.LANCZOS)
    ic.alpha_composite(e, (66, 60))
    ic.save('icon.png')
print('presplash.png et icon.png prêts')
