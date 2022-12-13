# Arkkitehtuuri
## Rakenne
Sovelluksen pakkausrakenne nähdään alla olevasta flowchartista.

```mermaid
flowchart TB
  subgraph ui
    UI
    StartView
    GameView
    TextObject
    Panel
    InputField
    Button
  end
  subgraph game
    Game
    Board
    Cell
    button_functions
  end
  subgraph database
    Scores
  end
  ui-.->game
  game-.->ui
  game-.->database
```

Luokkakaavio on seuraavanlainen:

```mermaid
classDiagram
  Game "*" -- "1" Scores
  GameView "*" -- "1" Game
  Game "*" -- "1" UI
  Game "1" -- "1" Board
  Board "*" -- "*" Cell
  Cell "*" -- "1" Button
  UI "*" -- "0..1" GameView
  UI "*" -- "0..1" StartView 
  StartView "*" -- "1" Game
  StartView "*" -- "3" InputField
  StartView "*" -- "4" Button
```

Luokka Game hallitsee Käyttöliittymää, tietokantaa ja sovelluslogiikkaa.
## Käyttöliittymä
Sovelluksen käyttöliittymää hallitsee luokka ```UI```. Luokalla UI on attribuutti ```__current_view```, mikä saa arvokseen aina toisen kahdesta näkymästä: ```StartView```, joka vastaa pelilaudan luomisesta ja ```GameView```, joka renderöi pelaajalle pelilaudan.

Näkymien välillä liikutaan luokan UI metodilla ```change_state(state, game)```, missä ```state = 0``` on GameView ja ```state = 1``` on StartView.

Luokille GameView ja StartView injektoidaan olio Game.

## Sovelluslogiikka
Sovelluksen logiikan muodostavat luokat Board ja Cell. Moduuli button_functions antaa nimensä mukaan toiminnallisuuksia napeille.

Oliolla board on attribuutti ```__board```, joka on matriisi Cell olioita.

Sovelluslogiikkaa hallitsee luokka Game.
## Sovelluksen toiminnallisuudet
Alla on skenaario yhden pelilaudan ruudun klikkaamisesta.

```mermaid
sequenceDiagram
  participant UI
  participant GameView
  participant Cell
  participant Button
  participant Game
  participant button_functions
  participant Board
  UI ->>+ GameView : click(1)
  GameView ->>+ Board : get_board()
  Board -->>- GameView : [[-1]]
  GameView ->>+ Cell : button
  Cell -->>- GameView : self.button
  GameView ->>+ Button : hovered
  Button -->>- GameView : True
  GameView ->>+ Board : game_over
  Board -->>- GameView : False
  GameView ->> Button : click(1)
  Button ->> button_functions : open_cell(board, (0, 0))
  button_functions ->>+Board : open_cell((0, 0))
  Board ->> Board : lose()
  Board ->>+Game : create_font_with_new_size(30)
  Game ->>+ UI : get_font_with_new_size(30)
  UI -->>- Game : pygame.font.Font(self.font[1], 30)
  Game -->>- Board : pygame.font.Font(self.font[1], 30)
  Board ->> GameView : add_message(TextObject("You lose", (600, 50), pygame.font.Font(self.font[1], 30), color=(0, 255, 0)))
  Board -->>- button_functions : True
  GameView ->> Board : open_cell_recursion_stack_size(0)
```

Pelilaudan luominen:

```mermaid
sequenceDiagram
  participant UI
  participant button_functions
  UI->>+StartView:click(1)
  StartView->>+Button:click(1)
  Button->>+button_functions:create_board(width, height, mine_chance, game)
  button_functions->>Game:create_board(width, height, mine_chance)
  Game->>Game:board(Board(width, height, mine_chance))
  button_functions->>Game:change_state(0)
  Game->>UI:change_state(0, self)
  UI->>UI:current_view(GameView(self.font, game))
```
