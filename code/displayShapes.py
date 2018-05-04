#!/usr/bin/python
##!/anaconda3/bin/python
from __future__ import print_function
import ROOT as rt
from array import array
import os

def histobeautification(hist):
    hist.GetXaxis().SetRangeUser(0, 550)
    hist.SetLineWidth(3)

    hist.GetYaxis().SetTitleOffset(1.0)
    hist.GetYaxis().SetTitleSize(0.06)
    hist.GetYaxis().SetLabelSize(0.05)

    hist.GetXaxis().SetTitleOffset(1.0)
    hist.GetXaxis().SetTitleSize(0.06)
    hist.GetXaxis().SetLabelSize(0.05)


def graphbeautification(graph):
    graph.SetMarkerStyle(1)
    graph.SetMarkerColor(1)
    graph.GetXaxis().SetTitle( 'time [ns]' )
    graph.GetYaxis().SetTitle( 'normalized amplitude [ADC]' )


### Setting print style
print ("Setting TDR style")
rt.gROOT.LoadMacro("setTDRStyle.C")
from ROOT import setTDRStyle
setTDRStyle()
rt.gStyle.SetOptTitle(0)

### Setting paths + filenames
path = "../ROOTs/"
dir1 = "PhaseI_m_array/"
dir2 = "produced_PhaseI_m_array/"
dir3 = "produced_PhaseII_m_array/"
cmsswFile1 = "printCMSSWfiles/TXTs/EB_SimPulseShape.txt"

### Open ROOT file read shape
fp1 = rt.TFile.Open(path+dir1+"ecalshapes.root") 
tree1 = fp1.Get("demo/shapes")  
tree1.GetEntry(0)
gr1_EB = rt.TGraph(len(tree1.time), tree1.time, tree1.shape_EB )
graphbeautification(gr1_EB)

### Open TXT file read data and make graph
def graphFromTXT(filename, thresh, time_interval):
    x = array('d')
    y = array('d')
    data = open(filename,'r')
    counter = 0
    for ele in data:
	fillArrays = False
	value = float(ele)
	if  value >= thresh: fillArrays = True
	if(fillArrays):
	    time = counter*time_interval + 0.5
	    y.append(value)
	    x.append(time)
	    #print ("counter is now:{0:2d} for t = {1:3.3f} and y = {2:1.6f}".format(counter, time, value))
	    counter += 1

    gr = rt.TGraph(len(x), x, y)
    graphbeautification(gr)
    gr.SetMarkerColor(rt.kRed)
    gr.SetMarkerStyle(4)
    return gr


#####################
filename = cmsswFile1
thresh_EB = 0.00013
time_interval = 1.0
gr1_EB_ref = graphFromTXT(cmsswFile1, thresh_EB, 1.0)


### Start Drawing
c1 = rt.TCanvas() 
gr1_EB.Draw("AP")
gr1_EB.GetXaxis().SetRangeUser(0,500)
gr1_EB.GetYaxis().SetRangeUser(0,1.1)
gr1_EB_ref.Draw("P, SAME")
c1.Update()

c2 = rt.TCanvas() 
gr1_EB_ref2 = graphFromTXT(cmsswFile1, -1.e+9, 1.0)
gr1_EB_ref2.Draw("AP")
gr1_EB_ref2.GetXaxis().SetRangeUser(0,500)
gr1_EB_ref2.GetYaxis().SetRangeUser(0,1.1)
gr1_EB_ref2.Draw("AP same")
leg = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
leg.SetTextSize(28)
leg.SetTextFont(43)
leg.SetFillColor(rt.kWhite)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.AddEntry(gr1_EB_ref2, "EB data H4 (2004)","p")
leg.Draw("same")
c2.Update()




#n = 20
#x, y = array( 'd' ), array( 'd' )
# 
#from math import sin
#from ROOT import TCanvas, TGraph
#
#for i in range( n ):
#    x.append( 0.1*i )
#    y.append( 10*sin( x[i]+0.2 ) )
#    print(' i %i %f %f ' % (i,x[i],y[i]))
#
#c1 = TCanvas('c1') 
#gr = TGraph( n, x, y )
#gr.SetLineColor( 2 )
#gr.SetLineWidth( 4 )
#gr.SetMarkerColor( 4 )
#gr.SetMarkerStyle( 21 )
#gr.SetTitle( 'a simple graph' )
#gr.GetXaxis().SetTitle( 'X title' )
#gr.GetYaxis().SetTitle( 'Y title' )
#gr.Draw( 'ACP' )
#c1.Update()

#tree1.Draw("shape_EB:time","","goff")
#tree1.GetV1().size()

#time1, tree1_EB = array( 'd' ), array( 'd' )
#tree1_EB = tree1.shape_EB
#gr = rt.TGraph(len(tree1.shape_EB), tree1.time, tree1.shape_EB)

#gr = rt.TGraph(20, array('d',tree1.time), array('d',tree1.shape_EB) )
#gr = rt.TGraph(20, tree1.time, tree1.shape_EB )
