```mermaid
 classDiagram
      Pelaaja "2-8" --> "1" Pelilauta
      Pelilauta "1" --> "40" Ruutu
      Ruutu "1" --> "0-8" Pelaaja
      Noppa "2" --> "1" Pelilauta
      Pelinappula "1" --> "1" Pelaaja
      Pelinappula "1" --> "1" Ruutu
```