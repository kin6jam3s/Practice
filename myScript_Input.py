import glob

# fileList = ['BB1.initial.config.v5.txt', 'BB2.initial.config.v5.txt', 'BB3.initial.config.v5.txt']

fileList = glob.glob('*BB*.txt')


def readFile(fileName):
    f = open(fileName, 'r')
    for line in f.readlines():
        print(line.strip())
    f.close()


for configFile in fileList:
    readFile(configFile)


# readfile('BB1.initial.config.v5.txt')
