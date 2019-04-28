import pickle
import numpy as np

def switch(grade):
    if grade == "S":
        return 10
    elif grade == "A":
        return 9
    elif grade == "B":
        return 8
    elif grade == "C":
        return 7
    elif grade == "D":
        return 6
    elif grade == "E":
        return 5
    else:
        return 0

def find_cluster(grade):
    cluster_center=np.zeros(4,dtype=str)
    X=np.zeros(4,dtype=int)
    for i in range(0,4):
            value=switch(grade[i])
            X[i]=value
    X=X.reshape(1,-1)
    print(X)        
    kmeans = pickle.load(open('saved/kmeans.sav', 'rb'))


    Y = kmeans.predict(X)
    print(Y)
    if(Y == 1):
        cluster_center=np.array(["A","A","A","A"])
        cluster_rank=0
    elif(Y == 2):
        cluster_center=np.array(["B","C","C","A"])
        cluster_rank=1
    elif(Y == 0):
        cluster_center=np.array(["B","B","B","C"])
        cluster_rank=2
    else:
        cluster_center=np.array(["C","C","D","D"])
        cluster_rank=3
    return cluster_center,cluster_rank

