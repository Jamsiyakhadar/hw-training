#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


data=pd.read_csv(r"C:\Users\Althaf s hussain\Downloads\iowarealty_2024_08_05.csv")
data.head()


# In[4]:


data.columns


# In[5]:


data.info()


# In[7]:


data.shape


# In[11]:


data.describe()


# In[12]:


data.isnull().sum()


# In[13]:


data[data.isnull().any(axis=1)]


# In[16]:


data.duplicated().sum()


# In[17]:


duplicate_names = data[data.duplicated(subset='first_name', keep=False)]

# Step 2: Print rows with duplicate first names
print(duplicate_names)


# In[18]:


#Full name in First name column

full_name_rows = data[data['first_name'].str.split().str.len() > 1]

# Display these rows
print("Rows with full names in the 'first_name' column:")
print(full_name_rows[['first_name']])


# In[21]:


# Step 1: Find duplicate last names, excluding rows with null values
duplicate_names = data[data.duplicated(subset='last_name', keep=False) & ~data['last_name'].isna()]

# Step 2: Print rows with duplicate last names
print(duplicate_names)


# In[22]:


data['title'].value_counts()


# In[23]:


data['office_name'].value_counts()


# In[26]:


data['address'].value_counts()


# In[27]:


data['description'].value_counts()


# In[28]:


data['languages__001'].value_counts()


# In[29]:


data['languages__002'].value_counts()


# In[30]:


data['languages__003'].value_counts()


# In[31]:


data['languages__004'].value_counts()


# In[32]:


data['country'].value_counts()


# In[33]:


data['city'].value_counts()


# In[34]:


data['zipcode'].value_counts()


# In[35]:


data['state'].value_counts()


# In[38]:


data['agent_phone_numbers__-'].value_counts()


# In[40]:


data['email'].value_counts()


# In[56]:


import pandas as pd

def url_qa(data, column_name):
    results = {
        'Total URLs': data[column_name].count(),
        'Missing URLs': data[column_name].isnull().sum(),
        'Valid URLs': data[data[column_name].str.startswith(('http://', 'https://'), na=False)].shape[0],
        'Invalid URLs': data[~data[column_name].str.startswith(('http://', 'https://'), na=False) & data[column_name].notnull()].shape[0]
    }
    return results

# Assuming `data` is your DataFrame and 'website' is the column you're checking
website_results = url_qa(data, 'website')

# Printing out the results
print("\nWebsite Checking:")
for key, result_data in website_qa_results.items():
    print(f"\n{key}: {result_data}")

# If you want to display the rows with invalid URLs
invalid_urls = data[~data['website'].str.startswith(('http://', 'https://'), na=False) & data['website'].notnull()]
print("\nRows with Invalid URLs:")
print(invalid_urls.dropna(subset=['website']))


# In[73]:


data['website'].value_counts()


# In[63]:


# Function definition
def url_qa(data, column_name):
    results = {
        'Total URLs': data[column_name].count(),
        'Missing URLs': data[column_name].isnull().sum(),
        'Valid URLs': data[data[column_name].str.startswith(('http://', 'https://'), na=False)].shape[0],
        'Invalid URLs': data[~data[column_name].str.startswith(('http://', 'https://'), na=False) & data[column_name].notnull()].shape[0]
    }
    return results

# Apply the function to the 'social__facebook_url' column
facebook_results = url_qa(data, 'social__facebook_url')

# Print out the QA results for the Facebook URLs
print("\nfacebook_url_checking:")
for key, result_data in facebook_results.items():
    print(f"{key}: {result_data}")

# To show rows with invalid or missing Facebook URLs
invalid_facebook_urls = data[~data['social__facebook_url'].str.startswith(('http://', 'https://'), na=False) & data['social__facebook_url'].notnull()]
print("\nRows with Invalid Facebook URLs:")
print(invalid_facebook_urls.dropna(subset=['social__facebook_url']))


# In[74]:


data['social__facebook_url'].value_counts()


# In[65]:


# Function to check the URLs in a column
def url_qa(data, column_name):
    results = {
        'Total URLs': data[column_name].count(),
        'Missing URLs': data[column_name].isnull().sum(),
        'Valid URLs': data[data[column_name].str.startswith(('http://', 'https://'), na=False)].shape[0],
        'Invalid URLs': data[~data[column_name].str.startswith(('http://', 'https://'), na=False) & data[column_name].notnull()].shape[0]
    }
    return results

# Apply the function to the 'social__twitter_url' column
twitter_url_qa_results = url_qa(data, 'social__twitter_url')

# Print out the QA results for Twitter URLs
print("\ntwitter_url_qa_results QA Results:")
for key, result_data in twitter_url_qa_results.items():
    print(f"{key}: {result_data}")

# To show rows with invalid or missing Twitter URLs
invalid_twitter_urls = data[~data['social__twitter_url'].str.startswith(('http://', 'https://'), na=False) & data['social__twitter_url'].notnull()]
print("\nRows with Invalid Twitter URLs:")
print(invalid_twitter_urls.dropna(subset=['social__twitter_url']))


# In[76]:


data['social__twitter_url'].value_counts()


# In[68]:


# Function to check the URLs in a column
def url_qa(df, column_name):
    results = {
        'Total URLs': data[column_name].count(),
        'Missing URLs': data[column_name].isnull().sum(),
        'Valid URLs': data[data[column_name].str.startswith(('http://', 'https://'), na=False)].shape[0],
        'Invalid URLs': data[~data[column_name].str.startswith(('http://', 'https://'), na=False) & data[column_name].notnull()].shape[0]
    }
    return results

# Apply the function to the 'social__linkedin_url' column
linkedin_url_qa_results = url_qa(data, 'social__linkedin_url')

# Print out the QA results for LinkedIn URLs
print("\nlinkedin_url_qa_results QA Results:")
for key, result_data in linkedin_url_qa_results.items():
    print(f"{key}: {result_data}")

# To show rows with invalid LinkedIn URLs
invalid_linkedin_urls = data[~data['social__linkedin_url'].str.startswith(('http://', 'https://'), na=False) & data['social__linkedin_url'].notnull()]
print("\nRows with Invalid LinkedIn URLs:")
print(invalid_linkedin_urls.dropna(subset=['social__linkedin_url']))


# In[77]:


data['social__linkedin_url'].value_counts()


# In[69]:


# Function to check the URLs in a column
def url_qa(df, column_name):
    results = {
        'Total URLs': data[column_name].count(),
        'Missing URLs': data[column_name].isnull().sum(),
        'Valid URLs': data[data[column_name].str.startswith(('http://', 'https://'), na=False)].shape[0],
        'Invalid URLs': data[~data[column_name].str.startswith(('http://', 'https://'), na=False) & data[column_name].notnull()].shape[0]
    }
    return results

# Apply the function to the 'social__other_urls__001' column
twitter_url_qa_results = url_qa(data, 'social__other_urls__001')

# Print out the QA results for the 'social__other_urls__001' column
print("\ntwitter_url_qa_results QA Results:")
for key, result_df in twitter_url_qa_results.items():
    print(f"{key}: {result_df}")

# To show rows with invalid or missing URLs in 'social__other_urls__001'
invalid_urls = data[~data['social__other_urls__001'].str.startswith(('http://', 'https://'), na=False) & data['social__other_urls__001'].notnull()]
print("\nRows with Invalid URLs:")
print(invalid_urls.dropna(subset=['social__other_urls__001']))


# In[78]:


data['social__other_urls__001'].value_counts()


# In[70]:


def url_qa(df, column_name):
    results = {
        'Total URLs': data[column_name].count(),
        'Missing URLs': data[column_name].isnull().sum(),
        'Valid URLs': data[data[column_name].str.startswith(('http://', 'https://'), na=False)].shape[0],
        'Invalid URLs': data[~data[column_name].str.startswith(('http://', 'https://'), na=False) & data[column_name].notnull()].shape[0]
    }
    return results

# Apply the function to the 'social__other_urls__001' column
twitter_url_qa_results = url_qa(data, 'social__other_urls__002')

# Print out the QA results for the 'social__other_urls__001' column
print("\ntwitter_url_qa_results QA Results:")
for key, result_df in twitter_url_qa_results.items():
    print(f"{key}: {result_df}")

# To show rows with invalid or missing URLs in 'social__other_urls__001'
invalid_urls = data[~data['social__other_urls__002'].str.startswith(('http://', 'https://'), na=False) & data['social__other_urls__002'].notnull()]
print("\nRows with Invalid URLs:")
print(invalid_urls.dropna(subset=['social__other_urls__002']))


# In[79]:


data['social__other_urls__002'].value_counts()


# In[ ]:




