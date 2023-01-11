import win32com.client as com
import os

ver_file_path = r"\\sweco.se\gb\LDS01\Legacy\LND\65204376 Worcestershire Strategic Transport Model\05 Design and Calc\03_StrategicModelling\BaseYear\DemandModel\RealismTests\Highway Assignment Models\Realism Test_Fuel 20pc Increase"

Visum22 = com.Dispatch("Visum.Visum.22")

files = os.listdir(ver_file_path)

for file in files:

    if file.endswith(".ver"):
        version_file = os.path.join(ver_file_path,file)
        try:
            Visum22.LoadVersion(version_file , False)
        except IOError:
            print("Something wrong while trying to read the file")
        
        #The below step will execute the procedure sequence whichever are highlighted in the individual model for execution.
        Visum22.Procedures.Execute()
        
        Visum22.SaveVersion(version_file)

Visum22 = None