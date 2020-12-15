#!/usr/bin/env python
# coding: utf-8

# # Getting All Labels

# In[1]:


import pandas as pd
import numpy as np
import math


# In[2]:


debug_flag = True


# In[3]:


def calculate_top_k_score(predicted_list,actual_list,top_k):
    predicted_list_local = None
    final_score_value = 0
    iteration = min(top_k,len(predicted_list))
    for index in range(iteration):
        lcl_value = predicted_list[index]
        if lcl_value in actual_list:
            final_score_value = final_score_value + 1
    
    if debug_flag and final_score_value>0:
        print("")
        print(final_score_value)
        print("")

    return final_score_value


# In[4]:


def calculate_top_k_score_dcn(predicted_list,actual_list,top_k):
    
    predicted_list_local = None
    final_score_value = 0
    
    iteration = top_k
    
    for index in range(iteration):
        
        if len(predicted_list) <= index:
            break
            
        lcl_value = predicted_list[index]
        if lcl_value in actual_list:
            final_score_value = final_score_value + (1/np.log2(index +1 + 1))
    
    return final_score_value


# In[5]:


def calculate_top_k_score_i_dcn(predicted_list,actual_list,top_k):
    
    predicted_list_local = None
    final_score_value = 0
    iteration = min(top_k,len(predicted_list))
    
    for index in range(iteration):
        lcl_value = predicted_list[index]
        
#         if lcl_value in actual_list:
        final_score_value = final_score_value + (1 / np.log2(index + 1 +1))
    
    return final_score_value


# In[6]:


def read_file_and_get_details(predicted_label_name,actual_label_name):
    df_predicted_labels = pd.read_csv(predicted_label_name, sep="\n",header=None)
    df_actual_labels = pd.read_csv(actual_label_name, sep="\n",header=None)
    return df_predicted_labels,df_actual_labels


# In[7]:


top = 3


# # Get Details 

# In[8]:


# predicted = "EUR-Lex_labels_1024"
# actual = "EUR-Lex_test_labels.txt"

dataset = "Amazon-670K"
predicted = "./results/{}_labels"
actual = "./data/{}/test_labels.txt"


# In[9]:


df_predicted_labels,df_actual_labels = read_file_and_get_details(predicted,actual)
print(df_predicted_labels[0].shape)
print(df_actual_labels[0].shape)


# # Set the K 

# In[10]:


k = 50


# # Calculate Precision ![image.png](attachment:image.png)

# In[11]:


def evaluate_score(df_predicted_labels,df_actual_labels,top_k):
    
    final_shape = min(df_predicted_labels[0].shape[0],df_actual_labels[0].shape[0])
#     print(final_shape)
    
    get_score = 0

    for iteration in range(final_shape):
        
        # get Predicted Label
        predicted_label = df_predicted_labels[0][iteration]
        predicted_label_list = predicted_label.split(' ')
        
        # get Actual Label 
        actual_label = df_actual_labels[0][iteration]
        actual_label_list = actual_label.split(' ')
#         if iteration>1000:
#             break
        get_score = get_score +         calculate_top_k_score(predicted_label_list,actual_label_list,top_k) 
    
    return get_score


# In[12]:


def evaluate_precision(df_predicted_labels,df_actual_labels,top_k):

    final_shape = min(df_predicted_labels[0].shape[0],df_actual_labels[0].shape[0])
#     print(final_shape)
    
    get_score = evaluate_score(df_predicted_labels,df_actual_labels,top_k)
        
    final_score = (get_score) 
    
    return final_score


# In[13]:


for k in [1,2,3,4,5,10,15,50]:
    
    debug_flag = False
    
    final_shape = min(df_predicted_labels[0].shape[0],df_actual_labels[0].shape[0])
#     print(final_shape)

    precision_value = 0
    
#     for index_k in range(k):
    precision_value =     evaluate_precision(df_predicted_labels,df_actual_labels,k)
        
    precision_value =  precision_value / (k * final_shape)
    
    print(" Value of K ",k)
    print(" Value of precision_value ",precision_value)


# # Getting DCG ![image.png](attachment:image.png)

# In[14]:


def evaluate_dcn(df_predicted_labels,df_actual_labels,top_k):

    final_shape = min(df_predicted_labels[0].shape[0],df_actual_labels[0].shape[0])
#     print(final_shape)
    
    get_dcn_score = 0

    for iteration in range(final_shape):
        
        # get Predicted Label
        predicted_label = df_predicted_labels[0][iteration]
        predicted_label_list = predicted_label.split(' ')
        
        # get Actual Label 
        actual_label = df_actual_labels[0][iteration]
        actual_label_list = actual_label.split(' ')

        get_dcn_score = get_dcn_score +         (calculate_top_k_score_dcn(predicted_label_list,actual_label_list,top_k))
    
    return get_dcn_score


# In[15]:


for k in [1,3,5,10,15,50]:
    debug_flag = False
    
    final_shape = min(df_predicted_labels[0].shape[0],df_actual_labels[0].shape[0])
#     print(final_shape)

    dcn_value = 0

    dcn_value = dcn_value + evaluate_dcn(df_predicted_labels,df_actual_labels,k)
    
    print(" Value of K ",k)
    print(" Value of dcn_value ",dcn_value)


# # Getting DCGi ![image.png](attachment:image.png)

# In[16]:


def evaluate_dcn_i(df_predicted_labels,df_actual_labels,top_k):

    final_shape = min(df_predicted_labels[0].shape[0],df_actual_labels[0].shape[0])    
    get_dcn_score = 0
    for iteration in range(final_shape):
        # get Predicted Label
        predicted_label = df_predicted_labels[0][iteration]
        predicted_label_list = predicted_label.split(' ')
        
        # get Actual Label 
        actual_label = df_actual_labels[0][iteration]
        actual_label_list = actual_label.split(' ')
        
        get_dcn_score = get_dcn_score +         calculate_top_k_score_i_dcn(predicted_label_list,actual_label_list,top_k)
        
    return get_dcn_score


# In[17]:


for k in [1,3,5,10,15,50]:
    debug_flag = False
    
    final_shape = min(df_predicted_labels[0].shape[0],df_actual_labels[0].shape[0])
#     print(final_shape)

    dcn_value = 0
    dcn_value = dcn_value + evaluate_dcn_i(df_predicted_labels,df_actual_labels,k)
    
    print(" Value of K ",k)
    print(" Value of dcn_value ",dcn_value)


# # Get nDCG  ![image.png](attachment:image.png)

# In[18]:


def evaluate_n_dcn_k(df_predicted_labels,df_actual_labels,top_k):
    dcn_score = evaluate_dcn(df_predicted_labels,df_actual_labels,top_k)
    dcn_score_i = evaluate_dcn_i(df_predicted_labels,df_actual_labels,top_k)
    return (dcn_score/dcn_score_i)


# In[19]:


for k in [1,3,5,10,15,50]:
    debug_flag = False
    
    final_shape = min(df_predicted_labels[0].shape[0],df_actual_labels[0].shape[0])
#     print(final_shape)

    dcn_value = 0
    dcn_value = dcn_value + evaluate_n_dcn_k(df_predicted_labels,df_actual_labels,k)
    
    print(" Value of K ",k)
    print(" Value of dcn_value ",dcn_value)


# In[ ]:





# In[ ]:




