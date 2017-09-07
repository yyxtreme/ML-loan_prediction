import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("/home/ubuntu/Downloads/train_u6lujuX_CVtuZ9i.csv")
#plot for yes/no on basics of gender
b = df.groupby(["Gender","Loan_Status"]).size()
# a = df['Gender'].value_counts()
plt.figure()
sno = np.array([0,1])
plt.bar(sno,[b[('Male', 'Y')],b[('Female', 'Y')]], color = 'b', width = 0.25,label = 'Yes')
plt.bar(sno+0.25,[b[('Male', 'N')],b[('Female', 'N')]], color = 'g', width = 0.25,label = 'No')
plt.xlabel('Gender')
plt.ylabel('Total Number')
plt.title('Loan Status by gender')
plt.xticks(sno + .25/ 2, ("Male","Female"))
plt.legend()
plt.savefig('gender.png')
 
#plot on basic of marriage
b = df.groupby(["Married","Loan_Status"]).size()
plt.figure()
sno = np.array([0,1])
plt.bar(sno,[b[('Yes', 'Y')],b[('No', 'Y')]], color = 'b', width = 0.25,label = 'Yes')
plt.bar(sno+0.25,[b[('Yes', 'N')],b[('No', 'N')]], color = 'g', width = 0.25,label = 'No')
plt.xlabel('Marriage Status')
plt.ylabel('Total Number')
plt.title('Loan Status by Marriage')
plt.xticks(sno + .25/ 2, ("Married","Single"))
plt.legend()

#plot on basic of Graduation
b = df.groupby(["Education","Loan_Status"]).size()
plt.figure()
sno = np.array([0,1])
plt.bar(sno,[b[('Graduate', 'Y')],b[('Not Graduate', 'Y')]], color = 'b', width = 0.25,label = 'Yes')
plt.bar(sno+0.25,[b[('Graduate', 'N')],b[('Not Graduate', 'N')]], color = 'g', width = 0.25,label = 'No')
plt.xlabel('Graduate Status')
plt.ylabel('Total Number')
plt.title('Loan Status by Graduate')
plt.xticks(sno + .25/ 2, ("Graduate","Not Graduate"))
plt.legend()
 
#plot on basic of Credit History
b = df.groupby(["Credit_History","Loan_Status"]).size()
plt.figure()
sno = np.array([0,1])
plt.bar(sno,[b[(1, 'Y')],b[(0, 'Y')]], color = 'b', width = 0.25,label = 'Yes')
plt.bar(sno+0.25,[b[(1, 'N')],b[(0, 'N')]], color = 'g', width = 0.25,label = 'No')
plt.xlabel('Credit History')
plt.ylabel('Total Number')
plt.title('Loan Status by Credit History')
plt.xticks(sno + .25/ 2, ("Good","Defaulter"))
plt.legend()
 
#plot on basic of Property AREA
b = df.groupby(["Property_Area","Loan_Status"]).size()
plt.figure()
sno = np.array([0,1,2])
plt.bar(sno,[b[('Urban', 'Y')],b[('Semiurban', 'Y')],b[('Rural', 'Y')]], color = 'b', width = 0.25,label = 'Yes')
plt.bar(sno+0.25,[b[('Urban', 'N')],b[('Semiurban', 'N')],b[('Rural', 'N')]], color = 'g', width = 0.25,label = 'No')
plt.xlabel('Property Area')
plt.ylabel('Total Number')
plt.title('Loan Status by Property Area')
plt.xticks(sno + .25/ 2, ("Urban","SemiUrban","Rural"))
plt.legend()

#plot on basics of dependencies
b = df.groupby(["Dependents","Loan_Status"]).size()
plt.figure()
sno = np.array([0,1,2,3])
plt.bar(sno,[b[('0', 'Y')],b[('1', 'Y')],b[('2', 'Y')],b[('3+', 'Y')]], color = 'b', width = 0.25,label = 'Yes')
plt.bar(sno+0.25,[b[('0', 'N')],b[('1', 'N')],b[('2', 'N')],b[('3+', 'N')]], color = 'g', width = 0.25,label = 'No')
plt.xlabel('Dependents')
plt.ylabel('Total Number')
plt.title('Loan Status by Property Area')
plt.xticks(sno + .25/ 2, ("0","1","2","3+"))
plt.legend()

#plot on basic of income
d = { 'Y' : 1 , 'N' : 0}
a = df.replace({'Loan_Status':d})
plt.figure()
r = a[a["Credit_History"] == 0]
y = a[a["Credit_History"] == 1]
plt.scatter(r["ApplicantIncome"]+r["CoapplicantIncome"],r['Loan_Status'])
plt.scatter(y["ApplicantIncome"]+y["CoapplicantIncome"],y['Loan_Status'])
plt.title('Loan Status by Income')

#Scatter plot 


plt.show()