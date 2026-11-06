# Rozdział 1. Analiza Booksy i usprawnienia

> Stan na 06.11.2026. Źródła: centrum pomocy Booksy (polskie i amerykańskie), opinie z App Store, Google Play i Trustpilot, wątki na Reddicie. Linki są na końcu.

> Krótka wersja projektu, wiadomość w windzie i odpowiedzi na pytania brzegowe: [Krótko o projekcie](00_krotko_o_projekcie.md).

---

## 1.1. Czym jest Booksy, w skrócie

Booksy to **polska aplikacja do rezerwowania wizyt** u fryzjera, barbera, kosmetyczki itp. Założyli ją Stefan Batory, Konrad Howard oraz Agnieszka i Tomasz Zembrzyccy. Dziś działa m.in. w USA, Wielkiej Brytanii, Hiszpanii, Francji, Meksyku, Brazylii i RPA. W Polsce jest liderem: w 2018 r. przejęła Lavito, a w 2020 r. połączyła się z Versum.

Booksy składa się z **dwóch aplikacji**:
- **Booksy (dla klienta):** wyszukujesz salon, wybierasz usługę, pracownika i godzinę, rezerwujesz.
- **Booksy Biz (dla salonu):** kalendarz, baza klientów, płatności, przypomnienia SMS, marketing.

**Jak Booksy zarabia:**
- **abonament:** ok. 145 zł netto miesięcznie za salon + 35 zł za każdego kolejnego pracownika;
- **Boost:** płatna promocja salonu w wyszukiwarce Booksy. Gdy nowy klient znajdzie salon w ten sposób, salon oddaje Booksy **35–45% netto ceny jego pierwszej wizyty** (szczegóły w punkcie 1.3);
- **prowizje od płatności online:** ok. 1,89% + 0,49 zł od transakcji.

**Ciekawy kontrast w opiniach:**
- na Capterra (oceniają głównie salony, czyli sam program) Booksy ma **4,4 / 5**;
- na Trustpilot (oceniają firmę i obsługę) ma tylko **2,9 / 5** przy 16 590 opiniach.

Wniosek: **ludzie lubią samą aplikację, ale nie lubią tego, jak Booksy obchodzi się z ich pieniędzmi** (prowizje, kary, zwroty) **i jak działa support**.

---

## 1.2. Mocne strony Booksy

### 1. Wszystko w jednym miejscu: wyszukiwarka + program do prowadzenia salonu
Salon nie potrzebuje osobnego kalendarza, osobnej strony do rezerwacji i osobnego systemu SMS. Booksy daje to wszystko naraz i dodatkowo **przyprowadza nowych klientów** z wyszukiwarki. Klient z kolei ma tysiące salonów w jednej aplikacji.

To tzw. **efekt sieci**: im więcej salonów, tym więcej klientów, a im więcej klientów, tym bardziej salony chcą tam być. Dlatego nowej konkurencji tak trudno wejść na rynek.

### 2. Rezerwacja przez całą dobę i automatyczne przypomnienia
Klient nie musi dzwonić w godzinach otwarcia, bo rezerwuje o dowolnej porze. System sam wysyła potwierdzenie i przypomnienie SMS przed wizytą (w Polsce te SMS-y są w cenie abonamentu). Mniej telefonów oznacza mniej pracy dla salonu i mniej zapomnianych wizyt.

### 3. Wiarygodne opinie
Opinię może wystawić **tylko ktoś, kto naprawdę odbył wizytę** zarezerwowaną przez Booksy. System sam prosi o ocenę ok. 30 minut po wizycie. Dla porównania: w Google Maps opinię może dodać każdy, nawet ktoś, kto nigdy nie był w salonie.

> 💡 **Ważna obserwacja:** Booksy ma bardzo dużo funkcji, w tym listę oczekujących, karty lojalnościowe, karty podarunkowe i kampanie z promocjami. Nasze usprawnienie nie może więc być „dodajmy listę oczekujących”, tylko musi pokazywać, **co zrobimy lepiej niż Booksy**.

---

## 1.3. Problemy

### Jak to sprawdziliśmy

Przejrzeliśmy **509 negatywnych i średnich opinii** (1–3 gwiazdki) z App Store, Google Play i Trustpilot, ok. 6 wątków o Booksy na Reddicie oraz centrum pomocy Booksy. To próba, a nie badanie całego rynku: liczby poniżej są orientacyjne, a w opiniach częściej piszą osoby niezadowolone.

| Najczęstsze skargi klientów | Liczba | Najczęstsze skargi salonów | Liczba |
|---|---|---|---|
| opłaty, zadatki, kary za odwołanie | 35 | Boost i prowizje | 77 |
| błędy aplikacji | 31 | błędy i zawieszanie aplikacji | 47 |
| rezerwacja, której salon nie ma albo ją odwołuje | 22 | support | 39 |
| blokada opinii, oznaczanie klienta jako nieobecnego | 22 | cena i abonament | 36 |
| spam i powiadomienia marketingowe | 19 | trudna rezygnacja z umowy | 33 |

### Problem klienta: „Odwołałem wizytę, straciłem pieniądze, a termin i tak ktoś zajął”

Wiele salonów wymaga przy rezerwacji **zadatku**. Booksy nazywa go przedpłatą. Salon sam ustala zasady, np. „darmowe odwołanie do 24 h przed wizytą”. Po tym czasie pieniądze zostają u salonu, nawet jeśli termin chwilę później zajmie ktoś inny.

To nie jest błąd, tylko sposób działania. Centrum pomocy Booksy poleca salonom łączyć listę oczekujących z ochroną przed nieobecnościami:

> *„Jeśli ktoś odwoła wizytę zbyt późno, pobierzesz kaucję/opłatę za odwołanie, a lista oczekujących natychmiast znajdzie kogoś na to miejsce. Zarabiasz dwukrotnie!”*

**Co piszą klienci:**
- *„Nie otrzymałam zwrotu zadatku w kwocie 100zl”* (Trustpilot, Polska, 13.07.2026)
- *„I canceled my appointment a day before and they still charged me 50%... I think it's a scam”* (App Store, USA, 23.06.2026)

Booksy pozostawia zwrot przedpłaty salonowi: *„Decyzja o zwrocie przedpłaty należy do Ciebie”*. Automatyczny zwrot działa tylko przy płatności z góry przez Booksy Pay i tylko w terminie ustawionym przez salon.

> **Uczciwie:** to największa kategoria skarg klientów, ale w naszej próbie tylko 7 z 35 opinii pochodziło z Polski, a 28 było po angielsku. Problem jest realny, ale w tej próbie mocniej widać go poza Polską.

### Problem salonu nr 1: prowizja od wizyty

To największa skarga salonów: 77 opinii, z czego 48 z Polski. Boost to płatna promocja w wyszukiwarce Booksy. Salon płaci, gdy nowy klient odbędzie pierwszą wizytę: 45% netto ceny tej wizyty (35% przy umowie na 12 miesięcy), najmniej 25 zł, najwyżej 250 zł netto.

*Przykład:* farbowanie za 300 zł przy stawce 45% to 135 zł netto, czyli ok. 166 zł z VAT. Ponad połowa ceny idzie do Booksy.

**Co piszą salony:**
- *„Omijać szerokim łukiem, naliczanie boosta po 200zł od klientki??”* (Trustpilot, Polska, 24.06.2026)
- *„booksy would claim all appointments as boost appointments, even people that found me on instagram”* (Reddit, 10.2025)

Booksy ma formularz do podważenia prowizji i nie pobiera jej przy rezerwacji z linku salonu, ale salonowi trudno udowodnić, skąd klient naprawdę się dowiedział. Rezygnacja obowiązuje dopiero na koniec następnego okresu rozliczeniowego.

Prowizja ma też skutek uboczny dla klientów. Polscy klienci opisują wizyty anulowane lub zmienione po wyjściu z salonu: *„Mi dziś po wizycie zmieniono wizytę z takiej która kosztowała 450 zł, na taką która kosztowała 30 zł.”* (Reddit, r/Polska, 30.08.2026). Autorzy tych relacji podejrzewają, że salon omija w ten sposób prowizję.

### Problem salonu nr 2: późne odwołania i nieobecności

Gdy klient odwołuje w ostatniej chwili albo nie przychodzi, salon zostaje z pustą godziną. Lista oczekujących w Booksy wysyła SMS z linkiem do **wszystkich** czekających, a pierwszy, kto zarezerwuje, wygrywa. Booksy pisze wprost: *„Lista oczekujących nie blokuje miejsc automatycznie”*.

Kary też nie rozwiązują tego do końca. Klient może zakwestionować płatność w banku, a w USA salon płaci wtedy dodatkowo **20 dolarów** za spór. Jedna z osób na Reddicie pisze, że aż 86% nieobecności w jej salonie skończyło się niepobraną opłatą (to dane tylko tej osoby).

### Problem klienta nr 2: blokada opinii

W Booksy to salon oznacza nieobecność. Klienci piszą, że w ten sposób blokuje się im negatywną opinię: *„Jeśli wyrazisz niezadowolenie z usługi salon ma możliwość oznaczenia cię jako nieobecną, abyś nie wystawiła negatywnego komentarza.”* (App Store, Polska, 18.05.2026). W naszej próbie takich skarg jest 22, z czego 12 z Polski. Rozwiązujemy to kodem QR w salonie (usprawnienie 3 w punkcie 1.4).

---

## 1.4. Co byśmy zrobili

Budujemy własną aplikację do rezerwacji, podobną do Booksy. Roboczo nazywamy ją **Zwolnione** (punkt 1.7). Dodalibyśmy trzy usprawnienia:

| Usprawnienie | Kierunek z zadania | Kogo dotyczy |
|---|---|---|
| **Szybka Zamiana** | rezerwacje last minute na wolne okienka, ograniczenie nieodwołanych nieobecności | klient i salon |
| **Prowizja z limitem i dowodem** | nasza wersja kierunku „brak prowizji od wizyty” | salon |
| **Potwierdzona obecność** | ograniczenie nieodwołanych nieobecności | klient i salon |

### Usprawnienie 1: Szybka Zamiana

> **Gdy zwalnia się termin, aplikacja sama szuka na niego osoby, a zadatek odwołującego nie przepada, tylko zostaje na jego kolejną wizytę.**

**Jak to działa w 4 krokach**

1. **Dzień przed wizytą klient klika „Będę”.** Dzięki temu salon wcześniej wie, czy wizyta jest pewna.
2. **Gdy klient odwołuje, widzi skutki.** Aplikacja pokazuje przed potwierdzeniem, co stanie się z jego zadatkiem.
3. **Aplikacja proponuje termin po kolei.** Oferta idzie do jednej osoby z listy oczekujących, a termin czeka tylko na nią. Brak odpowiedzi oznacza, że oferta idzie do następnej osoby.
4. **Termin przejęty, zadatek zostaje na kolejną wizytę.** Nowa osoba wpłaca własny zadatek. Odwołujący dostaje kwotę do wykorzystania w tym salonie przez 3 miesiące.

Jeśli nikt nie przejmie terminu, wraca on do puli wolnych terminów, a zadatek zostaje u salonu zgodnie z jego zasadami.

**Przykład**

Barber Tomek ma w piątek o 17:00 wizytę z Kamilem. Kamil wpłacił 30 zł zadatku. Darmowe odwołanie jest możliwe do 24 h przed wizytą. Kasia i Marek są na liście oczekujących, Kasia zapisała się pierwsza.

1. W czwartek wieczorem Kamil odwołuje wizytę. Widzi komunikat: *„Jeśli ktoś przejmie Twój termin, 30 zł zostanie na Twoją kolejną wizytę. Jeśli nie, zadatek przepada.”*
2. Kasia dostaje ofertę i ma 15 minut. Nie odpowiada.
3. Oferta idzie do Marka. Marek klika „Przyjmuję” i wpłaca 30 zł zadatku.
4. Kamil ma 30 zł na kolejną wizytę u Tomka. Gdy wróci na strzyżenie za 100 zł, zapłaci 70 zł.

**Co jeśli klient nie kliknie „Będę”?**

| Sytuacja | Co się dzieje |
|---|---|
| wizyta z zadatkiem | wizyta zostaje, bo salon ma zabezpieczenie |
| wizyta bez zadatku, brak potwierdzenia do 12 h przed wizytą | aplikacja proponuje termin kolejce |
| nikt nie przyjmie oferty | wizyta klienta zostaje |
| ktoś przyjmie ofertę | klient traci wizytę i dostaje powiadomienie |

Klient traci termin dopiero wtedy, gdy ktoś inny naprawdę go weźmie.

**Czas na decyzję zależy od tego, ile zostało do wizyty**

| Do wizyty zostało | Czas na decyzję | Kto dostaje ofertę |
|---|---|---|
| ponad 6 godzin | 15 minut | jedna osoba naraz |
| od 2 do 6 godzin | 5 minut | jedna osoba naraz |
| mniej niż 2 godziny | brak wyłączności | wszyscy naraz, wygrywa pierwszy |

Między 22:00 a 7:00 aplikacja nie wysyła ofert, a kolejka rusza o 7:00.

Klient zapisuje się na **okno czasowe** (np. „pn–śr po 16:00”) i wybranego lub dowolnego pracownika. Aplikacja proponuje termin tylko wtedy, gdy usługa tej osoby mieści się w zwolnionym czasie.

**Dlaczego to się opłaca obu stronom**

- **Salon:** niczego nie oddaje od ręki, ma pełny grafik, a klient ma powód, żeby wrócić.
- **Klient:** nie traci pieniędzy, gdy termin ktoś przejął, i nie czuje się oszukany.
- **Osoba z listy:** ma pewność, że termin na nią czeka.

To, że salon rozlicza potem te pieniądze przy kolejnej wizycie, jest kosztem. Zyskuje za to klienta, który mógłby już nie wrócić. To nasze założenie, które trzeba by sprawdzić na prawdziwych salonach.

**Zaliczka za projekt, np. u tatuażysty**

Tatuażyści biorą pieniądze za projekt, zanim klient usiądzie na fotelu. Dlatego salon może podzielić płatność z góry na dwie części:

| Część | Za co jest | Co się z nią dzieje przy odwołaniu po czasie |
|---|---|---|
| **Opłata za przygotowanie** | praca przed wizytą, np. projekt | zostaje u salonu, jeśli praca jest wykonana |
| **Zadatek za termin** | ochrona przed pustym terminem | zostaje na kolejną wizytę, jeśli ktoś przejmie termin |

Przykład: Ola wpłaca 200 zł za projekt i 100 zł za termin. Odwołuje po czasie, a ktoś przejmuje termin. 100 zł zostaje jej na kolejną wizytę, a 200 zł zostaje u tatuażystki za wykonany projekt. Salon, który nie robi nic przed wizytą, ustawia tylko zadatek za termin.

> **Uwaga o nazwach:** w tym dokumencie „zadatek” znaczy po prostu pieniądze za termin. Prawnie zadatek i zaliczka to różne rzeczy (art. 394 Kodeksu cywilnego reguluje zadatek), a zaliczka co do zasady podlega zwrotowi. Dlatego część za projekt nazywamy opłatą za przygotowanie. W prawdziwym produkcie nazwy i regulamin musiałby sprawdzić prawnik.

### Usprawnienie 2: Prowizja z limitem i dowodem

> **Salon płaci niższy abonament, a za nowego klienta z naszej wyszukiwarki oddaje 10% ceny pierwszej wizyty, najwyżej 30 zł. Przy każdej prowizji widzi dowód, skąd klient przyszedł.**

**Dlaczego nie sam abonament**

Rozważaliśmy model bez żadnej prowizji. Wtedy cały koszt aplikacji spadałby na stałą opłatę, także przy salonach, którym nie przyprowadzamy klientów. Dlatego obniżamy abonament, a resztę zarabiamy wtedy, gdy salon naprawdę zyskał nowego klienta.

Skargi salonów dotyczą dwóch rzeczy: wysokiej prowizji i braku dowodu, skąd przyszedł klient. Usprawnienie odpowiada na obie: limit rozwiązuje pierwszą, a dowód drugą.

**Ile to kosztuje**

| | Booksy | Nasza aplikacja |
|---|---|---|
| Abonament miesięczny | 145 zł + 35 zł za kolejnego pracownika | 119 zł + 25 zł za kolejnego pracownika |
| Prowizja za nowego klienta | 35–45% ceny pierwszej wizyty | 10% ceny pierwszej wizyty |
| Najmniejsza prowizja | 25 zł | 5 zł |
| Największa prowizja | 250 zł | 30 zł |

Kwoty są netto. Nasze stawki to założenia zespołu, bo nie znamy jeszcze kosztów działania aplikacji.

**Kiedy salon płaci prowizję**

Prowizja powstaje tylko wtedy, gdy spełnione są trzy warunki naraz:

1. **Klient przyszedł z naszej wyszukiwarki.** Przeszedł z wyników prosto do rezerwacji, w czasie do 60 minut.
2. **Klient jest dla salonu nowy.** Nie ma go w bazie salonu i nie miał tam wcześniej wizyty. Salon może zaimportować bazę klientów przed startem.
3. **Wizyta się odbyła.** Pracownik oznaczył ją jako odbytą albo klient zeskanował kod QR w salonie.

Rezerwacja z linku salonu, z Instagrama, przez telefon albo z listy oczekujących nigdy nie daje prowizji. Prowizja dotyczy tylko pierwszej wizyty, a kolejne są bez opłat.

**Dowód przy każdej prowizji**

W Booksy o pochodzeniu klienta decyduje głównie jego odpowiedź przy rezerwacji, a salonowi trudno ją podważyć. U nas system zapisuje drogę klienta, a salon widzi przy prowizji:

- datę rezerwacji,
- czego klient szukał,
- że przeszedł z wyników prosto do rezerwacji.

Jeśli salon uważa, że prowizja jest niesłuszna, ma 30 dni na zgłoszenie. Administrator sprawdza sprawę, a gdy salon wykaże wcześniejszą wizytę klienta, prowizja wraca.

**Przykład**

Ania wpisuje „koloryzacja Kraków”, wybiera z wyników salon Beaty i rezerwuje farbowanie za 300 zł. Nigdy tam nie była.

1. Po wizycie salon oddaje nam 10%, czyli 30 zł. W Booksy byłoby to 105–135 zł netto.
2. Beata widzi przy prowizji dowód: datę, wyszukiwanie „koloryzacja Kraków” i przejście z wyników do rezerwacji.
3. Gdy Ania wróci na kolejną wizytę, salon nie zapłaci prowizji.
4. Koleżanka Ani rezerwuje z linku na Instagramie salonu, więc salon też nic nie płaci.

**Ile płaci salon w miesiącu**

Przykładowy salon ma 3 pracowników, a wizyta kosztuje 150 zł. Kwoty są netto.

| Miesiąc | Booksy z Boostem | Nasza aplikacja |
|---|---|---|
| 10 nowych klientów z wyszukiwarki | 740–890 zł | 319 zł |
| brak nowych klientów | 215 zł | 169 zł |

**Co jeszcze się zmienia**

- Nie ma odpowiednika Boosta ani płatnej promocji w wyszukiwarce.
- Wyniki wyszukiwania zależą od dopasowania do klienta: usługi, odległości, wolnych terminów i oceny.
- Prowizję liczymy od ceny z chwili rezerwacji, więc zmiana wizyty po fakcie nie obniża opłaty.

**Jak zarabiamy:** na abonamencie i prowizji za nowych klientów. Opłaty operatora płatności zostają, bo to koszt zewnętrznej bramki, a nie nasza prowizja.

**Słabe strony**

- Jeśli klient nie zeskanuje kodu QR, salon nadal może oznaczyć go jako nieobecnego, żeby nie zapłacić. Skan zamyka tę lukę (usprawnienie 3).
- Tracimy proste hasło „bez prowizji”, więc model trzeba salonowi krótko wytłumaczyć.
- Część naszego przychodu zależy od tego, czy wyszukiwarka faktycznie przyprowadza klientów.

Prowizję za nowego klienta mają też inne serwisy. Według źródeł z Wielkiej Brytanii Fresha bierze ok. 20%, a Treatwell ok. 35%, a stawki w Polsce mogą być inne. Nie twierdzimy, że wymyśliliśmy niską prowizję. Wyróżnia nas połączenie limitu i dowodu.

### Usprawnienie 3: Potwierdzona obecność

> **Klient skanuje kod QR w salonie, więc to nie sam salon decyduje, czy klient przyszedł. Kto naprawdę nie przychodzi, z czasem musi wpłacać zadatek.**

Dziś jeden przycisk „nieobecny” decyduje o trzech rzeczach: czy zadatek przepada, czy salon płaci prowizję i czy klient może wystawić ocenę. Dlatego jest to wygodne miejsce do nadużyć po obu stronach. Usprawnienie ma cztery części.

**1. Pytanie przed wizytą**

2 godziny przed wizytą klient dostaje pytanie „Nadal będziesz?” z opcją „Nie dam rady”. Kliknięcie działa jak późne odwołanie, ale termin od razu trafia do kolejki. Salon ma więc szansę go zapełnić, zamiast czekać na kogoś, kto nie przyjdzie.

**2. Kod QR w salonie**

Każdy salon ma wydrukowany kod QR. Klient skanuje go w aplikacji po przyjściu. Skan jest ważny od 30 minut przed wizytą do jej końca i tylko w odległości do 200 m od salonu, więc zdjęcie kodu zrobione wcześniej nie pomoże w domu. Aplikacja sprawdza lokalizację tylko w chwili skanu i jej nie zapisuje.

Skan nie zależy od dobrej woli salonu, bo klient robi go sam. Nie jest też obowiązkowy: klient z rozładowanym telefonem normalnie skorzysta z usługi.

| Czy klient zeskanował kod? | Co oznaczył salon | Co się dzieje |
|---|---|---|
| tak | odbyta | wizyta się odbyła |
| tak | nieobecny | skan wygrywa, wizyta się odbyła |
| nie | odbyta | wizyta się odbyła, bo skan nie jest obowiązkowy |
| nie | nieobecny | nieobecność, ale klient może kliknąć „Byłem” |

Gdy wizyta się odbyła, klient może wystawić ocenę, a jeśli był nowym klientem z wyszukiwarki, salon płaci prowizję.

**3. Sprzeciw „Byłem”**

Gdy salon oznaczy nieobecność, a klient nie ma skanu, klient dostaje powiadomienie i ma 48 h na kliknięcie „Byłem”. Bez skanu nie da się ustalić, kto ma rację, dlatego sprzeciw daje tylko jedno: ta nieobecność nie liczy się do licznika. Zadatek zostaje u salonu, a klient nie może wystawić oceny. Taki sprzeciw można zgłosić raz na 6 miesięcy, żeby nie dało się nim stale omijać licznika.

**4. Licznik nieobecności**

Po 2 nieobecnościach w ciągu 6 miesięcy klient przez 3 miesiące wpłaca przy każdej rezerwacji zadatek w wysokości 20% ceny wizyty, także w salonach, które zwykle go nie wymagają. Jeśli salon wymaga wyższego zadatku, obowiązuje wyższy. Salon nie widzi licznika, tylko wymaganą płatność, więc nie ujawniamy historii klienta innym salonom.

**Przykład**

Paweł klika „Będę”, ale dwa razy nie przychodzi na wizyty bez zadatku. Salony oznaczają nieobecność, a Paweł nie zgłasza sprzeciwu. Przy kolejnej rezerwacji strzyżenia za 100 zł musi wpłacić 20 zł zadatku.

Julia przychodzi na wizytę i skanuje kod. Jest niezadowolona, a salon oznacza ją jako nieobecną. Skan wygrywa, więc wizyta się odbyła i Julia może wystawić ocenę.

**Słabe strony**

- Klient może stać pod salonem, zeskanować kod i nie wejść, jeśli zna kod. Tego nie sprawdzamy.
- Salon może ukryć wydrukowany kod. Wtedy zostaje sprzeciw „Byłem”, który nie rozstrzyga sporu.
- Pierwsze dwie nieobecności bez zadatku nadal nic nie kosztują.
- Liczby, np. 200 m, 48 h i 20%, to założenia zespołu.

### Czym to się różni od Booksy?

| | Booksy | Nasza aplikacja |
|---|---|---|
| Kto dostaje ofertę terminu? | wszyscy z listy naraz, SMS z linkiem | **po kolei jedna osoba** |
| Czy termin czeka? | nie, „kto pierwszy, ten lepszy” | **tak, z czasem zależnym od pory odwołania** |
| Na co się zapisuję? | na dzień lub zakres dat | na **okno czasowe** i pracownika |
| Co z zadatkiem odwołującego? | decyduje salon | **zostaje na kolejną wizytę, jeśli termin został przejęty** |
| Praca przed wizytą | jedna przedpłata | **osobno opłata za przygotowanie i zadatek za termin** |
| Prowizja za nowego klienta | do 45% netto pierwszej wizyty, najwyżej 250 zł | **10% netto, najwyżej 30 zł** |
| Dowód, skąd przyszedł klient | salonowi trudno to sprawdzić | **widoczny przy każdej prowizji** |
| Kto decyduje o nieobecności? | salon | **salon, ale skan kodu QR przez klienta ma pierwszeństwo** |
| Płatna promocja w wyszukiwarce | Boost | **brak** |

Samo proponowanie terminu po kolei mają też inne systemy, np. Fresha, Vagaro i Zenoti. Nie twierdzimy, że wymyśliliśmy kolejkę. Naszym rozwiązaniem jest połączenie jej z potwierdzaniem wizyty i zadatkiem na kolejną wizytę.

### Czego usprawnienia NIE rozwiązują

Klient może kliknąć „Będę” i mimo to nie przyjść. Pytanie 2 godziny przed wizytą i licznik nieobecności zmniejszają liczbę takich sytuacji, ale ich nie usuwają. Gdy klient nie odpowie i nie przyjdzie, godzina zostaje pusta, a salon ma tylko zadatek, jeśli go wymagał.

### Jak zmierzymy, czy działa
- jaki % odwołanych terminów udało się zapełnić z kolejki,
- ile średnio trwa zapełnienie terminu,
- jaki % wizyt klienci potwierdzają przed terminem,
- jaki % klientów z kwotą na kolejną wizytę wraca do salonu,
- jaki % wizyt ma potwierdzoną obecność kodem QR,
- jak często klienci zgłaszają sprzeciw „Byłem”.

### Jak usprawnienia pojawią się w kolejnych rozdziałach

| Rozdział | Co dzięki nim dodajemy |
|---|---|
| 2. Wymagania | potwierdzanie wizyty, lista oczekujących z oknem czasowym, oferty z czasem zależnym od pory, kwota na kolejną wizytę, abonament, prowizja z limitem, dowód źródła klienta, podważenie prowizji, wyszukiwanie bez płatnej promocji, pytanie przed wizytą, kod QR, sprzeciw „Byłem”, licznik nieobecności, ocena wizyty |
| 3.1 Przypadki użycia | „Potwierdź wizytę”, „Zapisz się na listę oczekujących”, „Przyjmij ofertę terminu”, „Odwołaj wizytę”, „Wykorzystaj kwotę na wizytę”, „Podważ prowizję”, „Zeskanuj kod QR”, „Zgłoś sprzeciw” |
| 3.2 Diagram aktywności | rozgałęzienie: *czy ktoś czeka?* → oferta → *przyjął / minął czas?* → następna osoba / termin wraca do puli |
| 4. Diagram klas | klasy `ListaOczekujacych`, `WpisNaLiscie`, `OfertaTerminu`, `PolitykaOdwolania`, `Platnosc`, `KwotaNaWizyte`, `Abonament`, `Prowizja`, `DowodZrodla`, `KodQR`, `PotwierdzenieObecnosci`, `Sprzeciw`, `LicznikNieobecnosci` |
| 5. Ryzyka | dwie osoby akceptują w tej samej sekundzie, za dużo powiadomień, zapisywanie się „na zapas”, salony niechętne kwocie na kolejną wizytę, przychody niepokrywające kosztów, omijanie prowizji przez oznaczanie nieobecności, skanowanie kodu bez wejścia do salonu, ukrywanie kodu przez salon |
| 6. Wzorce | **Observer** (zwolnienie terminu uruchamia kolejkę), **State** (oferta i wizyta), **Strategy** (zasady odwołania, czas oferty, naliczanie prowizji) |
| 6.2 Testy | „oferta wygasła → aplikacja wysyła ją następnej osobie”; test błędu: „dwie osoby przyjmują ten sam termin” |

---

## 1.5. Dlaczego te usprawnienia

1. **Odpowiadają na najczęstsze skargi:** prowizja to największa skarga salonów, a zadatki to największa skarga klientów. Salonom przeszkadza nie tylko jej wysokość, ale też brak dowodu, skąd przyszedł klient, dlatego rozwiązujemy obie sprawy.
2. **Pomagają obu stronom:** żadne nie opiera się na zabraniu pieniędzy jednej stronie, żeby dać je drugiej. Salon płaci mniej, a my nadal zarabiamy na klientach, których mu przyprowadzamy.
3. **Działają z BLIK-iem i Google Pay:** kwota na kolejną wizytę jest zapisana w aplikacji, więc nie potrzebuje zwrotu ani blokady na karcie.
4. **Zmieniają działanie systemu:** dotykają rezerwacji, wyszukiwania, powiadomień i rozliczeń.
5. **Uzupełniają się:** kod QR uszczelnia zadatek, prowizję i oceny, bo wszystkie zależą od tego, czy wizyta się odbyła.

---

## 1.6. Czego NIE modelujemy

Booksy ma bardzo dużo funkcji. Żeby projekt był wykonalny, skupiamy się na rezerwacjach i naszych usprawnieniach.

| Co pomijamy | Dlaczego |
|---|---|
| **Szczegóły płatności:** działanie bramki, BLIK, karty, zwroty bankowe | robi to zewnętrzny system, a my tylko wysyłamy polecenie „pobierz” albo „zwróć” |
| **Faktury i księgowość** | wystarczy nam kwota abonamentu i prowizji do pobrania, a nie sam proces wystawiania faktur |
| **Kasa, magazyn, raporty sprzedaży, wynagrodzenia** | to prowadzenie firmy, a nie rezerwowanie wizyt |
| **Marketing:** kampanie SMS, promocje, karty podarunkowe i lojalnościowe | nie wpływa na nasze usprawnienia, a mocno powiększa system |
| **Integracje z Instagramem, Facebookiem, Google** | źródło klienta śledzimy tylko w naszej wyszukiwarce, a wszystko spoza niej nie daje prowizji |
| **Moderacja opinii** | wymaga osobnego procesu; modelujemy tylko ocenę salonu |
| **Wiele krajów, języków i walut** | zakładamy tylko Polskę, żeby nie mnożyć zasad i przepisów |
| **Szczegóły prawne:** regulaminy, skutki zadatku i zaliczki, kwota po zamknięciu salonu | w prawdziwym produkcie musiałby to ocenić prawnik |

---

## 1.7. Nazwa produktu

Naszą aplikację nazywamy roboczo **Zwolnione**, ze sloganem *„Żaden termin nie przepada.”*

Nazwa od razu mówi, co nas wyróżnia: zwolnione terminy nie marnują się, tylko trafiają do kogoś, kto na nie czeka.

---

## Ściąga: co powiedzieć na zajęciach (ok. 2 minuty)

1. **Booksy** to polska aplikacja do rezerwacji wizyt, lider w Polsce. Program jest oceniany dobrze (Capterra 4,4), firma słabo (Trustpilot 2,9).
2. **Mocne strony:** wyszukiwarka i program dla salonu w jednym (efekt sieci), rezerwacja 24/7 z przypomnieniami, opinie tylko po prawdziwej wizycie.
3. **Problem klienta:** odwołuje po czasie i traci zadatek, nawet gdy termin od razu zajmie ktoś inny.
4. **Problemy salonu:** prowizja do 45% netto za nowego klienta to największa skarga, także w Polsce. Do tego późne odwołania i nieobecności.
5. **Szybka Zamiana:** klient potwierdza wizytę dzień wcześniej. Gdy termin się zwolni, proponujemy go po kolei osobom z listy. Jeśli ktoś go weźmie, zadatek zostaje na kolejną wizytę.
6. **Prowizja z limitem i dowodem:** salon płaci niższy abonament, a za nowego klienta z naszej wyszukiwarki 10% pierwszej wizyty, najwyżej 30 zł. Przy każdej prowizji widzi dowód, skąd klient przyszedł. Wyszukiwarka nie ma płatnej promocji.
7. **Zaliczka za projekt:** opłata za wykonaną pracę zostaje u salonu, a zadatek za termin działa jak wyżej.
8. **Potwierdzona obecność:** 2 godziny przed wizytą pytamy „Nadal będziesz?”. Klient skanuje kod QR w salonie, a skan ma pierwszeństwo przed oznaczeniem nieobecności. Po 2 nieobecnościach w 6 miesięcy klient wpłaca zadatek przy każdej rezerwacji.
9. **Czego nie rozwiązujemy:** klient może kliknąć „Będę”, nie odpowiedzieć na pytanie i nie przyjść. Zostaje wtedy pusta godzina.

---

## Źródła

**Centrum pomocy Booksy**
- Lista oczekujących (PL): https://support.booksy.com/hc/pl-pl/articles/16463469277714
- Przedpłata a opłata za odwołanie: https://support.booksy.com/hc/pl-pl/articles/16487431553810
- Zwrot przedpłaty opłaconej BLIKIEM: https://support.booksy.com/hc/pl-pl/articles/33226355093906
- Zwrot przy Booksy Pay: https://support.booksy.com/hc/pl-pl/articles/25167278511250
- Prowizja Boost: https://support.booksy.com/hc/pl-pl/articles/19727962368274
- Kiedy prowizja Boost nie zostanie naliczona: https://support.booksy.com/hc/pl-pl/articles/16485524178066
- Rezygnacja z Boost: https://support.booksy.com/hc/pl-pl/articles/23203437000978
- Boost i oznaczanie nieobecności (USA): https://support.booksy.com/hc/en-us/articles/16486248108946
- Spory bankowe i opłata 20 USD (USA): https://support.booksy.com/hc/en-us/articles/16464649383570

**Booksy i rynek**
- Booksy Biz, lista funkcji: https://biz.booksy.com/pl-pl/funkcje
- Booksy, jak działają opinie: https://biz.booksy.com/blog/how-booksy-reviews-work
- Booksy Boost: https://biz.booksy.com/pl-pl/blog/booksy-boost-bez-tajemnic
- Cennik Booksy (artykuł firmy konkurencyjnej, 08.2026): https://meetergo.com/pl/blog/booksy-cennik
- Przejęcie Lavito: https://www.money.pl/gospodarka/wiadomosci/artykul/booksy-przejmuje-lavito-pl-polski-globalny,133,0,2411397.html

**Inne serwisy (prowizja za nowego klienta, dane z Wielkiej Brytanii)**
- Fresha, cennik (artykuł firmy konkurencyjnej): https://pabau.com/blog/fresha-pricing/
- Treatwell, oferta dla salonów: https://www.treatwell.co.uk/partners?p=45

**Opinie**
- Trustpilot PL: https://pl.trustpilot.com/review/booksy.com
- Trustpilot, opinie 1★: https://www.trustpilot.com/review/booksy.com?stars=1
- App Store, Booksy: https://apps.apple.com/us/app/id723961236 oraz https://apps.apple.com/pl/app/id723961236
- Google Play, Booksy Biz: https://play.google.com/store/apps/details?id=net.booksy.business
- Capterra: https://capterra.com/p/142741/Booksy/reviews/
- Reddit, „Booksy is literally the WORST app for service providers” (10.2025): https://reddit.com/r/hairstylist/comments/1o0kvz2/
- Reddit, „If you're considering using Booksy's scheduling platform, read this first” (09.2026): https://reddit.com/r/hairstylist/comments/1wh89n6/
- Reddit, „Booksy - anulowana wizyta… po wizycie?” (08.2026): https://www.reddit.com/r/Polska/comments/1vy96cg/

**Zaliczka i zadatek**
- Art. 394 Kodeksu cywilnego: https://standardyprawa.pl/akt/2/art/4482
- Zadatek a zaliczka: https://poradnikprzedsiebiorcy.pl/-zadatek-a-zaliczka-jakie-sa-roznice-i-co-lepiej-zabezpiecza
- Przykład zasad zadatku studia tatuażu: https://sites.google.com/view/bewelltattoo/deposit-cancellation-policy
