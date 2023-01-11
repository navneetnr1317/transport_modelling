import numpy as np

Purposes = [ "HBEB" , "HBO" , "HBW" ]
Peaks = [ "AM" , "IP" , "PM" ]
Modes = [ "CYCLE", "WALK" ]

for purpose in Purposes:
	for peak in Peaks:
		for mode in Modes:
			
			#assuming the Code Name of the Peak Hour OD matrix is set as OD_PEAK_PURPOSE_MODE. eg. OD_AM_HBW_WALK
			PeakHour_OD_Matrix = Visum.Net.Matrices.ItemsByRef( 'Matrix([Code] = \"OD_{}_{}_{}\")'.format(peak,purpose,mode) ).GetAll[0]
			PeakHour_OD_values = np.array( PeakHour_OD_Matrix.GetValues() )
			
			PeakPeriod_PA_Matrix_values = ( PeakHour_OD_values + PeakHour_OD_values.T ) / 2
			
			#assumign the Code Name of the Peak is set as PA_PEAK_PURPOSE_MODE. eg. OD_AM_HBW_WALK
			PeakPeriod_Matrix = Visum.Net.Matrices.ItemsByRef( 'Matrix([Code] = \"PA_{}_{}_{}\")'.format(peak,purpose,mode) ).GetAll[0]
			PeakPeriod_Matrix.SetValues(PeakPeriod_PA_Matrix_values)

