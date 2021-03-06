#!/usr/bin/env python

"""
Write to standard output a diffable representation of IPython notebook.

Only cell sources (markdown or code) are preserved.
"""

import argparse
import json

from _version import __version__

def parse_command_line():
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--version', action='version',
                        version='%(prog)s '+__version__)
    parser.add_argument('filename', metavar='FILE.IPYNB', 
                       help='IPython notebook file.')
    return parser.parse_args()

def main():
    args = parse_command_line()
    notebook = json.load( open(args.filename) )
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            print '--- markdown '.ljust(78,'-')
        else:
            print '--- code '.ljust(78,'-')
        print u''.join(cell['source']).encode('utf-8')

if __name__ == '__main__':
    main()
