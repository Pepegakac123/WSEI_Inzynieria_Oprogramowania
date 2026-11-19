"""Generator diagramów aktywności w stylu diagramów przypadków użycia.

Tory są pionowymi kolumnami, przepływ idzie z góry na dół. Pozycje węzłów
podajemy sami (tor + wysokość), a linie prowadzimy przez punkty pośrednie.
"""
import math
from xml.sax.saxutils import escape

from ucgen import INK, MUTED, IMPROVED_FILL, Diagram, text_width


class Activity(Diagram):
    def __init__(self, lanes, lane_w=340, top=110, height=1400, left=20, title=None):
        self.lanes = lanes
        self.lane_w = lane_w
        self.left = left
        self.top = top
        width = left * 2 + lane_w * len(lanes)
        super().__init__(width, height)
        header = 56
        y0 = top - header
        if title:
            self.parts.append(f'<text x="{width / 2}" y="{y0 - 22}" text-anchor="middle" '
                              f'font-size="22" font-weight="bold" fill="{INK}">'
                              f'{escape(title)}</text>')
        body_h = height - y0 - 90
        for i, name in enumerate(lanes):
            x = left + i * lane_w
            self.parts.append(
                f'<rect x="{x}" y="{y0}" width="{lane_w}" height="{body_h}" fill="none" '
                f'stroke="{INK}" stroke-width="1.6"/>'
                f'<rect x="{x}" y="{y0}" width="{lane_w}" height="{header}" fill="#f2f2f4" '
                f'stroke="{INK}" stroke-width="1.6"/>'
                f'<text x="{x + lane_w / 2}" y="{y0 + 36}" text-anchor="middle" font-size="19" '
                f'font-weight="bold" fill="{INK}">{escape(name)}</text>')
        self.body_bottom = y0 + body_h

    def lx(self, lane, dx=0):
        """Środek toru (indeks albo nazwa) z opcjonalnym przesunięciem."""
        i = lane if isinstance(lane, int) else self.lanes.index(lane)
        return self.left + i * self.lane_w + self.lane_w / 2 + dx

    # ---------- węzły ----------
    def start(self, key, lane, y, dx=0):
        x = self.lx(lane, dx)
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="15" fill="{INK}"/>')
        self.nodes[key] = ("circle", x, y, 15, 15)

    def end(self, key, lane, y, dx=0, label=None):
        x = self.lx(lane, dx)
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="17" fill="#fff" stroke="{INK}" '
                          f'stroke-width="2.2"/><circle cx="{x}" cy="{y}" r="10" fill="{INK}"/>')
        if label:
            self.note(x, y + 42, label, size=15)
        self.nodes[key] = ("circle", x, y, 17, 17)

    def action(self, key, lane, y, text, dx=0, improved=False, size=17, w=None):
        x = self.lx(lane, dx)
        lines = text.split("\n")
        tw = max(text_width(l, size) for l in lines)
        w = w or max(tw + 40, 170)
        h = len(lines) * size * 1.3 + 26
        fill = IMPROVED_FILL if improved else "#fff"
        out = [f'<rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" '
               f'rx="16" fill="{fill}" stroke="{INK}" stroke-width="2"/>']
        y0 = y - (len(lines) - 1) * size * 1.3 / 2 + size * 0.35
        for i, l in enumerate(lines):
            out.append(f'<text x="{x}" y="{y0 + i * size * 1.3:.1f}" text-anchor="middle" '
                       f'font-size="{size}" fill="{INK}">{escape(l)}</text>')
        self.parts.append("".join(out))
        self.nodes[key] = ("rect", x, y, w / 2, h / 2)

    def decision(self, key, lane, y, question=None, dx=0, side="right", improved=False):
        """Romb decyzji/scalenia. Pytanie stoi obok rombu, kursywą."""
        x = self.lx(lane, dx)
        a, b = 26, 26
        fill = IMPROVED_FILL if improved else "#fff"
        self.parts.append(f'<polygon points="{x},{y - b} {x + a},{y} {x},{y + b} {x - a},{y}" '
                          f'fill="{fill}" stroke="{INK}" stroke-width="2"/>')
        if question:
            lines = question.split("\n")
            if side == "right":
                tx, anchor = x + a + 10, "start"
            elif side == "left":
                tx, anchor = x - a - 10, "end"
            else:  # nad rombem
                tx, anchor = x, "middle"
            ty = y - b - 10 - (len(lines) - 1) * 19 if side == "top" else y - 16 - (len(lines) - 1) * 9
            for i, l in enumerate(lines):
                self.parts.append(f'<text x="{tx}" y="{ty + i * 19:.1f}" text-anchor="{anchor}" '
                                  f'font-size="15" font-style="italic" fill="{MUTED}">'
                                  f'{escape(l)}</text>')
        self.nodes[key] = ("diamond", x, y, a, b)

    # ---------- geometria ----------
    def _clip(self, key, toward):
        kind, cx, cy, a, b = self.nodes[key]
        dx, dy = toward[0] - cx, toward[1] - cy
        if dx == 0 and dy == 0:
            return cx, cy
        if kind == "diamond":
            t = 1 / (abs(dx) / a + abs(dy) / b)
            return cx + dx * t, cy + dy * t
        if kind == "circle":
            d = math.hypot(dx, dy)
            return cx + dx * a / d, cy + dy * a / d
        return super()._clip(key, toward)

    # ---------- przepływ ----------
    def flow(self, src, dst, via=(), guard=None, guard_at=0, gdx=0, gdy=0, anchor="middle"):
        """Strzałka przepływu. `guard` to warunek w nawiasach kwadratowych.

        `via` to punkty pośrednie; `guard_at` = numer odcinka, przy którego
        początku stoi warunek; gdx/gdy przesuwają etykietę.
        """
        pts = self._path(src, dst, via)
        out = [f'<path d="{self._d(pts, radius=18)}" fill="none" stroke="{INK}" '
               f'stroke-width="2"/>']
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        ang = math.atan2(y2 - y1, x2 - x1)
        L, s = 14, 0.42
        out.append(f'<polygon points="{x2},{y2} '
                   f'{x2 - L * math.cos(ang + s):.1f},{y2 - L * math.sin(ang + s):.1f} '
                   f'{x2 - L * math.cos(ang - s):.1f},{y2 - L * math.sin(ang - s):.1f}" '
                   f'fill="{INK}"/>')
        if guard:
            (ax, ay) = pts[guard_at]
            gx, gy = ax + gdx, ay + gdy
            w = text_width(guard, 15) + 12
            bx = gx - w / 2 if anchor == "middle" else (gx if anchor == "start" else gx - w)
            out.append(f'<rect x="{bx:.1f}" y="{gy - 15:.1f}" width="{w:.1f}" height="22" '
                       f'rx="4" fill="#fff"/>'
                       f'<text x="{bx + w / 2:.1f}" y="{gy + 1:.1f}" text-anchor="middle" '
                       f'font-size="15" fill="{INK}">{escape(guard)}</text>')
        self.parts.append("".join(out))

    def activity_legend(self, x, y, improved=True):
        items = [f'<text x="{x + 18}" y="{y + 6}" font-size="15" font-weight="bold" '
                 f'fill="{INK}">Jak czytać:</text>']
        cx = x + 18 + text_width("Jak czytać:", 15, True) + 22

        def label(t, at):
            items.append(f'<text x="{at}" y="{y + 6}" font-size="15" fill="{INK}">{escape(t)}</text>')
            return at + text_width(t, 15) + 30

        items.append(f'<circle cx="{cx + 9}" cy="{y}" r="9" fill="{INK}"/>')
        cx = label("start", cx + 26)
        items.append(f'<circle cx="{cx + 10}" cy="{y}" r="10" fill="#fff" stroke="{INK}" '
                     f'stroke-width="2"/><circle cx="{cx + 10}" cy="{y}" r="5.5" fill="{INK}"/>')
        cx = label("koniec", cx + 28)
        items.append(f'<polygon points="{cx + 12},{y - 12} {cx + 24},{y} {cx + 12},{y + 12} '
                     f'{cx},{y}" fill="#fff" stroke="{INK}" stroke-width="1.6"/>')
        cx = label("decyzja, warunki w [ ]", cx + 32)
        if improved:
            items.append(f'<rect x="{cx}" y="{y - 11}" width="40" height="22" rx="8" '
                         f'fill="{IMPROVED_FILL}" stroke="{INK}" stroke-width="1.5"/>')
            cx = label("krok z usprawnienia", cx + 50)
        w = cx - x - 12
        self.parts.append(f'<rect x="{x}" y="{y - 22}" width="{w}" height="44" rx="6" '
                          f'fill="#fafafa" stroke="#c8c8cc" stroke-width="1.2"/>' + "".join(items))
