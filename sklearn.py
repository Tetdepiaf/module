# -*- coding: utf-8 -*-

from sklearn import tree

features = [[7, 0.6, 40], [7, 0.6, 41], [37, 600, 37], [37, 600, 38]] #definition des caractéristiques de classification
#labels = [chicken, chicken, horse, horse] 
labels = [0, 0, 1, 1] #définition des résultats de classification
classif = tree.DecisionTreeClassifier() #définition de la variable de classification
classif.fit(features, labels) #feed or fit your data to the classifier
 
print(classif.predict([[7, 0.6, 41]])) #prédiction
 
#output
# [0]  == Chicken