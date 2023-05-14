# Muistipeli / Memory game

Sovellus on muistipeli, jota pelaamalla käyttäjä voi testata ja harjoittaa muistiaan. Käyttäjälle näytetään ruutujen väläytys sarja, jonka käyttäjä yrittää toistaa oikeassa järjestyksessä. Sarja pitenee pelin edetessä ja väärästä painalluksesta käyttäjä häviää. Pelissä on kolme vaikeustasoa. Vaikeustason valinta vaikuttaa välähdysnopeuteen sekä siihen, kuinka monta uutta painallusta jokaisen kierroksen jälkeen tulee lisää. Pelissä on rekisteröitymissysteemi, minkä avulla käyttäjä voi tarkastella omaa kehitystään, ja vertailla omaa suoritusta muiden käyttäjien ennätyksiin.

## Releases

- [Loppupalautus](https://github.com/Savones/ot-harjoitustyo/releases/tag/loppupalautus)
- [Viikko6 release](https://github.com/Savones/ot-harjoitustyo/releases/tag/viikko6)
- [Viikko5 release](https://github.com/Savones/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

- [Käyttöohje](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/kayttoohje.md)

- [Työaikakirjanpito](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/tyoaikakirjanpito.md)

- [Vaatimusmäärittely](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/vaatimusmaarittely.md)

- [Changelog](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/arkkitehtuuri.md)

- [Testausdokumentti](https://github.com/Savones/ot-harjoitustyo/blob/master/memory_game/dokumentaatio/testausdokumentti.md)

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
Ennen mitä tahansa komentoa siirry pelin juurihakemistoon:
```
cd memory_game
```
Testaa ohjelmaa alla olevalla komennolla. **Huom** - mikäli testit eivät mene läpi ensimmäisellä suorituksella, suorita komento uudelleen. Tämän pitäisi ratkaista ongelma.
```
poetry run invoke test
```
Testikattavuusraportin saa komennolla:
```
poetry run invoke coverage-report
```
Pylint tulokset saa komennolla:
```
poetry run invoke lint
```
