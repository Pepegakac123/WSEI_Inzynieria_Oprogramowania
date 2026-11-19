from ucgen import Diagram

d = Diagram(1640, 770)
d.boundary(200, 30, 1200, 640, "Zwolnione: odwołanie i potwierdzanie")

C1, C2, C3 = 440, 820, 1200
d.usecase("UC08", C1, 140, "UC-08", "Potwierdź wizytę", improved=True)
d.usecase("UC04", C1, 360, "UC-04", "Odwołaj wizytę")
d.usecase("UC05", C1, 590, "UC-05", "Przełóż wizytę", improved=True)
d.usecase("UC14", C2, 540, "UC-14", "Zaproponuj termin\nkolejce", improved=True)
d.usecase("UC15", C3, 380, "UC-15", "Wyślij powiadomienie")

d.actor("Klient", 90, 360, "Klient")
d.actor("Bramka", 1540, 170, "Bramka\npłatności", system=True)
d.actor("Dostawca", 1540, 380, "Dostawca\npowiadomień", system=True)

d.assoc("Klient", "UC08")
d.assoc("Klient", "UC04")
d.assoc("Klient", "UC05")
d.assoc("UC04", "Bramka")
d.assoc("UC15", "Dostawca")

d.dep("UC04", "UC08", "extend", "tylko gdy klient wybiera „Nie przyjdę”", label_at=0.5)
d.dep("UC04", "UC14", "include", label_at=0.5)
d.dep("UC05", "UC14", "include", label_at=0.5)
d.dep("UC14", "UC15", "include", label_at=0.5)
d.dep("UC04", "UC15", "include", label_at=0.5)

d.legend(200, 725)
d.save_png("uc_2_odwolanie.png")
