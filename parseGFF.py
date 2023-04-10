#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="This script read the gff file")

# add positional (required) arguments
parser.add_argument("gff", help="The file which you want to read line by line", type=str)
parser.add_argument("fasta", help="Name of fasta file you want to parse", type=str)

# parse the actual arguments

# access argument values via `args` variable
args = parser.parse_args()


# open the gff file
with open(args.gff) as gff_line:

    # loop over the line in the file
    for line in gff_line:
        print(line)







