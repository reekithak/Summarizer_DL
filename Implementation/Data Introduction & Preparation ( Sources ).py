#!/usr/bin/env python
# coding: utf-8

# **Data -1**

# In[1]:


#Articles
art_dict = dict({
'business' : r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\BBC News Summary\News Articles\business"
,'ent' : r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\BBC News Summary\News Articles\entertainment"
,'pol' : r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\BBC News Summary\News Articles\politics"
,'sport' : r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\BBC News Summary\News Articles\sport"
,'tech' : r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\BBC News Summary\News Articles\tech"})

#Sumamries
sum_dict = dict({'business_summ' : r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\BBC News Summary\Summaries\business"
,'ent_summ' : r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\BBC News Summary\Summaries\entertainment"
,'pol_summ' :r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\BBC News Summary\Summaries\politics"
,'sport_summ' : r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\BBC News Summary\Summaries\sport"
,'tech_summ' : r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\BBC News Summary\Summaries\tech"}
)


# In[2]:


art_ = list(art_dict.keys())
sum_ = list(sum_dict.keys())


# In[3]:


import os
import pandas as pd
import numpy as np


# In[4]:


art_data = []
for key in art_:
    print(key)
    file_list = os.listdir(art_dict[key])
    for file in file_list:
        #print(file)
        f1 = open(art_dict[key]+"\\"+file,"r")
        art_data.append(f1.readlines())
sum_data = []
for key in sum_:
    print(key)
    file_list = os.listdir(sum_dict[key])
    for file in file_list:
        #print(file)
        f1 = open(sum_dict[key]+"\\"+file,"r")
        sum_data.append(f1.readlines())


# In[5]:


tad = []
for i in art_data:
    tad.append(' '.join(sent for sent in i))


# In[6]:


sad = []
for i in sum_data:
    sad.append(i[0])


# In[7]:


len(art_data),len(sum_data)
D1_df = pd.DataFrame()
D1_df['Text'] = tad
D1_df['Summary'] = sad


# In[8]:


#D1_df


#  

#  

#  

# **Data -2**

# In[9]:


t_df1 = pd.read_csv(r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\news_summary.csv",encoding='latin-1')
t_df2 = pd.read_csv(r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\news_summary_more.csv",encoding='latin-1')


# In[10]:


D2_df = pd.DataFrame()


# In[11]:


D2_df['Text'] = t_df1['ctext'].tolist()
D2_df['Summary'] = t_df1['text'].tolist()


# In[12]:


tm = pd.DataFrame()

tm['Text'] = t_df2['text'].tolist()
tm['Summary'] = t_df2['headlines'].tolist()


# In[13]:


D2_df = pd.concat([D2_df,tm])


# In[14]:


#D2_df


# In[15]:


Final_df = pd.concat([D1_df,D2_df])


# In[17]:


#Final_df


# In[18]:


#Final_df.to_csv(r"C:\Users\Akhil Sanker\Desktop\seminar__\Implementation\Data_training\Final_data\working1.csv")

