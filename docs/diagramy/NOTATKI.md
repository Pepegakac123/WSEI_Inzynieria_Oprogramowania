# Notatki do diagramów rozdziału 3

Stan na 19.11.2026. Rozdział 3 jest gotowy: tekst w `docs/03_przypadki_uzycia_i_aktywnosc.md`.

## Stan prac

| Etap | Stan |
|---|---|
| Lista przypadków użycia i relacji | uzgodniona |
| Narzędzie | własny generator `ucgen.py` zamiast PlantUML |
| Diagramy 1–6 i mapa całości | gotowe, bez przecięć linii |
| Szare tło dla usprawnień | gotowe na wszystkich diagramach |
| Tabela aktorów, główne scenariusze, opis pod diagramami | gotowe w `docs/03_przypadki_uzycia_i_aktywnosc.md` |
| 3.2 Diagramy aktywności | gotowe: `ad_1_rezerwacja`, `ad_2_szybka_zamiana` (generator `adgen.py`) |
| Status rozdziału w `README.md` | zaktualizowany |

## Pliki

| Plik | Diagram |
|---|---|
| `uc_0_mapa.py` | mapa całości: aktorzy i sześć obszarów |
| `uc_1_rezerwacja.py` | 1. Rezerwacja |
| `uc_2_odwolanie.py` | 2. Odwołanie i potwierdzanie |
| `uc_3_konto.py` | 3. Konto, obecność i ocena |
| `uc_4_salon.py` | 4. Praca salonu |
| `uc_5_uruchomienie.py` | 5. Uruchomienie salonu |
| `uc_6_rozliczenia.py` | 6. Rozliczenia i administracja |

| `ad_1_rezerwacja.py` | 3.2a. Diagram aktywności: rezerwacja wizyty |
| `ad_2_szybka_zamiana.py` | 3.2b. Diagram aktywności: odwołanie i Szybka Zamiana |

Każdy skrypt tworzy PNG o tej samej nazwie. Renderowanie wszystkich: `for f in uc_*.py ad_*.py; do python3 $f; done`. Diagramy aktywności używają `adgen.py`: tory to kolumny, węzły ustawiamy przez tor i wysokość, a `flow(..., via=[...], guard="[warunek]")` rysuje strzałkę z warunkiem. Wymaga Pythona z Pillow, `rsvg-convert` i czcionki Noto Sans.

## Dlaczego własny generator

PlantUML i D2 same układają elementy, więc linie się wyginają, przecinają albo łamią pod kątem prostym. W `ucgen.py` pozycję każdego elementu podajemy sami, a generator przycina linie do krawędzi elips, rysuje grot, etykietę z białym tłem i legendę z rysunkami.

## Zasady czytelności

1. Najwyżej 7 przypadków na diagram, podział tematyczny.
2. Format poziomy. Wysoki obraz jest zmniejszany do wysokości ekranu i tekst staje się nieczytelny.
3. Zero przecięć linii. Sprawdzać to na renderze, a nie zakładać.
4. Styl czarno-biały, Noto Sans 18, linie 2 px.
5. W elipsie numer przypadku pogrubiony, pod nim cel.
6. Na każdym diagramie legenda „Jak czytać”.
7. Warunek przy `extend` prostymi słowami: „tylko gdy…”.
8. Przypadki z usprawnień mają szare tło, a podstawowe białe.
9. Pod każdym diagramem w dokumencie krótki opis zdaniami, zrozumiały bez znajomości UML.

## Jak ułożyć diagram w `ucgen.py`

- `d.usecase(klucz, x, y, "UC-xx", "Nazwa", improved=True)`: elipsa, rozmiar liczony z tekstu.
- `d.actor(klucz, x, y, "Nazwa", system=True)`: figurka, przy systemach dopisek «system».
- `d.assoc(a, b, via=[(x, y), ...])`: linia aktora; `via` dodaje punkty pośrednie z zaokrąglonymi narożnikami.
- `d.dep(src, dst, "include" lub "extend", "tylko gdy…", label_at=0.5)`: przerywana strzałka od `src` do `dst`. `label_at` przesuwa etykietę wzdłuż linii.
- `d.area(...)`, `d.point(...)`, `d.note(...)`: obszary, niewidoczne punkty zaczepienia i dopiski na mapie.

Pułapka: gdy dwa przypadki łączą się z tymi samymi trzema elementami (np. UC-03 i UC-07 z Klientem, Bramką i UC-15), przecięcia nie da się uniknąć na płaszczyźnie (graf K3,3). Wtedy jedna linia musi obejść aktora, jak linie do Bramki na diagramie 1, albo przypadek trzeba przenieść na inny diagram.

Na mapie Bramka i Dostawca łączą się z ramką systemu, a nie z każdym obszarem, z tego samego powodu. Pod nazwą jest dopisek, których obszarów dotyczą.

## Podział na diagramy

| # | Diagram | Przypadki | Aktorzy |
|---|---|---|---|
| 1 | Rezerwacja | UC-02, 03, 06, 07, 09, 15 | Klient, Bramka, Dostawca |
| 2 | Odwołanie i potwierdzanie | UC-04, 05, 08, 14, 15 | Klient, Bramka, Dostawca |
| 3 | Konto, obecność i ocena | UC-01, 10, 11, 12, 13 | Klient |
| 4 | Praca salonu | UC-13, 15, 16, 17, 18 | Pracownik, Właściciel, Bramka, Dostawca |
| 5 | Uruchomienie salonu | UC-19 do UC-24 | Właściciel |
| 6 | Rozliczenia i administracja | UC-15, UC-25 do UC-30 | Właściciel, Administrator, Bramka, Dostawca |

Mapa całości pokazuje tylko aktorów i sześć obszarów, bez `include` i `extend`. Zadanie mówi o „diagramie” w liczbie pojedynczej, więc warto zapytać prowadzącego, czy podział mu odpowiada.

## Przypadki użycia

| ID | Przypadek | Wymaganie | Aktor |
|---|---|---|---|
| UC-01 | Utwórz konto | WF-30 | Klient |
| UC-02 | Wyszukaj salon | WF-12 | Klient |
| UC-03 | Zarezerwuj wizytę | WF-01 | Klient, Bramka |
| UC-04 | Odwołaj wizytę | WF-02 | Klient, Bramka |
| UC-05 | Przełóż wizytę | WF-15 | Klient |
| UC-06 | Zapisz się na listę oczekujących | WF-03 | przez `extend` z UC-03 |
| UC-07 | Przyjmij ofertę terminu | WF-05 | Klient, Bramka |
| UC-08 | Potwierdź wizytę | WF-06, WF-24 | Klient |
| UC-09 | Wykorzystaj kupon | WF-08 | przez `extend` z UC-03 |
| UC-10 | Zeskanuj kod QR | WF-25 | Klient |
| UC-11 | Zgłoś sprzeciw „Byłem” | WF-26 | Klient |
| UC-12 | Oceń wizytę | WF-29 | Klient |
| UC-13 | Przejrzyj swoje wizyty | WF-22 | Klient, Pracownik |
| UC-14 | Zaproponuj termin kolejce | WF-04 | fragment wspólny |
| UC-15 | Wyślij powiadomienie | wiele | Dostawca powiadomień |
| UC-16 | Prowadź grafik | WF-10 | Pracownik, Właściciel |
| UC-17 | Odwołaj wizytę jako salon | WF-14 | Pracownik, Właściciel, Bramka |
| UC-18 | Oznacz przebieg wizyty | WF-11 | Pracownik |
| UC-19 | Zarejestruj salon | WF-21 | Właściciel |
| UC-20 | Ustal usługi i cennik | WF-09 | Właściciel |
| UC-21 | Ustal zasady odwołań | WF-17 | Właściciel |
| UC-22 | Załóż konto pracownika | WF-18 | Właściciel |
| UC-23 | Zaimportuj bazę klientów | WF-19 | Właściciel |
| UC-24 | Pobierz kod QR salonu | WF-28 | Właściciel |
| UC-25 | Włącz abonament | WF-13 | Właściciel, Bramka |
| UC-26 | Podważ prowizję | WF-16 | Właściciel |
| UC-27 | Zatwierdź salon | WF-20 | Administrator |
| UC-28 | Rozpatrz zgłoszenie prowizji | WF-16 | Administrator |
| UC-29 | Zmień uprawnienia | WF-23 | Administrator |
| UC-30 | Zmień konfigurację systemu | WF-23 | Administrator |

**`include`:**
- UC-04 i UC-05 → UC-14
- UC-03, UC-04, UC-07, UC-14, UC-17, UC-27 i UC-28 → UC-15

**`extend`:**
- UC-06 → UC-03, tylko gdy brak wolnych terminów
- UC-09 → UC-03, tylko gdy klient ma ważny kupon
- UC-04 → UC-08, tylko gdy klient wybiera „Nie przyjdę”

## Uzgodnione decyzje

- Sześciu aktorów z rozdziału 2. Pracownik i Właściciel bez dziedziczenia, wspólne przypadki mają dwie linie.
- CEIDG i KRS nie są aktorami, bo dane sprawdza Administrator (WF-20).
- WF-07 (kupon) i WF-27 (licznik) to kroki systemu, więc nie są przypadkami użycia. Pokazujemy je w scenariuszach i na diagramie aktywności.
- WF-06 i WF-24 tworzą jeden przypadek. WF-16 i WF-23 dzielą się na dwa.
- Bramka łączy się bezpośrednio z przypadkami, które pobierają lub zwracają pieniądze.
- Odwołanie przez salon nie uruchamia kolejki, bo WF-14 tego nie przewiduje.
- Logowania nie modelujemy.
