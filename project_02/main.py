#Renaming- bulk files

import json
import os

def main():
    i = 0
    with open('config.json') as config_file:
        config = json.load(config_file)
    path = config['path']
   
    for filename in os.listdir(path):
        my_dest = 'img' + str(i) +'.jpg'
        print(my_dest)
        my_source = path + filename
        print(my_source)
        my_dest = path + my_dest
        print(my_dest)
        os.rename(my_source, my_dest)
        i += 1

if __name__ =='__main__':
    main()
