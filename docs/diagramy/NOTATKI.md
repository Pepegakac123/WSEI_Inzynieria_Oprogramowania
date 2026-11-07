# Notatki do diagramów rozdziału 3

Stan na 07.11.2026. Rozdział 3 jest w trakcie. Wzorzec do naśladowania: `uc_2_odwolanie`.

## Stan prac

| Etap | Stan |
|---|---|
| Lista przypadków użycia i relacji | uzgodniona |
| Styl diagramów | uzgodniony, wzorzec `uc_2_odwolanie` |
| Diagram 1 Rezerwacja | próbka, linie do Bramki wychodzą dołem ramki i wymagają poprawy |
| Diagram 2 Odwołanie i potwierdzanie | gotowy |
| Diagramy 3–6 i mapa całości | do zrobienia |
| Szare tło dla usprawnień | do zrobienia na wszystkich diagramach |
| Tabela aktorów, główne scenariusze, opis pod diagramami | do zrobienia w `docs/03_przypadki_uzycia_i_aktywnosc.md` |
| 3.2 Diagram aktywności | do zrobienia |
| Status rozdziału w `README.md` | zaktualizować po ukończeniu |

## Zasady czytelności

1. Najwyżej 7 przypadków na diagram, podział tematyczny.
2. Format poziomy. Wysoki obraz jest zmniejszany do wysokości ekranu i tekst staje się nieczytelny.
3. Zero przecięć linii. Sprawdzać to na renderze, a nie zakładać.
4. Styl z `_styl.iuml`: czarno-biały, czcionka 18, grubsze linie.
5. Nazwa przypadku w dwóch liniach: numer, potem cel.
6. Na każdym diagramie legenda „Jak czytać”.
7. Warunek przy `extend` prostymi słowami: „tylko gdy…”.
8. Przypadki z usprawnień mają szare tło, a podstawowe białe.
9. Pod każdym diagramem w dokumencie krótki opis zdaniami, zrozumiały bez znajomości UML.

## Jak ułożyć diagram w PlantUML

- Renderowanie: `plantuml -tpng plik.puml`, potem `-tsvg`. Nazwa pliku wynikowego pochodzi z `@startuml nazwa`.
- `@startuml` zaczyna każdy diagram, a `!include _styl.iuml` dodaje styl.
- `UC08 <.. UC04` stawia przypadek bazowy w lewej kolumnie, a rozszerzenie po prawej. Tak dostajemy krótką, prostą strzałkę `extend`.
- Liczba kresek ustawia odległość: `Klient --- UC04` to dwie kolumny, `UC05 ...> UC14` trzy.
- `-[norank]-` rysuje linię, która nie wpływa na układ. `-[hidden]-` wpływa na układ, ale nie jest rysowana.
- Kolejność aktorów ma znaczenie. W `uc_2_odwolanie` Dostawca jest zadeklarowany przed Bramką, żeby ich linie się nie przecinały.

Czego nie robić:
- jednokropkowego `.>` z etykietą, bo strzałka w tej samej kolumnie zatacza łuki przez inne linie;
- łańcuchów `-[hidden]>` do ustawiania kolejności, bo Graphviz ich nie pilnuje;
- `!pragma layout smetana`, bo daje te same kolizje;
- `!pragma layout elk`, bo nie działa na tej instalacji.

Jeśli przecięcia nie da się usunąć, przenieść przypadek na inny diagram. Dotyczy to UC-03 i UC-07, które łączą się z tymi samymi trzema elementami. W razie potrzeby UC-07 zmienia diagram.

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

## Do 3.2

Zalecany proces to rezerwacja wizyty, a usprawnienie musi być widoczne także na diagramie aktywności. Punkt 1.4 zapowiada rozgałęzienie: *czy ktoś czeka?* → oferta → *przyjął / minął czas?* → następna osoba / termin wraca do puli. Do rozstrzygnięcia: jeden diagram czy dwa, rezerwacja oraz odwołanie z kolejką.

W diagramie aktywności PlantUML trzeba podawać tor jawnie w każdej gałęzi, np. `|System|` po `else`. Inaczej krok trafia do toru poprzedniego uczestnika.

`uc_klient` i `uc_salon` to stare, nieczytelne wersje. Nie są w repo i można je usunąć po zrobieniu sześciu diagramów.
