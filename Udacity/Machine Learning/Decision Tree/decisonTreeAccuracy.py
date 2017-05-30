import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import numpy as np
import pylab as pl
from sklearn import tree
features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################



#### your code goes here

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)

acc = clf.score(features_test, labels_test)### you fill this in!
### be sure to compute the accuracy on the test set


    
def submitAccuracies():
  return {"acc":round(acc,3)}

