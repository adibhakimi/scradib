import streamlit as st
import pandas as pd

#Dataframe manipulation library

#Math functions, we'll only need the sqrt function so let's import only that
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel 

st.title(" Career Recommendation System ")
#navigation
navi = st.sidebar.radio("Navigation: ", ("Home", "Career Recommendation")) 
def get_navi(navi):
    if navi == "Home":
        st.subheader('How it works?')
        st.write("1. Find your path")
        st.write("Have a look to each computer sciences path and choose the best path that you prefer")
        st.write(" ")
        st.write("2. Filter and choose your ideal career")
        st.write("Get the career id after you choose the most ideal career for you based on its description, in the career list")
        st.write(" ")
        st.write("3. Recommending Similar Career")
        st.write("Type the career id on the recommendation page and you will get a list of career that similar to your preference career")
              
        out = 0
     
    elif navi == "Career Recommendation":
        job_df = pd.read_csv('Job_listnew.csv')
        st.write("List of job")
        job_df
        st.write("Type the career ID that you have chosen below")
        
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 4), min_df=0, stop_words='english')
        tfidf_matrix = tf.fit_transform(job_df['Description'])
        
        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix) 
        results = {}
        for idx, row in job_df.iterrows():
            similar_indices = cosine_similarities[idx].argsort()[:-100:-1] 
            similar_items = [(cosine_similarities[idx][i], job_df['id'][i]) for i in similar_indices] 
            results[row['id']] = similar_items[1:]
        out = 0
        def item(id):  
            return job_df.loc[job_df['id'] == id]['Description'].tolist()[0].split(' - ')[0] 
# Just reads the results out of the dictionary.def 
        out = 0
        
        def recommend(item_id, num):
            st.write("Recommending " + str(num) + " products similar to job ID: " + str(item_id)+ "...")
            st.write(" ")
            st.write("Career ID            Career Name              Salary          ")
            st.write("--------------------------------------------------------------")    
            recs = results[item_id][:num]   
            for rec in recs: 
                st.write(item(rec[1]))
                
        jobid = st.number_input("Career ID: ")
        if jobid != 0:
            recommend(item_id = jobid, num=10)
                
        out = 0
        
        return out
#each out variable is use to end each fucntion
out = get_navi(navi)