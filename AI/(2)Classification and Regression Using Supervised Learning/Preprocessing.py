import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3],
                       [-1.2, 7.8, -6.1],
                       [3.9, 0.4, 2.1],
                       [7.3, -9.9, -4.5]])

#Binarization
data_binarized = preprocessing.Binarizer(threshold = 2.1).transform(input_data)
print("\n Binarized Data: ",data_binarized)


#Print mean and standard Deviation
print("\n Before ")
print("Mean = ",input_data.mean(axis=0))
print("Std Deviation = ", input_data.std(axis=0))

#Remove mean
data_scaled = preprocessing.scale(input_data)
print("\n After ")
print("Mean = ",data_scaled.mean(axis=0))
print("Std Deviation = ", data_scaled.std(axis=0))


# Min Max Scaling

data_scaler_minimax = preprocessing.MinMaxScaler(feature_range=(0,1))
print("\nMin max scaler data: \n",data_scaler_minimax)
data_scaled_minimax = data_scaler_minimax.fit_transform(input_data)
print("\nMin max scaled data: \n",data_scaled_minimax)

#Normalization
data_normalized_l1 = preprocessing.normalize(input_data,norm='l1')

data_normalized_l2 = preprocessing.normalize(input_data,norm='l2')

print("\nL1 normalized data:\n", data_normalized_l1)
print("\nL2 normalized data:\n", data_normalized_l2)