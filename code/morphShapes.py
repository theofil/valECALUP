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

### Open TXT file read data and make graph
def graphFromTXT(filename, thresh, time_interval):
    x = array('d')
    y = array('d')
    data = open(filename,'r')
    counter = 0
    fillArrays = False
    for ele in data:
        value = float(ele)
        if  value >= thresh and not fillArrays: 
            fillArrays = True
            print("first sample over thershold = ",value)

        if(fillArrays):
            time = counter*time_interval + 0.50
            y.append(value)
            x.append(time)
            #$print ("counter is now:{0:2d} for t = {1:3.3f} and y = {2:1.6f}".format(counter, time, value))
            counter += 1

    gr = rt.TGraph(len(x), x, y)
    graphbeautification(gr)
    gr.SetMarkerColor(rt.kRed)
    gr.SetMarkerStyle(4)
    return gr

### read m_array from TXT erase push_back string
def graphFromTXT2(filename, thresh, time_interval):
    myfile = open(filename, 'r')
    counter = 0
    x,y = array('d'), array('d')
    fillGraph = False
    for line in myfile:
        if float(line[14:-3]) > thresh: fillGraph = True ### set this once and go on
        if fillGraph:
                y_val = float(line[14:-3])
                x_val = counter*(time_interval) + 0.5*(time_interval)
                y.append( y_val )
                x.append( x_val )
                #print ("x_val = {0:1.4f} y_val = {1:1.3f}".format(x_val, y_val))
                counter = counter + 1
    gr = rt.TGraph(len(x), x, y)
    graphbeautification(gr)
    return gr


### Setting print style
print ("Setting TDR style")
rt.gROOT.LoadMacro("setTDRStyle.C")
from ROOT import setTDRStyle
setTDRStyle()
rt.gStyle.SetOptTitle(0)

### Setting paths + filenames
cmsswFile_ref = "printCMSSWfiles/TXTs/EE_SimPulseShape.txt"
cmsswFile_p23ns = "printCMSSWfiles/TXTs/EE_SimPulseShape_p23ns.txt"
cmsswFile_p20ns = "printCMSSWfiles/TXTs/EE_SimPulseShape_p20ns.txt"
cmsswFile_p17ns = "printCMSSWfiles/TXTs/EE_SimPulseShape_p17ns.txt"
marray_ref = "../ROOTs/PhaseI_m_array/EEShape.txt"
marray_p23ns = "../ROOTs/PhaseI_m_array/m_array_EE_SimPulseShape_p23ns.txt"
marray_p20ns = "../ROOTs/PhaseI_m_array/m_array_EE_SimPulseShape_p20ns.txt"
marray_p17ns = "../ROOTs/PhaseI_m_array/m_array_EE_SimPulseShape_p17ns.txt"


### make graph from TXT data for EE Phase I
thresh_EE = 0.00025
time_interval = 1.0
gr_EE_ref     = graphFromTXT(cmsswFile_ref, thresh_EE, 1.0)
gr_EE_p23ns   = graphFromTXT(cmsswFile_p23ns, thresh_EE, 1.0)
gr_EE_p20ns   = graphFromTXT(cmsswFile_p20ns, thresh_EE, 1.0)
gr_EE_p17ns   = graphFromTXT(cmsswFile_p17ns, thresh_EE, 1.0)
gr_EE_marray_ref  = graphFromTXT2(marray_ref, thresh_EE, 0.1)
gr_EE_marray_p23ns  = graphFromTXT2(marray_p23ns, thresh_EE, 0.1)
gr_EE_marray_p20ns  = graphFromTXT2(marray_p20ns, thresh_EE, 0.1)
gr_EE_marray_p17ns  = graphFromTXT2(marray_p17ns, thresh_EE, 0.1)




###############################################3
### Start Drawing
###############################################3

c11 = rt.TCanvas("c11","c11") 
gr_EE_ref.SetMarkerColor(rt.kBlue)
gr_EE_p20ns.SetMarkerColor(rt.kGreen)
gr_EE_p17ns.SetMarkerColor(rt.kMagenta)
gr_EE_ref.Draw("AP")
gr_EE_ref.GetXaxis().SetRangeUser(0,150)
gr_EE_p23ns.Draw("P SAME")
gr_EE_p20ns.Draw("P SAME")
gr_EE_p17ns.Draw("P SAME")
#gr_EE_marray_ref.Draw("same")
#gr_EE_marray_p23ns.Draw("same")
leg1 = rt.TLegend(0.48,0.18,0.91,0.4)
leg1.SetTextSize(28)
leg1.SetTextFont(43)
leg1.SetFillColor(rt.kWhite)
leg1.SetFillStyle(0)
leg1.SetBorderSize(0)
leg1.AddEntry(gr_EE_ref, "EE pulse","p")
leg1.AddEntry(gr_EE_p23ns, "EE pulse + 23ns","p")
leg1.AddEntry(gr_EE_p20ns, "EE pulse + 20ns","p")
leg1.AddEntry(gr_EE_p17ns, "EE pulse + 17ns","p")
leg1.Draw("same")
c11.Update()
c11.SaveAs("../FIGs/c11.pdf")
c11.SaveAs("../FIGs/c11.png")

