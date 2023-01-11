import os
import shutil

source_path = r"\\sweco.se\gb\LDS01\Legacy\LND\65204376 Worcestershire Strategic Transport Model\05 Design and Calc\03_StrategicModelling\BaseYear\DemandModel\RealismTests\Demand Matrices\Realism Test_Fuel 20pc Increase\Input_Demand\IT0"
destination_path = r"\\sweco.se\gb\LDS01\Legacy\LND\65204376 Worcestershire Strategic Transport Model\05 Design and Calc\03_StrategicModelling\BaseYear\DemandModel\RealismTests\Demand Matrices\Realism Test_Fuel 20pc Increase\Input_Demand"

all_files = os.listdir(source_path)

for file in all_files:
    
    source_file = os.path.join(source_path,file)
    destination_file = os.path.join(destination_path,file)
    
    shutil.copy(source_file,destination_file)