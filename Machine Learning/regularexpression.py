import re;

str="India is my country. All Indians are my brothers and sisters.";

x=re.search("brothers and sisters",str);
y=re.split("\.",str);
z=re.sub("India","British",str)
print(x);
print(y);
print(z);