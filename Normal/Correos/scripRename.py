# -*- encoding utf-8 -*-
import glob2

filenames = glob2.glob("*.txt")  # list of all .txt files in the directory

with open('outfile.txt', 'w', encoding='utf8') as f:
    for file in filenames:
        with open(file, encoding='utf8', errors='ignore') as infile:
            f.write(infile.read()+'\n')
