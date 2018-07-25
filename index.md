---
title: Unicode Parser
description: Unicode Parser is a client-side mod for Minetest by muhdnurhidayat, it's temporary solution to chat in unicode characters.
lang: en
layout: default
---


# Unicode Parser
View the source for the release [here](https://github.com/MuhdNurHidayat/unicodeparser) and source for this website [here](https://github.com/MuhdNurHidayat/unicodeparser/tree/gh-pages).


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

If you use Windows, run the included exe file under `tools` folder, or else run
the Python2 script file under `tools` folder, then write the usual text using
your IME into the "Input" field, then just enter and the output codepoint will
be copied to your clipboard.

In game, to use GUI then send `.ug` and a formspec will appear asking for input,
paste (Ctrl-V) the codepoint and click on "Say". To use CLI then send `.uc` followed
by the unicode codepoint that was copied from the tool earlier.

### As workaround of paste problem

The codepoint appeared when you paste into Minetest itself is supposedly already
in the format supported by the CSM, so you don't need to run any tools.

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

Licensed under The MIT License, see [LICENSE.txt](LICENSE.txt "The MIT License").


## Changelog

### v1.2

- The tool now convert the codepoint when you press enter after writing the text, so you don't need to click the button "Convert" anymore, but the button is still there for compatibility reasons.
- The tool now copies the converted codepoint to your clipboard when ypu enter or press the "Convert" button, so you don't need to manually copy (Ctrl-C) anymore.
- Added link to GitHub at the tool.
- The tools now have icon, which is modified from Minetest icon.
- Added Windows executable for the tool so that those who don't have Python2 would not need to install it just to use the tool.
- Additional thanks to the following people who either tested the Windows executable file or given some advice to me:
  - `Heathcliff#0001` (`Anime Trending` Discord server)
  - `Fidoze#7037` (`Anime Trending` Discord server)
  - `Aqo#5414` (`A.I. Channel Unofficial` Discord server)
  - `xnamkcor#3740` (`A.I. Channel Unofficial` Discord server)
  
(Note: I purposely ask people not from Minetest community to test it because I don't want biased feedback.) 


### v1.1

- Added support for `\uXXXX` unicode escape in addition to the existing `\0xXXXX` unicode sequence.
- Added command `.uc` for command line interface, this means those who don't want to use the GUI can now straight away write the unicode escape in chat.
- Updated `README` to reflect the changes.


### v1.0

- The original initial release.
