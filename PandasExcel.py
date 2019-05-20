import pandas;
import numpy;

# data=[ {'Name':'PPA','Fees':'4000','Duration':'4'}, {'Name':'LB','Fees':'5000','Duration':'5'}, {'Name':'Web','Fees':'6000','Duration':'6'}];
# frame=pandas.DataFrame(data);
# print(frame);

# writer=pandas.ExcelWriter('Sheet1.xlsx',engine='xlsxwriter');
# frame.to_excel(writer);

# writer.save();





# data=[1.1,2.1,3,4,5];
# result=pandas.Series(data,index=['a','b','c','d','e']);
# print("\n",result,"\n"	);

# result1=pandas.DataFrame(result);
# print(result1);

# ret=pandas.Panel(result1);
# print(ret);


df1={'1':pandas.Series([1,2,3,4],index=['a','b','c','d']),'2':pandas.Series([5,6,7,8],index=['e','f','g','h'])};

df2={'3':pandas.Series([9,10,11,12],index=['i','j','k','l']) , '4':pandas.Series([13,14,15,16],index=['m','n','o','p'])};

frame1=pandas.DataFrame(df1);
frame2=pandas.DataFrame(df2);

data={"frame1":df1,"frame2":df2};


result=pandas.Panel(data);
print("Result: \n",result);