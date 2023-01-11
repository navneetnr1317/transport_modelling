
import shutil

source_path = r"\\sweco.se\gb\LDS01\Legacy\LND\65204376 Worcestershire Strategic Transport Model\05 Design and Calc\03_StrategicModelling\BaseYear\DemandModel\RealismTests\Demand Matrices\Realism Test_PT Fare Increase\Input_Demand\IT0"
destination_path = r"\\sweco.se\gb\LDS01\Legacy\LND\65204376 Worcestershire Strategic Transport Model\05 Design and Calc\03_StrategicModelling\BaseYear\DemandModel\RealismTests\Demand Matrices\Realism Test_PT Fare Increase\Input_Demand"

shutil.copytree(source_path,destination_path,dirs_exist_ok=True)
