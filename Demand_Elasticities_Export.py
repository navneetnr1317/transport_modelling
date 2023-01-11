import pandas as pd
import datetime as dt
import numpy as np


PeakHours = [ "AM" , "IP" , "PM" , "ALLPEAKS" ]
Purposes = [ "EB" , "W" , "O" , "TOTAL" ]

output_file = r"\\sweco.se\gb\LDS01\Legacy\LND\65204376 Worcestershire Strategic Transport Model\05 Design and Calc\03_StrategicModelling\BaseYear\DemandModel\RealismTests\Outputs\Elasticity_Fuel_20pc_Log.csv"
#output_file = r"C:\Data\WSTM\VDM\Test_DE_UDAs.csv"
 
DemandElasticity_CurrentIteration = {}

all_network_attributes = [ attribute.Name for attribute in Visum.Net.Attributes.GetAll]

for peak in PeakHours:
    for purpose in Purposes:
        if( "DE_{}_{}".format(purpose,peak) in all_network_attributes ):
            
            DemandElasticity_CurrentIteration["Timestamp"] = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            DemandElasticity_CurrentIteration["DE_{}_{}".format(purpose,peak)] = Visum.Net.AttValue("DE_{}_{}".format(purpose,peak))



matrix_set = [ '3073', '3074', '3075', '3076', '3077', '3127', '3128', '3129', '3130', '3131', '3132', '3133', '3134', '3135' ,
            '3078',	'3079',	'3080',	'3081',	'3082',	'3083',	'3084',	'3085',	'3086',	'3087',	'3088',	'3089',	'3090',	'3091',	'3092',	'3093',	'3094',	'3095',	'3096',	'3097' ,
            '106' , '107' , '105' , '109' , '108' , '2211' , '2212' , '2213' , '2215' , '2214',
            "402",	"404",	"400",	"123",	"124", "101",	"102",	"100",	"104",	"103", "403",	"405",	"401",	"128",	"129" 
            ]

for matrix_no in matrix_set:
    
    matrix = Visum.Net.Matrices.ItemByKey(matrix_no)
    DemandElasticity_CurrentIteration[matrix.AttValue("Name")] = sum(sum(np.array(matrix.GetValues())))    


DemandElasticity_CurrentIteration = pd.DataFrame(DemandElasticity_CurrentIteration , index = [0] ) 

DemandElasticity_CurrentIteration["DemandGap"] = Visum.Net.AttValue("DemandGap")

DemandElasticity_PreviousIteration = pd.read_csv(output_file)


Updated_DE_list = pd.concat([DemandElasticity_PreviousIteration,DemandElasticity_CurrentIteration])


Updated_DE_list.to_csv(output_file , index = False)