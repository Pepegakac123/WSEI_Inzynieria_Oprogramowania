from ucgen import Diagram

d = Diagram(1760, 960)
d.boundary(200, 30, 1240, 660, "Zwolnione: praca salonu")

C1, C2, C3 = 450, 790, 1220
d.usecase("UC13", C1, 130, "UC-13", "Przejrzyj swoje wizyty")
d.usecase("UC18", C1, 290, "UC-18", "Oznacz przebieg wizyty")
d.usecase("UC16", C1, 560, "UC-16", "Prowadź grafik")
d.usecase("UC17", C2, 420, "UC-17", "Odwołaj wizytę\njako salon")
d.usecase("UC15", C3, 420, "UC-15", "Wyślij powiadomienie")

d.actor("Pracownik", 100, 330, "Pracownik")
d.actor("Wlasciciel", 640, 790, "Właściciel")
d.actor("Bramka", 1620, 170, "Bramka\npłatności", system=True)
d.actor("Dostawca", 1620, 420, "Dostawca\npowiadomień", system=True)

for uc in ("UC13", "UC18", "UC16", "UC17"):
    d.assoc("Pracownik", uc)
d.assoc("Wlasciciel", "UC16")
d.assoc("Wlasciciel", "UC17")
d.assoc("UC17", "Bramka")
d.assoc("UC15", "Dostawca")
d.dep("UC17", "UC15", "include", label_at=0.5)

d.legend(200, 915, improved=False)
d.save_png("uc_4_salon.png")
