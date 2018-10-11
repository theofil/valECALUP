#!/usr/bin/python
import ROOT as rt



fp = rt.TFile.Open("ecalshapes.root","R") 
rt.gROOT.LoadMacro("setTDRStyle.C")
from ROOT import setTDRStyle
setTDRStyle()
rt.gStyle.SetOptTitle(0)

EBShape = fp.Get("demo/EBShape")
EEShape = fp.Get("demo/EEShape")
APDShape = fp.Get("demo/APDShape")

### print array
def printArray(hist):
    NBins = hist.GetNbinsX()
    print ("printing"+hist.GetTitle())
    for bin in range(NBins):
	print ("array[{0:5d}] = {1:1.6f}".format(bin, hist.GetBinContent(bin)))

printArray(EBShape)
