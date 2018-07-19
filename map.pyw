#! python3
# map.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip
from urllib import parse
if len(sys.argv) > 1:
    # Get address from cmdline.
    address = ' '.join(sys.argv[1:])
    # URL escaping
    address = parse.quote_plus(address)
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/dir/?api=1&travelmode=walking&destination=' + address)
