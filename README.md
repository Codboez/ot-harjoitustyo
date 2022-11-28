# Miinaharava

## Asennus
1. Asenna ohjelman riippuvuudet komennolla
```
poetry install
```
2. Käynnistä ohjelma komennolla
```
poetry run invoke start
```
## Dokumentaatio
* [Vaatimusmäärittely](https://github.com/Codboez/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
* [Tuntikirjanpito](https://github.com/Codboez/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
* [Changelog](https://github.com/Codboez/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
* [Arkkitehtuuri](https://github.com/Codboez/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
## Poetry tehtäväkomentoja
* Käynnistä sovellus
```
poetry run invoke start
```
* Käynnistä testit
```
poetry run invoke test
```
* Luo testikattavuusraportti
```
poetry run invoke coverage-report
```
* Käynnistä pylint testit
```
poetry run invoke lint
```
