import  matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#link of data : https://github.com/inesriahi/Matplotlib-series/blob/master/main.ipynb

"""
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.title("Engineers Salary")
plt.xlabel("x axis")
plt.ylabel("y axis")
#plt.style.use('seaborn')
plt.plot(dev_x,dev_y,color="r",label="mean all  salary")
plt.plot(py_dev_x,py_dev_y,color="k",marker='o',linestyle='--',label="mean python salary")
#to make name for every curve: plt.legend(["mean all Salary","mean Python Salary"])
#or we can use plot when we plot the curve like
#to change color of the curve we use color in plot fun:plt.plot(py_dev_x,py_dev_y,color="k",label="mean python salary"),"تغيير سمك الخط":linewidth=5
#plt.plot(py_dev_x,py_dev_y,color="k",marker='o',linestyle='--',label="mean python salary")

#to change style:

#to change in line :linestyle='--',to show the point in the curve:marker='o'
plt.legend(["mean all Salary","mean Python Salary"])
plt.grid()#to make squar in background
#to save the plot:plt.savefig('salaryage.png')
plt.savefig('salaryage.png')
plt.show()
"""

#by default you can not plot many bars in the same grap so we should the bars left and right by:

"""
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_values=np.arange(len(dev_x))
widthh=0.3 #change the width of the bar

#we cahnge dev_x to x_values in plot bar function
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.title("Engineers Salary")
plt.xlabel("x axis")
plt.ylabel("y axis")
#plt.style.use('seaborn')
plt.bar(x_values-widthh/2,dev_y,width=widthh,label="mean all  salary")



plt.bar(x_values+widthh/2,py_dev_y,width=widthh,color="k",label="mean python salary")

#to change style:

#to change in line :linestyle='--',to show the point in the curve:marker='o'


#to save the plot:plt.savefig('salaryage.png')

plt.show()
"""

#to make grap it 3 bars

"""
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_values=np.arange(len(dev_x))
widthh=0.27 #change the width of the bar

#we cahnge dev_x to x_values in plot bar function
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.title("Engineers Salary")
plt.xlabel("x axis")
plt.ylabel("y axis")
js_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
js_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
#plt.style.use('seaborn')
plt.bar(x_values-widthh,dev_y,width=widthh,label="mean all  salary")



plt.bar(x_values,py_dev_y,width=widthh,color="k",label="mean python salary")

plt.bar(x_values+widthh,js_dev_y,width=widthh,color="g",label="mean python salary")
#to change style:

#to change in line :linestyle='--',to show the point in the curve:marker='o'

#to change the values of x bar:
plt.xticks(x_values,labels=dev_x)
#to save the plot:plt.savefig('salaryage.png')

plt.show() 
"""
"""
#histogram
ages = [10, 30, 45, 30, 31, 46, 12, 16, 32, 23, 28, 29]
bins = [10,20,30,40,50,60]
#"لتغيير لون الحواف" :"edgecolor='k'"
#determine the width of the bins like: we make the step equal 5 :plt.hist(ages,edgecolor='k',bins=5)
#or we can make a list of the x-bar values
bins=[10,20,30,40,50,60]
#to count the mean and make virtical line in the x-axis
mean=np.mean(ages)
plt.axvline(mean,linewidth=2,color='black')
plt.hist(ages,edgecolor='k',bins=bins)

plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
"""
#small project
data=pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')
"""
heights=data['Height']
#to make bins with for loop
bins=[i for i in range(140,201,5)]
plt.hist(heights,bins = bins,edgecolor='black')

plt.title('heights Distribution')
plt.xlabel('Heights')
plt.ylabel('Frequency')
plt.show()
"""

#pie graph
"""
data = [70,20,10,50]
labels = ['Python', 'Javascript', 'HTML', 'Java']
colors=['gray','green','blue','orange']
s=[0,0.2,0,0] #explore :to make this part in the grap separeted from thr grap
#to make shadow in the grap:shadow='true'
#to start the graph from spacific angle:startangle=90 and without the movement of the clock
#to show the percantage in the grap:autopct="%1.2f%%"


plt.pie(data, labels=labels,colors=colors,startangle=90,autopct="%1.2f%%",explode=s, wedgeprops = {'edgecolor': 'black'})

plt.title('A Pie Chart')
plt.show()


"""

#find frquanncy of gender
"""
frequancy=data['Gender'].value_counts()
#to find the indexs of the x-axis : frequancy.index
#using pie grap
#plt.bar(frequancy.index,frequancy,color=['green','blue'])
plt.pie(frequancy,labels=frequancy.index)
plt.show()

"""

#scatter plots


"""
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

#  :  "لتغيير الوان النقاط حسب لست من الارقام اعطيه له بحيث قيمة اللون مقابل للرقم في اللست"
colo=[9 , 10 , 2 , 5 , 7 , 6, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
#  :  "لتغيير الحجم النقاط حسب لست من الارقام اعطيه له بحيث تكون قيمة الحجم مقابل للرقم في اللست"
sizes=[200,400,300,100,50,250,400,310,200,150,50,70,90,190,300,250,120,60,490,200]
#"لتوحيد درجة الالون مع لست الحجم ودرجة الالوان  :cmap="reds"
#alpha="تقوم بتغيير الشفافية للنقاط"


plt.scatter(x,y,c=colo,edgecolors='black',alpha=0.7,linewidths=2,s=sizes,cmap='Reds')
#لعمل دليل لقيم درجات الالوان:
x=plt.colorbar()
x.set_label('Color Bar')
plt.grid()
plt.show()
"""
#project in kaggle
"""
data=pd.read_csv('train.csv')
#plt.scatter(data['OverallQual'],data['SalePrice'])
#we note from the graph when the quality increase the sale increase
plt.scatter(data['YearBuilt'],data['SalePrice'],c=data['OverallQual'],cmap='summer',s= 10 * data['OverallCond'])
n=plt.colorbar()
n.set_label('Qualite')
#we note from the graph when the quality increase the sale increase,to make the colors of points depend on quality
plt.grid()
plt.show()
"""

#subplots
"""
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
# to plot them in the same figure
fig,ax=plt.subplots()
ax.set_title('Salary for each age')
ax.set_xlabel('Age')
ax.set_ylabel('Salary')

ax.plot(dev_x, dev_y, color='r', linestyle='--', marker='o', label = 'Mean Dev Salary')
ax.plot(py_dev_x, py_dev_y, color='b', linestyle='--', marker='o', label = 'Mean Dev Salary')

plt.show()
"""
#to make eachh plot in separate figure

"""

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
# to plot them in the same figure

#"if they have the same x axis or the same y axis we make sharex=true ||sharey=true"
#to change the size of the plots
fig,ax=plt.subplots(nrows=1,ncols=2,sharey=True,figsize=(5,20))#"عدد الصفوف والاعمدة"
#now we have two figres to plot in it
ax[0].set_title('Salary for each age')
ax[0].set_xlabel('Age')
ax[0].set_ylabel('Salary')

ax[0].plot(dev_x, dev_y, color='r', linestyle='--', marker='o', label = 'Mean Dev Salary')

ax[1].set_title('Salary for pyhon age')
ax[1].set_xlabel('Age')
ax[1].set_ylabel('Salary')
ax[1].plot(py_dev_x, py_dev_y, color='b', linestyle='--', marker='o', label = 'Mean Dev Salary')
plt.tight_layout()#"لمنع تداخل الرسمتين مع بعض"
plt.show()

"""
#with four plots
"""
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


fig, axes = plt.subplots(nrows = 2, ncols = 2, sharex = True, figsize = (10,10))
# print(axes)
axes[0,0].set_title('Salary for each age')
axes[0,0].set_xlabel('Age')
axes[0,0].set_ylabel('Salary')
axes[0,0].plot(dev_x, dev_y, color='r', linestyle='--', marker='o', label = 'Mean Dev Salary')

py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

axes[0,1].plot(py_dev_x, py_dev_y,color='k',linewidth=5 , label = 'Mean Python Salary')
axes[0,1].set_title('Python Depeloper Salary for each age')
axes[0,1].set_xlabel('Age')
axes[0,1].set_ylabel('Salary')

axes[0,0].legend()
axes[0,1].legend()

fig.savefig('salaryage.png')

plt.tight_layout()
plt.show()
"""

df=pd.read_csv('kaggle_survey_2021_responses.csv')
#to delete first column as it the questions about the servay
#so there is some data which is numeric but we make it object as the first row was question so we want to make it numeric
count_str="Morocco, Iraq, Jordan, Tunisia, Saudi Arabia, Kuwait, Lebanon, Occupied Palestinian Territory, Oman, Qatar, Egypt, Algeria, United Arab Emirates"
arabs=count_str.split(", ")
df_arabs=df[df['Q3'].isin(arabs)]
print("------------------------------")
"""
#str convert from seriase to string to check the condition
df.drop(index=0,inplace=True)

print("------------------------------")
for col in df.columns:
    if df[col].str.isnumeric().all():
        df[col]=pd.to_numeric(df[col])

count_str="Morocco, Iraq, Jordan, Tunisia, Saudi Arabia, Kuwait, Lebanon, Occupied Palestinian Territory, Oman, Qatar, Egypt, Algeria, United Arab Emirates"
arabs=count_str.split(", ")
df_arabs=df[df['Q3'].isin(arabs)] #will gave me the columns which have arab countries
print("--------------------")
#print(df_arabs)



#to know all the values which is not repeated:unique():print(df['Q3'].unique())

print("---------###----------")
"""

#"نوجد الدول العربية في هيئة نص ثم نقوم بتحويله ب بايثون الي لست"
#################################################################################
#################################################################################


#Age distribution for arab countres
"""
count_str="Morocco, Iraq, Jordan, Tunisia, Saudi Arabia, Kuwait, Lebanon, Occupied Palestinian Territory, Oman, Qatar, Egypt, Algeria, United Arab Emirates"
arabs=count_str.split(", ")
df_arabs=df[df['Q3'].isin(arabs)]
#to order the values:.sort_values and to order index we use:sort_index
x=df_arabs['Q1'].value_counts().sort_index().index
y=df_arabs['Q1'].value_counts().sort_index().values
plt.figure(figsize=(10,7))
plt.title('Age Distribution')
plt.xlabel("Ages")
plt.ylabel("Frequancy")



plt.plot(x,y)

plt.show()
"""
#country distarabtion
"""
count_str="Morocco, Iraq, Jordan, Tunisia, Saudi Arabia, Kuwait, Lebanon, Occupied Palestinian Territory, Oman, Qatar, Egypt, Algeria, United Arab Emirates"
arabs=count_str.split(", ")
df_arabs=df[df['Q3'].isin(arabs)]
x=df_arabs['Q3'].value_counts().index
y=df_arabs['Q3'].value_counts().values
plt.figure(figsize=(10,7))
plt.title('Country Distribution')
plt.xlabel("Country")
plt.ylabel("Frequancy")
plt.xticks(rotation=45)#"لتدوير النص علي المحور اكس"
#canot be used in subplots


plt.bar(x,y)
plt.show()
"""


#kaggel arabs programing distrabotion
#consat of 10 question about programing language we will count how many values in each column

"""

Q7col=df.columns[df.columns.str.contains('Q7')]

#will make dictionary of indexs and it values
dic7=dict()
for col in df_arabs[Q7col]:
    key=df[col].value_counts().index[0]
    dic7[key]=df[col].value_counts()[0]

print("00000000000000000000000000000000")
print(dic7)
print("00000000000000000000000000000000")

#convert it from dictionary to seriase
Q7series=pd.Series(dic7)

plt.figure(figsize=(10,10))
plt.pie(Q7series,labels=Q7series.index,autopct="%1.2f%%")
plt.legend(Q7series.index)
plt.show()
"""

#two plots with each other
"""

Q7col=df.columns[df.columns.str.contains('Q7')]

#will make dictionary of indexs and it values
dic7=dict()
for col in df_arabs[Q7col]:
    key=df[col].value_counts().index[0]
    dic7[key]=df[col].value_counts()[0]

print(dic7)
#convert ut from dictionary to seriase
Q7series=pd.Series(dic7)



fig,axes=plt.subplots(1,2,figsize=(20,8))
axes[0].bar(Q7series.index,Q7series.sort_values(ascending=False))
axes[0].tick_params(labelrotation=80,labelsize=15)
axes[1].pie(Q7series,labels=Q7series.index,autopct="%1.2f%%",explode=[0.04 for i in range(len(Q7series)) ])


plt.show()
"""
##################################
#crash course
#plt.title('',fontdict={'fontname':'Coni Sans MS','fontsize':20)#to change the kind of font and its size and we can do it in xlable and ylable
#bars.set_hatch("/")
#bars.set_hatch("o")
#bars.set_hatch("*")
#shortcut of styling #plt.plot(x,y,'b.-')
