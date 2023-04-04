```mermaid
 classDiagram
      Pelaaja "2-8" -- "1" Pelilauta
      Pelilauta "1" -- "40" Ruutu
      Ruutu "1" -- "0-8" Pelaaja
      Noppa "2" -- "1" Pelilauta
      Pelinappula "1" -- "1" Pelaaja
      Pelinappula "1" -- "1" Ruutu
      Aloitusruutu --|> Ruutu
      Vankila --|> Ruutu
      Toiminto "1" -- "1" Ruutu
      Sattuma --|> Ruutu
      Yhteismaa --|> Ruutu
      Kortti "1" -- "1" Toiminto
      Sattuma "1" -- "1" Kortti
      Yhteismaa "1" -- "1" Kortti
      Asema --|> Ruutu
      Laitos --|> Ruutu
      Normaali katu --|> Ruutu
      Normaali katu "1" -- "0-4" Talo
      Normaali katu "1" -- "0-1" Hotelli
      Normaali katu "*" -- "1" Pelaaja
      Rahaa -- Pelaaja
```