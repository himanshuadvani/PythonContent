import pandas as pd;


print("Data Frame...");
data=pd.DataFrame();
print(data);

temp=[1,2,3,4,5];
data=pd.DataFrame(temp);
print(data);

temp=[['PPA',4],['LB',8],['Web',6],['Python',5]];
data=pd.DataFrame(temp);
print(data);

temp={'Name':['PPA','LB','Web','Python'],'Fees':[300,400,500,600]};
data=pd.DataFrame(temp);
print(data);

temp=[ {'Name':'PPA','Fees':4000}, {'Duration':5,'Fees':4000}, {'Name':'LB','Duration':4000}];
data=pd.DataFrame(temp);
print(data);

temp={'one':pd.Series([1,2,3],index=['a','b','c']), 'two':pd.Series([4,5,6],index=['a','b','c'])};
data=pd.DataFrame(temp);
print(data['one']);
