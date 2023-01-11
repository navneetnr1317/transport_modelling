import numpy as np

Purposes = [ "HBEB" , "HBO" , "HBW" ]
Peaks = [ "AM" , "IP" , "PM" ]
Modes = [ "C" ]

peakPeriodFactors = {"AM":3.0, "IP":6.0, "PM":3.0}


#Outbound and return tour factors

outTourFactors = {"HBW":{"AM":0.669, "IP":0.142, "PM":0.066},
                  "HBEB":{"AM":0.485, "IP":0.318, "PM":0.101},
                  "HBO":{"AM":0.219, "IP":0.403, "PM":0.177}}



returnTourFactors = {"HBW":{"AM":0.043, "IP":0.215, "PM":0.583},
                     "HBEB":{"AM":0.043, "IP":0.298, "PM":0.435},
                     "HBO":{"AM":0.062, "IP":0.409, "PM":0.242}}


def PeakHour_Conversion( matrix , PeakFact, outTourFact , returnTourFact ):
    
    FactMat = matrix * 2
    
    outProportion = outTourFact / (outTourFact + returnTourFact)
    returnProportion = returnTourFact / (outTourFact + returnTourFact)
    
    outPA = FactMat * outProportion 
    returnPA = FactMat.T * returnProportion   
    
    PeakHour_outMat = outPA / PeakFact
    PeakHour_returnMat = returnPA / PeakFact
    
    PeakHour_Final_mat = PeakHour_outMat + PeakHour_returnMat
    
    return PeakHour_Final_mat


for purpose in Purposes:
	for peak in Peaks:
		for mode in Modes:
			
			#assuming the Code Name of the Peak Hour OD matrix is set as RT_PEAK_PA_PURPOSE_MODE. eg. RT_AM_PA_HBW_C
			PeakPeriod_PA_Matrix = Visum.Net.Matrices.ItemsByRef( 'Matrix([Code] = \"RT_{}_PA_{}_{}\")'.format(peak,purpose,mode) ).GetAll[0]
			PeakPeriod_PA_values = np.array( PeakPeriod_PA_Matrix.GetValues() )
			
			PeakHour_OD_Matrix_values = PeakHour_Conversion( PeakPeriod_PA_values , peakPeriodFactors[peak] , outTourFactors[purpose][peak] , returnTourFactors[purpose][peak] )
			
			#assumign the Code Name of the Peak is set as OD_PEAK_PER_PURPOSE_MODE. eg. OD_AM_HBW_C_RT
			PeakHour_Matrix = Visum.Net.Matrices.ItemsByRef( 'Matrix([Code] = \"OD_{}_{}_{}_RT\")'.format(peak,purpose,mode) ).GetAll[0]
			PeakHour_Matrix.SetValues(PeakHour_OD_Matrix_values)