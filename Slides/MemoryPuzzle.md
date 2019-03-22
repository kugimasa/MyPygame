<!--
$theme: gaia
template: invert
-->
# Memory Puzzle
## [python script](../GameFiles/memorypuzzle.py)
---
## Fuctions

|function|behavior|
|:------:|:------:|
|main()|The main function|
|generateReavealedBoxesData()|Returns a data structre that represents which boxes are covered|
|getRandomizedBoard()|Returns the state of the board|
|splitIntoGroupsOf()|Splits a list into a list of lists|

---
|function|behavior|
|:------:|:------:|
|leftTopCoordsOfBox()|Converts board -> pixel|
|getBoxAtPixel()|Converts pixel -> box|
|drawIcon()|Draws an icon|
|getShapeAndColor()|Gets board space's icon's shape and color|
|drawBoxCovers()|Draws boxes in covered or revealed state|
|revealBoxesAnimation()|Plays the reveal animation|
|coverBoxesAnimation()|Plays the cover animation|

---
|function|behavior|
|:------:|:------:|
|drawBoard()|Draws the current state of the board|
|drawHighlightBox()|Draws highlighted box|
|startGameAnimation()|Plays the "Start Game" animation|
|gameWonAnimation()|Plays the "Game Won" animation|
|hasWon()|Tells if the player won|

