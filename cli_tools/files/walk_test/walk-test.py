import os

for root,dinames,filenames in os.walk('.'):
    print(root)
    print(dinames)
    print(filenames)
    print('------')