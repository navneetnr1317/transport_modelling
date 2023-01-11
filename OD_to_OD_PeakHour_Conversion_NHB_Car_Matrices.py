import numpy as np

Purposes = [ "NHBEB" , "NHBO" ]
Peaks = [ "AM" , "IP" , "PM" ]
Modes = [ "C" ]

peakPeriodFactors = {"AM":3.0, "IP":6.0, "PM":3.0}


for purpose in Purposes:
	for peak in Peaks:
		for mode in Modes:
			
			#assuming the Code Name of the Peak Hour OD matrix is set as RT_PEAK_PA_PURPOSE_MODE. eg. RT_AM_PA_HBW_C
			PeakPeriod_OD_Matrix = Visum.Net.Matrices.ItemsByRef( 'Matrix([Code] = \"RT_{}_OD_{}_{}\")'.format(peak,purpose,mode) ).GetAll[0]
			PeakPeriod_OD_values = np.array( PeakPeriod_OD_Matrix.GetValues() )
			
			PeakHour_OD_Matrix_values = PeakPeriod_OD_values / peakPeriodFactors[peak]
			
			#assumign the Code Name of the Peak is set as OD_PEAK_PER_PURPOSE_MODE. eg. OD_AM_HBW_C_RT
			PeakHour_Matrix = Visum.Net.Matrices.ItemsByRef( 'Matrix([Code] = \"OD_{}_{}_{}_RT\")'.format(peak,purpose,mode) ).GetAll[0]
			PeakHour_Matrix.SetValues(PeakHour_OD_Matrix_values)