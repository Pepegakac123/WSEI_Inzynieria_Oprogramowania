# Rozdział 2. Wymagania systemowe

> Stan na 06.11.2026. Wymagania opisują aplikację z rozdziału 1, z usprawnieniami „Szybka Zamiana” i „Prowizja z limitem i dowodem”. Wartości liczbowe to nasze założenia projektowe.

## Aktorzy

| Aktor | Kim jest |
|---|---|
| **Klient** | rezerwuje wizyty, odwołuje je, zapisuje się na listę oczekujących |
| **Pracownik** | wykonuje usługi, widzi swój grafik, oznacza przebieg wizyty |
| **Właściciel** | zarządza salonem, usługami, pracownikami i zasadami odwołań |
| **Administrator** | zatwierdza salony, zarządza uprawnieniami i konfiguracją systemu, rozstrzyga zgłoszenia dotyczące prowizji |
| **Bramka płatności** | zewnętrzny system, który pobiera i zwraca pieniądze |
| **Dostawca powiadomień** | zewnętrzny system, który wysyła SMS i push |

---

## 2.1. Wymagania funkcjonalne

### WF-01. Rezerwacja wizyty

**Aktor:** Klient

**Opis:** klient rezerwuje wolny termin na wybraną usługę.

**Scenariusz podstawowy:**
1. Klient wybiera salon i usługę.
2. Klient wybiera pracownika albo opcję „dowolny dostępny”.
3. System wyświetla wolne terminy na najbliższe 14 dni.
4. Klient wybiera termin, a system pokazuje zasady odwołania i wymaganą płatność.
5. Klient potwierdza i, jeśli salon tego wymaga, wpłaca zadatek.
6. System tworzy wizytę, wysyła potwierdzenie i planuje prośbę o potwierdzenie „Będę”.

**Scenariusze alternatywne:**
- **3a. Brak wolnych terminów:** system proponuje zapis na listę oczekujących (WF-03).
- **4a. Klient rezygnuje:** wizyta nie powstaje.
- **5a. Termin zajęty w trakcie rezerwacji:** system informuje o zajęciu, odświeża listę i nie tworzy wizyty.
- **5b. Płatność się nie powiodła:** system nie tworzy wizyty i pozwala spróbować ponownie.

**Warunki poprawności:** RB-01, RB-02, RB-03, RB-04.

### WF-02. Odwołanie wizyty

**Aktor:** Klient

**Opis:** klient odwołuje wizytę i przed potwierdzeniem widzi skutki finansowe.

**Scenariusz podstawowy:**
1. Klient wybiera wizytę i opcję „Odwołaj”.
2. System sprawdza, czy klient mieści się w czasie darmowego odwołania.
3. System pokazuje kwotę i dalszy los zadatku.
4. Klient potwierdza odwołanie.
5. System zwalnia termin i uruchamia kolejkę (WF-04).
6. System wysyła potwierdzenie klientowi i powiadamia pracownika.

**Scenariusze alternatywne:**
- **2a. Odwołanie w darmowym czasie:** system zleca bramce płatności zwrot zadatku.
- **4a. Klient rezygnuje:** wizyta pozostaje bez zmian.
- **5a. Lista oczekujących jest pusta:** termin wraca do puli wolnych terminów.

**Warunki poprawności:** RB-05, RB-08.

### WF-03. Zapis na listę oczekujących

**Aktor:** Klient

**Opis:** klient zapisuje się na okno czasowe, gdy nie ma pasującego terminu.

**Scenariusz podstawowy:**
1. Klient wybiera salon, usługę oraz pracownika albo opcję „dowolny”.
2. Klient podaje okno czasowe, np. „pn–śr po 16:00”.
3. System zapisuje wpis i pokazuje klientowi jego kolejność.

**Scenariusze alternatywne:**
- **2a. Okno czasowe jest w przeszłości:** system pokazuje błąd przy polu.
- **3a. Klient ma już aktywne 3 wpisy:** system odmawia zapisu i informuje o limicie.

**Warunki poprawności:** RB-09.

### WF-04. Wysłanie oferty terminu

**Aktor:** System, Dostawca powiadomień

**Opis:** po zwolnieniu terminu system proponuje go osobom z listy oczekujących.

**Scenariusz podstawowy:**
1. Termin się zwalnia.
2. System wybiera pierwszą pasującą osobę z listy.
3. System rezerwuje termin dla tej osoby na czas oferty.
4. System wysyła ofertę przez push i SMS.

**Scenariusze alternatywne:**
- **2a. Nikt nie pasuje:** termin wraca do puli wolnych terminów.
- **3a. Do wizyty zostało mniej niż 2 godziny:** system wysyła ofertę do wszystkich pasujących osób bez wyłączności.
- **4a. Oferta wygasa bez odpowiedzi:** system wraca do kroku 2 i wybiera następną osobę.
- **4b. Klient odrzuca ofertę:** system od razu wraca do kroku 2.

**Warunki poprawności:** RB-06, RB-10, RB-11, RB-17, RB-18.

### WF-05. Przyjęcie oferty terminu

**Aktor:** Klient

**Opis:** klient z listy oczekujących przyjmuje zaproponowany termin.

**Scenariusz podstawowy:**
1. Klient otwiera ofertę i widzi usługę, termin i wymaganą płatność.
2. Klient klika „Przyjmuję” i, jeśli salon tego wymaga, wpłaca zadatek.
3. System tworzy wizytę i usuwa klienta z listy oczekujących.
4. System rozlicza zadatek poprzedniego klienta (WF-07).
5. System powiadamia pracownika o zmianie klienta.

**Scenariusze alternatywne:**
- **1a. Oferta wygasła:** system informuje, że termin jest już niedostępny.
- **2a. Termin zajęty przez inną osobę (oferta dla wszystkich):** system informuje o zajęciu i nie tworzy wizyty.
- **2b. Płatność się nie powiodła:** oferta trwa do swojego końca, a klient może spróbować ponownie.

**Warunki poprawności:** RB-01, RB-10.

### WF-06. Potwierdzenie wizyty „Będę”

**Aktor:** Klient, System

**Opis:** klient potwierdza dzień wcześniej, że przyjdzie na wizytę.

**Scenariusz podstawowy:**
1. Na 24 h przed wizytą system wysyła prośbę o potwierdzenie.
2. Klient klika „Będę”.
3. System oznacza wizytę jako potwierdzoną i pokazuje to pracownikowi.

**Scenariusze alternatywne:**
- **1a. Wizyta powstała mniej niż 24 h przed terminem:** system nie prosi o potwierdzenie.
- **2a. Klient klika „Nie przyjdę”:** system przechodzi do WF-02.
- **2b. Brak reakcji przez 6 h:** system wysyła drugie przypomnienie.
- **2c. Brak potwierdzenia do 12 h przed wizytą, wizyta bez zadatku:** system uruchamia kolejkę (WF-04), ale wizyta klienta zostaje do czasu przyjęcia oferty.
- **2d. Ktoś przyjął ofertę z kroku 2c:** system odwołuje wizytę i powiadamia klienta.
- **2e. Brak potwierdzenia, wizyta z zadatkiem:** wizyta zostaje, a pracownik widzi status „niepotwierdzona”.

**Warunki poprawności:** RB-07.

### WF-07. Zadatek na kolejną wizytę

**Aktor:** System

**Opis:** gdy termin odwołany po czasie zostanie przejęty, zadatek staje się kwotą do wykorzystania.

**Scenariusz podstawowy:**
1. System wykrywa, że odwołany po czasie termin ma nową wizytę.
2. System tworzy kwotę na wizytę w wysokości zadatku za termin.
3. System powiadamia klienta o kwocie i dacie ważności.

**Scenariusze alternatywne:**
- **1a. Nikt nie przejął terminu do jego rozpoczęcia:** zadatek zostaje u salonu.
- **2a. Płatność ma opłatę za przygotowanie za wykonaną pracę:** ta część zostaje u salonu.

**Warunki poprawności:** RB-08, RB-12, RB-13, RB-19.

### WF-08. Wykorzystanie kwoty na wizytę

**Aktor:** Klient

**Opis:** klient wykorzystuje kwotę przy rezerwacji w tym samym salonie.

**Scenariusz podstawowy:**
1. Podczas rezerwacji system pokazuje dostępną kwotę.
2. Klient decyduje, czy jej użyć.
3. System odlicza kwotę od zadatku, a pozostałość od ceny wizyty.

**Scenariusze alternatywne:**
- **2a. Kwota wygasła:** system jej nie pokazuje.
- **3a. Klient odwoła wizytę w darmowym czasie:** kwota wraca z pierwotną datą ważności.
- **3b. Klient odwoła wizytę po czasie:** kwota jest rozliczana jak zwykły zadatek.

**Warunki poprawności:** RB-12, RB-13.

### WF-09. Usługi i cennik

**Aktor:** Właściciel

**Opis:** właściciel dodaje usługi oraz ustala ich ceny i czas trwania.

**Scenariusz podstawowy:**
1. Właściciel otwiera listę usług.
2. Właściciel dodaje usługę albo zmienia jej cenę lub czas trwania.
3. System zapisuje zmiany i stosuje je do nowych rezerwacji.

**Scenariusze alternatywne:**
- **2a. Dane są niepoprawne:** system pokazuje błąd przy polu i nie czyści formularza.

**Warunki poprawności:** RB-03, RB-04.

### WF-10. Grafik pracownika

**Aktor:** Pracownik, Właściciel

**Opis:** pracownik lub właściciel ustala godziny pracy i nieobecności, a system wylicza z nich wolne terminy.

**Scenariusz podstawowy:**
1. Użytkownik ustawia godziny pracy na wybrane dni.
2. System zapisuje grafik i przelicza wolne terminy.

**Scenariusze alternatywne:**
- **2a. Zmiana koliduje z istniejącą wizytą:** system blokuje zapis i pokazuje kolidujące wizyty.

**Warunki poprawności:** RB-01, RB-02.

### WF-11. Zakończenie wizyty

**Aktor:** Pracownik

**Opis:** pracownik oznacza, czy wizyta się odbyła.

**Scenariusz podstawowy:**
1. Pracownik wybiera wizytę i oznacza ją jako odbytą.
2. System rozlicza zadatek i kwotę na wizytę z ceną usługi.
3. Jeśli spełnione są warunki prowizji, system ją nalicza i zapisuje dowód.

**Scenariusze alternatywne:**
- **1a. Klient nie przyszedł:** pracownik oznacza nieobecność, a zadatek zostaje u salonu. System nie nalicza prowizji.
- **3a. Warunki prowizji nie są spełnione:** system nie nalicza prowizji.

**Warunki poprawności:** RB-04, RB-21, RB-22, RB-23.

### WF-12. Wyszukiwanie salonów

**Aktor:** Klient

**Opis:** klient wyszukuje salony po usłudze, lokalizacji i dostępności.

**Scenariusz podstawowy:**
1. Klient wpisuje usługę i lokalizację.
2. System zwraca salony posortowane według dopasowania.
3. Klient otwiera profil salonu.
4. Gdy klient przechodzi do rezerwacji, system zapisuje wyszukiwanie i czas przejścia.

**Scenariusze alternatywne:**
- **2a. Brak wyników:** system proponuje szerszy obszar wyszukiwania.

**Warunki poprawności:** RB-14, RB-22, RB-23.

### WF-13. Abonament i prowizje salonu

**Aktor:** Właściciel, Bramka płatności

**Opis:** salon płaci miesięczny abonament i prowizje naliczone za nowych klientów.

**Scenariusz podstawowy:**
1. Właściciel włącza abonament.
2. System co miesiąc sumuje abonament i prowizje z poprzedniego okresu.
3. System zleca bramce płatności pobranie kwoty.
4. Salon pozostaje widoczny w wyszukiwarce i przyjmuje rezerwacje.

**Scenariusze alternatywne:**
- **3a. Płatność się nie powiodła:** system informuje właściciela i ponawia próbę przez 7 dni.
- **3b. Abonament wygasł:** salon znika z wyszukiwarki, a istniejące wizyty zostają.
- **4a. Właściciel rezygnuje:** abonament kończy się na koniec opłaconego okresu.

**Warunki poprawności:** RB-15, RB-21.

### WF-14. Odwołanie wizyty przez salon

**Aktor:** Pracownik, Właściciel

**Opis:** salon odwołuje wizytę, a klient wybiera, co stanie się z jego pieniędzmi.

**Scenariusz podstawowy:**
1. Użytkownik wybiera wizytę i opcję „Odwołaj”.
2. System prosi o potwierdzenie i powód.
3. System odwołuje wizytę i powiadamia klienta.
4. Klient wybiera zwrot płatności albo nowy termin.

**Scenariusze alternatywne:**
- **4a. Klient nie wybierze przez 48 h:** system zleca pełny zwrot.

**Warunki poprawności:** RB-16.

### WF-15. Przełożenie wizyty

**Aktor:** Klient

**Opis:** klient zmienia termin wizyty bez utraty opłaty za przygotowanie.

**Scenariusz podstawowy:**
1. Klient wybiera wizytę i opcję „Przełóż”.
2. System pokazuje wolne terminy i skutki finansowe.
3. Klient wybiera nowy termin i potwierdza.
4. System przenosi wizytę i zwalnia stary termin (WF-04).

**Scenariusze alternatywne:**
- **3a. Termin zajęty w trakcie:** system odświeża listę i nie zmienia wizyty.

**Warunki poprawności:** RB-01, RB-02, RB-20.

### WF-16. Podważenie prowizji

**Aktor:** Właściciel, Administrator

**Opis:** właściciel sprawdza dowód prowizji i może ją podważyć, gdy klient był już w salonie.

**Scenariusz podstawowy:**
1. Właściciel otwiera listę prowizji i widzi dowód przy każdej z nich.
2. Właściciel zgłasza prowizję i wskazuje wcześniejszą wizytę klienta.
3. Administrator sprawdza zgłoszenie i je uznaje.
4. System cofa prowizję i powiadamia właściciela.

**Scenariusze alternatywne:**
- **2a. Minęło 30 dni od naliczenia prowizji:** system nie przyjmuje zgłoszenia.
- **3a. Administrator odrzuca zgłoszenie:** prowizja zostaje, a właściciel widzi powód.

**Warunki poprawności:** RB-23, RB-24.

### WF-17. Zasady odwołań i płatności z góry

**Aktor:** Właściciel

**Opis:** właściciel ustala czas darmowego odwołania oraz wysokość zadatku i opłaty za przygotowanie. System stosuje te zasady do nowych rezerwacji.

**Warunki poprawności:** RB-05.

### WF-18. Konta pracowników

**Aktor:** Właściciel

**Opis:** właściciel zakłada konta pracowników salonu.

### WF-19. Import bazy klientów

**Aktor:** Właściciel

**Opis:** właściciel wczytuje numery telefonów swoich klientów, a system nie nalicza za nich prowizji.

**Warunki poprawności:** RB-22.

### WF-20. Zatwierdzenie salonu

**Aktor:** Administrator

**Opis:** administrator sprawdza zgłoszony salon, a potem go zatwierdza albo odrzuca.

**Scenariusz podstawowy:**
1. Administrator otwiera zgłoszenie salonu z listy oczekujących na sprawdzenie.
2. Administrator sprawdza dane salonu i właściciela.
3. Administrator zatwierdza salon.
4. System aktywuje salon i powiadamia właściciela.

**Scenariusze alternatywne:**
- **3a. Salon nie spełnia wymagań:** administrator odrzuca zgłoszenie i podaje powód. System powiadamia właściciela, a salon pozostaje nieaktywny.
- **3b. Właściciel poprawia odrzucone zgłoszenie:** zgłoszenie wraca na listę do sprawdzenia.

**Warunki poprawności:** RB-25, RB-26.

### WF-21. Rejestracja salonu

**Aktor:** Właściciel

**Opis:** właściciel zakłada konto, podaje dane salonu i wysyła zgłoszenie do zatwierdzenia.

**Warunki poprawności:** RB-25.

### WF-22. Przeglądanie swoich wizyt

**Aktor:** Klient

**Opis:** klient widzi listę nadchodzących i minionych wizyt wraz z ich statusem.

### WF-23. Uprawnienia i konfiguracja

**Aktor:** Administrator

**Opis:** administrator nadaje i odbiera uprawnienia kont oraz zmienia ustawienia systemu, np. stawki abonamentu i prowizji.

---

### Reguły biznesowe

| ID | Reguła |
|---|---|
| RB-01 | Wizyta nie może kolidować z inną wizytą tego samego pracownika. |
| RB-02 | Wizyta musi mieścić się w czasie pracy pracownika. |
| RB-03 | Czas trwania wizyty wynika z usługi. |
| RB-04 | Cena wizyty jest ustalana w chwili rezerwacji. Późniejsza zmiana cennika nie ma na nią wpływu. |
| RB-05 | Zasady odwołania obowiązujące wizytę są ustalane w chwili rezerwacji. |
| RB-06 | Czas na decyzję wynosi 15 minut, gdy do wizyty zostało ponad 6 h, oraz 5 minut przy 2–6 h. Poniżej 2 h oferta idzie do wszystkich bez wyłączności. |
| RB-07 | Klient traci wizytę z powodu braku potwierdzenia tylko wtedy, gdy nie wpłacił zadatku i ktoś inny przyjął ofertę. |
| RB-08 | Przy odwołaniu po czasie zadatek zamienia się w kwotę na wizytę tylko wtedy, gdy nowa wizyta innej osoby zajmuje co najmniej połowę zwolnionego czasu. |
| RB-09 | Klient może mieć najwyżej 3 aktywne wpisy na listach oczekujących. |
| RB-10 | Jeden termin danego pracownika może przyjąć tylko jedna osoba. |
| RB-11 | Osoby z listy dostają ofertę według kolejności zapisu, a oferta musi pasować do okna czasowego, pracownika i długości usługi. |
| RB-12 | Kwotę na wizytę można wykorzystać tylko w salonie, który ją wydał, przez 3 miesiące od jej powstania. |
| RB-13 | Kwoty na wizytę nie można wypłacić ani przekazać innej osobie. |
| RB-14 | Kolejność wyników wyszukiwania nie może zależeć od płatności salonu. |
| RB-15 | Abonament wynosi 119 zł netto miesięcznie oraz 25 zł netto za każdego kolejnego pracownika. |
| RB-16 | Gdy wizytę odwołuje salon, klient dostaje pełny zwrot płatności z góry albo przenosi je na nowy termin. |
| RB-17 | Po 3 zignorowanych ofertach z rzędu wpis na liście oczekujących zostaje wyłączony. |
| RB-18 | Między 22:00 a 7:00 system nie wysyła ofert. Kolejka rusza o 7:00. |
| RB-19 | Opłata za przygotowanie zostaje u salonu tylko wtedy, gdy salon oznaczył pracę jako wykonaną przed odwołaniem. W przeciwnym razie wraca do klienta. |
| RB-20 | Przy przełożeniu w darmowym czasie płatności przechodzą na nowy termin. Po czasie zadatek jest rozliczany jak przy odwołaniu, a opłata za przygotowanie przechodzi na nowy termin. |
| RB-21 | Prowizja wynosi 10% netto ceny pierwszej wizyty, najmniej 5 zł i najwyżej 30 zł netto. Podstawą jest cena z chwili rezerwacji. |
| RB-22 | Prowizja powstaje tylko wtedy, gdy spełnione są trzy warunki: klient przeszedł z wyników wyszukiwania prosto do rezerwacji w czasie do 60 minut, nie ma go w bazie salonu ani wcześniejszej wizyty w tym salonie, a wizyta została oznaczona jako odbyta. |
| RB-23 | Każda prowizja ma zapisany dowód: datę rezerwacji, wyszukiwanie i czas przejścia do rezerwacji. Bez dowodu system nie nalicza prowizji. |
| RB-24 | Właściciel może podważyć prowizję przez 30 dni od jej naliczenia. Gdy wykaże wcześniejszą wizytę klienta, prowizja jest cofana. |
| RB-25 | Zgłoszenie salonu musi zawierać nazwę, adres, NIP i dane właściciela. NIP i dane właściciela muszą zgadzać się z wpisem w CEIDG albo KRS. |
| RB-26 | Salon jest widoczny w wyszukiwarce i przyjmuje rezerwacje dopiero po zatwierdzeniu przez administratora. |

---

## 2.2. Wymagania niefunkcjonalne

| ID | Co mierzymy | W jakich warunkach | Jaka wartość | Jak weryfikujemy |
|---|---|---|---|---|
| NF-01 | czas wyznaczenia wolnych terminów dla salonu i usługi na 14 dni | 200 równoczesnych użytkowników | poniżej 500 ms dla 95% zapytań, po stronie serwera | raport percentyli z testu obciążeniowego |
| NF-02 | czas od zwolnienia terminu do wysłania oferty | 50 odwołań na minutę | poniżej 60 s dla 99% ofert | logi zdarzeń z testu obciążeniowego |
| NF-03 | liczba podwójnych rezerwacji tego samego terminu | 100 równoczesnych prób przyjęcia jednego terminu | 0, powstaje dokładnie 1 wizyta | test współbieżności przy każdym wydaniu |
| NF-04 | dokładność wygaśnięcia oferty | normalne obciążenie | oferta wygasa najpóźniej 30 s po upływie czasu | test automatyczny na zegarze testowym |
| NF-05 | dostępność rezerwacji i odwołań | cały miesiąc, bez zaplanowanych prac | co najmniej 99,9% miesięcznie | monitoring zewnętrzny, raport miesięczny |
| NF-06 | zgodność kwot na wizytę z płatnościami | codzienne rozliczenie wszystkich transakcji | 100% zgodnych wpisów | automatyczne porównanie z danymi bramki płatności |
| NF-07 | liczba kroków rezerwacji od ekranu głównego | nowy klient, aplikacja mobilna | najwyżej 4 kroki | test użyteczności na 5 osobach |
| NF-08 | liczba numerów kart i kodów BLIK zapisanych przez system | baza danych i logi całej aplikacji | 0 | przegląd bazy danych i kodu przed wydaniem |
| NF-09 | udział prowizji z zapisanym dowodem | wszystkie prowizje z danego miesiąca | 100% | automatyczny raport miesięczny |
| NF-10 | czas od prośby klienta o usunięcie konta do usunięcia lub anonimizacji jego danych osobowych | każda prośba, poza danymi, które trzeba zachować z powodów prawnych, np. rozliczeń | najwyżej 30 dni | test automatyczny i raport miesięczny |
| NF-11 | liczba równoczesnych użytkowników obsługiwanych bez utraty jakości | ruch rosnący przez 30 minut | 1000 użytkowników, wolne terminy poniżej 1000 ms dla 95% zapytań, najwyżej 0,5% błędnych żądań | raport z testu obciążeniowego |
| NF-12 | pokrycie kodu rezerwacji i rozliczeń testami automatycznymi | każde wydanie | co najmniej 80% | raport pokrycia z automatycznego budowania |

**Obszary z zadania projektowego:**

| Obszar | Wymagania |
|---|---|
| Wydajność | NF-01, NF-02, NF-04 |
| Skalowalność | NF-11 |
| Ergonomia interfejsu | NF-07 |
| Bezpieczeństwo i dane osobowe | NF-08, NF-10 |
| Niezawodność | NF-03, NF-05, NF-06, NF-09 |
| Standardy jakości | NF-12 |

---

## 2.3. Powiązanie wymagań z usprawnieniami

| Usprawnienie | Wymagania |
|---|---|
| Szybka Zamiana: kolejka | WF-03, WF-04, WF-05, RB-06, RB-09, RB-10, RB-11, RB-17, RB-18, NF-02, NF-03, NF-04 |
| Szybka Zamiana: potwierdzenie „Będę” | WF-06, RB-07 |
| Szybka Zamiana: zadatek na kolejną wizytę | WF-02, WF-07, WF-08, WF-14, WF-15, RB-08, RB-12, RB-13, RB-16, RB-20, NF-06 |
| Zaliczka za projekt | WF-07, WF-15, WF-17, RB-19, RB-20 |
| Prowizja z limitem i dowodem | WF-11, WF-12, WF-13, WF-16, WF-19, RB-14, RB-15, RB-21, RB-22, RB-23, RB-24, NF-09 |
