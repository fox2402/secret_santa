#!/bin/python3


import os
import pdb
import argparse
import random

class santa:
    def __init__(self, inp):
        with open(inp, "r") as f:
            self.gver = []
            self.rver = []
            for line in f:
                self.gver.append(line[0:len(line) - 1])
                self.rver.append(line[0:len(line) - 1])

    def print_list(self):
        i = 0
        for elt in self.gver:
            print (i, elt)
            i += 1
    def run(self):
        while (True):
            print ("Select your name: (number expected, -1 to quit)")
            self.print_list()
            c = int(input())
            if c == -1:
                break
            if c >= len(self.gver) or c < 0:
                print ("invalid input")
                continue
            while (True):
                i = random.randint(0, len(self.rver) - 1)
                if (self.gver[c] != self.rver[i]):
                    break

            print ("You'll give " + self.rver[i] + " a present!")
            self.gver.remove(self.gver[c])
            self.rver.remove(self.rver[i])
            print ("Press key to hide this result and keep it secret!")
            g = input()
            os.system('cls' if os.name == 'nt' else 'clear')








def main():
    parser = argparse.ArgumentParser(description = "Secret Santa!")
    parser.add_argument("-i", "--input", type = str)
    args = parser.parse_args()
    if args.input is None:
        print ("secret_sant: No input file give, run with -i or --input")
        print ("** Are all the children in the universe that for you not\
 to consider anything for their Christmas?!**")
        return
    s = santa(args.input)
    s.run()

main()
