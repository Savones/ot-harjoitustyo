# Vaatimusmäärittely (Muistipeli)


## Sovelluksen idea
Sovellus on muistipeli, jota pelaamalla käyttäjä voi testata ja harjoittaa muistiaan. Käyttäjälle näytetään ruutujen väläytys sarja, jonka käyttäjä yrittää toistaa oikeassa järjestyksessä. Sarja pitenee pelin edetessä ja väärästä painalluksesta käyttäjä häviää. Pelissä on rekisteröitymissysteemi, minkä avulla käyttäjä voi tarkastella omaa kehitystää, ja vertailla omaa suoritusta muiden käyttäjien ennätyksiin.


## Käyttäjät
Sovelluksessa on vain käyttäjä-/pelaajarooli.

## Käyttöliittymä
- Kirjautumisnäkymä (1)
- Uuden tunnuksen luonti näkymä (2)
- Pelin aloitus näkymä (3)
- Itse pelin näkymä (4)
- Leaderboard näkymä (5)

## Perustoiminnallisuus
### Ennen kirjautumista

- Kirjautumis näkymästä nappia painamalla pääsee uuden tunnuksen luonti näkymään, jossa käyttäjätunnuksen voi luoda (1 -> 2)
  - Käyttäjänimen oltava ainakin 3 merkkiä ja se ei saa olla jo käytössä
  - Salasanan oltava ainakin kuusi merkkiä

- Käyttäjä voi kirjautua sisään jo olemassa olevalle tilille (1 -> 3)
  - Käyttäjätunnuksen on oltava olemassa (oikea nimi ja salasana yhdistelmä)

### Kirjautumisen jälkeen

- Käyttäjä voi aloittaa uuden pelin (3 -> 4)
  - Käyttäjä voi pelata peliä (4)
    - Peli näyttää painallussarjan, jonka käyttäjä toistaa painamalla ruutuja oikeassa järjestyksessä
    - Jokaisen oikean toiston jälkeen pelaaja nousee seuraavalle tasolle, jolloin pelaajalle näytetään uudestaan sama sarja +1 uusi painallus
  - Käyttäjä voi lopettaa pelin (4 -> 3)
  -  Kun käyttäjä häviää palataan pelin aloitus näkymään (4 -> 3)

- Käyttäjä voi siirtyä leaderboard näkymään (3 -> 5)
  - Käyttäjä voi palata napista pelinaloitusnäkymään (5 -> 3)

- Käyttäjä voi kirjautua ulos (3 -> 1)

## Laajennusideoita 
