#! /usr/bin/env python
import os,sys
import pprint
import optparse

script = os.path.realpath(sys.argv[0])
sys.path.insert(0, os.path.dirname(script))

DEBUG = False
VERBOSE = False

def parse_args(argv):
    # Options!
    try:
        parser = optparse.OptionParser()

        # Print only
        parser.add_option('-d', '--debug',
                          action='store_true', dest='debug',
                          default=False)

        parser.add_option('-v', '--verbose',
                          action='store_true', dest='verbose',
                          default=False)

        (opts, args) = parser.parse_args()

        if opts.debug is True:
            global DEBUG
            DEBUG = True
            print "\nSTATUS: DEBUG is ON\n"

        if opts.verbose is True:
            global VERBOSE 
            VERBOSE = True
            print "\nSTATUS: VERBOSE is ON\n"

        return args

    except Exception, detail:
        print "ERROR: Problem during argument parsing:  " + str(detail)
        sys.exit(1)


def main(argv):
    args = parse_args(argv)
    return

if __name__ == "__main__":
    main(sys.argv[1:])

sys.exit(1)
