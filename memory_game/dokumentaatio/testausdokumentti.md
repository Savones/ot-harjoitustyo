# Testausdokumentti

## Yksikkötestaus

### Testikattavuus

[coverage-report](kuvat/test_coverage.png)

Testikattavuus on 36%, kun ui pakkauksessa olevia käyttöliittymää käsitteleviä tiedostoja ei ole otettu mukaan.
Testauksessa painopiste on logic ja object pakkauksissa olevissa luokissa, joiden yksittäisiä metodeita on testattu kattavasti.
Lisäksi tietokannan käsittelystä vastaavaa luokkaa Database on testattu 91% kattavuudella.
loops pakkauksessa olevia luokkia ei ole testattu ollenkaan, mikä vaikuttaa paljon ohjelmen yhteenlaskettuun haarautumakattavuuteen.

## Järjestelmätestaus

Pelin asennusta sekä pelaamista on testattu manuaalisesti Linux-ympäristössä. Testauksessa on selvinnyt, että 
```poetry run invoke test``` komento täytyy suorittaa kahdesti siinä tilanteessa, että peliä ei ole vielä pelattu ja testejä
suoritetaan koneella ensimmäistä kertaa.

Manuaalisesti on myös testattu, että vääränlaiset toiminnot eivät aiheuta pelissä ongelmia. Esimerkiksi, jos peliä pelatessa
käyttäjä painaa ruutua ennen vuoroaan, painallusta ei lasketa. Myöskään väärän pituiset tunnukset tai salasanat eivät aiheuta virheitä
pelin toiminnassa.

## Laatuongelmia

Testikattavuus on jäänyt liian alhaiseksi. Kokonaisuuksia, esimerkiksi sisäänkirjautumista ei ole testattu muuten, kuin manuaalisesti.

Konfiguraatioita ei ole määritelty ohjelman ulkopuolella. Tämän takia testit hyödyntävät samaa tietokantaa, kuin peli.
Jotta testit ja käyttäjien tiedot eivät sekottuisi, testien suoritus aina poistaa olemassa olevan tietokannan.
