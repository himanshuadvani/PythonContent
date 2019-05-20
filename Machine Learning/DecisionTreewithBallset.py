from sklearn import tree;
import pandas;


temp=pandas.read_excel('Marvellous Training Set Balls.xlsx');
weight=temp['Weight'].tolist();
pattern=temp['Pattern'].tolist();
target=temp['Label'].tolist();

for i in range(0,len(pattern)):
	if(pattern[i].lower()=='rough'):
		pattern[i]=0;
	else:
		pattern[i]=1;

for i in range(0,len(pattern)):
	if(target[i].lower()=='tennis'):
		target[i]=0;
	else:
		target[i]=1;
		
		
		
DataSet=[];

for i in range(len(weight)):
	DataSet.append([]);
	DataSet[i].append(weight[i]);
	DataSet[i].append(pattern[i]);
	


print("Dataset for Training: \n",DataSet);
print("Target for Training: \n",target);
	
wt=int(input("Enter Weight of object: "));
pt=input("Enter surface type of object(Rough/Smooth): ");

if(pt.lower()=='rough'):
	pt=0;
else:
	pt=1;
	
test_data=[];
temp=[];
temp.append(wt);
temp.append(pt);
test_data.append(temp);
print(test_data);

clf=tree.DecisionTreeClassifier();
clf=clf.fit(DataSet,target);
result=clf.predict(test_data);

if(result==0):
	result="Tennis";
else:
	result="Cricket";
	
print("Result of ",test_data," : ",result);
