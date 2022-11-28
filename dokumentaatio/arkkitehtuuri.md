```mermaid
classDiagram
  Game "*" -- "1" UI
  Game "*" -- "1" Board
  Board "*" -- "*" Cell
  Cell "*" -- "1" Button
  UI "*" -- "0..1" GameView
  GameView "*" -- "1" Board
```
