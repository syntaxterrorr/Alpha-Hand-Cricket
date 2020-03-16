#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sklearn.model_selection as skcv
import random
import numpy as np

from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten
from keras.regularizers import l2


# In[2]:


#Currently took data from a list and made a csv file
l=[2,4,1,6,1,2,1,1,6,5,4,2,1,5,2,2,3,2,4,6,5,1,1,3,4,1,2,5,6,2,1,4,2,3,1,4,2,5,4,2,1,6,4,2,5,4,4,1,2,5,6]
# hold=[4, 4]
# pred=[1, 2, 5, 6]


# In[3]:


#To make batches of 4 for training purposes
pred=l[-4:]
l=l[:-4]
m=len(l)%5
if m!=0:
    hold=l[-m:]
    l=l[:-m]


# In[4]:


#Temp
col_names =  ['Sequences']
df_train = pd.DataFrame(columns = col_names)
for i in range(0,len(l),5):
    df_train = df_train.append({"Sequences":l[i:i+5]},ignore_index=True)


# In[5]:


# df_train=pd.read_csv("train_new.csv")


# In[6]:


# for i in range(0,len(l),5):
#     df_train = df_train.append({"Sequences":l[i:i+4],"nint":l[i+5]},ignore_index=True)


# In[7]:


df_train


# In[8]:


l=hold+pred
l


# In[9]:


# data_train = pd.read_csv("train1.csv")


# In[10]:


# def create_vector(line):
#     return line.split(",")


# In[11]:


# data_train['vector'] = data_train["Sequence"].apply(create_vector)
# data_train


# In[12]:


def get_last(x):
    return x.pop()


# In[13]:


df_train['nint'] = df_train["Sequences"].apply(get_last)


# In[14]:


df_train
df_train.to_csv('train_new.csv')


# In[15]:


# df_train_X = df_train['Sequences'].values
# df_train_y = df_train['nint'].values
# df_test_X = np.asarray(pred,dtype=object)


# In[16]:


# df_test_X


# In[17]:


# df_train_X = pad_sequences(df_train_X, dtype='int')
# df_test_X = pad_sequences(df_test_X, dtype='int')


# In[18]:


# df_train_X_rshp = df_train_X.reshape(df_train_X.shape + (1,))
# df_test_X_rshp = df_test_X.reshape(df_test_X.shape + (1,))
# df_test_X_rshp.shape
# input_shape = df_train_X_rshp[0].shape


# In[19]:


# model = Sequential()
# model.add(LSTM(128, input_shape=input_shape, return_sequences=True, go_backwards=False,
#                W_regularizer=l2(0.005), U_regularizer=l2(0.005),
#                inner_init='glorot_normal', init='glorot_normal', activation='tanh'))  # try using a GRU instead, for fun
# model.add( LSTM( 128, return_sequences=False))
# model.add(Dense(1,activation='linear'))


# In[20]:


# model.compile(loss='mse', optimizer='rmsprop')
# model.fit(df_train_X_rshp, df_train_y, batch_size=32, nb_epoch=5)


# In[21]:


# df_pred_y = model.predict(df_test_X_rshp)
# df_pred_y


# In[22]:


#To incorporate new user_gestures for new predictions

# i=0
# while True:
#     print("1 to exit")
#     if i==0:
#         break
#     user_gesture = int(input())
#     l.append(user_gesture)
#     for i in range(len(pred)-1):
#         pred[i]=pred[i+1]
#     pred[-1]=user_gesture
#     df_test_X = np.asarray(pred)
#     df_test_X = pad_sequences(df_test_X, dtype='int')
#     df_test_X_rshp = df_test_X.reshape(df_test_X.shape + (1,))
#     df_pred_y = model.predict(df_test_X_rshp)


# In[23]:


X_train, X_test, y_train, y_test = skcv.train_test_split(df_train['Sequences'].values, df_train['nint'].values, test_size=.3)


# In[24]:


X_train = pad_sequences(X_train, dtype='int')
X_test = pad_sequences(X_test, dtype='int')


# In[25]:


X_train
pd.DataFrame(X_test)


# In[26]:


X_train_rshp = X_train.reshape(X_train.shape + (1,))
X_test_rshp = X_test.reshape(X_test.shape + (1,))
X_train_rshp.shape
input_shape = X_train_rshp[0].shape


# In[27]:


model = Sequential()
model.add(LSTM(128, input_shape=input_shape, return_sequences=False, go_backwards=False,
               W_regularizer=l2(0.005), U_regularizer=l2(0.005),
               inner_init='glorot_normal', init='glorot_normal', activation='tanh'))
model.add(Dense(1,activation='linear'))


# In[28]:


model.compile(loss='mse', optimizer='rmsprop')
model.fit(X_train_rshp, y_train, batch_size=32, nb_epoch=5)


# In[29]:


y_pred = model.predict(X_test_rshp)
print(y_test)
print()
print(np.round(y_pred))

