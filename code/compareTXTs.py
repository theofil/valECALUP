#!/anaconda3/bin/python
##!/usr/bin/python

import numpy as np
import pandas as pd

def parseTXTfile(filepath):
    df = pd.read_csv(filepath)
    se = df.iloc[:,0]
    se = se.str.replace('vec.push_back\(','')
    se = se.str.replace('\);','')
    se = pd.to_numeric(se)
    return se


def compareFiles(filename1, filename2, thresh):
    se1 = parseTXTfile(filename1)
    se2 = parseTXTfile(filename2)
    #print ("se1 has len = {0:3d} \nse2 has len = {1:3d}".format(len(se1), len(se2)))
    if len(se1) != len(se2): print ("different length of se1 and se2")

    for x in range(len(se1)):
        ele = se1[x] - se2[x]
        if ele>thresh:  
            print ("se1 {0:1.10f} vs se2 {1:1.10f}".format(se1[x], se2[x]))

print ("comparing the arrays as are in txt files")

path = "../ROOTs/"
dir1 = "PhaseI_m_array/"
dir2 = "produced_PhaseI_m_array/"
dir3 = "produced_PhaseII_m_array/"

fil1 = "EBShape.txt"
fil2 = "EEShape.txt"
fil3 = "APDShape.txt"

compareFiles(path+dir1+fil1, path+dir2+fil1, 1.e-5)
compareFiles(path+dir1+fil2, path+dir2+fil2, 1.e-5)
compareFiles(path+dir1+fil3, path+dir2+fil3, 1.e-5)
