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
|leftTopCoordsOfBox()|Converts board -> pixel|
|getBoxAtPixel()|Converts pixel -> box|
|drawIcon()|Draws an icon|
|getShapeAndColor()|Gets board space's icon's shape and color|
|drawBoxCovers()|Draws boxes in covered or revealed state|
|revealBoxesAnimation()|Plays the reveal animation|
|coverBoxesAnimation()|Plays the cover animation|
|drawBoard()|Draws the current state of the board|
|drawHighlightBox()|Draws highlighted box|
|startGameAnimation()|Plays the "Start Game" animation|
|gameWonAnimation()|Plays the "Game Won" animation|
|hasWon()|Tells if the player won|

---
## generateRevealedBoxesData()

```python
def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes
```

## returns boolean list 

True : when the item is revealed
False : when the item is hidden

---
## getRandomizedBoard()

```python
def getRandomizedBoard():
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )

    random.shuffle(icons) 
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2) 
    icons = icons[:numIconsUsed] * 2 
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] 
        board.append(column)
    return board
```

## returns board data structure
Get a list of all possible icons 

shuffle them -> calculate how many of them you need and get 2 each -> shuffle again

Delete the first icon (icon[0])  in the  list as we append them so we can add each icon.
icon[0] will be updated every time.

---

