from ucgen import Diagram

d = Diagram(1180, 780)
d.boundary(240, 30, 900, 660, "Zwolnione: konto, obecność i ocena")

# Jedna kolumna w lekkim łuku: linie od aktora rozchodzą się wachlarzem
CASES = [
    ("UC01", "UC-01", "Utwórz konto", False),
    ("UC13", "UC-13", "Przejrzyj swoje wizyty", False),
    ("UC10", "UC-10", "Zeskanuj kod QR", True),
    ("UC11", "UC-11", "Zgłoś sprzeciw „Byłem”", True),
    ("UC12", "UC-12", "Oceń wizytę", True),
]
n = len(CASES)
for i, (key, code, name, improved) in enumerate(CASES):
    t = (i - (n - 1) / 2) / ((n - 1) / 2)
    d.usecase(key, 700 + 90 * (1 - t * t), 140 + i * 120, code, name, improved=improved)

d.actor("Klient", 110, 380, "Klient")
for key, *_ in CASES:
    d.assoc("Klient", key)

d.legend(240, 740, deps=False)
d.save_png("uc_3_konto.png")
