# import xlsxwriter;

# workbook=xlsxwriter.Workbook('Marvellous.xlsx');

# worksheet=workbook.add_worksheet('MarvellousSheet');

# worksheet.write('A1','name');
# worksheet.write('B1','address');
# worksheet.write('C1','email');
# worksheet.write('D1','contact');
# worksheet.write('A10','Himanshu Advani');
# worksheet.write('B13','Hiti Advani');
# worksheet.write('C16','Hitu Advani');
# worksheet.write('D19','Advani Hiti');

# workbook.close();

import pandas;
import matplotlib.pyplot as plt;

file='Marvellous Training Set Balls.xlsx';
data=pandas.read_excel(file);

print("Data from excel: \n");

print(data.head());


data['Weight'].plot(kind="barh");
plt.show();

xlsx=pandas.ExcelFile(file);
print("xlsx: \n",xlsx.parse(xlsx.sheet_names[0]));


