#include <iostream>
#include <fstream>
#include <math.h>
#include "TFile.h"
#include "TH1D.h"
#include <string>

using namespace std;



TH1D *h1;


void printArraysPhaseII()
{
    TFile fp("../../ROOTs/marc_v1/shape_9862.root");
    h1 = (TH1D*)fp.Get("average_shape_filtered");

    int nbins = h1->GetXaxis()->GetNbins();

    ofstream shapeFile;
    shapeFile.open("EB_SimPulseShape_PhaseII.txt");
   
    double threshold = -1e+9;
//    double threshold = (0.4/1000)*503.109;

    for(int bin = 1; bin<nbins; ++bin)
    {
        double val = h1->GetBinContent(bin);
        double thresh =  threshold;
   
	if(val > thresh)shapeFile << val << endl;
    }
    shapeFile.close();

    for(int bin = 1; bin<nbins; ++bin)
    {
        double val = h1->GetBinContent(bin);
        double thresh =  threshold;
   
	cout << val << " at i = "<< bin << endl;
    }

/*
    ofstream shapeEBFile;
    shapeEBFile.open("EB_simpulseshape.txt");

    for(int i=0; i<500; ++i)
    {
	 shapeEBFile <<EBShape[i] << endl;
    }
    shapeEBFile.close();

    ofstream shapeEEFile;
    shapeEEFile.open("EE_simpulseshape.txt");

    for(int i=0; i<500; ++i)
    {
	 shapeEEFile <<EEShape[i] << endl;
    }
    shapeEEFile.close();

    ofstream shapeAPDFile;
    shapeAPDFile.open("APD_simpulseshape.txt");

    for(int i=0; i<500; ++i)
    {
	 shapeAPDFile <<APDShape[i] << endl;
    }
    shapeAPDFile.close();
*/
}




