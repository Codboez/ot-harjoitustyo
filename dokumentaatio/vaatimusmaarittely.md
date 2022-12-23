# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on oma versio Miinaharava pelistä.

## Nykyisen version toiminnallisuudet
* Toimiva versio Miinaharava pelistä
  * Laudan ruutua klikkaamalla paljastetaan kyseinen ruutu.
  * Paljastetut ruudut näyttävät kuinka monta miinaa kyseisen ruudun ympärillä on.
  * Tyhjän ruudun (ruutu jonka ympärillä ei ole yhtäkään miinaa) paljastaessa peli paljastaa automaattisesti kaikki tämän ympärillä olevat ruudut.
  * Ensimmäisen ruudun paljastaessa peli generoi laudan siten, että vähintään klikatun kohdan ympärillä ei ole yhtäkään miinaa.
  * Miinan paljastaessa pelaaja häviää.
  * Ruutuja voi merkata miinoiksi.
  * Pelaaja voittaa kun kaikki ruudut missä ei ole miinaa on paljastettu.
* Pelissä voi luoda eritasoisia/-kokoisia lautoja muutamasta valmiista vaihtoehdosta, sekä luoda kustomoidun laudan, jolle voi valita oman koon ja miinojen määrän.
* Graafinen käyttöliittymä
  * Sisältää aloitusnäkymän, missä voi luoda eritasoisia Miinaharava lautoja, ja näkymän itse Miinaharava pelistä.
  * Käyttöliittymää varten on rakennettu helposti uudelleenkäytettävät ja helposti kustomoitavat luokat Button, InputField, TextObject ja Panel, jotka renderöivät nimensä mukaisia olioita käyttöliittymään.
* Pelaajan voittaessa pelin, peli tallentaa tietokantaan tiedot pelilaudasta ja peliin käytetystä ajasta.
* Peli näyttää pelaajalle tulostaulun lokaaleista aikaennätyksistä jokaiselle vaikeustasolle.
