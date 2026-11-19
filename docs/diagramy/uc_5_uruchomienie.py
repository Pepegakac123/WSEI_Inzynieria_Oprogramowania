from ucgen import Diagram

d = Diagram(1180, 900)
d.boundary(240, 30, 900, 780, "Zwolnione: uruchomienie salonu")

# Jedna kolumna w lekkim łuku: linie od aktora rozchodzą się wachlarzem
CASES = [
    ("UC19", "UC-19", "Zarejestruj salon", False),
    ("UC20", "UC-20", "Ustal usługi i cennik", False),
    ("UC21", "UC-21", "Ustal zasady odwołań", False),
    ("UC22", "UC-22", "Załóż konto pracownika", False),
    ("UC23", "UC-23", "Zaimportuj bazę klientów", True),
    ("UC24", "UC-24", "Pobierz kod QR salonu", True),
]
n = len(CASES)
for i, (key, code, name, improved) in enumerate(CASES):
    t = (i - (n - 1) / 2) / ((n - 1) / 2)
    d.usecase(key, 700 + 90 * (1 - t * t), 140 + i * 120, code, name, improved=improved)

d.actor("Wlasciciel", 110, 440, "Właściciel")
for key, *_ in CASES:
    d.assoc("Wlasciciel", key)

d.legend(240, 860, deps=False)
d.save_png("uc_5_uruchomienie.png")
