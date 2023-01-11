import numpy as np

Purposes = [ "HBEB" , "HBO" , "HBW" ]
Peaks = [ "AM" , "IP" , "PM" ]
Modes = [ "CAR" ]

peakPeriodFactors = {"AM":3.0, "IP":6.0, "PM":3.0}


#Outbound and return tour factors

outTourFactors = {"HBW":{"AM":0.669, "IP":0.142, "PM":0.066},
                  "HBEB":{"AM":0.485, "IP":0.318, "PM":0.101},
                  "HBO":{"AM":0.219, "IP":0.403, "PM":0.177}}



returnTourFactors = {"HBW":{"AM":0.043, "IP":0.215, "PM":0.583},
                     "HBEB":{"AM":0.043, "IP":0.298, "PM":0.435},
                     "HBO":{"AM":0.062, "IP":0.409, "PM":0.242}}


def PeakPeriod_Conversion( matrix , PeakFact, outTourFact , returnTourFact ):
	
    outPA = np.zeros(matrix.shape)
    returnPA = np.zeros(matrix.shape)
	
    outProportion = outTourFact / (outTourFact + returnTourFact)
    returnProportion = returnTourFact / (outTourFact + returnTourFact)
	
    outPA = matrix * PeakFact * outProportion
    returnPA = matrix * PeakFact * returnProportion
	
    return (outPA + returnPA.T)/ 2
	
	
	

for purpose in Purposes:
	for peak in Peaks:
		for mode in Modes:
			
			#assuming the Code Name of the Peak Hour OD matrix is set as OD_PEAK_PURPOSE_MODE. eg. OD_AM_HBW_CAR
			PeakHour_OD_Matrix = Visum.Net.Matrices.ItemsByRef( 'Matrix([Code] = \"OD_{}_{}_{}\")'.format(peak,purpose,mode) ).GetAll[0]
			PeakHour_OD_values = np.array( PeakHour_OD_Matrix.GetValues() )
			
			PeakPeriod_PA_Matrix_values = PeakPeriod_Conversion( PeakHour_OD_values , peakPeriodFactors[peak] , outTourFactors[purpose][peak] , returnTourFactors[purpose][peak] )
			
			#assumign the Code Name of the Peak is set as PA_PEAK_PER_PURPOSE_MODE. eg. PA_AM_PER_HBW_CAR
			PeakPeriod_Matrix = Visum.Net.Matrices.ItemsByRef( 'Matrix([Code] = \"PA_{}_PER_{}_{}\")'.format(peak,purpose,mode) ).GetAll[0]
			PeakPeriod_Matrix.SetValues(PeakPeriod_PA_Matrix_values)