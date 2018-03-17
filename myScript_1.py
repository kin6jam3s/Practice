import re
import glob


fileList = glob.glob('*BB*.*v5*txt')
# fileList = ['BB1.initial.config.v5.txt', 'BB2.initial.config.v5.txt', 'BB3.initial.config.v5.txt']
pattern = re.compile(r'router bgp .*no ip http server', re.DOTALL)

for i in fileList:
    outFileName = i.split('.')[0] + '_BGP_Output1.txt'
    print(outFileName)


    # read input file
    inputFile = open(i)
    text = inputFile.read()
    result = re.search(pattern, text)
    s = result.start()
    e = result.end() - 18
    inputFile.close()

    #
    #
    # write to output file
    outFile = open(outFileName, 'w')
    outFile.write(text[s:e])
    outFile.close()



#
#
#
# f = open('BB1.initial.config.v5.txt')
# # for line in f.readlines():
# #     print(line.strip())
# text = f.read()
# result = re.search(pattern, text)
# s = result.start()
# e = result.end() - 18
#
# print(text[s:e])
# f.close()
#
# outFile = open('BB1_BGP.txt', 'w')
# outFile.write(text[s:e])
# outFile.close()





