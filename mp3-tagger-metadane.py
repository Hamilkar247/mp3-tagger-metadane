import logging
from mp3_tagger import MP3File, VERSION_1#, VERSION_BOTH
import argparse
import os
from pprint import pprint


# tworzę MP3File
# mp3 = MP3File('Przygody.Dobrego.Wojaka.Szwejka.cz.1A.mp3')

# ustawiam tag
# mp3.album = 'CzeskiZHamilkarem'
# mp3.artist = 'Hamilkar'

# tags = mp3.get_tags()
# print(tags)
# mp3 = MP3File('JezuCzeskiZHamilkarem-bohužel.mp3')
# mp3.artist = 'Hamilkar'
# mp3.album = 'CzeskiZHamilkarem'
# tags = mp3.get_tags()
# mp3.save()
# print(tags)

#186 Podcast, 183 audiobook

def def_params():
    parser = argparse.ArgumentParser(
        description='testowy opis'
    )
    parser.add_argument("-f", "--file", help="plik mp3 do tagowania", required=True)
    parser.add_argument("-l", "--loghami", action='store_true'
                        , help="increase output verbosity", required=False)
    parser.add_argument("-al", "--album", help="tag dla albumu", required=False, default="")
    parser.add_argument("-ar", "--artist", help="tag dla autora/artysty", required=False, default="")
    parser.add_argument("-s", "--song", help='tag dla piosenki', required=False, default="")
    parser.add_argument("-t", "--track", help="tag dla ścieszki", required=False, default=1)
    parser.add_argument("-c", "--comment", help="tag dla komentarzy", required=False, default="")
    parser.add_argument("-g", "--genre", help="tag dla gatunku 186 podcast, 183 audiobook", required=False, default=186)
    parser.add_argument("-y", "--year", help="tag dla roku utworu", required=False, default="")

    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG)
    return args


def main():
    args = def_params()
    bas_dir = os.path.dirname(os.path.realpath(__file__))
    logging.debug("parametry:" + str(args))
    mp3 = MP3File(args.file)
    mp3.set_version(VERSION_1)
    logging.debug("parametry:" + str(args))
    if args.album is not None:
        mp3.album = args.album
    if args.artist is not None:
        mp3.artist = args.artist
    if args.song is not None:
        mp3.song = args.song
    if args.track is not None:# track powinno być number nie literal !
        mp3.track = args.track
    if args.comment is not None:
        mp3.comment = args.comment
    else:
        mp3.comment = ""
    if args.genre is not None:
        mp3.genre = args.genre #to jest enum de facto - przyjmijmy że wpisujemy 0
    if args.year is not None:
        mp3.year = args.year
    mp3.save()

    pprint(mp3.get_tags())


if __name__ == "__main__":
    main()
