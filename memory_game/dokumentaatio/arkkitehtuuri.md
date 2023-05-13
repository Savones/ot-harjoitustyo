# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne koostuu viidestä eri pakkauksesta: ui, loops, logic, objects ja database.

![rakenne](kuvat/rakenne.jpg)

Ui pakkauksesta löytyy kaikki graafiseen käyttöliittymään kuuluvat luokat. Loops pakkauksessa olevat luokat pyörittävät ohjelmaa ja reagoivat käyttäjän toimintoihin. Logic pakkauksessa löytyy pelin logiikkaa hallinnoivia luokkia. Objects pakkauksessa olevat luokat alustaa objekteja. Database pakkauksessa oleva luokka suorittaa tietokantaan liittyviä toimintoja.

## Toiminnallisuuksia

### Sisäänkirjautuminen

Oheisessa sekvenssikaaviossa oletuksena on, että tietokannasta on löytynyt aiemmin syötetty käyttäjänimi "Testi", käyttäjä on syöttänyt käyttäjänimeen yhteensopivan salasanan "testi123" ja painanut käyttöliittymän "enter" painiketta.

![login_sekvenssikaavio](kuvat/login_sekvenssikaavio.jpg)

### Käyttäjän luonti

Oheisessa sekvenssikaaviossa oletuksena on, että käyttäjä on jo syöttänyt uuden käyttäjänimen "Testi", jota ei löydy vielä tietokannasta. Sitten käyttäjä on syöttänyt salasanan "testi123" ja painanut käyttöliittymän "enter" painiketta.

![create_sekvenssikaavio](kuvat/create_sekvenssikaavio.jpg)


## Pelin sovelluslogiikka

Kun pelaaja on kirjautunut onnistuneesti sisään, RegisLoop palauttaa pelaajan käyttäjänimen, joka annetaan variables luokan oliolle attribuutiksi. Variables noutaa tähän pelaajaan liittyvät tiedot tietokannasta tietokantaa käsittelevän luokan Database kautta. Peliä pyörittävä Loop saa attribuutikseen tämän variables olion, jolloin esimerkiksi pelin aikana tapahtuvat muutokset (highscoren muutos) tallettuvat ensin variables oliossa ja myöhemmin tietokantaan.

![pelin_toiminnallisuus](kuvat/pelin_toiminnallisuus.jpg)

## Tietojen pysyväistallennus

Paikallisten käyttäjien käyttäjänimet, salatut salasanat sekä paras tulos talletetaan paikallisesti luotuun SQLite-tietokantaan, player_database.db. Tätä tietokantaa käsittelee pakkauksen database luokka Database. 

## Rakenteen heikkouksia

Esimerkiksi loops pakkauksessa olevat luokat ovat vastuussa useista asioista, eli tehtäviä ei ole jaettu kaikkialla yksi /luokka.
Lisäksi tietokannan sovelluksessa ei ole käytetty ympäristömuuttujia (eivät toimineet). Näin ollen testien ajamisesta seuraa tietokannan poisto.
