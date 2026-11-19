from ucgen import Diagram

d = Diagram(1820, 1000)
d.boundary(220, 30, 1360, 660, "Zwolnione: rozliczenia i administracja")

d.usecase("UC25", 470, 140, "UC-25", "Włącz abonament", improved=True)
d.usecase("UC26", 470, 310, "UC-26", "Podważ prowizję", improved=True)
d.usecase("UC15", 1040, 330, "UC-15", "Wyślij powiadomienie")
d.usecase("UC28", 470, 560, "UC-28", "Rozpatrz zgłoszenie\nprowizji", improved=True)
d.usecase("UC27", 800, 560, "UC-27", "Zatwierdź salon")
d.usecase("UC29", 1110, 560, "UC-29", "Zmień uprawnienia")
d.usecase("UC30", 1400, 560, "UC-30", "Zmień konfigurację\nsystemu")

d.actor("Wlasciciel", 100, 230, "Właściciel")
d.actor("Admin", 900, 820, "Administrator")
d.actor("Bramka", 1700, 140, "Bramka\npłatności", system=True)
d.actor("Dostawca", 1700, 330, "Dostawca\npowiadomień", system=True)

d.assoc("Wlasciciel", "UC25")
d.assoc("Wlasciciel", "UC26")
for uc in ("UC28", "UC27", "UC29", "UC30"):
    d.assoc("Admin", uc)
d.assoc("UC25", "Bramka")
d.assoc("UC15", "Dostawca")
d.dep("UC28", "UC15", "include", label_at=0.45)
d.dep("UC27", "UC15", "include", label_at=0.5)

d.legend(220, 955)
d.save_png("uc_6_rozliczenia.png")
