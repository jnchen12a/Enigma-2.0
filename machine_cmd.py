from machine import Machine, InvalidCypherText, CharNotSupported, GoofyException
import modes
from pathlib import Path
import argparse

def printTerminal(s: str, verbose: bool) -> None:
    if verbose:
        print(s)

def processFile(p: Path) -> None:
    # assumes p is a file
    try:
        contents = p.read_text(encoding='utf-8')
        out = myMachine.encode(contents) if encode else myMachine.decode(contents)
        p.write_text(out, encoding='utf-8')
    except CharNotSupported as e:
        print(f'ERROR: {e} is currently not a supported character. Skipping for now...')
    except Exception as e:
        print('ERROR: Something wrong occured.')
        print(e)
        print('Skipping for now...')

if __name__ == '__main__':
    supportedFileTypes = ['.txt']
    # intake command line arguments
    # py machine_cmd.py <list of files/folders> -m [n|g]
    parser = argparse.ArgumentParser(description='Input files/folders that you want to be encoded/decoded.')
    parser.add_argument('paths', nargs='+', help='Directories or files to process. Currently, for directories, subdirectories will not also be processed.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Toggle the verbosity of the program.')
    parser.add_argument('-m', '--mode', default='n', choices=['n', 'g'], help='Choose the mode to run the machine in, (n)ormal or (g)oofy.')
    parser.add_argument('-o', '--operation', choices=['e', 'd'], required=True, help='Choose whether to (e)ncode or (d)ecode files (required).')
    
    args = parser.parse_args()
    verbose = args.verbose
    mode = modes.NORMAL if args.mode == 'n' else modes.GOOFY
    encode = True if args.operation == 'e' else False
    inputs = args.paths

    myMachine = Machine(mode)

    operationString = 'Encoding' if encode else 'Decoding'
    modeString = 'normal' if mode == modes.NORMAL else 'goofy'
    printTerminal(f'{operationString} in {modeString} mode...', verbose)
    for item in inputs:
        p = Path(item)
        if not p.exists():
            print(f'ERROR: {p} does not exist. Skipping for now...')
            continue
        
        printTerminal(f'Processing {p}...', verbose)
        # check p is a file or directory
        if p.is_file():
            if p.suffix in supportedFileTypes:
                processFile(p)
            else:
                print(f'ERROR: {p} is not a supported file type.')
                print('Supported file types:', supportedFileTypes)
                print('Skipping for now...')
        elif p.is_dir():
            for subItem in p.iterdir():
                if subItem.is_file() and subItem.suffix in supportedFileTypes:
                    printTerminal(f'Processing {subItem}...', verbose)
                    processFile(subItem)
        else:
            print(f'ERROR: {p} is neither a file nor directory. Skipping for now...')
            continue
    
    printTerminal('Finished.', verbose)
