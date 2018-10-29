import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-dest", "--destinationDir", required=True, help="destination directory where files should be copied to")
parser.add_argument("-source", "--sourceDir", required=True, help="source directories where files that need to be copied live")
flags = vars(parser.parse_args())

dest = flags["destinationDir"]
source = flags["sourceDir"]

source_files = os.listdir(source)

print "***copying files***"

i = 0
for file in source_files:
    filename = source + "/" + file
    shutil.move(filename, dest)
    i += 1

print('Copied %s files'%(i))