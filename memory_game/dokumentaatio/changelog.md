# Changelog

## Viikko 3

- Lisätty Pattern-luokka, joka on vastuussa painallussarjan muodostamisesta
- Lisätty Check-luokka, jonka tehtävänä on tarkistaa, ovatko pelaajan syötteet oikein
- Lisätty Loop-luokka, joka huolehtii pelin pyörityksestä
- Lisätty main.py, jossa main-funktion kutsuminen käynnistää ohjelman
- Lisätty Display-luokka, joka piirtää graafisen käyttöliittymän
- Testattu, että Pattern-luokka toimii halutulla tavalla

- Käyttäjä näkee, joka kierroksen alussa painallussarjan
- Käyttäjä pystyy painamaan ruutuja
  - Jos osuu oikeaan ruutuun, peli jatkuu
  - Jos osuu väärään ruutuun, peli päättyy
  - Jos ei osu mihinkään ruutuun, ei tapahdu mitään
- Käyttäjä voi sulkea pelin

## Viikko 4 

- Lisätty sisäänkirjautumisnäkymä, käyttäjän luomisnäkymä, gameover näkymä sekä scoreboard näkymä
- Lisätty tietokannasta huolehtiva Database-luokka
- Lisätty sisäänkirjautumisesta huolehtiva RegisterationLoop-luokka
- Pattern-luokka uudelleennimetty Variables-luokaksi

- Käyttäjä voi tehdä käyttäjän ja kirjautua sisään (toistaiseksi vain käyttäjänimellä)
- Käyttäjä voi pelata uudelleen, kirjautua ulos tai siirtyä Scoreboard näkymään hävittyään pelin
- Käyttäjien nimet ja highscore:t talletetaan paikalliseen tietokantaan, ja niitä voidaan tarkastella Scoreboard näkymässä

- Suoritettu testejä check-, variables- ja database-luokille

## Viikko 5

- Lisätty LoginEvents-luokka, johon on siirretty kirjautumiseen liittyvä logiikka
- Lisätty ja sovellettu Squares-luokka, jossa pelin ruudut määritellään

- Käyttäjän täytyy syöttää salasanan käyttäjän luodessaan
- Käyttäjän täytyy syöttää käyttäjänimeen yhteensopiva salasana kirjautuakseen sisään
- Pelinäkymässä näkyy kirjautuneen pelaajan käyttäjänimi

## Viikko 6

- Lisätty Difficulties-luokka, jossa on määritelty eri vaikeustasojen väliset erot
- Lisätty MakeButtons ja Buttons-luokat, joilla painikkeiden määrittely ja hyödyntäminen on eroteltu muusta koodista
- Lisätty SettingsDisplay-luokka, josta löytyy uuden asetusnäkymän koodi

- Kun käyttäjä aloittaa uuden pelin, hän valitsee uudestä asetusnäkymästä vaikeustason, jolla peliä haluaa pelata
  - Toistaiseksi vaikeustason muutos muuttaa ainoastaan sarjan ruutujen välähdysnopeutta

## Viikko 7

- Käyttäjän valitsema vaikeustaso muuttaa nopeuden lisäksi sitä, kuinka monta uutta ruutua sarjaan lisätään joka kierroksella
  - Easy + 1, Medium +2, Hard +3
- Scoreboard näkymässä voi valita vaikeustason, jonka ennätystaulun käyttäjä haluaa esille
