# Arkkitehtuurikuvaus

## Luokkarakenne

```mermaid
 classDiagram
      Game "1" <-- "1" Player
      Game "1" <-- "*" Platform
      Game "1" <-- "*" Boost_platform
      Game "1" <-- "*" Coin
      
```

## Tietojen tallennus

Pelin parhaat tulokset eli highscore ja most coins tallennetaan omiin tiedostoihinsa. Nämä tiedot haetaan tiedostoista startmenu- ja gameover-näkymiin.

## Ohjelman rakenteen heikkoudet

Sovelluslogiikka ja käyttöliittymää ei ole eriytetty.
