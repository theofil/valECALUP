#!/usr/bin/python
import ROOT as rt
rt.gROOT.LoadMacro("setTDRStyle.C")
from ROOT import setTDRStyle
setTDRStyle()
rt.gStyle.SetOptTitle(0)



fp_1 = rt.TFile.Open("../ROOTs/ecalshapes_original.root","R") 
EBShape_1 = fp_1.Get("demo/EBShape")
EEShape_1 = fp_1.Get("demo/EEShape")
APDShape_1 = fp_1.Get("demo/APDShape")
tree_1 = fp_1.Get("demo/shapes")


fp_2 = rt.TFile.Open("../ROOTs/newecalshapes.root","R") 
EBShape_2 = fp_2.Get("demo/EBShape")
EEShape_2 = fp_2.Get("demo/EEShape")
APDShape_2 = fp_2.Get("demo/APDShape")
tree_2     = fp_2.Get("demo/shapes")

### print array
def printArray(hist1, hist2):
    NBins = hist1.GetNbinsX()
    print ("printing"+hist1.GetTitle())

    for bin in range(NBins):
	y1 = hist1.GetBinContent(bin)
    	y2 = hist2.GetBinContent(bin) 
	if y1!=y2: print ("array[{0:5d}] = {1:2.10f} vs {2:2.10f}".format(bin, y1, y2))


def printInternalArray_EB(tree_1, tree_2):
    NBins = 10000

    for bin in range(NBins):
	y1 = tree_1.shape_EB[bin]
    	y2 = tree_2.shape_EB[bin]
	if y1!=y2: print ("time({0:1.2f}) = {1:2.10f} vs {2:2.10f}".format(tree_1.time[bin], y1, y2))

tree_1.GetEntry(0)
tree_2.GetEntry(0) 


#print("### EB Shape ###")
#printArray(EBShape_1, EBShape_2)
#print("### EE Shape ###")
#printArray(EEShape_1, EEShape_2)
#print("### APD Shape ###")
#printArray(APDShape_1, APDShape_2)


#printInternalArray_EB(tree_1, tree_2)

print ("timeToRise_EB {0:3.3f} vs {1:3.3f}".format(tree_1.timeToRise_EB, tree_2.timeToRise_EB))
print ("timeToRise_EE {0:3.3f} vs {1:3.3f}".format(tree_1.timeToRise_EE, tree_2.timeToRise_EE))
print ("timeToRise_APD {0:3.3f} vs {1:3.3f}".format(tree_1.timeToRise_APD, tree_2.timeToRise_APD))

print ("timeOfThr_EB {0:3.3f} vs {1:3.3f}".format(tree_1.timeOfThr_EB, tree_2.timeOfThr_EB))
print ("timeOfThr_EE {0:3.3f} vs {1:3.3f}".format(tree_1.timeOfThr_EE, tree_2.timeOfThr_EE))
print ("timeOfThr_APD {0:3.3f} vs {1:3.3f}".format(tree_1.timeOfThr_APD, tree_2.timeOfThr_APD))

print ("timeOfMax_EB {0:3.3f} vs {1:3.3f}".format(tree_1.timeOfMax_EB, tree_2.timeOfMax_EB))
print ("timeOfMax_EE {0:3.3f} vs {1:3.3f}".format(tree_1.timeOfMax_EE, tree_2.timeOfMax_EE))
print ("timeOfMax_APD {0:3.3f} vs {1:3.3f}".format(tree_1.timeOfMax_APD, tree_2.timeOfMax_APD))

print ("threshold_EB {0:3.3f} vs {1:3.3f}".format(tree_1.threshold_EB, tree_2.threshold_EB))
print ("threshold_EE {0:3.3f} vs {1:3.3f}".format(tree_1.threshold_EE, tree_2.threshold_EE))
print ("threshold_APD {0:3.3f} vs {1:3.3f}".format(tree_1.threshold_APD, tree_2.threshold_APD))




#for branch in tree_1.GetListOfBranches():
#    print(branch.GetName())
