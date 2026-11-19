from ucgen import Diagram

d = Diagram(1700, 770)
d.boundary(200, 30, 1090, 640, "Zwolnione: rezerwacja")

C1, C2 = 440, 1010
d.usecase("UC02", C1, 140, "UC-02", "Wyszukaj salon")
d.usecase("UC03", C1, 320, "UC-03", "Zarezerwuj wizytę")
d.usecase("UC07", C1, 590, "UC-07", "Przyjmij ofertę terminu", improved=True)
d.usecase("UC09", C2, 125, "UC-09", "Wykorzystaj kupon", improved=True)
d.usecase("UC06", C2, 270, "UC-06", "Zapisz się na listę\noczekujących", improved=True)
d.usecase("UC15", C2, 470, "UC-15", "Wyślij powiadomienie")

d.actor("Klient", 90, 360, "Klient")
d.actor("Dostawca", 1400, 450, "Dostawca\npowiadomień", system=True)
d.actor("Bramka", 1600, 450, "Bramka\npłatności", system=True)

d.assoc("Klient", "UC02")
d.assoc("Klient", "UC03")
d.assoc("Klient", "UC07")
d.assoc("UC15", "Dostawca")
d.assoc("UC03", "Bramka", via=[(1250, 370), (1500, 370)])
d.assoc("UC07", "Bramka", via=[(1250, 590), (1500, 590)])

d.dep("UC09", "UC03", "extend", "tylko gdy klient ma ważny kupon", label_at=0.45)
d.dep("UC06", "UC03", "extend", "tylko gdy brak wolnych terminów", label_at=0.55)
d.dep("UC03", "UC15", "include", label_at=0.55)
d.dep("UC07", "UC15", "include", label_at=0.5)

d.legend(200, 725)
d.save_png("uc_1_rezerwacja.png")
