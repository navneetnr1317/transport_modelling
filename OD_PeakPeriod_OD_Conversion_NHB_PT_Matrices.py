import numpy as np

peakPeriodFactors = {"AM":3.0, "IP":6.0, "PM":3.0}

Purposes = [ "NHBEB" , "NHBO" ]
Peaks = [ "AM" , "IP" , "PM" ]
Modes = [ "PT" ]


for purpose in Purposes:
	for peak in Peaks:
		for mode in Modes:
			
			#assuming the Code Name of the Peak Hour OD matrix is set as OD_PEAK_PURPOSE_MODE. eg. OD_AM_NHBEB_CAR
			PeakHour_OD_Matrix = Visum.Net.Matrices.ItemsByRef( 'Matrix([Code] = \"OD_{}_{}_{}\")'.format(peak,purpose,mode) ).GetAll[0]
			PeakHour_OD_values = np.array( PeakHour_OD_Matrix.GetValues() )
			
			PeakPeriod_PA_Matrix_values = PeakHour_OD_values * peakPeriodFactors[peak]
			
			#assumign the Code Name of the Peak is set as PA_PEAK_PER_PURPOSE_MODE. eg. OD_AM_PER_NHBEB_CAR
			PeakPeriod_Matrix = Visum.Net.Matrices.ItemsByRef( 'Matrix([Code] = \"OD_{}_PER_{}_{}\")'.format(peak,purpose,mode) ).GetAll[0]
			PeakPeriod_Matrix.SetValues(PeakPeriod_PA_Matrix_values)



