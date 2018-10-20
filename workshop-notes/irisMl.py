from sklearn.datasets import load_iris
iris = load_iris()
#for make sure the lables are correct
print(list(iris.target_names)) 

from sklearn import tree
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(iris.data, iris.target)
print(classifier.predict([[5.1, 5.3, 1.4, 1.5]]))