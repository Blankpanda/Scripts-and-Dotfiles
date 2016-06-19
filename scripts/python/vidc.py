#!/usr/bin/env python

# rather memorizing how FFMEPG does this, I decieded just to create a script
# that can cut up videos


import sys
import os

def main():
    
    if not len(sys.argv) == 5:
        print("Invalid number of arguments. ")
        print("format: python vidc.py <HH:MM:SS.0> <Time> <in_file> <out_file>")
        exit(0)

    args = sys.argv

    #TODO: error checking
    start_time = args[1]
    end_time = args[2]
    in_file = args[3]
    out_file = args[4]
    
    os.system("ffmpeg -i {0} -ss {1} -c copy -t {2} {3}".format(
        in_file,
        start_time,
        end_time,
        out_file,
    ))

    
if __name__ == '__main__':
    main()
