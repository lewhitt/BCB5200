#!/usr/bin/env python

import os, sys, re
from Bio.Seq import Seq
from optparse import OptionParser

def custom(s):
    for i in s:
        if i not in 'ATCGatcg':
            print "** Error: Not a DNA sequence"
            sys.exit()
    s = s.upper()
    comp_dict = {"A":"T", "C":"G", "G":"C", "T":"A"}
    rev = list(s)
    rev.reverse()
    rev = [comp_dict[base] for base in rev]
    return ''.join(rev)

def main():
    parser = OptionParser(usage="%prog [options]")
    parser.add_option("-f", "--file_input", dest="input_filename", 
                    default="filename", help="for input format")  
    parser.add_option("-o", "--output", dest="output_filename", 
                      default="input_base_filename_reverse.extention", 
                      help="filename of output")   
    parser.add_option("-c", "--custom", action='store_true', default= False, help="calls custom reverse-complement function,\ndefualt is biopython function")
    parser.add_option("--fasta", dest="fasta_input", action="store_true",                         default= False, help="for FASTA format files,\n adds (reverse) end of ID lines")
    (options, args) = parser.parse_args()

    with open(options.output_filename, "w") as output_holder:
        if options.input_filename is not "filename":
            with open(options.input_filename, "r") as f:
                for line in f:
                    if options.fasta_input and line[0] == ">":
                        output_holder.write(line.strip() + "(reverse)" + '\n')
                    else:
                        if options.custom:
                            output_holder.write(custom(line.strip()) + '\n')
                        else:
                            dna_bioseq = Seq(str(line.strip()))
                            dna_bioseq = dna_bioseq.reverse_complement()
                            output_holder.write(str(dna_bioseq) + '\n')
        else:
            dna_input = raw_input('Type your DNA sequence : ')
            if options.custom:
                output_holder.write(custom(dna_input))
            else:
                dna_bioseq = Seq(dna_input)
                dna_bioseq = dna_bioseq.reverse_complement()
                output_holder.write(str(dna_bioseq))
    if options.output_filename is "input_base_filename_reverse.extention":
        os.rename(options.output_filename, "input_base_"+ options.input_filename+ "_reverse.extention")
    sys.exit()

if __name__ == '__main__':
    main()
