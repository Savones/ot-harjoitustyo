```mermaid
 classDiagram
      Pelaaja "  2-8" -- "1" Ruutu
      class Pelaaja{
          nappula
      }
      class Ruutu{
          seuraava_ruutu
      }
      Lauta "1" -- "  40" Ruutu
      class Lauta{
          2 noppaa
      }
      Lauta "1" -- "  2-8" Pelaaja
```
