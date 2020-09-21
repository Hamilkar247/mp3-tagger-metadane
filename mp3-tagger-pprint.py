import argparse
import os
from pprint import pprint
from mp3_tagger import MP3File

def def_params():
    parser = argparse.ArgumentParser(
        description='testowy opis'
    )
    parser.add_argument("-f", "--file", help="plik mp3 do tagowania", required=True)
    args = parser.parse_args()
    return args

def main():
    args = def_params()
    bas_dir = os.path.dirname(os.path.realpath(__file__))
    mp3 = MP3File(args.file)
    pprint(mp3.get_tags())


if __name__ == "__main__":
    main()
