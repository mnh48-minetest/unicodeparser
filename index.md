---
title: Unicode Parser
description: Unicode Parser is a client-side mod for Minetest by muhdnurhidayat.
lang: en
layout: default
---

# Unicode Parser

## What is Unicode Parser
Unicode Parser `unicodeparser` is a client-side mod (CSM) for [Minetest](https://www.minetest.net).
It allows you write unicode codepoint in either \uXXXX format or \0xXXXX format
then it will convert to real text string of that codepoint and send it out on
public chat. Both GUI and CLI now available.

![The GUI](images/thegui.png?raw=true "The GUI")

## Intended use

This CSM is used as a workaround of the inability to use Input Method Editors
(IME) on Minetest, especially for Windows users as I could use IME on Android
version of Minetest but not on Windows version.

This CSM could also be used by certain Ubuntu version users who couldn't paste
text in Minetest (where the paste text appears as codepoints and not real text).

## How to use

### As workaround of IME

Run the included Python2 script under `tools` folder to write the usual text
using your IME, click on "Convert" button, then copy (Ctrl-C) the output
codepoint.

In game, to use GUI then send `.ug` and a formspec will appear asking for input,
paste (Ctrl-V) the codepoint and click on "Say". To use CLI then send `.uc` followed
by the unicode codepoint you want to convert.

### As workaround of paste problem

The codepoint appeared when you paste into Minetest itself is supposedly already
in the same format needed by the CSM, so you don't need to run the Python2 script.

In game, to use GUI then send `.ug` and directly paste in the input, then click "Say".
To use CLI then send `.uc` followed by the unicode codepoint you want to convert.

## CSM in action

GUI version and as workaround of IME:

![GUI In Action](images/inaction.gif?raw=true "GUI In Action")

CLI version and as workaround of paste problem:

![CLI In Action](images/cli.gif?raw=true "CLI In Action")

## To do

- Include translation support (which seems to be impossible right now because CSM can't access other files)

## License

(C) muhdnurhidayat (MNH48.com) and contributors

Licensed under The MIT License.
