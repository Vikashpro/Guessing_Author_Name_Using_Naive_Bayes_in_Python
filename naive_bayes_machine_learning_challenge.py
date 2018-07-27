import nltk
import random

feature_list = []
for line in open('pos_tag_finals_data.dat', 'r'):   					#getting features matrix from the file 
	line_list = []
	for word in line.split():											#splitting the features line by line
		line_list.append(word)		
		
	for j in range(1,6):
		single_feature = ({line_list[0] : line_list[j]},'0s')			#combining feature with feature name tag and book tag
		feature_list.append(single_feature)								#appending it in a list
	for j in range(6,11):
		single_feature = ({line_list[0] : line_list[j]},'1s')			# same for other book
		feature_list.append(single_feature)
accu = 0

for i in range(3):
	random.shuffle(feature_list)
	train_set, test_set = feature_list[:77],feature_list[77:]			#shuffling the feature set and apply into the NaiveBayesClassifier
	classifier = nltk.NaiveBayesClassifier.train(train_set)				#&and training the classifier on 70% data 
	accu +=nltk.classify.accuracy(classifier,test_set)					#testing the data on 30%

average_accuracy = accu/3*100 											#getting the average accuracy of the data.
print("Average Accuracy is : ",average_accuracy)

print classifier.show_most_informative_features(5)						#prints the most informative features.
