```mermaid
classDiagram
  Monopoli "*" -- "2" Noppa
  Monopoli "*" -- "2..8" Pelaaja
  Monopoli "*" -- "1" Pelilauta
  Pelilauta "1" -- "40" Ruutu
  Ruutu "1" -- Ruutu
  Pelaaja "1" -- "1" Pelinappula
  Pelinappula "*" -- "1" Ruutu
  Aloitusruutu --|> Ruutu
  Vankila --|> Ruutu
  Sattuma --|> Ruutu
  Yhteismaa --|> Ruutu
  Asema --|> Ruutu
  Laitos --|> Ruutu
  Katu --|> Ruutu
  Sattuma -- "*" Kortti
  Yhteismaa -- "*" Kortti
  Ruutu "*" -- "1" Toiminto
  Kortti "*" -- "1" Toiminto
  Katu "*" -- "0..4" Talo
  Katu "*" -- "0..1" Hotelli
  Katu "*" -- "1" Pelaaja
  class Monopoli {
    aloitusruudun_sijainti
    vankilan_sijainti
  }
  class Pelaaja {rahaa}
  class Noppa
  class Pelilauta
  class Ruutu
  class Pelinappula
  class Aloitusruutu
  class Vankila
  class Sattuma
  class Yhteismaa
  class Asema
  class Laitos
  class Katu
  class Kortti
  class Toiminto
  class Talo
  class Hotelli
```
