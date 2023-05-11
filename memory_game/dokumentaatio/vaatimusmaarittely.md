# Vaatimusmäärittely (Muistipeli)


## Sovelluksen idea
Sovellus on muistipeli, jota pelaamalla käyttäjä voi testata ja harjoittaa muistiaan. Käyttäjälle näytetään ruutujen väläytys sarja, jonka käyttäjä yrittää toistaa oikeassa järjestyksessä. Sarja pitenee pelin edetessä ja väärästä painalluksesta käyttäjä häviää. Pelissä on kolme vaikeustasoa. Vaikeustason valinta vaikuttaa välähdysnopeuteen sekä siihen, kuinka monta uutta painallusta jokaisen kierroksen jälkeen tulee lisää. Pelissä on rekisteröitymissysteemi, minkä avulla käyttäjä voi tarkastella omaa kehitystään, ja vertailla omaa suoritusta muiden käyttäjien ennätyksiin.


## Käyttäjät
Sovelluksessa on vain käyttäjä-/pelaajarooli.

## Käyttöliittymä
- Kirjautumisnäkymä (1)
- Uuden tunnuksen luonti näkymä (2)
- Pelin aloitus näkymä (vaikeustason valinta) (3)
- Itse pelin näkymä (4)
- Pelin häviämis näkymä (5)
- Tulostaulu näkymä (6)

## Perustoiminnallisuus
### Ennen kirjautumista

- Kirjautumis näkymästä pääsee uuden tunnuksen luonti näkymään, jossa käyttäjätunnuksen voi luoda (1 -> 2)
  - Käyttäjänimen oltava 1-7 merkkiä ja se ei saa olla jo käytössä
  - Salasanan täytyy olla 5-19 merkkiä
  - Tunnuksen luonti näkymästä voi palata luomatta käyttäjää return napista (2 -> 1)
  - Tunnuksen luonti näkymästä siirtyy kirjautumisnäkymään, kun salasanan on syöttänyt enteristä (2 -> 1)

- Käyttäjä voi kirjautua sisään jo olemassa olevalle tilille (1 -> 3)
  - Käyttäjätunnuksen on oltava olemassa (oikea nimi ja salasana yhdistelmä)

### Kirjautumisen jälkeen

- Käyttäjä voi valita vaikeustason ja aloittaa pelin (3 -> 4)
- Käyttäjä voi kirjautua ulos (3 -> 1)

- Käyttäjä voi pelata peliä (4)
  - Peli näyttää painallussarjan, jonka käyttäjä toistaa painamalla ruutuja oikeassa järjestyksessä
  - Jokaisen oikean toiston jälkeen pelaaja nousee seuraavalle tasolle, jolloin pelaajalle näytetään uudestaan sama sarja, mutta pidempänä

- Kun käyttäjä häviää, eli painaa väärää ruutua, näkymä vaihtuu pelin häviämis näkymään (4 -> 5)
  - Käyttäjä voi aloittaa pelin alusta siirtymällä aloitus näkymään (5 -> 3)
  - Käyttäjä voi siirtyä tulostaulunäkymään (5 -> 6)
  - Käyttäjä voi kirjautua ulos (5 -> 1)

- Tulostaulu näkymässä käyttäjä voi valita, minkä vaikeustason tulostaulun haluaa esille (6)
- Käyttäjä voi palata pelin häviämis näkymään (6 -> 5)

## Laajennusideoita 

- Vaikeustasojen eroavaisuuksia voisi laajentaa, esimerkiksi ruutujen määrä voisi olla suurempi vaikeammalla tasolla.
- Peliin voisi sisällyttää useita eri muistipelejä, esimerkiksi numerosarjan muistamista testaavan pelin.
