import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import csv


#link to revagin numpy
#https://numpy.org/doc/stable/


##create array
#np.array([10,20.3,30,50])
##craete random
#np.random.random(3)
## random with mean and standard devision
#np.random.normal(0,1,(3,3))
##random with range
#np.random.randint(0,10,3)
##random with identity matrix
#np.eye(3)
##random with garbage value
#np.empty(3)
## array with zeros
#x=np.zeros((3,3,5))
"""x.ndim يجيب عدد الابعاد
x.shapeيجيب ارقام الابعاد
x.size حجم الarray
x.dtype يجيب النوع
"""
#in python index in array start from 0
#للوصول الي عنصر ما في array
# x[0,1]


#slicing x[3:7] يكون array الي الرقم 6
# slice with incremant x[1:20:3]
#a=np.random.randint(low,high,iter)
#a[2:15:2] a[start point:end point:iter]
#slice in 2D ARRAY
# a[start point:end point:iter  ,start point:end point:iter]

#عند عمل اسليس فانه يشير علي الجزء المقطوع من الذاكره 
# وعند التغييرة فيه يتغير في الاصلية والمقطوعه ولكن عند استخدام فانكشن كوبي لا تغير في الاصلية
#ex:  a[:2,:2].copy




#reshaping اعادة التشكيل
"""
make new array
grid=np.arrange(1,10)   
هيعمل اراي من 1 ل9

grid =grid.reshape((3,3))


لو كتبت في خانه -1 هتكمل باقي صفوف او اعمدة لتنشا العمل الكامل لل اراي
grid[6,3]
grid .reshape((2,-1)) 
فيكون y =9
"""
#comcatenate array
"""
np.concatenate((array name1,array name 2))

np.full((3,5),6)       تنشا اراي 3*5 جميع عناصره تساوي 6

by defalt الجمع يكون علي طول الاعمدة ولذلك عند الدمج يجب تساوي عدد الااعمدة
عند الaxis يساوي 0 الجمع بالاعتماد علي الاعمده
عند الaxis يساوي 1 الجمع بالاعتماد علي الصفوف
np.concatenate([x,y],axis=1)
"""
#split array

"""
هيقسم الاراي لعدد من الاراي
x1,x2,x3=np.split(array name,[النقط اللي هيفصل عندها])
np.vsplit تستعمل في الاراي ثنائي الابعاد ليتم التقسيم بالنسبة الصفوف
np.hsplit تستعمل في الاراي ثنائي الابعاد ليتم التقسيم بالنسبة للاعمدة
"""
#ufunc

"""
من خلال المكتبة عند تكوين اراي يتحدد نوع البيانات مما يوفر بعض المساحة

"""

#m.sum(axis=0) will sum every colum and will result row of value
#m.sum(axis=1) will sum every row and will result a colum of value
#m.sum() will sum all values in the array will result 1 value



###################################################################################################
#project 1 date about people weight and height etc....
df=pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')



data=df.iloc[:,-3:].values
#data.size find the size

#data.ndim find the dimantions

#data.shape find the all dimention num of rows and num of colums

#data.dtype find the type of the array

#find the target ||target mean the last colum
#data[:,-1]

#slicing data[row info,colum info]===data[::3,:]
#a[start point:end point:iter  ,start point:end point:iter]


#extract first and last colum
# col1=data[:,0] ||data[:,-1]
#comcatenate the two colum in 2D array
#np.concatenate((col1,col2))
#to present them as 500row and 2 colum
#we can reshape the array using this function [np.hstack((col1.reshape(-1,1),col2.reshape(-1,1)))]

"""
col1 = data[:, 0]
col2=data[:, -1]
print(np.hstack((col1.reshape(-1,1),col2.reshape(-1,1))))
"""

#reverse the array
#will reverse the rows  data[::-1]
#will reverse the colums  data[::,::-1]

#find the maximum height
#height=data[:,0]  || height.max()

#and so the weights


#find mean and stander deviation
# data[:,0].mean(),data[:,0].std()

#finding the 25% 50% 75% percentile
#np.percentile(data[:,0],[25 ,50 ,75]) np is a function in numpy




#function argmax return the index of the heights element
#np.argmax(data[:,0])

#Broadcasting this topic about the operation in two arrays or more diffrent or the same in shape
#operation like sum multiply supstracte

###########################################
#project 2
#rained in settle


#important function
# np.count_nonzerose(function applyied in the array)like:np.count_nonzerose(x<6)
# will count how many values which not equal zero

"""
df=pd.read_csv('seattleWeather_1948-2017.csv',parse_dates=[0])[['DATE','PRCP']]
rainfall=df[df['DATE'].dt.year==2016]['PRCP'].values
plt.hist(rainfall,bins=30)
plt.title('rainfall')
plt.xlabel('PRCP')
plt.ylabel("Frequency")
"""

#find the days which rained in it ::np.count_nonzero(rainfall)
#find the days not rained in it ::np.sum(rainfall==0)
# find the days which rained more than 5 inch ::np.sum(rainfall>0.5)


# to create an array from a condation in a notehr array we do ::
# x[x<5] will make new array contane the values which is < 5 from x


#extract summer days which starts in 172th and end at 172+90th
#1-n1=np.arange(366)
#v=(n1>172)&(n1<172+90) as true and false array
#print(v)



#2-summer=n1[(n1>172) &(n1<(172+90))]
#print (summer) as days

#finding the mean of rainy days ::rainfall[rainfall>0].mean()

#find the maximum precipation on summer days :: np.max(rainfall[summer])
#n1=np.arange(366)
#summer=(n1>172)&(n1<172+90)
#print(rainfall[summer]) will print the value of rain at the summer

#print(np.max(rainfall[summer]))



#find the median precipation on rainy and non suny days ::print(np.median(rainfall[(~summer)&(rainfall>0)]))


######################################################################################



#fancy indexing
#extract some value from array
rand=np.random.RandomState(42)  #to make the random array constant every time i ran the program

x=rand.randint(100,size=10)     #x=rand.randint(range of random number,number of element)
#to get spacific element
#x=[x[3] ,x[7],x[9]]
#another solution :make array of index

#ind=[3,7,4]
#x=x[ind]

#we can also make x[[1,3,2,5]]
# and if it 2D array x[[1,3],1:]===will take the second and foured row with colum 2 to the end

##sort
#np.sort(x) to sort every colum independatenly np.sort(x,axis=0)
# to sort every row independatenly np.sort(x,axis=1)
#in numpy sort always be acsinding
#so to make it decing form big to small
#we will reverse the array np.sort(x)[::-1]


#if we make np.sort(x) it will make array x will not be sorted if we make x.sort() x will change

#np.argsort(x) will return array of index of the element



#np.any(x) //np.all(x)
#if we have an array and have at least one value true  any will return true and if all values equal true all wiil return true
#np.any(x,axis=0,keepdims=true)=== axis =0 wil make the function apply in each colum
# and keepdims will make the result as the input if the input 2D array result will be 2D array





#np.where(array with condition ,value when the condition true ,value when condition false)
#np.where(x>30,100,66) in every element in the array
# if the condition true will change the value to 100 and if it false will change to 66
#np.where(x>30,100,x) if it false will remain it as it is
#if we make np.where(x>0)only  will return teh index in the array that condition is true in it

#np.isnan() return an array of true if the value is nan and false other whise



#np.savetxt(file with والامتداد ,name of array,the separator between the values)

#np.savetxt('saved array.txt',x,delimiter=',')
################################################################
#crash course
#in array we can not append values
#we can make dot prodect===np.dot(first att=array,second array)  or dot=array1 @ array2
