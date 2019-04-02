<!--
$theme: gaia
template: invert
-->
# Making Games with Pygame
---
#### Step1 : Create an virtual enviornment.
`python2.7 -m venv <name>`

I couldn't install with Python3 for some reason :(
#### Step2 : Activate your venv.
`source activate <name>`
#### Step3 : Install Pygame using pip.
`pip pygame`

---
### To Play Your Pygame
Move to the directory where your python file is at.
And activate your venv

`source activate <name>`

Execute your pygame.

`python <file>`

If you want to deactivate your env,

`source deactivate <name>`

---
###  Pygame Reference

* Initializing the window of the game
```python

pygame.display.set_mode((width, height), flags, depth)

```
flags: collection of additional options
depth: number of bits to use for color

---
##  [Tutorials](https://inventwithpython.com/pygame/)

* [Memory Puzzle](/Slides/MemoryPuzzle.md)
---
## My PyGame

* [Catch The Cat](/GameFiles/catanimation.py)(Under construction ...??)
