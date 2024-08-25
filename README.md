# Enigma 2.0
Updated version of my previous Encryption-Decryption program. With an improved GUI and special mode! Also written by someone with 2 more years of programming experience, and hopefully the code and GUI reflects that.

## Contents
1. [Set Up](#set-up)
2. [How to Use](#how-to-use)
3. [Changelog](#changelog)

## Set Up
After cloning this repo locally, create a virtual environment. After activating it, run `pip install -r requirements.txt` to install all necessary packages. <br>
**NOTE:** this program was developed using Python 3.11.1

## How to Use
After activating your virtual environment, run `py ./main_gui.py` <br>

This section will explain the items in the GUI.
* Input Text Box - where the user enters in either the plaintext that they want to encode or the cyphertext that they want to decode.
* Clear Input and Output Button - clears both the Input and Output Text boxes
* Output Text Box - where the resulting plaintext or cyphertext will appear after decoding or encoding, respectfully.
    * This box is read-only
    * Text is automatically copied to the clipboard for ease of use.
* Encoding Mode Section - allows user to choose either how the plaintext will be encoded or how the cyphertext is currently encoded.
    * **Note:** When decoding, make sure the correct mode is selected, matching the mode used when encoding the cyphertext. Mode should be evident through cyphertext.
* Encode Button - encodes the text currently in the Input Text Box, using the mode currently selected.
* Decode Button - decodes the text currently in the Input Text Box, using the mode currently selected.

![Image of GUI](/images/gui_used.png)

## Changelog
Last updated 8/25/2024 by Jason Chen