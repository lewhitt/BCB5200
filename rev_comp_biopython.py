#!/usr/bin/env python

import os, sys, re
from Bio.Seq import Seq

def main():
    #get input seq

    dna_seq = raw_input('Type your DNA sequence : ')

    #convert to seq_object

    dna_bioseq = Seq(dna_seq)

    #call reverse_complement function in Bio.Seq
    
    rev_comp_seq = dna_bioseq.reverse_complement()

    #print output
    print "Reverse complement DNA :", rev_comp_seq

    #exit the program
    sys.exit()

if __name__== '__main__':
    main()
