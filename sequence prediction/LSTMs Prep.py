#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sklearn.model_selection as skcv
import random
import numpy as np
from ast import literal_eval
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten
from keras.regularizers import l2


# In[2]:


#This comes from stored data
l=[2,3,1,3,4,5,1,2,4,6,4,4,1,2,5,6]


# In[3]:


#To make groups of 4 and split leftover into hold to hold the elements and pred to make predictions
pred=l[-4:]
l=l[:-4]
m=len(l)%5
if m!=0:
    hold=l[-m:]
    l=l[:-m]


# In[4]:


l


# In[5]:


df_train=pd.read_csv("train_new.csv")


# In[6]:


# Enter new values into dataframe from l
c=0
for i in range(0,len(l),5):
    c+=1
    df_train = df_train.append({"Sequences":str(l[i:i+4]),"nint":l[i+4]},ignore_index=True)


# In[7]:


# Manipulation to make np arrays of list objects for training
df_train.loc[:,'Sequences'] = df_train.loc[:,'Sequences'].apply(literal_eval)
df_train


# In[8]:


# Reform the list l from the leftover elements and pred(prediction elements) 
l=hold+pred
l


# In[9]:


#Write back to csv file
df_train.to_csv('train_new.csv',index=False)


# In[10]:


df_train_X = df_train['Sequences'].values
df_train_y = df_train['nint'].values


# In[11]:


df_train_X


# In[12]:


df1=pd.DataFrame(columns=['pred'])
df1.loc[0]=[str(pred)]
df1.loc[:,'pred']=df1.loc[:,'pred'].apply(literal_eval)
df_test_X = df1['pred'].values


# In[13]:


df_train_X = pad_sequences(df_train_X, dtype='int')
df_test_X = pad_sequences(df_test_X, dtype='int')


# In[14]:


df_train_X_rshp = df_train_X.reshape(df_train_X.shape + (1,))
df_test_X_rshp = df_test_X.reshape(df_test_X.shape + (1,))
df_test_X_rshp.shape
input_shape = df_train_X_rshp[0].shape


# In[15]:


#Adding layers
model = Sequential()
model.add(LSTM(128, input_shape=input_shape, return_sequences=True, go_backwards=False,
               W_regularizer=l2(0.005), U_regularizer=l2(0.005),
               inner_init='glorot_normal', init='glorot_normal', activation='tanh'))  # try using a GRU instead, for fun
model.add( LSTM( 128, return_sequences=False))
model.add(Dense(1,activation='linear'))


# In[16]:


#Model training
model.compile(loss='mse', optimizer='rmsprop')
model.fit(df_train_X_rshp, df_train_y, batch_size=32, nb_epoch=5)


# In[17]:


#prediction
df_pred_y = model.predict(df_test_X_rshp)
print(int(np.round(df_pred_y)[0][0]))


# In[18]:


#preparing new inputs function
def prepareTest(pred):
    df1=pd.DataFrame(columns=['pred'])
    df1.loc[0]=[str(pred)]
    df1.loc[:,'pred']=df1.loc[:,'pred'].apply(literal_eval)
    df_test_X = df1['pred'].values
    df_test_X = pad_sequences(df_test_X, dtype='int')
    df_test_X_rshp = df_test_X.reshape(df_test_X.shape + (1,))


# In[19]:


# To incorporate new user_gestures for new predictions by shifting elemnts in pred list and make prediction. Also append new elemnts to l list
i=0
while True:
    print("-1 to exit")
    user_gesture = int(input())
    if user_gesture==-1:
        break
    l.append(user_gesture)
    for i in range(len(pred)-1):
        pred[i]=pred[i+1]
    pred[-1]=user_gesture
    prepareTest(pred)
    df_pred_y = model.predict(df_test_X_rshp)
    print(int(np.round(df_pred_y)[0][0]))
    


# In[20]:


l
# 2,4,6 added to the list which will be appended to the csv file through the process executed at the top of the file. Save this list l to database

