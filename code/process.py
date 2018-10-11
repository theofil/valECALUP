#!/usr/bin/python
import ROOT as rt

def histobeautification(hist):
    hist.GetXaxis().SetRangeUser(0, 550)
    hist.SetLineWidth(3)
    
    hist.GetYaxis().SetTitleOffset(1.0)
    hist.GetYaxis().SetTitleSize(0.06)
    hist.GetYaxis().SetLabelSize(0.05)
    
    hist.GetXaxis().SetTitleOffset(1.0)
    hist.GetXaxis().SetTitleSize(0.06)
    hist.GetXaxis().SetLabelSize(0.05)



fp = rt.TFile.Open("ecalshapes.root","R") 
rt.gROOT.LoadMacro("setTDRStyle.C")
from ROOT import setTDRStyle
setTDRStyle()
rt.gStyle.SetOptTitle(0)

EBShape = fp.Get("demo/EBShape")
EEShape = fp.Get("demo/EEShape")
APDShape = fp.Get("demo/APDShape")

### hisogram beautification
histobeautification(EBShape)
histobeautification(EEShape)
histobeautification(APDShape)
EEShape.SetLineColor(rt.kRed)
APDShape.SetLineColor(rt.kGreen)
EEShape.SetLineStyle(2)
APDShape.SetLineStyle(3)

### legend

leg = rt.TLegend(0.69,0.69,0.92,0.92)
leg.SetTextSize(28)
leg.SetTextFont(43)
leg.SetFillColor(rt.kWhite)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.AddEntry(EBShape, "EB","l")
leg.AddEntry(EEShape, "EE","l")
leg.AddEntry(APDShape, "APD","l")

### pave text

paveText = rt.TPaveText( 0.58, 0.41, 0.79, 0.61,"blNDC")
paveText.SetBorderSize(0)
paveText.SetFillColor(0)
paveText.SetFillStyle(0)
paveText.SetTextSize(28)
paveText.SetTextFont(43)
paveText.SetTextColor(9)
paveText.AddText("ECAL Pulse Shapes")

### plot in canvas
c1 = rt.TCanvas()
c1.cd()
EBShape.Draw("hist");
EEShape.Draw("hist same");
APDShape.Draw("hist same");
leg.Draw("same")
paveText.Draw("same")
c1.Update()
c1.SaveAs("ecalshapes.png")
c1.SaveAs("ecalshapes.pdf")

