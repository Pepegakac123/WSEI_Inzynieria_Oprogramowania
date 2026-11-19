from ucgen import Diagram

d = Diagram(1760, 960)
d.boundary(260, 30, 1200, 600, "Zwolnione: mapa przypadków użycia")

W, H = 400, 110
C1, C2 = 620, 1100
d.area("A1", C1, 140, W, H, "1. Rezerwacja", "UC-02, 03, 06, 07, 09, 15")
d.area("A2", C1, 320, W, H, "2. Odwołanie i potwierdzanie", "UC-04, 05, 08, 14, 15")
d.area("A3", C1, 500, W, H, "3. Konto, obecność i ocena", "UC-01, 10, 11, 12, 13")
d.area("A4", C2, 140, W, H, "4. Praca salonu", "UC-13, 15, 16, 17, 18")
d.area("A5", C2, 320, W, H, "5. Uruchomienie salonu", "UC-19 do UC-24")
d.area("A6", C2, 500, W, H, "6. Rozliczenia i administracja", "UC-15, UC-25 do UC-30")

d.actor("Klient", 110, 330, "Klient")
d.actor("Pracownik", 1640, 130, "Pracownik")
d.actor("Wlasciciel", 1640, 330, "Właściciel")
d.actor("Admin", 1640, 530, "Administrator")
d.actor("Bramka", 640, 760, "Bramka płatności", system=True)
d.actor("Dostawca", 1080, 760, "Dostawca powiadomień", system=True)
d.note(640, 848, "obszary 1, 2, 4, 6")
d.note(1080, 848, "obszary 1, 2, 4, 6")

for a in ("A1", "A2", "A3"):
    d.assoc("Klient", a)
d.assoc("Pracownik", "A4")
for a in ("A4", "A5", "A6"):
    d.assoc("Wlasciciel", a)
d.assoc("Admin", "A6")

# Systemy zewnętrzne łączą się z ramką, a nie z każdym obszarem osobno:
# pełne połączenia dałyby nieuniknione przecięcia linii.
d.point("ramka_b", 640, 630)
d.point("ramka_d", 1080, 630)
d.assoc("Bramka", "ramka_b")
d.assoc("Dostawca", "ramka_d")

d.legend(260, 915, deps=False, improved=False, assoc_text="aktor korzysta z obszaru")
d.save_png("uc_0_mapa.png")
