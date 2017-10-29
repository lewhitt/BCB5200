#!/usr/bin/env python

import os, sys, re

def reverse(s): # return seq string in reverse order
    #string to list

    dna_list=[]
    for i in s:
        dna_list.append(i)

    #reverse

    rev_dna_list = []
    rev_dna_list = dna_list[::-1]

    #list to string
    global dna_seq_rev
    dna_seq_rev = "".join(rev_dna_list)
    return dna_seq_rev

def complement(s): # return complementary seq string
    #dictionary

    comp_dict = {"A":"T", "T":"A", "G":"C", "C":"G"}

    #string to list

    rev_list = []
    for i in s:
        rev_list.append(i)

    #change to complement

    transversions = []
    for item in rev_list:
        transversions.append(comp_dict[item])

    #list to string
    global dna_comp_seq
    dna_comp_seq = "".join(transversions)
    return dna_comp_seq

def main(): #where the magic hopefully happens
    #get input seq
    dna_seq = raw_input('Type your DNA sequence : ')
    
    #change to upper case
    
    dna_seq = dna_seq.upper()

    #check DNA letter
    
    for i in dna_seq:
        if i not in 'ATCG':
            raise ValueError('Sequence must be nucleic acids (eg: A,T,G,C)')
            return

    #call reverse(s)

    reverse(dna_seq)

    #call complement(s)

    complement(dna_seq_rev)

    #print output complement seq
    print "Reverse complement DNA:", dna_comp_seq

    #exit program
    sys.exit()

if __name__ == '__main__':
    main()
