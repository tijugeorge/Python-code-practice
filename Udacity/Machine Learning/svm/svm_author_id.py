from sklearn import svm
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]


#########################################################
### your code goes here ###

#########################################################
#features_train = features_train[:]
#labels_train = labels_train[:]

#########################################################
### your code goes here ###
clf = svm.SVC(kernel="rbf", C=10000)
t0 = time()
clf.fit(features_train, labels_train)
print "Training time:", round(time()-t0, 3), "s"

t1 = time()
prediction = clf.predict(features_test)
print "Prediction time:", round(time()-t1, 3), "s"

print "accuracy is: ",accuracy_score(prediction, labels_test)


# Prediction for feature_test[10][26][50] = [1][0][1]
# print clf.predict(features_test[50])

chris = []
# Get number of predicted emails written by Chris.  
for i in prediction:
    if i == 1:
        chris.append(i)

print len(chris)
#########################################################
