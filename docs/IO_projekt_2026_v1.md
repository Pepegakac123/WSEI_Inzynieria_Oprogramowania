# Inżynieria Oprogramowania

## Temat projektu

Projektujecie marketplace rezerwacji usług, czyli system łączący klientów z usługodawcami (fryzjerzy, barberzy, kosmetyczki, fizjoterapeuci, groomerzy). System obsługuje poniższy zakres oraz zawiera usprawnienia względem Booksy, które sami zaproponujecie. Produktowi nadajecie własną nazwę. Referencja: Booksy, <u>[https://booksy.com/](https://booksy.com/)</u>

|Obszar|Zakres|
|---|---|
|Salon i usługi|Rejestracja salonu, usługi z czasem trwania i ceną, pracownicy salonu|
|Grafik|Godziny pracy pracowników, wyliczanie wolnych terminów|
|Rezerwacja|Wybór usługi, pracownika i terminu, potwierdzenie, blokada kolizji|
|Odwołanie wizyty|Po stronie klienta i salonu, obowiązująca zasada odwołania|
|Powiadomienia|Potwierdzenie rezerwacji, przypomnienie o wizycie|

Do powyższego zakresu dochodzi minimum jeden dodatkowy obszar, wynikający z waszego usprawnienia.

## Aktorzy

|Aktor|Odpowiedzialność|
|---|---|
|Klient|Wyszukuje usługi, rezerwuje i odwołuje wizyty, przegląda swoje wizyty|
|Pracownik salonu|Prowadzi swój grafik, widzi swoje wizyty, oznacza wizyty jako odbyte|
|Właściciel salonu|Rejestruje salon, definiuje usługi i cennik, zakłada konta pracowników|
|Administrator|Zatwierdza zgłoszone salony, zarządza uprawnieniami i konfiguracją systemu|
|System zewnętrzny|Bramka SMS lub e-mail wysyłająca powiadomienia|

## Harmonogram zajęć i powstawania dokumentu

|Zajęcia|Data|Temat zajęć|Rozdział dokumentu|
|---|---|---|---|
|1|03.10.2026|Cykl życia oprogramowania|1. Analiza i usprawnienia|
|2|17.10.2026|Inżynieria wymagań|2. Wymagania systemowe|
|3|07.11.2026|UML: modelowanie zachowań|3. Przypadki użycia, diagram aktywności|
|4|21.11.2026|UML: modelowanie architektury|4. Diagram klas|
|5|05.12.2026|Proces wytwarzania oprogramowania|5. Harmonogram i ryzyka|
|6|19.12.2026|Wzorce projektowe, testowanie (zdalnie na Teams)|6. Wzorce i strategia testowania|
|7|16.01.2027|Prezentacje projektów|Prezentacja i oddanie dokumentu|

## 1. Analiza Booksy i usprawnienia

- Minimum 2 mocne strony Booksy
- Jedna luka produktowa lub bolączka po stronie klienta i jedna po stronie salonu
- Minimum jedno usprawnienie, które wprowadza wasz produkt, wraz z uzasadnieniem
- Jakie elementy zostaną pominięte w modelowaniu
- Nazwa produktu Przykładowe kierunki usprawnień:
- Lista oczekujących, która automatycznie powiadamia klienta o zwolnionym terminie
- Program lojalnościowy odblokowujący zniżki
- Zakup vouchera dla innego użytkownika
- Kampanie marketingowe z promocjami Usprawnienie powinno wpływać na działanie systemu i być widoczne w kolejnych rozdziałach dokumentu.

## 2. Wymagania systemowe

**2.1. Wymagania funkcjonalne** Zakres, który należy przygotować:
- Opis funkcji systemu
- Interakcje użytkownika z systemem
- Reakcje systemu na zdarzenia
- Scenariusz podstawowy i alternatywny dla najważniejszych wymagań
- Wymagania obejmujące także wprowadzone usprawnienie Każde wymaganie ma identyfikator, aktora i opis. Sprawdźcie przy każdym, czy da się zweryfikować jego spełnienie. Uwzględnijcie wszystkich aktorów z tabeli powyżej.
## 2.2. Wymagania niefunkcjonalne

Wymagania powinny pokrywać obszary:

- Wydajność i skalowalność
- Ergonomia interfejsu
- Bezpieczeństwo danych, w tym ochrona danych osobowych klientów
- Niezawodność
- Standardy jakości Każde wymaganie zapisujcie z konkretną wartością liczbową. Przykład: wyszukiwanie wolnych terminów zwraca wynik poniżej 500 ms dla 95% żądań.
## 3. UML: modelowanie zachowań

Narzędzie dowolne: Mermaid, PlantUML, draw.io, Modelio. Diagram musi być czytelny po wydruku.

**3.1. Diagram przypadków użycia**
- Opis aktorów i głównych scenariuszy
- Tabela aktorów z zakresem odpowiedzialności
- Aktorzy klienta, usługodawcy, moderacji oraz systemy zewnętrzne
- Relacje include i extend
## 3.2. Diagram aktywności

Model przepływu logiki działania wybranego procesu, zalecany proces rezerwacji wizyty

- Węzeł początkowy i końcowy
- Węzły decyzyjne z opisanymi warunkami
- Tory dla uczestników procesu Uwzględnijcie także przebiegi, w których proces nie kończy się powodzeniem.
## 4. UML: modelowanie architektury

**4.1. Diagram klas** Odwzorowanie struktury systemu:
- Klasy
- Atrybuty
- Metody
- Relacje: asocjacje, dziedziczenie, kompozycja, agregacja
- Krotności relacji
- Klasy wynikające z wprowadzonego usprawnienia Klasy powinny zawierać metody odpowiadające działaniom systemu. Zadbajcie o zgodność z diagramami z rozdziału 3.

## 5. Harmonogramowanie projektu

- Szacowanie pracochłonności metodą COCOMO II: przyjęte parametry, obliczenia, wynik w osobotygodniach, czas trwania i liczebność zespołu
- Uzasadnienie przyjętych parametrów
- Etapy projektu: nazwa, czas trwania, produkty etapu
- Harmonogram w postaci wykresu Gantta
- Ryzyka wraz z poziomem i sposobem redukcji Zadbajcie o zgodność harmonogramu z wynikiem szacowania. Ryzyka mają dotyczyć waszego projektu.
## 6. Wzorce projektowe i strategia testowania

**6.1. Wzorce projektowe**
- Minimum 2 wzorce projektowe adekwatne do projektu
- Powód wyboru, wynikający z konkretnej funkcji systemu
- Implementacja w pseudokodzie
- Wpływ wzorca na strukturę systemu, czyli jak wyglądałby system bez niego
## 6.2. Strategia testowania

- Opis strategii testowania w układzie piramidy testów: udział testów jednostkowych, integracyjnych i e2e, zakres każdego poziomu, narzędzie, kryterium akceptacji
- Wskazanie, które elementy systemu pokrywają testy integracyjne i e2e
- Przykłady testów jednostkowych, w tym test sprawdzający sytuację błędną
- Opis narzędzi testujących
- Interpretacja wyników testów