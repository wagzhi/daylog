__author__ = 'root'

from daylog.parse_utils import *
import os


def exeDemo(func):
    ex_file = os.path.dirname(__file__)+"/../example/mexample.log"
    with open(ex_file,'r') as f:
        while True:
            line=f.readline()
            if not line:
                break
            #print "line: ",line,"\n"
            yield func(line)

if __name__ == "__main__":
    ex_file = os.path.dirname(__file__)+"/../example/mexample.log"
    with open(ex_file,'r') as f:
        while True:
            line=f.readline()
            if not line:
                break

            print line