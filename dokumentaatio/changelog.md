# Changelog
## Viikko 3
* Käyttöliittymä näyttää pelaajalle ikkunan, mutta ei vielä piirrä mitään.
* Lisätty pelilaudan logiikasta suurin osa. Pelilaudasta voidaan avata ruutuja ja pelilauta generoituu ensimmäisellä avauksella. Pelilaudan logiikkaa ei kuitenkaan ole yhdistetty vielä käyttöliittymään millään tavalla.
* Testattu, että ensimmäisellä ruudun avauksella pelilauta generoituu.
* Testattu, että ruudun avauksella palautetaa False kun yritetään avata ruutu joka on pelilaudan ulkopuolella.
## Viikko 4
* Lisätty luokka GameView, joka renderöi miinaharavalaudan käyttöliittymään.
* Tehty klikkaamisen toiminnallisuus loppuun.
* Lisätty luokka Button, jossa on nappulan toiminnallisuus.
* Testattu pelilaudan kaikki tämänhetkinen toiminnallisuus.
* Testattu moduulin button_functions kaikki tämänhetkinen toiminnallisuus.
## Viikko 5
* Lisätty luokka StartView, joka renderöi aloitusnäkymän.
* Tehty kaikki miinaharavan perustoiminnallisuudet loppuun.
* Aloitusnäkymästä voi luoda eri tasoisia pelilautoja ja myös kustoimoidun laudan.
* Lisätty luokat InputField, TextObject ja panel.
* Kasvatettu pelilaudan ja moduulin button_functions testausta.
## Viikko 6
* Lisätty luokka Scores, joka hallitsee tietokantaa. Tietokantaan tallennetaan tuloksia pelikerroista.
* Tietokannan tulokset renderöidään tulostauluihin.
* Testattu luokka Scores.
