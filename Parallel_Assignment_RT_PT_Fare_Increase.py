import os
import win32com.client as com
from multiprocessing.pool import ThreadPool as Pool
import re


def assign_models(visum_file_path,peak):
    Visum = com.Dispatch("Visum.Visum.220")
    Visum.LoadVersion(visum_file_path)
    Visum.Procedures.Execute()
    Visum.SaveVersion(visum_file_path)
    Visum = None

#version file path
file_path = r"\\sweco.se\gb\LDS01\Legacy\LND\65204376 Worcestershire Strategic Transport Model\05 Design and Calc\03_StrategicModelling\BaseYear\DemandModel\RealismTests\Highway Assignment Models\Realism Test_PT Fare Increase"
files = os.listdir(file_path)

all_model_file_location = []

for file in files:
    if (file.endswith(".ver")):
        all_model_file_location.append(( os.path.join(file_path,file) , re.findall("AM|IP|PM",file)[0] ))

if __name__ == '__main__':
        with Pool(5) as pool:
        
            pool.starmap(assign_models,all_model_file_location)
    