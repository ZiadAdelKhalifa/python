import pandas as pd
import numpy as np
import seaborn as sns

#pandas is devolped than numpy and more good with dealing with tables

#series is a 1D array differnt from numpy array is it print the index(the main colum that control the all prosess) with it

#dataFrame is a 2D array

#to create a series
#data=pd.Series([10, 20 ,30,256,900])

"""
#to convert from series to numpy array
print(data.values)
"""
#indexing is to name point to value and show it with this name


"""
data=pd.Series([10, 20 ,30,256,900],index=["first","second","thrid","foured","fived"])
#in indexing number of indexes equal number of values
print(data)
print(data["first"])
"""


#note the the series in pandas lokes exactly like dictionary in python
"""
population_dict={"egypt":902305251,
            "tones":215256251,
            "soadia":262216,
            "iraq":95648,
            "morak":456213}
#and i can convert from dixtionary to Series

pdd=pd.Series(population_dict)
print(pdd)

area_dict={"egypt":6666,
            "tones":3333,
            "soadia":5555,
            "iraq":7777,
            "morak":99999}

"""

#slicing in serises we can slice using numbers of index or the name of indexes

#data=pd.Series([10, 20 ,30,256,900],index=["first","second","thrid","foured","fived"])
#print(data["first":"second"]) including the end
#print(data[0:3])  not including the end



#dataFrame is more popualr than Series and used in life looks like table

#converting dictionary to series
"""
population_dict={"egypt":902305251,
            "tones":215256251,
            "soadia":262216,
            "iraq":95648,
            "morak":456213}
area_dict={"egypt":6666,
            "tones":3333,
            "soadia":5555,
            "iraq":7777,
            "morak":99999}

population=pd.Series(population_dict) #convert dictionary to Series

area=pd.Series(area_dict)             #convert dictionary to Series

"""
#convert the data to dataFrame in two ways:
#1
#Alldatatable=pd.DataFrame({'population':population,
#                            'area':area})

#2
"""
Alldatatable=pd.DataFrame({'population':[30000 ,200000,330000,555654,8479897],
                           "area":[22025,3333,48484,985,2000]})
#will create it with number index if i want to name the rows we  do
Alldatatable=pd.DataFrame({'population':[30000 ,200000,330000,555654,8479897],
                           "area":[22025,3333,48484,985,2000]},index=['egypt','seria','morac','iraq','phalasten'])
print(Alldatatable)
"""

#Alldatatable=pd.DataFrame({'population':[30000 ,200000,330000,555654,8479897],
#                           "area":[22025,3333,48484,985,2000]},index=['egypt','seria','morac','iraq','phalasten'])
#to know the name of the rows :Alldatatable.index

#to know the name of the colums: Alldatatable.columns

#to show data from spacific colum :Alldatatable["area"] #the result will be a series array

#to show data from spacific colum and spacific value :Alldatatable["area"] ["iraq"]

#make a numpy array and convert it to dataFrame

"""
arr=np.random.randint(1,20,30).reshape(10,3)
data=pd.DataFrame(arr,columns=["name","age","study"],index=[i*2 for i in range (10)])
print(data)
j"""

########################################
#project one with kaggle

#indexing and selection

df=pd.read_csv('ramen-ratings.csv')
#we can read also exal and txt file:pd.read_excel:read_txt
#show the first five colum
print(df.head())
print("---------------------")
#sorting data :df.sort_values (['Brand','Style'],ascending=[1,0]
#to drop a colum:df.drop(columns='colum name')
#show colum from the data:print(df.columns)
#using contain in searching
#df.loc[df['Name'].str.contains("the text i want to search",flags=re.I)]
#flags=re.I :will ignor sensitive of string upper or lower

#print(df[50:1000:20]) #slicing


#to show data we have two ways :
#[1]- indexing which present data number in the table "ترتيبها" and we use (iloc) function
#df.iloc[:,0] show first colum with all rows
#df.iloc[0:3,:] show first 3rows with all columns
#df.iloc[:,-1] show the last colum with all rows
#df.iloc[[1,50,200],:] show spacific rows with all colums
#df.iloc[-10:-1,:] show the last ten rows with all colums

#[2] lable based selection by using the name of the colum and function(loc)
#df.loc[:,['Brand','Country','Stars']]
#print(df.loc[:,['Brand','Country','Stars']])


#important fun to change the index column ("نغير اسماء الصفوف الي اسماء من احدي الاعمدة")
#"لكن لا تتغير علي نفس الداتا يجب ان ننسخها في داتا اخري"
#df1=df.set_index('Country')
#print(df1.head())

#conditinal selection
#we want to know the remain deshes in (tiwan)
#firstly we make atrue and false array of the condition::df.Country =="Taiwan"
print(df[df["Review #"]>2000])
#df.loc[df.Country =="Taiwan"] #will show all rows with country tiwan
#exstract data
#we have two way to select data:
#1-with loc like the previous example:: df.loc[:,'Stars']
# 2-with the attribute if the name of the colum is one word: df.Stars

#exstract data which stars >2.5


#if we make (df.Stars>2.5)will make this error:: TypeError: '>' not supported between instances of 'str' and 'float'
#because there is some straning in this colum colled "unrated" to remove it :
# df=df[df.Stars !='Unrated'] after this we convert it to float because number stored in  string value
# ::df.Stars=df.Stars.astype(float)
#to show the rate more than 2.5
#df[df.Stars>2.5] or df.loc[df.Stars>2.5]

#dishes in tiwan and rates >2.5

"""
df=df[df.Stars !='Unrated']
df.Stars=df.Stars.astype(float)
print(df.loc[(df.Country=='Taiwan')& (df.Stars>2.5)])

#we want to show colum brand and style where (dishes in country tiwan and rates >2.5)
df=df[df.Stars !='Unrated']
df.Stars=df.Stars.astype(float)
print(df.loc[(df.Country=='Taiwan')& (df.Stars>2.5),['Brand','Style']])
print(df.loc[(df["Country"]=="Japan"),["Stars","Review #"]])

#to extract data from two diffrent countery
ddd=df.loc[df.Country.isin(['South Korea','Taiwan','Thailand'])]
eee=df.loc[df.Brand.isin(['Samyang Foods'])]
print(ddd)
print(eee)

"""

"""
#show the data in top ten which is not null we have a function return the null value in data ::isnull
# there is another function called notnull
print(~df['Top Ten'].isnull()) #array of faluse and true

print(df[~df['Top Ten'].isnull()]) #will print the value which is only true in the array

"""

"""
#Assining data
df['Brand']='Egypt'
print(df)
"""

#to insert new colum
#df["isStyleCup"]=df['Style']=='Cup'
#"لاستبدال عناصر عمودو بعنناصر عمود اخر يجب ان يكونوا متساويين"
"""
print(len(df['Review #'])) #to know the lenght of the colum
df.loc[:,'Review #']=list(range(0,2580))
print(df)
"""

#deleting all null values from the table :df[df.notnull()]
#to count number of null value in each colum:df.isnull().sum(axis=0)

#in null values we can drop the row ao fill it with another value
#to delete rows whic contan we use: df=df.dropna()

#to drop the colum which contane nall value: df=df.dropna(axis="columns") or df.dropna(axis="columns",inplace='true')
#to change the data  after an operation we use df=df"ثم العملية" or inplace='true'

#to delete the all row depend on spacific column we use:df=df.dropna(subset=["name of the colum"]):df=df.dropna(subset=["Style"])


#to bring the two null value in the style:df=df.loc[df['Style'].isnull()]

#using function fillna we change null values :df=df.fillna({'Style':-1, 'Top Ten':0})
#we can fill null value with the data before it like :method='ffill' df=df.fillna(method='ffill')
# or the data after like method='bfill' df=df.fillna(method='bfill')
print("########################################")
#count how many values not equal null :print(df[df!="null"].count())

print("########################################")
#to count how many each value counted in the column:df['column name'].values_counts()

#to converet values in colum to another value: df['colum name'].replace('old value','new value') :df['Stars']=df['Stars'].replace('Unrated','0')
#we want to convert all values in the colum to float so it will not diffrent between 5 and 5.0

#df['Stars']=df['Stars'].replace('Unrated','0')
#df['Stars']=df['Stars'].astype(float)
#print(df['Stars'].value_counts())


##############################################################
#project two will be in kaggle as the data is big:problem in kaggle called(Predict Future Sales)

#joining in pandas like joinning  in data base:

#[common colum name] the colum we chose to join depend on it and exists in the two table but there is some values exist in
#the fist table only and some exist in the second table only and there is common values between the two table
# and this make the diffrence when we join tables


#[1]inner join : take only the values which exist in the two table depend on the common named colum
#in this join there a same name of a column exist in the two table
# in inner join we will join the data colum in the table two to table one  if there is a common value in table one and table two
# of the common colum in the same name

#to merge two colum in pandas using marge function
#b=pd.merge(table one name,table two name,how='type of join',on='the colum name we join depend on it')


#[2]outer joined:will take all the values of the two table
#but if the value of the common coulm named exist in the two table we will join it as inner join (with each other)
#and if it is not we will add the values in the first table and will make non to the rest of the colum of the new row we make
#untill the value of the first table finched
#after it we will continue in the second table


#b=pd.merge(a,b,how='outer',on='cat_id')
#"لو في اكتر من عمود عايز ادمج عليه ممكن نعمل لست بالعواميد في خانة"on
#pd.merge(a,b,how='outer',on=['cat_id','item_name'])


#[3]left joining eaxtly like the outer joining excapt if we have value in the left and nan in the right in the new table
#will take it and if the left is non and the right has a value will not take it(tooking about the table result from outer joining)

#[4]-right joining :the opisite of left


#when we marge if the colum we marge the table depend on it have diffrent names in the two table we use
#b=pd.merge(first table (left table),second table (right table)
# ,how='outer',left_on='colum name in the first table',right_on='colum name in the second table')


#to merge two colum in pandas using join function

#name table1.join(name of table 2,how='inner or outer or left or right',
# lsuffix='colum name in left table',rsuffix='table name in right table')===we use (lsuffix='colum name in left table',rsuffix='table name in right table')
#when they are common in colums name

#in join function by default we join depend on index colum(first colum in the two table)
#if we want to change joining depend to another colum we should change the colum index by:
#a.set_index('اسم العمود الجدلد')

######################################
#concate
#pd.concat([pf1,pf2])
#pd.concat([pf1,pf2],ignor_index=true)==ignor index=="لكي يكمل العد علي العناصر الجديدة في عمود الاندكس بعد الدمح"
# "لتميز كل قيمة من اين جائت بعد الدمج نستخدم "keys
#pd.concate([pf1,pf2],keys=['الاسم المميز للجدول الثاني','الاسم المميز للجدول الاول'])
#to concate depend on the colum(there is a condotion the tables have the same numbers of rows)
#pd.concat([pf1,pf2],axis=1)


############################
#aggriation function :built in function you can use
#like sum mean std var

#sales.decripe() will give you some information about each colum in the table

#print(df['Stars'].describe())


#to know data about special groub we use groupby

#table name.groupby('colum i want to group data depend on him')[['the operation done in this colum'],['this colum too']].operation i want to do


#sales.groupby('shop_id')[['item_price],['itm_cnt_day']].mean()


#i want to print each group in the table
#for (shop_id,grop) in sales.gropby("shop_id")
#print(shop_id,grop) will print every grop separated


#function aggregate

df=pd.DataFrame({'key':['A','B','C','A','B','C'],
                           "data1":[5,1,2,3,7,5],
                           "data2":[2,4,6,8,10,12],})
#print(df.groupby('key').aggregate([np.max,np.min]))
"""
gf=df.groupby('key')
for (key,group) in gf:
    print(key)
    print(group)
"""

#to group data by acolum and make some function on it :
#df.groupby('colum name').aggreate([np.mean,np.min]) or
#df.groupby('colum name').aggreate(['mean',"min"])
#df.groupby('colum name').aggreate({'data1':np.min
#                                   'data2':np.mean})

#####
#function filter
#i want the groups which the mean of data2 in it <5 using fillter
#when using filter we should prebare the function i pass to it
'''
df=pd.DataFrame({'key':['A','B','C','A','B','C'],
                           "data1":[1,2,30,2,1,30],
                           "data2":[1,2,1,2,1,3],})
gf=df.groupby('key')
for (key,group) in gf:
    print("########")
    print(key)
    print(group)
    print("########")
def func(dataFrame):
    return dataFrame['data1'].mean()>5
dd=df.groupby('key').filter(func) #will remove the ggroup that make the func (group c)
print(dd)
'''
####
#normalizing:"طرح قيم العمود من متوسط العمود قبل العمل في الداتا"

#using fun transform with groupby :will change in data due to the function
#first we prebare the function
'''
def trans(dataFrame):
    return dataFrame-dataFrame.mean()
#we will make normalizing
df=pd.DataFrame({'key':['A','B','C','A','B','C'],
                           "data1":[0,1,2,3,4,5],
                           "data2":[5,0,3,3,7,9]})
gf=df.groupby('key')
for (key,group) in gf:
    print("########")
    print(key)
    print(group)
print("-----------------")
dd=df.groupby('key').transform(trans)
print(dd)
'''

#func apply with groupby:
'''
def applyy(dataFrame):
    dataFrame['data1']=dataFrame['data1']/dataFrame['data1'].sum()
    return dataFrame
df=pd.DataFrame({'key':['A','B','C','A','B','C'],
                           "data1":[0,1,2,3,4,5],
                           "data2":[5,0,3,3,7,9]})
gf=df.groupby('key')
for (key,group) in gf:
    print("########")
    print(key)
    print(group)
print("-----------------")
dd=df.groupby('key').apply(applyy)
print(dd)

'''
'''
rng=np.random.RandomState(0)
df=pd.DataFrame({'key':['A','B','C','A','B','C'],
                           "data1":range(6),
                           "data2":rng.randint(0,10,6)},
                            columns=['key','data1','data2'])
print(df)

'''

#note that:in apply function it resive dataFrame and make operation on it
#in transform function it resive column by column and make operation on it
'''
def applyy(dataFrame):
    return dataFrame/dataFrame.sum()
df=pd.DataFrame({'key':['A','B','C','A','B','C'],
                           "data1":[0,1,2,3,4,5],
                           "data2":[5,0,3,3,7,9]})
print("-----------------")
dd=df.groupby('key',group_keys=True).apply(applyy)
print(dd)


def trans(colum):
    return colum/colum.sum()
df=pd.DataFrame({'key':['A','B','C','A','B','C'],
                           "data1":[0,1,2,3,4,5],
                           "data2":[5,0,3,3,7,9]})
print("-----------------")
dd=df.groupby('key').transform(trans)
print(dd)
'''
#tit=sns.load_dataset('titanic')
'''
print(tit.head())
print("----------------------------------------")
print(tit['who'].value_counts())
print("----------------------------------------")
'''

#pivot function :to show data in groubed way
#pivot take four arrgumante
#index:will be the main column ||colums :the columns in the new table||values="column i make the operation on it like age,survivd"
# ||aggfunc :the function will apply in the column i chose
#will count how many person servive in diffrent calsses ::n=tit.pivot_table(index='sex',columns='class',values='survived',aggfunc='sum')
#will count the average of ages in diffrent classes ::n=tit.pivot_table(index='sex',columns='class',values='age',aggfunc='mean')
#we can entr many values :n=tit.pivot_table(index='sex',columns='class',values=['age','survived'],aggfunc='mean')
#"يمكن ان اخصص دالة معينة لكل قيمة من values" :n=tit.pivot_table(index='sex',columns='class',values=['age','survived'],aggfunc={'age':'mean','survived':'count'})

#i can add more than one index
#n=tit.pivot_table(index=['sex','who'],columns='class',values=['age','survived'],aggfunc={'age':'mean','survived':'count'})
#print(n)

###############(microsoft data time)
"""
df=pd.read_csv('Microsoft_Stock.csv')
print(df.head())
print("-------------------")
print(df.shape)
print("-------------------")
#we want to know first colum in data is date (data type )or no by using fun day_name()
#print(df.loc[0,'Date'].day_name()) #result= 'str' object has no attribute 'day_name' so it is not date time
#to convert the colum ['Date']to date time type
df["Date"]=pd.to_datetime(df["Date"], format='%m/%d/%Y %H:%M:%S')
#print(df['Date'])
#print(df.loc[0,'Date'].day_name()) #result is a day so it right
#to make new colum
#df['DayOfWeek']=df["Date"].dt.day_name() #we use dt when we deal with date un pandas

#to find max value in date
#print(df["Date"].max())
#to find min value in date
#print(df["Date"].min())
#finding the diffrence between them
#print(df["Date"].max() - df["Date"].min())
#making masking to find special data
print("-------------------")
k=df[(df['Date']>"2020")&(df['Date'] < "2021")]
#to make it easy to use dates in columns wiwth date we make the index of the column is the colum date
df=df.set_index('Date')
#print(df.loc['2020'])
#print(df.loc['2020-02':"2021-06"]) #using slicing after the Date become the index column
#we can make some operation
#print(df.loc['2020']['Close'].mean()) #"ايجلد المتوسط في عمود ما في سنة 2020"
#print(df.loc['2020']['Close'].plot()) #to draw the data of the year
#to apply function for weekly or monthly or in the year data we use resample
print(df['High'].resample("M").mean())
print(df['High'].resample("W").mean())
#if we want spacific function for spacific column we use:
#print(df.resample("M").agg({"Open":"mean","High":"max","Low":"std"}))
"""