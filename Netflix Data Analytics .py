#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the data set
import pandas as pd
data=pd.read_csv(r"C:\Users\AKE\Desktop\dataman\pythonproj\file.csv")


# In[2]:


data


# ### Getting some basic information about the dataset 

# ### 1. head()

# In[3]:


data.head() # to show top 5 records


# ### 2. tail()

# In[4]:


data.tail()   # to show bootom 5 records


# ### 3. shape

# In[5]:


data.shape # to show the number of rows and columns


# ### 4. Size

# In[6]:


data.size # to show Number of total values(elements)


# ### 5. Columns

# In[7]:


data.columns #to show each column name


# ### 6. dtypes

# In[8]:


data.dtypes   #to show the data type of each column


# ### 7. info()

# In[9]:


data.info() #to show indexs, columns, data-types of each column, memory at once


# ### Task 1. Is there any duplicate records in this dataset? if yes, then remove the duplicate records

# #### duplicate()

# In[10]:


data.head()


# In[11]:


data.shape


# In[58]:


data.duplicated()


# In[12]:


data[data.duplicated()] # to check row wise and detect the duplicate rows


# In[13]:


data.drop_duplicates() # to remove the duplicate rows 


# In[60]:


data.drop_duplicates(inplace = True)    #to remove duplicated rows permanently


# In[61]:


data[data.duplicated()]


# #### there is no duplicates because it removed permanently

# In[14]:


data.shape


# ### Task 2. Is there any Null Value present in any column? Show with Heat-map 

# ### Isnull()

# In[15]:


data.head()


# In[16]:


data.isnull() #to show where is Null value is present


# In[17]:


data.isnull().sum() #to show the count of Null values in each column


# #### seaborn library(heat-map)

# In[18]:


import seaborn as sns #to import seaborn library


# In[19]:


sns.heatmap(data.isnull()) #using heat-map to show  null values count


# ### Q.1. For 'House of Cards',what is the show Id and who is the director of this show?

# #### isin()

# In[20]:


data.head()


# In[21]:


data[data ['Title'].isin(['House of Cards'])] #To show all records of a particular item in any column


# #### str.contains()

# In[22]:


data[data ['Title'].str.contains('House of Cards')]


# ### Q.2. in which year highest number of the TV Shows & Movies were released?show with Bar Graph

# #### dtypes

# In[23]:


data.dtypes


# #### to_datetime

# In[33]:


data['Date_N']=pd.to_datetime(data['Release_Date'])


# In[25]:


data.head()


# In[26]:


data.dtypes


# #### dt.year.value_counts()

# In[27]:


data['Date_N'].dt.year.value_counts() # it counts all occurance of all individual years in Date column


# In[31]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# ### Q.3. How many TV Shows & Movies are in the dataset?show with Bar Graph

# #### groupby()

# In[34]:


data.head(2)


# In[79]:


data.groupby('Category').Category.count() #to show the count of all unique items of a column and show their count


# #### countplot()

# In[19]:


#sns.countplot(data['Category'])          #to show the count of all unique of any column in the form of bar graph


# ### Q.4. Show all the Movies that were released in year 2000

# #### Creating new column

# In[29]:


data.head(2)


# In[35]:


data['Year']=data['Date_N'].dt.year #to create a new year column it will consider only year  


# In[36]:


data.head(2)


# ### Filitering 

# In[37]:


data[(data['Category']=='Movie')& (data['Year']==2000.0)]


# In[84]:


data.head(2)


# In[38]:


data[(data['Category']=='Movie') & (data['Year']==2020.0)]


# ### Q.5. Show only title ofall tv shows that were released in india

# In[39]:


data.head()


# In[40]:


data[(data['Category']=='TV Show') & (data['Country']=='India')]['Title']


# In[79]:


data[(data['Category']=='TV Show') & (data['Country']=='India')]['Title']


# ### Q.6. Show Top 10 directors, who gave the highest number of TV Shows & Movies to Netflix

# In[41]:


data['Director'].value_counts().head(10)


# In[42]:


data.head(5)


# ### Q.7. Show all the records, whereCategory is movie & type is commedies or country is uk 

# In[43]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies')| (data['Country']=='United Kingdom')]


# ### Q.8.In how many movies/shows, Tom Cruise was cast? 

# In[44]:


data.head()


# In[46]:


data[data['Cast']=='Tom Cruise']


# In[48]:


data[data['Cast'].str.contains('Tom Cruise')]


# In[52]:


data_new=data.dropna()


# In[54]:


data_new.head(2)


# In[55]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# ### Q.9. What are the different Ratings defined by Netflix?

# #### nunique()

# In[56]:


data_new.head(2)


# In[57]:


data['Rating'].nunique()


# In[58]:


data_new['Rating'].nunique()


# In[60]:


data_new['Rating'].unique()


# #### How many Movies got the 'TV-14' rating in canada?

# In[62]:


data_new.head(2)


# In[73]:


#data[data['Category']=='Movies'] 
data_new[(data_new['Rating']=='TV-14')&(data_new['Country']=='Canada')] 


# In[74]:


data_new[(data_new['Rating']=='TV-14')&(data_new['Country']=='Canada')].shape 


# #### How many TV show got the 'R' rating, after year 2018?

# In[75]:


data_new.head(2)


# In[83]:


data[(data['Category']=='Tv Show')&(data['Rating']=='R')& (data['Year']> 2018)]


# In[84]:


data[(data['Category']=='TV Show') &(data['Rating']=='R') & (data['Year']> 2018)]


# #### Q.10 What is maximum duration of Movie/TV Shows in NetFlix?

# In[85]:


data.Duration.unique()


# In[86]:


data.Duration.dtypes


# #### str.split()

# In[88]:


data.head(2)


# In[90]:


data[['Minutes','Unit']]=data['Duration'].str.split(' ', expand=True)


# In[91]:


data.head(2)


# In[92]:


data['Minutes'].max()


# In[93]:


data['Minutes'].min()


# In[94]:


data['Minutes'].mean() #inf infinite because this all are in the form of object


# In[96]:


data.dtypes


# #### Q.11. Which individual country has the highst No. of TV Shows?

# In[97]:


data.head(2)


# In[99]:


data_tvshow= data[data['Category'] == 'TV Show']


# In[101]:


data_tvshow.head(2)


# In[103]:


data_tvshow.Country.value_counts()


# In[104]:


data_tvshow.Country.value_counts().head(1)


# #### Q.12. How Can we sort the data set by year?

# In[105]:


data.head(2)


# In[112]:


data.sort_values(by='Year').head(2)


# In[113]:


data.sort_values(by='Year',ascending=False).head(2)


# #### Q.13. Find all the instances where:
#  Category is 'Movie' and Type is 'Dramas'
#     or  Category is 'TV Show' and Type is 'Kids TV'

# In[115]:


data.head(2)


# In[118]:


data[(data['Category']=='Movie') & (data['Type']=='Dramas')].head(2)


# In[121]:


data[(data['Category']=='TV Show') & (data['Type']=="Kids' TV")].head(2)


# In[123]:


data[(data['Category']=='Movie') & (data['Type']=='Dramas') | (data['Category']=='TV Show') & (data['Type']=="Kids' TV")]


# ##### The End

# #### Real World Project   
#     By Aklilu Abera

# In[ ]:




