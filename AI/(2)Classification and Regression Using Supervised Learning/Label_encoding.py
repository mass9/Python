import numpy as np
from sklearn import preprocessing

# Sample input labels
input_labels = ['red','black','red','green','black','yellow','while']

#Create label encoder and fit the labels
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

#Print the mapping
print("\n Label Mapping:")
for i,item in enumerate(encoder.classes_):
    print(item, '-->',i)

#Encode a set of lebels using the encoder
test_labels = ['green','red','black']
encoded_values = encoder.transform(test_labels)
print("\nLabels = ",test_labels)
print("Encoded values = ",list(encoded_values))

#Decode a set of values using the encoder
encoded_values = [3,4,0,1]
decoded_list = encoder.inverse_transform(encoded_values)
print('Encoded values = ',encoded_values)
print("Decoded values = ",list(decoded_list))