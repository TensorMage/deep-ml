import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	
	mean=np.mean(data,axis=0)
	std_dev=np.std(data,axis=0)

	std_dev=np.where(std_dev==0,1,std_dev)
	standardize=(data-mean)/std_dev 

	#for min max feature_scaling

	min_val=np.min(data,axis=0)
	max_val=np.max(data,axis=0)

	section=max_val-min_val
	section=np.where(section==0,1,section)
	normalize=(data-min_val)/section

	standardized_data=np.round(standardize,4)
	normalized_data=np.round(normalize,4)



	return standardized_data, normalized_data