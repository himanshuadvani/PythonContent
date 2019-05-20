from sklearn import tree;

Ballfeatures=[[35,0],[47,0],[91,1],[111,1],[38,0],[39,0],[60,0],[80,1],[61,1],[120,1],[30,0],[40,0],[101,1],[118,1]];

Names=[0,0,1,1,0,0,0,1,1,1,0,0,1,1];

print("Balls: ",len(Ballfeatures));
print("Names: ",len(Names));

classifier=tree.DecisionTreeClassifier();

classifier=classifier.fit(Ballfeatures,Names);

result=classifier.predict([[41,1]]);

if(result==0):
	result="Tennis";
else:
	result="Cricket";
	
print("Prediction: ",result);