## Viikko 4

- Lisätty Game, Player ja Platform -luokat(keskeinen sovelluslogiika)
- Käyttäjä näkee pelihahmon ja tasoja joille pelihahmo voi hyppiä
- Pelin perustoiminnallisuudet toteutettu
    - aloitusnäkymässä on ohjeet pelaamiseen ja voi aloittaa uuden pelin
    - pelihahmolla voi hyppiä tasoja pitkin loputtomasti ylöspäin ja tasot siirtyvät sitä mukaan alaspäin
    - ylälaidassä näkyy pisteet ja ohjeet aloitusnäkymään palaamiseen
    - kun putoaa tulee gameover-näkymä jossa näkyy pisteet ja voi aloittaa uuden pelin
    - alustava muuttuva tausta

## Viikko 5

- Lisätty BoostPlatform-luokka ja sen toiminnallisuudet
    - tämän luokan tasoja tulee tavallisten tasojen lisäksi, mutta harvemmin ja niiltä pääsee hyppäämään tavallista korkeammalle
- BoostPlatform-luokan testiluokka ja testit lisätty

## Viikko 6

- Lisätty Coin-luokka ja sen toiminnallisuudet
    - pelissä voi kerätä kolikoita
    - kerättyjen kolikoiden määrän voi nähdä pelin aikana ylälaidassa sekä gameover-näkymässä
- Coin-luokan testiluokka ja testit lisätty

## Viikko 7

- Highscore lisätty
    - parhaan tuloksen voi nähdä startmenu- ja gameover-näkymissä
    - highscore tallentuu tiedostoon ja luetaan sieltä tarvittaessa
- Most coins lisätty
    - suurimman määrän kerättyjä kolikoita voi nähdä nähdä startmenu- ja gameover-näkymissä
    - tallentuu highscoren tapaan tiedostoon
