import numpy as np
import pickle
import pandas as pd
import statistics as st
from django.core.files import File

def convert(grade):
    if(grade=='S' or grade=='s'):
        value=10
    elif(grade=='A' or grade=='a'):
        value=9
    elif(grade=='B' or grade=='b'):
        value=8
    elif(grade=='C' or grade=='c'):
        value=7
    elif(grade=='D' or grade=='d'):
        value=6
    elif(grade=='E' or grade=='e'):
        value=5
    elif(grade=='R' or grade=='r'):
        value=2
    else:
        value=0 
    return value    
def predict_result(gender,cgpa,school_grade,internship,os,networks,dbms,dsa,interviews):
    f=open("prediction-svm(82).sav",'rb')
    svclassifier = pickle.load(f)
    if(gender=='F'):
        gender=0
    else:
        gender=1
    if(internship=='Y'):
        internship=1
    else:
        internship=0
    os=convert(os)
    networks=convert(networks)
    dbms=convert(dbms)
    dsa=convert(dsa)
    X=np.array([gender,cgpa,school_grade,internship,os,networks,dbms,dsa,interviews])
    
    data = pd.read_csv("three.csv")
    w = len(data.columns.values.tolist())-2
    for i in range(2,w+1):
        mean = st.mean(data.iloc[:,i].values.tolist())
        std = st.stdev(data.iloc[:,i].values.tolist())
        data.iloc[:,i] = (data.iloc[:,i]-mean)/std
        X[i-1]=(X[i-1]-mean)/std
    n=9
    X=np.reshape(X,(-1,int(n)))
    y=svclassifier.predict(X)
    f.close
    print("Predicted Tier: ", y)
    return y