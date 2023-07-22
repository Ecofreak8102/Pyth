import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Reading Data

## No of people killed by road accidents
"""

kills_df = pd.read_csv('Road_Accidents_2017-Annuxure_Tables_3_newww.csv')
kills_df

"""## No of people injured due to road accidents"""

injuries_df = pd.read_csv('Road_Accidents_2017-Annuxure_Tables_4_newww.csv')
injuries_df

"""Removing unnecessary columns"""

kills_df = kills_df.drop(columns = ['Share of States/UTs in Total Number of Persons Killed in Road Accidents - 2014',
       'Share of States/UTs in Total Number of Persons Killed in Road Accidents - 2015',
       'Share of States/UTs in Total Number of Persons Killed in Road Accidents - 2016',
       'Share of States/UTs in Total Number of Persons Killed in Road Accidents - 2017',
       'Total Number of Persons Killed in Road Accidents Per Lakh Population - 2014',
       'Total Number of Persons Killed in Road Accidents Per Lakh Population - 2015',
       'Total Number of Persons Killed in Road Accidents Per Lakh Population - 2016',
       'Total Number of Persons Killed in Road Accidents Per Lakh Population - 2017',
       'Total Number of Persons Killed in Road Accidents per 10,000 Vehicles - 2014',
       'Total Number of Persons Killed in Road Accidents per 10,000 Vehicles - 2015',
       'Total Number of Persons Killed in Road Accidents per 10,000 Vehicles - 2016',
       'Total Number of Persons Killed in Road Accidents per 10,000 Km of Roads - 2014',
       'Total Number of Persons Killed in Road Accidents per 10,000 Km of Roads - 2015',
       'Total Number of Persons Killed in Road Accidents per 10,000 Km of Roads - 2016'])
kills_df

injuries_df = injuries_df.drop(columns = ['Share of States/UTs in Total Number of Persons Injured in Road Accidents - 2014',
       'Share of States/UTs in Total Number of Persons Injured in Road Accidents - 2015',
       'Share of States/UTs in Total Number of Persons Injured in Road Accidents - 2016',
       'Share of States/UTs in Total Number of Persons Injured in Road Accidents - 2017',
       'Total Number of Persons Injured in Road Accidents Per Lakh Population - 2014',
       'Total Number of Persons Injured in Road Accidents Per Lakh Population - 2015',
       'Total Number of Persons Injured in Road Accidents Per Lakh Population - 2016',
       'Total Number of Persons Injured in Road Accidents Per Lakh Population - 2017',
       'Total Number of Persons injured in Road Accidents per 10,000 Vehicles - 2014',
       'Total Number of Persons injured in Road Accidents per 10,000 Vehicles - 2015',
       'Total Number of Persons injured in Road Accidents per 10,000 Vehicles - 2016',
       'Total Number of Persons injured in Road Accidents per 10,000 Km of Roads - 2014',
       'Total Number of Persons injured in Road Accidents per 10,000 Km of Roads - 2015',
       'Total Number of Persons injured in Road Accidents per 10,000 Km of Roads - 2016'])
injuries_df

"""Data Organization"""

north_india=['Jammu and Kashmir','Punjab','Himachal Pradesh','Uttarakhand','Delhi','Chandigarh','Haryana','Uttar Pradesh','Jammu & Kashmir']
east_india = ['Bihar', 'Odisha', 'Jharkhand', 'West Bengal', 'Orissa']
south_india = ['Andhra Pradesh', 'Karnataka', 'Kerala' ,'Tamil Nadu', 'Telangana']
west_india = ['Rajasthan' , 'Gujarat', 'Goa','Maharashtra','Goa']
central_india = ['Madhya Pradesh', 'Chhattisgarh']
north_east_india = ['Assam', 'Sikkim', 'Nagaland', 'Meghalaya', 'Manipur', 'Mizoram', 'Tripura', 'Arunachal Pradesh']
ut_india = ['Andaman and Nicobar Islands', 'Dadra and Nagar Haveli', 'Puducherry', 'Andaman & Nicobar Islands', 'Dadra & Nagar Haveli', 'Daman & Diu', 'Lakshadweep', 'A & N Islands', 'D & N Haveli']

def get_zonal_names (row):
  if row['States/UTs'].strip() in north_india:
    val = 'North_Zone'
  elif row['States/UTs'].strip() in south_india:
    val = 'South_Zone'
  elif row['States/UTs'].strip() in east_india:
    val = 'East_Zone'
  elif row['States/UTs'].strip() in west_india:
    val = 'West_Zone'
  elif row['States/UTs'].strip() in central_india:
    val = 'Central_Zone'
  elif row['States/UTs'].strip() in north_east_india:
    val = 'NE_Zone'
  elif row['States/UTs'].strip() in ut_india:
    val = 'Union Terr'
  else:
     val = 'No Value'
  return val

kills_df['Zones'] = kills_df.apply(get_zonal_names, axis=1)
kills_df

injuries_df['Zones'] = injuries_df.apply(get_zonal_names, axis=1)
injuries_df

s=kills_df.groupby('Zones')
ag=s.mean()
ag_df=pd.DataFrame(ag)
ag_df['Zones'] = ['Central_Zone','East_Zone','NE_Zone','North_Zone','South_Zone','Union Terr','West_Zone']
ag_df


m=[]
k=ag_df["2014"]
for i in k:
  m.append(i)
print(m)


p=[]
k=ag_df["2015"]
for i in k:
  p.append(i)
print(p)


o=[]
k=ag_df["2016"]
for i in k:
  o.append(i)
print(o)

z=[]
k=ag_df["2017"]
for i in k:
  z.append(i)
print(z)

x=ag_df["Zones"]
k=[]
for i in x:
  k.append(i)
print(k)
plt.plot(x,m,x,p,x,o,x,z)
plt.gcf().set_size_inches(15,15)
plt.xticks(rotation=90)
plt.show()

#PIE CHART
a=input("Enter the year:")
x=np.array([kills_df[a]])
y= kills_df['States/UTs']
fig = plt.figure(figsize =(15,20))
plt.pie(x,labels = y,labeldistance=1,
              rotatelabels =True, startangle=180,counterclock= False)
plt.title(a,fontsize=28)
plt.legend(title='states', bbox_to_anchor=(1.2,1), loc="upper left")
plt.show()

#PIE CHART
a=input("Enter the year:")
x=np.array([injuries_df[a]])
y= kills_df['States/UTs']
fig = plt.figure(figsize =(15,20))
plt.pie(x,labels = y,labeldistance=1,
              rotatelabels =True, startangle=180,counterclock=False)
plt.title(a,fontsize=28)
plt.legend(title='states', bbox_to_anchor=(1.2,1), loc="upper left")
plt.show()

a=input("Enter the year:")
x=kills_df['States/UTs']
y=kills_df[a]
plt.plot(x,y,linewidth =5)
plt.gcf().set_size_inches(13,13)
plt.xticks(rotation=90)
plt.title(a,fontsize=28)
plt.show()

a=input("Enter the year:")
x=injuries_df['States/UTs']
y=injuries_df[a]
plt.plot(x,y,linewidth =1)
plt.gcf().set_size_inches(12,12)
plt.xticks(rotation=90)
plt.title(a,fontsize=28)
plt.show()

m=[]
k=kills_df["2014"]
for i in k:
  m.append(i)
print(m)


p=[]
k=kills_df["2015"]
for i in k:
  p.append(i)
print(p)


o=[]
k=kills_df["2016"]
for i in k:
  o.append(i)
print(o)

z=[]
k=kills_df["2017"]
for i in k:
  z.append(i)
print(z)

x=kills_df["States/UTs"]
k=[]
for i in x:
  k.append(i)
print(k)
plt.plot(x,m,x,p,x,o,x,z)
plt.gcf().set_size_inches(15,15)
plt.xticks(rotation=90)
plt.show()
