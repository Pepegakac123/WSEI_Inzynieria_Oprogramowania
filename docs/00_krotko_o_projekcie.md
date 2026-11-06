# Krótko o projekcie

Budujemy aplikację do rezerwowania wizyt u fryzjerów, barberów, kosmetyczek, fizjoterapeutów, groomerów i tatuażystów, podobną do Booksy. Roboczo nazywamy ją **Zwolnione**, ze sloganem „Żaden termin nie przepada”.

Pełna analiza jest w [rozdziale 1](01_analiza_i_usprawnienia.md), a dokładne zasady w [rozdziale 2](02_wymagania.md).

## Wiadomość w windzie (ok. 50 sekund)

> Masz wizytę u fryzjera i wpłacasz 50 zł zadatku. Dzień wcześniej wypada Ci coś ważnego. Odwołujesz i 50 zł przepada, choć godzinę później ktoś inny bierze ten termin. Salon też nie ma lekko: klienci nie przychodzą, a za nowego klienta z Booksy oddaje nawet 45% ceny pierwszej wizyty.
>
> My zrobilibyśmy to inaczej. Dzień przed wizytą klikasz „Będę”. Gdy odwołasz, sami proponujemy termin kolejnym osobom z listy oczekujących. Jeśli ktoś go weźmie, Twój zadatek zostaje na następną wizytę. A salon płaci niższy abonament, za nowego klienta z naszej wyszukiwarki oddaje najwyżej 30 zł i zawsze widzi dowód, skąd ten klient przyszedł.
>
> Salon ma pełny grafik i niższe rachunki, a Ty nie tracisz pieniędzy za termin, który ktoś przejął.

## Jaki problem rozwiązujemy

| Kto | Problem | Dowód |
|---|---|---|
| Klient | Odwołuje po czasie i traci zadatek, nawet gdy termin od razu zajmie ktoś inny. | największa kategoria skarg klientów (35 opinii, głównie spoza Polski) |
| Salon | Oddaje prowizję za nowych klientów i nie może łatwo udowodnić, skąd przyszli. | największa skarga salonów (77 opinii, w tym 48 z Polski) |
| Salon | Późne odwołania i nieobecności zostawiają pustą godzinę. | lista oczekujących w Booksy nie trzyma terminu dla nikogo |

Booksy sam pisze salonom, że przy późnym odwołaniu i zapełnieniu terminu z listy *„Zarabiasz dwukrotnie!”*. To dobrze pokazuje, po czyjej stronie jest dziś ten mechanizm.

## Co byśmy zrobili

### 1. Szybka Zamiana

Działa w czterech krokach:

1. **Potwierdzenie.** Dzień przed wizytą klient klika „Będę”, więc salon wcześniej wie, czy wizyta jest pewna.
2. **Jasne skutki.** Przy odwołaniu klient widzi, co stanie się z jego pieniędzmi, zanim potwierdzi.
3. **Kolejka.** Wolny termin dostaje po kolei jedna osoba z listy oczekujących i termin czeka tylko na nią.
4. **Zadatek na kolejną wizytę.** Gdy ktoś przejmie termin po późnym odwołaniu, zadatek zostaje jako kwota do wykorzystania w tym salonie przez 3 miesiące.

**Przykład:** Kamil ma wizytę u barbera Tomka w piątek o 17:00 i wpłacił 30 zł. W czwartek wieczorem odwołuje po czasie. Kasia z listy ma 15 minut, ale nie odpowiada. Marek przyjmuje termin i wpłaca własne 30 zł. Kamil ma 30 zł na kolejną wizytę, więc za strzyżenie za 100 zł zapłaci 70 zł.

**Czas na decyzję:**

| Do wizyty zostało | Czas | Kto dostaje ofertę |
|---|---|---|
| ponad 6 godzin | 15 minut | jedna osoba |
| od 2 do 6 godzin | 5 minut | jedna osoba |
| mniej niż 2 godziny | bez wyłączności | wszyscy, wygrywa pierwszy |

Między 22:00 a 7:00 nie wysyłamy ofert. Kolejka rusza o 7:00.

**Czym to się różni od Booksy:** Booksy wysyła SMS do wszystkich od razu, termin na nikogo nie czeka, a o zwrocie zadatku decyduje salon. Samo proponowanie po kolei mają też inne systemy, np. Fresha, Vagaro i Zenoti. Naszym rozwiązaniem jest połączenie kolejki z potwierdzeniem i zadatkiem na kolejną wizytę.

### 2. Zaliczka za projekt

Tatuażysta rysuje projekt przed wizytą, więc część pracy jest już wykonana. Zwykły zadatek tego nie opisuje, dlatego płatność z góry można podzielić na dwie części:

| Część | Za co | Co przy późnym odwołaniu |
|---|---|---|
| **Opłata za przygotowanie** | praca przed wizytą, np. projekt | zostaje u salonu, jeśli praca jest wykonana |
| **Zadatek za termin** | ochrona przed pustym terminem | zostaje na kolejną wizytę, jeśli ktoś przejmie termin |

Obie części są odliczane od ceny, jeśli wizyta się odbędzie. Fryzjer czy barber ustawia tylko zadatek za termin. Salon sam decyduje, czy używa opłaty za przygotowanie.

**Przykład:** Ola wpłaca 200 zł za projekt i 100 zł za termin przy tatuażu za 800 zł.

| Co się dzieje | Co z 200 zł za projekt | Co ze 100 zł za termin |
|---|---|---|
| Ola przychodzi | odliczone od ceny | odliczone od ceny, zostaje 500 zł do zapłaty |
| odwołuje w darmowym czasie, projekt gotowy | zostaje u tatuażystki | wraca |
| odwołuje w darmowym czasie, projekt nierozpoczęty | wraca | wraca |
| odwołuje po czasie, ktoś przejmuje termin | zostaje u tatuażystki | zostaje na kolejną wizytę |
| odwołuje po czasie, nikt nie przejmuje | zostaje u tatuażystki | zostaje u tatuażystki |
| przekłada w darmowym czasie | przechodzi na nowy termin | przechodzi na nowy termin |
| tatuażystka odwołuje | wraca albo przechodzi na nowy termin, wybiera Ola | wraca albo przechodzi na nowy termin, wybiera Ola |

Nazywamy to opłatą, a nie zaliczką, bo zaliczka co do zasady podlega zwrotowi.

### 3. Prowizja z limitem i dowodem

Salon płaci mniej niż w Booksy, a prowizję oddaje tylko wtedy, gdy naprawdę przyprowadziliśmy mu nowego klienta.

| | Booksy | Nasza aplikacja |
|---|---|---|
| Abonament miesięczny | 145 zł + 35 zł za kolejnego pracownika | 119 zł + 25 zł za kolejnego pracownika |
| Prowizja za nowego klienta | 35–45% ceny pierwszej wizyty | 10% ceny pierwszej wizyty |
| Najmniejsza i największa prowizja | 25 zł i 250 zł | 5 zł i 30 zł |

Kwoty są netto. Nasze stawki to założenia zespołu.

**Prowizja powstaje tylko wtedy, gdy spełnione są trzy warunki naraz:**

1. Klient przeszedł z wyników naszej wyszukiwarki prosto do rezerwacji.
2. Klienta nie ma w bazie salonu i nie miał tam wcześniej wizyty.
3. Wizyta się odbyła.

Przy każdej prowizji salon widzi dowód: datę, czego klient szukał i jak doszedł do rezerwacji. Jeśli pokaże, że klient był już w salonie, prowizja wraca.

**Przykład:** Ania wpisuje „koloryzacja Kraków”, wybiera z wyników salon Beaty i rezerwuje farbowanie za 300 zł. Nigdy tam nie była. Po wizycie salon oddaje nam 30 zł. W Booksy byłoby to 105–135 zł. Gdy Ania wróci, salon nie zapłaci już nic. Za jej koleżankę, która zarezerwuje z linku na Instagramie salonu, też nie.

W wyszukiwarce nadal nie ma płatnej promocji. Wyniki zależą od usługi, odległości, wolnych terminów i oceny. Opłaty operatora płatności zostają, bo to koszt bramki, a nie nasza prowizja.

## Pytania i przypadki brzegowe

### Zadatek i kwota na wizytę

**Czy klient dostaje gotówkę z powrotem?**
Przy odwołaniu w darmowym czasie tak. Po czasie nie: dostaje kwotę na kolejną wizytę, jeśli ktoś przejął termin.

**Dlaczego nie zwykły zwrot pieniędzy?**
Bo salon by na tym tylko stracił i nie miałby powodu tego włączać. Kwota zatrzymuje pieniądze w salonie i daje klientowi powód, żeby wrócić.

**Co jeśli klient nie wykorzysta kwoty?**
Po 3 miesiącach wygasa i pieniądze zostają u salonu.

**Czy kwotę można oddać znajomemu albo wykorzystać w innym salonie?**
Nie. Działa tylko dla tego klienta i w tym salonie.

**Co jeśli termin przejmie ktoś spoza listy?**
Działa tak samo. Liczy się to, że termin został zapełniony.

**Co jeśli nowa wizyta jest krótsza?**
Termin uznajemy za przejęty, gdy nowa wizyta zajmuje co najmniej połowę zwolnionego czasu.

**Co jeśli nowa osoba przyjmie termin, a potem nie przyjdzie?**
Odwołujący zachowuje kwotę, bo termin został przejęty. Nowa osoba traci własny zadatek na zwykłych zasadach.

**Co jeśli klient odwoła wizytę opłaconą kwotą?**
W darmowym czasie kwota wraca z pierwotną datą ważności. Po czasie działa jak zwykły zadatek.

**Co jeśli salon się zamknie, a klient ma niewykorzystaną kwotę?**
Tego nie modelujemy. Kwota jest zobowiązaniem salonu, więc prawdziwy produkt potrzebowałby tu regulaminu.

**Czy to działa z BLIK-iem i Google Pay?**
Tak. Zadatek wpłaca się normalnie, a kwota jest zapisana w aplikacji.

**Czy salon musi brać zadatki?**
Nie. Bez zadatku działają potwierdzenie i kolejka.

### Kolejka

**Co jeśli dwie osoby klikną naraz?**
Termin dostaje tylko pierwsza. Druga widzi, że termin jest już zajęty.

**Co jeśli ktoś zignoruje ofertę?**
Oferta wygasa i idzie do następnej osoby. Po 3 zignorowanych ofertach z rzędu wpis zostaje wyłączony, a klient może zapisać się ponownie.

**Co jeśli klient dostanie ofertę w nocy?**
Nie dostanie. Oferty czekają do 7:00.

**Czy można zapisać się na wiele list „na zapas”?**
Najwyżej 3 aktywne wpisy na klienta.

**Co jeśli nikt nie przyjmie oferty?**
Termin wraca do puli wolnych terminów, a zadatek zostaje u salonu.

### Potwierdzenie „Będę”

**Co jeśli klient nie kliknie?**
Wizyta z zadatkiem zostaje. Przy wizycie bez zadatku kolejka rusza 12 h przed wizytą, ale klient traci termin dopiero, gdy ktoś inny go weźmie. Dostaje wtedy powiadomienie.

**Co jeśli wizyta jest zarezerwowana mniej niż 24 h wcześniej?**
Nie prosimy o potwierdzenie, bo sama rezerwacja jest świeża.

**Co jeśli ktoś kliknie „Będę” i nie przyjdzie?**
To zwykły no-show. Kolejka nie ma kiedy ruszyć, a zadatek zostaje u salonu. Potwierdzenie zmniejsza takie sytuacje, ale ich nie usuwa.

### Salon i tatuaże

**Co jeśli wizytę odwołuje salon?**
Klient dostaje pełny zwrot płatności z góry albo przenosi je na nowy termin.

**Kto decyduje, czy projekt jest gotowy?**
Salon oznacza pracę jako wykonaną przed odwołaniem, a klient widzi ten status. Bez oznaczenia opłata wraca. Nie sprawdzamy jakości projektu.

**Kto może przejąć termin u tatuażysty?**
Tylko ktoś z gotowym projektem albo usługą, która mieści się w tym czasie. Dlatego w tej branży przejęcia będą rzadsze niż u fryzjera.

**Co przy tatuażu na kilka sesji?**
Opłatę za projekt płaci się raz. Zadatek za termin dotyczy każdej sesji osobno.

**Co jeśli klient chce zmienić projekt?**
Salon może ustawić nową opłatę za przygotowanie. Poprzednia zostaje, jeśli praca była wykonana.

**Czy klient może przełożyć wizytę zamiast ją odwołać?**
W darmowym czasie pieniądze przechodzą na nowy termin. Po czasie zadatek traktujemy jak przy późnym odwołaniu, a opłata za przygotowanie przechodzi na nowy termin.

### Prowizja i abonament

**Z czego żyje aplikacja?**
Z abonamentu i prowizji za nowych klientów. Płatnej promocji w wyszukiwarce nie sprzedajemy.

**Dlaczego nie sam abonament?**
Wtedy cały koszt aplikacji spadałby na stałą opłatę, także przy salonach, którym nie przyprowadzamy klientów. Dlatego abonament jest niższy, a resztę zarabiamy wtedy, gdy salon naprawdę coś zyskał.

**Ile salon zapłaci w porównaniu z Booksy?**
Salon z 3 pracownikami i 10 nowymi klientami miesięcznie, przy wizycie za 150 zł, zapłaci 319 zł netto. W Booksy z Boostem będzie to 740–890 zł netto. Bez nowych klientów zapłaci 169 zł zamiast 215 zł.

**Skąd wiadomo, że klient przyszedł z wyszukiwarki?**
System zapisuje drogę klienta od wyników do rezerwacji. Nie pytamy klienta o to, skąd się dowiedział, i niczego nie zgadujemy.

**Co jeśli klient obejrzał salon w wyszukiwarce, a zarezerwował z Instagrama?**
Prowizji nie ma. Liczy się tylko przejście z wyników prosto do rezerwacji, w czasie do 60 minut.

**Co jeśli stały klient salonu znajdzie go w wyszukiwarce?**
Prowizji nie ma, jeśli jego numer telefonu jest w bazie salonu albo miał tam wcześniej wizytę. Salon może zaimportować bazę klientów przed startem.

**Co jeśli salon uważa, że prowizja jest niesłuszna?**
Ma 30 dni na zgłoszenie. Administrator sprawdza sprawę, a gdy salon wykaże wcześniejszą wizytę klienta, prowizja wraca.

**Czy płaci się za klienta z listy oczekujących?**
Nie. Taki termin zapełnia kolejka, a nie wyszukiwarka.

**Czy prowizja rośnie, jeśli klient dokupi coś na miejscu?**
Nie. Liczymy ją od ceny z chwili rezerwacji, więc zmiana wizyty po fakcie nic nie daje.

**Co jeśli nowy klient nie przyjdzie albo salon odwoła wizytę?**
Prowizji nie ma, bo wizyta się nie odbyła.

**Czy salon może oznaczyć klienta jako nieobecnego, żeby nie płacić?**
Może i to słaba strona modelu. Przy najwyżej 30 zł taka sztuczka opłaca się dużo mniej niż przy 250 zł, ale nie znika. Dopiero potwierdzanie obecności kodem QR rozwiązałoby to do końca.

**Czy salon może zapłacić za wyższą pozycję?**
Nie. Płatności salonu nie wpływają na wyniki wyszukiwania.

**Czy abonament nie odstraszy małych salonów?**
Może, ale jest niższy niż w Booksy. Nasze stawki to założenia, które trzeba by sprawdzić na prawdziwych kosztach aplikacji i rozmowach z salonami.

### Czego nie obiecujemy

- Nie usuwamy no-show, tylko je ograniczamy.
- Nie twierdzimy, że kolejka jest naszym wynalazkiem.
- Nie twierdzimy, że wymyśliliśmy niską prowizję. Wyróżnia nas połączenie limitu i dowodu.
- Korzyści dla salonu to założenia, które trzeba by sprawdzić na prawdziwych salonach.
- Liczby ze skarg pochodzą z naszej próby 509 opinii i ok. 6 wątków na Reddicie, a nie z badania całego rynku.
