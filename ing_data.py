# -*- encoding utf-8 -*-
import glob2

def data(route, name):
    filenames = glob2.glob(route)  # list of all .txt files in the directory

    with open(name, 'w', encoding='utf8') as f:
        for file in filenames:
            with open(file, encoding='utf8', errors='ignore') as infile:
                f.write(infile.read()+'\n')

data(route="./Datos/Spam/*.txt", name='spam.txt')
data(route="./Datos/Normal/*.txt", name='normal.txt')
