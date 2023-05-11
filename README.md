# Muistipeli / Memory game

Peliä pelaamalla käyttäjä voi testata ja harjoittaa muistiaan. Käyttäjälle näytetään sarja ruutujen välähdyksiä, jonka käyttäjä yrittää toistaa oikeassa järjestyksessä. Sarja pitenee pelin edetessä ja väärästä painalluksesta käyttäjä häviää. Pelissä on rekisteröitymissysteemi, minkä avulla käyttäjä voi tarkastella omaa kehitystään, ja vertailla omaa suoritusta muiden paikallisten käyttäjien ennätyksiin.

## Releases

- [Viikko6 release](https://github.com/Savones/ot-harjoitustyo/releases/tag/viikko6)
- [Viikko5 release](https://github.com/Savones/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

- [Käyttöohje](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/kayttoohje.md)

- [Työaikakirjanpito](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/tyoaikakirjanpito.md)

- [Vaatimusmäärittely](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/vaatimusmaarittely.md)

- [Changelog](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/arkkitehtuuri.md)

## Pelin asennus

Siirry pelin juurihakemistoon komennolla:
```
cd memory_game
```

Pelin riippuvuudet voit asentaa komennolla:
```
poetry install
```
Kun riippuvuudet on asennettu, voit käynnistää pelin komennolla:
```
poetry run invoke start
```
## Komentoja

Testaus
```
poetry run invoke test
```
Testikattavuusraportti
```
poetry run invoke coverage-report
```
Pylint
```
poetry run invoke lint
```
