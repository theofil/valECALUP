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
    for ele in data:
        fillArrays = False
        value = float(ele)
        if  value >= thresh: fillArrays = True

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
    myfile = open(filepath, 'r')
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
path = "../ROOTs/"
dir2 = "produced_PhaseI_m_array/"
dir4 = "marc_v1/"
cmsswFile1 = "printCMSSWfiles/TXTs/EB_SimPulseShape.txt"

### Open ROOT file read shape
fp1 = rt.TFile.Open(path+"PhaseI_m_array/"+"ecalshapes.root") 
tree1 = fp1.Get("demo/shapes")  
tree1.GetEntry(0)
gr1_EB = rt.TGraph(len(tree1.time), tree1.time, tree1.shape_EB )
graphbeautification(gr1_EB)

fp3 = rt.TFile.Open(path+"produced_PhaseII_m_array/"+"ecalshapes.root") 
tree3 = fp3.Get("demo/shapes")  
tree3.GetEntry(0)
gr3_EB = rt.TGraph(len(tree3.time), tree3.time, tree3.shape_EB )
graphbeautification(gr3_EB)
gr3_EB.SetMarkerColor(rt.kBlue)
gr3_EB.SetLineColor(rt.kBlue)

fp2 = rt.TFile.Open(path+"marc_v1/"+"shape_9862.root") 
histo2 = fp2.Get("average_shape")
histo2.Scale(1/503.109)


### make graph from TXT data for EB Phase I
filename = cmsswFile1
thresh_EB = 0.00013
time_interval = 1.0
gr1_EB_ref = graphFromTXT(cmsswFile1, thresh_EB, 1.0)


### translate histo2 (shape9862) for EB Phase II
histo2_x, histo2_y = array( 'd' ), array( 'd' )
nBins = histo2.GetNbinsX() ### histo2 is the average_shape of Marc (shape_9862.root) scaled by 1/503.109
threshold = 0.4/1000 ### threshold on normalized pulse
FillGraph = False
counter = 0
for bin in range(1,nBins+1):
    x = histo2.GetBinCenter(bin) -5
    #x = counter*0.250 + 0.125
    x = counter*0.249485 + 0.249485*0.5
    y = histo2.GetBinContent(bin)
    if y > threshold: FillGraph = True ### set this once the threshold reached
    if(FillGraph):
        histo2_x.append(x)
        histo2_y.append(y)
        counter = counter + 1

gr3_EB_ref = rt.TGraph(len(histo2_x), histo2_x, histo2_y)
graphbeautification(gr3_EB_ref)
gr3_EB_ref.SetMarkerColor(rt.kRed)
gr3_EB_ref.SetMarkerStyle(4)


### create graph from Phase II m_array
filepath = path+"produced_PhaseII_m_array/"+"EBShape.txt"
thresh = 0.4/1000
time_interval = 0.0250
gr3_EB_ref2 = graphFromTXT2(filepath, thresh, time_interval)
gr3_EB_ref2.SetMarkerColor(rt.kGreen)
gr3_EB_ref2.SetLineColor(rt.kGreen)
gr3_EB_ref2.SetMarkerStyle(7)

###############################################3
### Start Drawing
###############################################3

#c1 = rt.TCanvas("c1","c1") 
#gr1_EB_ref2 = graphFromTXT(cmsswFile1, -1.e+9, 1.0)
#gr1_EB_ref2.Draw("AP")
#gr1_EB_ref2.GetXaxis().SetRangeUser(0,500)
#gr1_EB_ref2.GetYaxis().SetRangeUser(0,1.1)
#gr1_EB_ref2.Draw("AP same")
#leg = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
#leg.SetTextSize(28)
#leg.SetTextFont(43)
#leg.SetFillColor(rt.kWhite)
#leg.SetFillStyle(0)
#leg.SetBorderSize(0)
#leg.AddEntry(gr1_EB_ref2, "EB data H4 (2004)","p")
#leg.Draw("same")
#c1.Update()
#c1.SaveAs("../FIGs/c1.pdf")
#c1.SaveAs("../FIGs/c1.png")
#
#
#c2 = rt.TCanvas("c2","c2") 
#gr1_EB.Draw("AP")
#gr1_EB.GetXaxis().SetRangeUser(0,435)
#gr1_EB.GetYaxis().SetRangeUser(0,1.1)
#gr1_EB_ref.Draw("P, SAME")
#leg1 = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
#leg1.SetTextSize(28)
#leg1.SetTextFont(43)
#leg1.SetFillColor(rt.kWhite)
#leg1.SetFillStyle(0)
#leg1.SetBorderSize(0)
#leg1.AddEntry(gr1_EB, "EB (CMSSW)","pl")
#leg1.AddEntry(gr1_EB_ref, "EB data H4 (2004)","p")
#leg1.Draw("same")
#c2.Update()
#c2.SaveAs("../FIGs/c2.pdf")
#c2.SaveAs("../FIGs/c2.png")

#c3 = rt.TCanvas("c3","c3") 
#gr1_EB.Draw("AP")
#gr1_EB.GetXaxis().SetRangeUser(50,63)
#gr1_EB.GetYaxis().SetRangeUser(0.98,1.01)
#gr1_EB.GetYaxis().SetNdivisions(504)
#gr1_EB_ref.Draw("P, SAME")
#leg1 = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
#leg1.SetTextSize(28)
#leg1.SetTextFont(43)
#leg1.SetFillColor(rt.kWhite)
#leg1.SetFillStyle(0)
#leg1.SetBorderSize(0)
#leg1.AddEntry(gr1_EB, "EB (CMSSW)","pl")
#leg1.AddEntry(gr1_EB_ref, "EB data H4 (2004)","p")
#leg1.Draw("same")
#c3.Update()
#c3.SaveAs("../FIGs/c3.pdf")
#c3.SaveAs("../FIGs/c3.png")


#c4 = rt.TCanvas("c4","c4") 
#gr1_EB.Draw("AP")
#gr1_EB.GetXaxis().SetRangeUser(56.0,56.8)
#gr1_EB.GetYaxis().SetRangeUser(0.999,1.0005)
#gr1_EB.GetYaxis().SetNdivisions(504)
#gr1_EB_ref.Draw("P, SAME")
#leg1 = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
#leg1.SetTextSize(28)
#leg1.SetTextFont(43)
#leg1.SetFillColor(rt.kWhite)
#leg1.SetFillStyle(0)
#leg1.SetBorderSize(0)
#leg1.AddEntry(gr1_EB, "EB (CMSSW)","pl")
#leg1.AddEntry(gr1_EB_ref, "EB data H4 (2004)","p")
##leg1.Draw("same")
#c4.SetGridx()
#c4.Update()
#c4.SaveAs("../FIGs/c4.pdf")
#c4.SaveAs("../FIGs/c4.png")

#c5 = rt.TCanvas("c5","c5") 
#gr1_EB.Draw("AP")
#gr1_EB.GetXaxis().SetRangeUser(0,20)
#gr1_EB.GetYaxis().SetRangeUser(0,0.4)
#gr1_EB.GetYaxis().SetNdivisions(504)
#gr1_EB_ref.Draw("P, SAME")
#leg1 = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
#leg1.SetTextSize(28)
#leg1.SetTextFont(43)
#leg1.SetFillColor(rt.kWhite)
#leg1.SetFillStyle(0)
#leg1.SetBorderSize(0)
#leg1.AddEntry(gr1_EB, "EB (CMSSW)","pl")
#leg1.AddEntry(gr1_EB_ref, "EB data H4 (2004)","p")
##leg1.Draw("same")
#c5.Update()
#c5.SaveAs("../FIGs/c5.pdf")
#c5.SaveAs("../FIGs/c5.png")

#c5 = rt.TCanvas("c5","c5") 
#gr1_EB.Draw("AP")
#gr1_EB.GetXaxis().SetRangeUser(0,250)
##gr1_EB.GetYaxis().SetRangeUser(0,0.4)
#gr1_EB.GetYaxis().SetNdivisions(504)
##gr1_EB_ref.Draw("P, SAME")
#gr3_EB.Draw("P, SAME")
#leg1 = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
#leg1.SetTextSize(28)
#leg1.SetTextFont(43)
#leg1.SetFillColor(rt.kWhite)
#leg1.SetFillStyle(0)
#leg1.SetBorderSize(0)
#leg1.AddEntry(gr1_EB, "EB Pulse Phase I","pl")
#leg1.AddEntry(gr3_EB, "EB Pulse Phase II","l")
##leg1.AddEntry(gr1_EB_ref, "EB data H4 (2004)","p")
#leg1.Draw("same")
#c5.Update()
#c5.SaveAs("../FIGs/c5.pdf")
#c5.SaveAs("../FIGs/c5.png")


#c6 = rt.TCanvas("c6","c6") 
#gr3_EB.Draw("AP")
#gr3_EB.GetXaxis().SetRangeUser(0,70)
##gr3_EB.GetYaxis().SetRangeUser(0,0.4)
#gr3_EB.GetYaxis().SetNdivisions(504)
#gr3_EB.Draw("P, SAME")
#gr3_EB_ref.Draw("P, SAME")
#leg1 = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
#leg1.SetTextSize(28)
#leg1.SetTextFont(43)
#leg1.SetFillColor(rt.kWhite)
#leg1.SetFillStyle(0)
#leg1.SetBorderSize(0)
#leg1.AddEntry(gr3_EB, "EB (CMSSW)","pl")
#leg1.AddEntry(gr3_EB_ref, "EB data H4 (2017)","p")
#leg1.Draw("same")
#c6.Update()
#c6.SaveAs("../FIGs/c6.pdf")
#c6.SaveAs("../FIGs/c6.png")


#c7 = rt.TCanvas("c7","c7")
#gr3_EB.Draw("AP")
#gr3_EB.GetXaxis().SetRangeUser(14,19)
#gr3_EB.GetYaxis().SetRangeUser(0.88,1.05)
#gr3_EB.GetYaxis().SetNdivisions(504)
#gr3_EB.Draw("P, SAME")
#gr3_EB_ref.Draw("P, SAME")
#leg1 = rt.TLegend(0.44,0.14,0.67,0.38)
#leg1.SetTextSize(28)
#leg1.SetTextFont(43)
#leg1.SetFillColor(rt.kWhite)
#leg1.SetFillStyle(0)
#leg1.SetBorderSize(0)
#leg1.AddEntry(gr3_EB, "EB (CMSSW)","pl")
#leg1.AddEntry(gr3_EB_ref, "EB data H4 (2017)","p")
#leg1.Draw("same")
#c7.Update()
#c7.SaveAs("../FIGs/c7.pdf")
#c7.SaveAs("../FIGs/c7.png")

#c7 = rt.TCanvas("c7","c7")
#gr3_EB.Draw("AP")
#gr3_EB.GetXaxis().SetRangeUser(14,19)
#gr3_EB.GetYaxis().SetRangeUser(0.88,1.05)
#gr3_EB.GetYaxis().SetNdivisions(504)
#gr3_EB.Draw("P, SAME")
#gr3_EB_ref.Draw("P, SAME")
#leg1 = rt.TLegend(0.44,0.14,0.67,0.38)
#leg1.SetTextSize(28)
#leg1.SetTextFont(43)
#leg1.SetFillColor(rt.kWhite)
#leg1.SetFillStyle(0)
#leg1.SetBorderSize(0)
#leg1.AddEntry(gr3_EB, "EB (CMSSW)","pl")
#leg1.AddEntry(gr3_EB_ref, "EB data H4 (2017)","p")
#leg1.Draw("same")
#c7.Update()
#c7.SaveAs("../FIGs/c7.pdf")
#c7.SaveAs("../FIGs/c7.png")

#c8 = rt.TCanvas("c8","c8")
#gr3_EB.Draw("AP")
#gr3_EB.GetXaxis().SetRangeUser(0.0,50)
#gr3_EB.GetYaxis().SetRangeUser(0.0,1.2)
#gr3_EB.GetYaxis().SetNdivisions(504)
#gr3_EB.Draw("P, SAME")
#gr3_EB_ref.Draw("P, SAME")
#leg1 = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
#leg1.SetTextSize(28)
#leg1.SetTextFont(43)
#leg1.SetFillColor(rt.kWhite)
#leg1.SetFillStyle(0)
#leg1.SetBorderSize(0)
#leg1.AddEntry(gr3_EB, "EB (CMSSW)","pl")
#leg1.AddEntry(gr3_EB_ref, "EB data H4 (2017)","p")
#leg1.Draw("same")
#c8.Update()
#c8.SaveAs("../FIGs/c8.pdf")
#c8.SaveAs("../FIGs/c8.png")

#c9 = rt.TCanvas("c9","c9")
#gr3_EB_ref2.Draw("AP")
#gr3_EB_ref2.GetXaxis().SetRangeUser(0.0,50)
#gr3_EB_ref2.GetYaxis().SetRangeUser(0.0,1.2)
#gr3_EB_ref2.GetYaxis().SetNdivisions(504)
#gr3_EB_ref2.Draw("P, SAME")
#gr3_EB_ref.Draw("P, SAME")
#gr3_EB.Draw("P, SAME")
#leg1 = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
#leg1.SetTextSize(28)
#leg1.SetTextFont(43)
#leg1.SetFillColor(rt.kWhite)
#leg1.SetFillStyle(0)
#leg1.SetBorderSize(0)
#leg1.AddEntry(gr3_EB, "EB (CMSSW)","pl")
#leg1.AddEntry(gr3_EB_ref2, "m_shape","pl")
#leg1.AddEntry(gr3_EB_ref, "EB data H4 (2017)","p")
#leg1.Draw("same")
#c9.Update()
#c9.SaveAs("../FIGs/c9.pdf")
#c9.SaveAs("../FIGs/c9.png")


c10 = rt.TCanvas("c10","c10")
gr3_EB.Draw("AP")
gr3_EB.GetXaxis().SetRangeUser(16.37-3,16.37+3)
gr3_EB.GetYaxis().SetRangeUser(0.92,1.1)
gr3_EB.GetYaxis().SetNdivisions(504)
gr3_EB.Draw("P, SAME")
gr3_EB_ref.Draw("P, SAME")
leg1 = rt.TLegend(0.69-0.2,0.69,0.92-0.2,0.92)
leg1.SetTextSize(28)
leg1.SetTextFont(43)
leg1.SetFillColor(rt.kWhite)
leg1.SetFillStyle(0)
leg1.SetBorderSize(0)
leg1.AddEntry(gr3_EB, "EB (CMSSW)","pl")
leg1.AddEntry(gr3_EB_ref, "EB data H4 (2017)","p")
leg1.Draw("same")
c10.Update()
c10.SaveAs("../FIGs/c10.pdf")
c10.SaveAs("../FIGs/c10.png")
