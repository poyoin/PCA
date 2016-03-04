import wx
import Functions as Func
import CatClass
import cPickle as pickle
import TIPPGen as TIPP
import dask.array as da
import numpy as np
from os import path as pt #split filepaths



class PCAPlugin(CatClass.ISpectralPlugin):
    def Run(self,FilePath,FileName,CurrentProject,WorkFolder,UserPref):
        self.Metadata = TIPP.LoadMetadata(FilePath[0])
        print self.Metadata

        # 1: self.inputs
        self.FilePath = FilePath



        # 2: Warning Dialogs
        ImageLst = []
        RefLst = []
        RefFileNameLst = []

        for i in range(len(FilePath)):
            if pt.split(pt.split(FilePath[i])[0])[1] == "Reference Samples":
                RefLst.append(FilePath[i])
                RefFileNameLst.append(pt.splitext(FileName[i])[0])
            else:
                ImageLst.append(FilePath[i])
                self.FileName = FileName[i]
        if len(ImageLst)!=1:
            Func.WarningDialog("Please select one Sample", "File Error")
        elif pickle.load(open(pt.splitext(ImageLst[0])[0]+"_metadata.pkl", "rb" ))["Image Type"] != "Normalized_HSI":
            Func.WarningDialog("Please select a normalized image", "Metadata Error")
        elif len(RefLst) <= 1:
            Func.WarningDialog("Please select at least two reference samples", "File Error")
        elif len(RefLst) >= pickle.load(open(pt.splitext(ImageLst[0])[0]+"_metadata.pkl", "rb" ))["Shape"][2]/2-1:
            Func.WarningDialog("Please select not more reference samples, than the half of the bands", "File Error")
        else:






        # 3: Algorithm





        # 4: save as Array(x,y,weights) as ".TippRCA";; Joan will convert to ".TippPCA"



        # 5: Define Class for dialog box

        class VariableBox(setpoint,id):




       
