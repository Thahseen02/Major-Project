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
def predict_result(gender,cgpa,school_grade,internship,os,networks,dbms,dsa):
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
    #input area1
    X1=np.array([gender,internship,os,networks,dbms,dsa]) # Gender,Internship,OS,Networks,DBMS,DSA
    X1=X1.reshape(1,-1)
    X1=pd.DataFrame(X1)
    X1.columns = ['Gender','Internship','OS','Networks','DBMS','DSA']

    #input area2 for Scaling
    X2=np.array([cgpa,school_grade])  # CGPA,12th
    X2=X2.reshape(1,-1)
    sc = pickle.load(open('models/metric.sav','rb'))
    X2 = sc.transform(X2)
    X2 = pd.DataFrame(X2)
    X2.columns = ['CGPA','12th']

    #combine all features
    X = X1.join(X2)

#    PCA reduction
    pca = pickle.load(open('models/reducer.sav','rb'))
    X = pca.transform(X)
    X = pd.DataFrame(X)

    svclassifier = pickle.load(open("models/prediction-svm.sav",'rb'))
    y=svclassifier.predict(X)
    #
    print("Predicted Tier: ", y)
    return y
