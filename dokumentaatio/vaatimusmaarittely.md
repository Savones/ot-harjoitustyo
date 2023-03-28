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
# Ennen kirjautumista
- Kirjautumis näkymästä nappia painamalla pääsee uuden tunnuksen luonti näkymään, jossa käyttäjätunnuksen voi luoda (1 -> 2)
- Käyttäjä voi kirjautua sisään jo olemassa olevalle tilille (1 -> 3)

# Kirjautumisen jälkeen
- Käyttäjä voi aloittaa uuden pelin (3 -> 4)
  _ Käyttäjä voi pelata peliä (4)
  _ Käyttäjä voi lopettaa pelin (4 -> 3)
  _ Kun käyttäjä häviää palataan pelin aloitus näkymään (4 -> 3)
- Käyttäjä voi siirtyä leaderboard näkymään (3 -> 5)
- Käyttäjä voi kirjautua ulos (3 -> 1)

## Laajennusideoita 
