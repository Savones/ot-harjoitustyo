# Muistipeli / Memory game

Sovellus on peli, jota pelaamalla käyttäjä voi testata ja harjoittaa muistiaan. Käyttäjälle näytetään sarja ruutujen välähdyksiä, jonka käyttäjä yrittää toistaa oikeassa järjestyksessä. Sarja pitenee pelin edetessä ja väärästä painalluksesta käyttäjä häviää. Pelissä on rekisteröitymissysteemi, minkä avulla käyttäjä voi tarkastella omaa kehitystään, ja vertailla omaa suoritusta muiden paikallisten käyttäjien ennätyksiin.

## Dokumetaatio

- [Työaikakirjanpito](https://github.com/Savones/ot-harjoitustyo/blob/master/memomy_game/dokumentaatio/tyoaikakirjanpito.md)

- [Vaatimusmäärittely](https://github.com/Savones/ot-harjoitustyo/blob/master/memomy_game/dokumentaatio/vaatimusmaarittely.md)

- [Changelog](https://github.com/Savones/ot-harjoitustyo/blob/master/memomy_game/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/Savones/ot-harjoitustyo/blob/master/memomy_game/dokumentaatio/arkkitehtuuri.md)

## Pelin asennus

Pelin riippuvuudet voit asentaa komennolla:
```
poetry install
```
Kun riippuvuudet on asennettu, voit käynnistää pelin komennolla:
```
poetry run invoke start
```
