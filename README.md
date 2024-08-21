# ColorSwapsFrameScript

## First time use

run **prerequisites.cmd** to make sure all dependencies are installed

## How to use

### Quick Start

- Make sure to have Python installed
- Run prerequisites once **when using for the first time**
- to import a SVG run **"RUN_IMPORT.CMD"**
- to generate pcode run **"RUN_GENERATOR.CMD"**

#### IMPORTANT

**IF THE GAME KEEPS CRASHING DO NOT USE THIS TOOL**
Try updating the repo by [downloading it again from github](https://github.com/bucccket/ColorSwapsFrameScript "Github Link")

### Parameters

Inside the file are 3 parameters you need to make sure are set correctly

ColorSwapClass, ColorSwapVector, ColorSwapArray change each update. Here is how you can find them inside BrawlhallaAir.swf:

- ColorSwapClass is the class defining the NO_COLOR_SCHEME object
- ColorSwapVector is the last static vector of ColorSwapClass
- ColorSwapArray is the last non-static public Array

### Running

make sure you have python installed and just use FrameScriptGen.py **OR** use RUN.CMD

Dont be stupid about this stuff
Feel free to maintain the code
