import numpy as np

#score for easy=5
#score for medium qn=7.5
#score for hard=10
#90% and above = S
#80% and above =A
#70% and above = B
#60% and above =C
#50% and above = D
#below 50% =E


def mapping(os_score,dbms_score,networks_score,dsa_score):
    grade=np.zeros(4,dtype=str)
    score=np.array([os_score,dbms_score,networks_score,dsa_score])
    i=0
    while(i<4):
        if(score[i]>=31.5):
            grade[i]='S'
        elif(score[i]>=28 and score[i]<31.5):
            grade[i]='A'
        elif(score[i]>=24.5 and score[i]<28):
            grade[i]='B'
        elif(score[i]>=21 and score[i]<24.5):
            grade[i]='C'    
        elif(score[i]>=17.5 and score[i]<21):
            grade[i]='D'    
        else:
            grade[i]='E'
        i=i+1
    return(grade)               