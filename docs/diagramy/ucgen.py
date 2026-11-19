"""Prosty generator diagramów przypadków użycia z ręcznym układem.

Pozycje elementów podajemy sami, więc linie idą tam, gdzie chcemy.
Wynik: PNG (SVG powstaje tylko w pamięci i trafia do rsvg-convert).
"""
import math
import subprocess
from xml.sax.saxutils import escape

from PIL import ImageFont

FONT_FILE = "/usr/share/fonts/noto/NotoSans-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/noto/NotoSans-Bold.ttf"
FAMILY = "Noto Sans"
INK = "#1d1d1f"
MUTED = "#55555a"
IMPROVED_FILL = "#e4e4e7"

_fonts = {}


def text_width(text, size, bold=False):
    key = (size, bold)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(FONT_BOLD if bold else FONT_FILE, size)
    return _fonts[key].getlength(text)


class Diagram:
    def __init__(self, width, height, title=None):
        self.w, self.h = width, height
        self.parts = []
        self.nodes = {}
        self.title = title

    # ---------- elementy ----------
    def boundary(self, x, y, w, h, title):
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="none" '
            f'stroke="{INK}" stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + 34}" text-anchor="middle" font-size="21" '
            f'font-weight="bold" fill="{INK}">{escape(title)}</text>'
        )

    def usecase(self, key, x, y, code, name, improved=False, size=18):
        lines = name.split("\n")
        tw = max([text_width(code, size - 2, True)] + [text_width(l, size) for l in lines])
        th = (len(lines) + 1) * size * 1.25
        rx = tw / 2 * 1.18 + 26
        ry = th / 2 * 1.25 + 12
        self.nodes[key] = ("uc", x, y, rx, ry)
        fill = IMPROVED_FILL if improved else "#fff"
        out = [f'<ellipse cx="{x}" cy="{y}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" '
               f'stroke="{INK}" stroke-width="2"/>']
        all_lines = [(code, size - 2, True)] + [(l, size, False) for l in lines]
        y0 = y - th / 2 + size * 0.95
        for i, (t, s, b) in enumerate(all_lines):
            weight = ' font-weight="bold"' if b else ""
            color = MUTED if b else INK
            out.append(f'<text x="{x}" y="{y0 + i * size * 1.25:.1f}" text-anchor="middle" '
                       f'font-size="{s}"{weight} fill="{color}">{escape(t)}</text>')
        self.parts.append("".join(out))

    def actor(self, key, x, y, name, system=False, size=18):
        # (x, y) = środek figurki
        hy = y - 30
        out = [
            f'<g stroke="{INK}" stroke-width="2.2" fill="none" stroke-linecap="round">',
            f'<circle cx="{x}" cy="{hy}" r="11" fill="#fff"/>',
            f'<line x1="{x}" y1="{hy + 11}" x2="{x}" y2="{y + 14}"/>',
            f'<line x1="{x - 20}" y1="{y - 6}" x2="{x + 20}" y2="{y - 6}"/>',
            f'<line x1="{x}" y1="{y + 14}" x2="{x - 16}" y2="{y + 40}"/>',
            f'<line x1="{x}" y1="{y + 14}" x2="{x + 16}" y2="{y + 40}"/>',
            "</g>",
        ]
        ty = y + 64
        for i, l in enumerate(name.split("\n")):
            out.append(f'<text x="{x}" y="{ty + i * size * 1.2:.1f}" text-anchor="middle" '
                       f'font-size="{size}" fill="{INK}">{escape(l)}</text>')
        if system:
            out.append(f'<text x="{x}" y="{hy - 20}" text-anchor="middle" font-size="14" '
                       f'font-style="italic" fill="{MUTED}">«system»</text>')
        self.parts.append("".join(out))
        # kotwica linii: okolice ramion, prostokąt do przycinania
        self.nodes[key] = ("actor", x, y, 26, 72 if system else 48)

    def area(self, key, x, y, w, h, title, items, improved=False):
        """Obszar na mapie całości: zaokrąglony prostokąt z nazwą i listą przypadków."""
        fill = IMPROVED_FILL if improved else "#fff"
        out = [f'<rect x="{x - w / 2}" y="{y - h / 2}" width="{w}" height="{h}" rx="14" '
               f'fill="{fill}" stroke="{INK}" stroke-width="2"/>',
               f'<text x="{x}" y="{y - h / 2 + 34}" text-anchor="middle" font-size="19" '
               f'font-weight="bold" fill="{INK}">{escape(title)}</text>']
        for i, l in enumerate(items.split("\n")):
            out.append(f'<text x="{x}" y="{y - h / 2 + 64 + i * 22}" text-anchor="middle" '
                       f'font-size="15" fill="{MUTED}">{escape(l)}</text>')
        self.parts.append("".join(out))
        self.nodes[key] = ("rect", x, y, w / 2, h / 2)

    def point(self, key, x, y):
        """Niewidoczny punkt zaczepienia linii, np. na krawędzi ramki systemu."""
        self.nodes[key] = ("pt", x, y, 0, 0)

    def note(self, x, y, text, size=15, anchor="middle"):
        for i, l in enumerate(text.split("\n")):
            self.parts.append(f'<text x="{x}" y="{y + i * size * 1.3:.1f}" text-anchor="{anchor}" '
                              f'font-size="{size}" font-style="italic" fill="{MUTED}">'
                              f'{escape(l)}</text>')

    # ---------- geometria ----------
    def _clip(self, key, toward):
        kind, cx, cy, a, b = self.nodes[key]
        dx, dy = toward[0] - cx, toward[1] - cy
        if (dx == 0 and dy == 0) or kind == "pt":
            return cx, cy
        if kind == "uc":
            t = 1 / math.sqrt((dx / a) ** 2 + (dy / b) ** 2)
        else:
            t = min(a / abs(dx) if dx else 1e9, b / abs(dy) if dy else 1e9)
        return cx + dx * t, cy + dy * t

    def _center(self, key):
        return self.nodes[key][1], self.nodes[key][2]

    def _path(self, src, dst, via):
        pts = [self._center(src)] + list(via) + [self._center(dst)]
        pts[0] = self._clip(src, pts[1])
        pts[-1] = self._clip(dst, pts[-2])
        return pts

    @staticmethod
    def _d(pts, radius=40):
        """Ścieżka z zaokrąglonymi narożnikami w punktach pośrednich."""
        if len(pts) == 2:
            return f"M{pts[0][0]:.1f},{pts[0][1]:.1f} L{pts[1][0]:.1f},{pts[1][1]:.1f}"
        d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
        for i in range(1, len(pts) - 1):
            p0, p1, p2 = pts[i - 1], pts[i], pts[i + 1]
            l1 = math.dist(p0, p1)
            l2 = math.dist(p1, p2)
            r = min(radius, l1 / 2, l2 / 2)
            a = (p1[0] + (p0[0] - p1[0]) * r / l1, p1[1] + (p0[1] - p1[1]) * r / l1)
            c = (p1[0] + (p2[0] - p1[0]) * r / l2, p1[1] + (p2[1] - p1[1]) * r / l2)
            d += f" L{a[0]:.1f},{a[1]:.1f} Q{p1[0]:.1f},{p1[1]:.1f} {c[0]:.1f},{c[1]:.1f}"
        d += f" L{pts[-1][0]:.1f},{pts[-1][1]:.1f}"
        return d

    # ---------- relacje ----------
    def assoc(self, a, b, via=()):
        pts = self._path(a, b, via)
        self.parts.insert(0, f'<path d="{self._d(pts)}" fill="none" stroke="{INK}" '
                             f'stroke-width="2"/>')

    def dep(self, src, dst, kind, condition=None, via=(), label_at=0.5, label_dx=0, label_dy=0):
        """include/extend: przerywana strzałka od src do dst z etykietą."""
        pts = self._path(src, dst, via)
        out = [f'<path d="{self._d(pts)}" fill="none" stroke="{INK}" stroke-width="1.8" '
               f'stroke-dasharray="9 6"/>']
        # grot otwarty
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        ang = math.atan2(y2 - y1, x2 - x1)
        L, s = 15, 0.42
        for sign in (-1, 1):
            out.append(f'<line x1="{x2}" y1="{y2}" x2="{x2 - L * math.cos(ang + sign * s):.1f}" '
                       f'y2="{y2 - L * math.sin(ang + sign * s):.1f}" stroke="{INK}" '
                       f'stroke-width="2" stroke-linecap="round"/>')
        # etykieta na wybranym odcinku
        seg = min(int(label_at), len(pts) - 2)
        frac = (label_at - int(label_at)) or 0.5
        (ax, ay), (bx, by) = pts[seg], pts[seg + 1]
        lx = ax + (bx - ax) * frac + label_dx
        ly = ay + (by - ay) * frac + label_dy
        lines = [(f"«{kind}»", 15, True)]
        if condition:
            lines.append((condition, 15, False))
        w = max(text_width(t, s) for t, s, _ in lines) + 16
        h = len(lines) * 20 + 8
        out.append(f'<rect x="{lx - w / 2:.1f}" y="{ly - h / 2:.1f}" width="{w:.1f}" '
                   f'height="{h}" rx="5" fill="#fff" fill-opacity="0.94"/>')
        for i, (t, s, b) in enumerate(lines):
            style = ' font-style="italic"' if not b else ""
            out.append(f'<text x="{lx:.1f}" y="{ly - h / 2 + 19 + i * 20:.1f}" '
                       f'text-anchor="middle" font-size="{s}"{style} fill="{INK}">'
                       f'{escape(t)}</text>')
        self.parts.append("".join(out))

    # ---------- legenda ----------
    def legend(self, x, y, improved=True, deps=True, assoc_text="aktor korzysta z przypadku"):
        items = []
        cx = x + 18
        def label(t, at):
            items.append(f'<text x="{at}" y="{y + 6}" font-size="15" fill="{INK}">{escape(t)}</text>')
            return at + text_width(t, 15) + 36
        items.append(f'<text x="{cx}" y="{y + 6}" font-size="15" font-weight="bold" '
                     f'fill="{INK}">Jak czytać:</text>')
        cx += text_width("Jak czytać:", 15, True) + 22
        items.append(f'<line x1="{cx}" y1="{y}" x2="{cx + 44}" y2="{y}" stroke="{INK}" stroke-width="2"/>')
        cx = label(assoc_text, cx + 54)
        if deps:
            items.append(f'<line x1="{cx}" y1="{y}" x2="{cx + 44}" y2="{y}" stroke="{INK}" '
                         f'stroke-width="1.8" stroke-dasharray="9 6"/>'
                         f'<polyline points="{cx + 34},{y - 6} {cx + 44},{y} {cx + 34},{y + 6}" '
                         f'fill="none" stroke="{INK}" stroke-width="2"/>')
            cx = label("«include» zawsze  ·  «extend» tylko gdy warunek", cx + 54)
        if improved:
            items.append(f'<ellipse cx="{cx + 22}" cy="{y}" rx="22" ry="12" fill="{IMPROVED_FILL}" '
                         f'stroke="{INK}" stroke-width="1.5"/>')
            cx = label("usprawnienie Zwolnione", cx + 54)
        w = cx - x - 18
        self.parts.append(f'<rect x="{x}" y="{y - 22}" width="{w}" height="44" rx="6" '
                          f'fill="#fafafa" stroke="#c8c8cc" stroke-width="1.2"/>' + "".join(items))

    # ---------- zapis ----------
    def save_png(self, path, scale=2):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
               f'viewBox="0 0 {self.w} {self.h}" font-family="{FAMILY}">'
               f'<rect width="100%" height="100%" fill="#fff"/>' + "".join(self.parts) + "</svg>")
        subprocess.run(["rsvg-convert", "-z", str(scale), "-o", path],
                       input=svg.encode(), check=True)
