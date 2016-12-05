#!/bin/ython3


import os
import pdb
import argparse

class santa:
    def __init__(self, inp):
        gver = []
        rver = []
        with open(inp, "r") as f:
            for line in f:
                gver.append(line)
                rver.append(line)

    def print_list():
        i = 0
        for elt in gver:
            print (i, elt)
            i += 1
    def run():
        while (True):
            print ("Select your name: (number expected, -1 to quit)")
            print_list()
            c = int(input())
            if c == -1:
                break
            if c > len(gver) or c < 0:
                print ("invalid input")
                continue
            i = random.randrage(0, len(rver))
            print ("You'll give " + rver[i] + " a present!")
            gver.remove(gver[c])
            rver.remove(rver[i])








def main():
    parser = argparse.ArgumentParser(description = "Secret Santa!")
    parser.add_argument("-i", "--input", type = str,
            description = "Input name list, see README for the format")
    args = parser.parse_args()
    if args.input is None:
        print ("secret_sant: No input file give, run with -i or --input")
        print ("** Are all the children in the universe that for you not
        to consider anything for their Christmas?!**")
        return
