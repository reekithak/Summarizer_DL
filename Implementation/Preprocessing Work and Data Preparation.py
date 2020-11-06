#!/usr/bin/env python
# coding: utf-8

# **WORK_WORD_PROCESSING**

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("D:\working repos\seminar__\Implementation\Data_training\Final_data\working1.csv")


# In[3]:


try:
    df.drop(['Unnamed: 0'],axis=1,inplace=True)
except:
    pass


# In[4]:


df


#  

#  

# **Preprocessing and Cleaning**

# In[5]:


import warnings
warnings.filterwarnings("ignore")


# In[64]:


#stopwords
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('english')

#stemming
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
import nltk 
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

#lemmatizing
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

def word_lemmatizer(text):
    lem_text = WordNetLemmatizer().lemmatize(text)
    return lem_text

def remove_url(text):
    import re
    rm_txt = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    rm_txt = rm_txt.replace("\n"," ")
    rm_txt = rm_txt.replace('\'s'," ")
    return rm_txt


def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def deEmojify(text):
    import re
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


# In[65]:


new_lis = []
for sent in df['Text'].tolist():
    new_lis.append(word_lemmatizer(str(sent)))


# In[66]:


new_lis = [remove_url(text) for text in new_lis]
new_lis = [remove_html_tags(text) for text in new_lis]
new_lis = [deEmojify(text) for text in new_lis]
new_lis = [text.lower() for text in new_lis]


# In[67]:


new_lis1 = []
for sent in df['Summary'].tolist():
    new_lis1.append(word_lemmatizer(str(sent)))
new_lis1 = [remove_url(text) for text in new_lis1]
new_lis1 = [remove_html_tags(text) for text in new_lis1]
new_lis1 = [deEmojify(text) for text in new_lis1]
new_lis1 = [text.lower() for text in new_lis1]


# In[68]:


data = pd.DataFrame()
data['Text'] = new_lis
data['Summary'] = new_lis1


# In[69]:


data['Summary'][1]


# In[70]:


#data.to_csv("D:\working repos\seminar__\Implementation\Data_training\Final_data\clean_data.csv")

