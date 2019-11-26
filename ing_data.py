import glob2

def data(route, name):
    filenames = glob2.glob(route)  # list of all .txt files in the directory

    with open(name, 'w', encoding='utf8') as f:
        for file in filenames:
            with open(file, encoding='utf8', errors='ignore') as infile:
                f.write(infile.read()+'\n')

# We pass the route where the spam emails are and the name of the file
data(route="./Datos/Spam/*.txt", name='spam.txt')
# We pass the route where the normal emails and the file name are
data(route="./Datos/Normal/*.txt", name='normal.txt')
