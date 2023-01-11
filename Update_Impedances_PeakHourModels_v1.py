import win32com.client as com
import os
from multiprocessing.pool import ThreadPool as Pool

ver_file_path = r"\\sweco.se\gb\LDS01\Legacy\LND\65204376 Worcestershire Strategic Transport Model\05 Design and Calc\03_StrategicModelling\BaseYear\DemandModel\RealismTests\Highway Assignment Models\Realism Test_Fuel 20pc Increase"


#specify the userclasses for which the Impedance Function is to be updated. Delete the rest, if not required. 
#Becareful if the Impedance is not updated from here, the model shall take whatever is already defined in the model.
userclasses = [ "C-EB" , "C-Oth" , "C-Work" , "LGV" , "HGV" ]


#operation 1 is for + , 2 is for - and 0 is for not performing any operation
#change "Length" to "T0_PRTSYS({})" in the definition if the second attribute should be T0, or any other option as you prefer. Leave it blank with "" if nothing is to be used.
procedure_parameters = {
                        "C-EB" :  { "first_coeff": 1 , "operation": 1, "second_coeff": 0.0248 , "second_attribute" : "Length" },
                        "C-Oth":  { "first_coeff": 1 , "operation": 1, "second_coeff": 0.0309 , "second_attribute" : "Length" },
                        "C-Work": { "first_coeff": 1 , "operation": 1, "second_coeff": 0.0196 , "second_attribute" : "Length" },
                        "LGV":    { "first_coeff": 1 , "operation": 1, "second_coeff": 0.0439 , "second_attribute" : "Length" },
                        "HGV":    { "first_coeff": 1 , "operation": 1, "second_coeff": 0.1042 , "second_attribute" : "Length" }
                        }


def update_impedance(visum_file_path , userclasses , procedure_parameters ):

    Visum22 = com.Dispatch("Visum.Visum.22")

    try:
        Visum22.LoadVersion(visum_file_path , False)
    except IOError:
        print("Something wrong while trying to read the file")
    
    for userclass  in userclasses:
        
        Visum22.Procedures.Functions.ImpedanceFunctions(userclass).ImpedanceFunction("").LinCombItem(1).SetAttValue("FirstAttrCoeff",procedure_parameters[userclass]["first_coeff"])
        Visum22.Procedures.Functions.ImpedanceFunctions(userclass).ImpedanceFunction("").LinCombItem(1).SetAttValue("Operation",procedure_parameters[userclass]["operation"])
        # if you want to use T0 as the 2nd att, use this command procedure_parameters[userclass]["second_attribute"].format(userclass) and change "Length" to "T0_PRTSYS({})" in the definition
        Visum22.Procedures.Functions.ImpedanceFunctions(userclass).ImpedanceFunction("").LinCombItem(1).SetAttValue("SecondAttrName",procedure_parameters[userclass]["second_attribute"])
        Visum22.Procedures.Functions.ImpedanceFunctions(userclass).ImpedanceFunction("").LinCombItem(1).SetAttValue("SecondAttrCoeff",procedure_parameters[userclass]["second_coeff"])

    Visum22.SaveVersion(visum_file_path)
    Visum22 = None


files = os.listdir(ver_file_path)

all_input_data = []

for file in files:

    if file.endswith(".ver"):
        all_input_data.append( (os.path.join(ver_file_path,file) , userclasses , procedure_parameters) )

if __name__ == '__main__':
    with Pool(5) as pool:
        pool.starmap( update_impedance , all_input_data )