#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


# Uploading movies and reviews data sets.
movies_df = pd.read_csv('/Users/sophiaweidner/Downloads/ml-latest-small/movies.csv')
ratings_df = pd.read_csv('/Users/sophiaweidner/Downloads/ml-latest-small/ratings.csv')


# In[4]:


movies_df.head()


# In[5]:


ratings_df.head()


# In[6]:


# Joining both data frames together.
df = ratings_df.merge(movies_df,on='movieId', how='left')


# In[7]:


df.head()


# In[8]:


# Finding average ratings for each movie
avg_ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
avg_ratings.head(10)


# In[9]:


# Finding total amount of rates for each movie / how many times a movie was rated. Adding as a column.
avg_ratings['Total Ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
avg_ratings.head(10)


# ### Building the Recommender

# In[10]:


# Using DF to create a new table where the rows are the UserIDs and the columns are the movies.
df_new = df.pivot_table(index='userId',columns='title',values='rating')
df_new.head()


# In[11]:


# Selecting a movie to check Recommender system. I am choosing Aladdin (1992).
# Using corrwth to determine correlation between movies.
correlations = df_new.corrwith(df_new['Aladdin (1992)'])
correlations.head()


# In[12]:


# Removing NaN values and merging total ratings to the new correlations table created above.
recommend = pd.DataFrame(correlations,columns=['Correlation'])
recommend.dropna(inplace=True)
recommend = recommend.join(avg_ratings['Total Ratings'])
recommend.head()


# In[13]:


# Filtering movies with a correlation value to Aladdin (1992) and with at least 100 ratings.
recc = recommend[recommend['Total Ratings']>100].sort_values('Correlation',ascending=False).reset_index()


# In[14]:


# Merging movies dataset for verifying the recommendations.
recc = recc.merge(movies_df,on='title', how='left')
recc.head(10) # Top 10 suggestions


# https://analyticsindiamag.com/how-to-build-your-first-recommender-system-using-python-movielens-dataset/
# 
# Used this article as a step by step to build this recommender system.

# # User Input

# In[16]:


# Creating a loop that allows users to enter multiple movies.
while True:
    entrance = input("Would you like to look up movie ratings? Enter 'Y' to continue or any key to exit: ")
    # The loop will run if the user inputs 'Y' and accepts lowercase y as well. Anything else breaks the loop.
    if entrance.upper() == 'Y':
        # Movie input.
        input_movie = input("Please enter which movie you would like the ratings for. Be sure to enter the year: ")
        # If the movie is in the set, it will generate a list. If it is not, it will prompt a user to input another movie.
        if input_movie in movies_df['title'].tolist():
            # Used previous code but created a new data frame with it.
            correlations1 = df_new.corrwith(df_new[input_movie])
            recommend1 = pd.DataFrame(correlations1,columns=['Correlation'])
            recommend1.dropna(inplace=True)
            recommend1 = recommend1.join(avg_ratings['Total Ratings'])
            recc1 = recommend1[recommend1['Total Ratings']>100].sort_values('Correlation',ascending=False).reset_index()
            recc1 = recc1.merge(movies_df,on='title', how='left')
            print(recc1.head(10))
        else:
            print("That movie is not in the dataset. Please try again.")
    else:
        print("Thank you for using the Movie Recommender System!")
        break


# In[ ]:




