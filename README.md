# Enigma 2.0
Updated version of my previous Encryption-Decryption program. The same plaintext will encode into different cyphertext each time. With an improved GUI and special mode!

## Contents
1. [Set Up](#set-up)
2. [How to Use](#how-to-use)
3. [Using Command Line Tool](#using-command-line-tool)
4. [Changelog](#changelog)

## Set Up
After cloning this repo locally, create a virtual environment. After activating it, run `pip install -r requirements.txt` to install all necessary packages. <br>
***NOTE:*** this program was developed using Python 3.11.1

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
* Choose File Button - allows you to use a text file as input.

![Image of GUI](/images/gui_used.png)

If you'd like to see an example of what the "I'm Feeling Goofy" mode outputs, take a look at /images/goofy.png ***(SPOILER ALERT!)***.

## Using Command Line Tool
The command line tool can be used to encode/decode files "in place". In other words, a file is read in, processed, and the output overwrites what was originally in the file.

**WARNING: If successful, file contents will be overwritten!**

Run the command line tool with the command `py machine_cmd.py [options]`.

Run `py machine_cmd.py --help` for help with the options.

## Changelog
Last updated 12/23/2025 by Jason Chen
