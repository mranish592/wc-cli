# wc-cli
A cli tool written in python to count lines, words, characters and bytes.

This project is inspired by [codingchallenges.fyi](https://codingchallenges.fyi/challenges/challenge-wc)

## Usage
wc-cli [-clmw] [file ...]

The following options are available:
        
- **-c**: The number of bytes in each input file is written to the standard output. This will cancel out any prior usage of the -m option.
- **-l**: The number of lines in each input file is written to the standard output.
- **-m**: The number of characters in each input file is written to the standard output. If the current locale does not support multibyte characters, this is equivalent to the -c option. This will cancel out any prior usage of the -c option.
- **-w**: The number of words in each input file is written to the standard output.

## Installation
1. Clone the repo
    ```bash
    git clone https://github.com/mranish592/wc-cli.git
    ```

2. Add an alias to run the python script.
    ### bash
    ```bash
    bash wc-cli/install-alias-bash.sh
    ```

    ### zsh
    ```bash
    zsh wc-cli/install-alias-zsh.sh
    ```

## Development steps/challenges
1. Python alias added in ~/.zshrc
2. How to take file input for python 
3. How to read lines as text in python
4. How to read files as binary in python
5. How to parse the options and files from arguments
6. How to handle multiple files
7. How to read from Standard input in python
