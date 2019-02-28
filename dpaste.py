#!/usr/bin/python3

from dpaste_api import dpaste_interface as dpi
import argparse
import pyperclip

parser = argparse.ArgumentParser(description="A simple command line script \
                                 for uploading text to dpaste.com")
parser.add_argument("content", help="[Required] Path to text file to be \
                    uploaded.")
parser.add_argument("--syntax", "-s", help="Syntax template for the text file.\
                     List can be found here: \
                    http://dpaste.com/api/v2/syntax-choices/", default=None)
parser.add_argument("--title", "-t", help="Title for new paste.", default=None)
parser.add_argument("--poster", "-p", help="Author name to be put on new \
                    paste.", default=None)
parser.add_argument("--expiry", "-e", help="Number of days until paste expires\
                    , maximum of 365.  Default 7.", type=int, default=7)


def open_file(filename):
    with open(filename, 'r') as content_file:
        content_text = content_file.read()
    return content_text


if __name__ == "__main__":
    args = parser.parse_args()
    content_text = open_file(args.content)
    dpaster = dpi(content_text, args.syntax, args.title, args.poster,
                  args.expiry)
    dpaster.post()
    print("dpaste {} created.  Expires {}.".format(dpaster.paste_url,
                                                   dpaster.expires))
    try:
        pyperclip.copy(dpaster.paste_url)
    except pyperclip.PyperclipException:
        print("Unable to copy to clipboard.")
