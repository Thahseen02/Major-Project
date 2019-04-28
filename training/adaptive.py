from .models import Adaptive_Question
import numpy as np
import random
from itertools import chain

def find_next_cluster(rank,code):
    cluster_center=np.zeros(4,dtype=str)
    if(rank==1):
        cluster_center=np.array(["A","A","A","A"])
        rank=0
    elif(rank==2):
        cluster_center=np.array(["B","C","C","A"])
        rank=1 
    elif(rank==3):
        cluster_center=np.array(["B","B","B","C"])
        rank=2
    else:
        rank=-1
    return cluster_center[code],rank

def encode(string):
    if(string == "S"):
        num = 5
    elif(string == "A"):
        num = 4
    elif(string == "B"):
        num = 3
    elif(string == "C"):
        num = 2
    elif(string == "D"):
        num = 1
    else:
        num=0
    return num

def get_random(query_set):
    index=random.sample(range(0,6), 3)
#    index1=random.randint(0, 4)
#    index2=random.randint(0, 6)
#    index3=random.randint(0, 5)
    leni=0
    for i in query_set:
        if(leni==index[0]):
            obj1=i
        if(leni==index[1]):
            obj2=i
        if(leni==index[2]):
            obj3=i
        leni=leni+1    
    result_list = np.array([obj1, obj2, obj3],dtype=object)
    return result_list

def mapping(student_grade,cluster_grade,subject,rank,code,count):
    student_grade=encode(student_grade)
    diff=encode(cluster_grade)-student_grade
    i=1
    total_score=0
    set_of_questions=np.empty(5,dtype=object)
    if(diff>0):
        while(i<=diff):
            category=student_grade+i
            total_score=total_score+(category*3)
            
            set_of_questions[i-1] = get_random(Adaptive_Question.objects.raw('SELECT * FROM training_adaptive_question WHERE category=%s and subject=%s', [category,subject]))
            i=i+1
    else:
        count=count+1
#        while(diff<=0 and rank!=0):
#            cluster_grade,rank=find_next_cluster(rank,code)
#            difference=encode(cluster_grade)-student_grade
#            i=1
#            if(difference>0):
#                while(i<=difference):
#                    category=student_grade+i
#                    total_score=total_score+(category*3)
#                    set_of_questions[i-1] = Adaptive_Question.objects.raw('SELECT * FROM training_adaptive_question WHERE category=%s and subject=%s ORDER BY RAND() LIMIT 3', [category,subject])
#                    i=i+1
#            diff=difference        
    return set_of_questions,total_score,cluster_grade,count  
                

def find_adaptive_questions(grade_os,grade_dbms,grade_networks,grade_dsa,cluster_os,cluster_dbms,cluster_networks,cluster_dsa,cluster_rank):
        while(cluster_rank != -1):
            count=0
            os_questions,total_score_os,new_cluster_os,count=mapping(grade_os,cluster_os,"OS",cluster_rank,0,count)
            dbms_questions,total_score_dbms,new_cluster_dbms,count=mapping(grade_dbms,cluster_dbms,"DBMS",cluster_rank,1,count)
            networks_questions,total_score_networks,new_cluster_networks,count=mapping(grade_networks,cluster_networks,"NET",cluster_rank,2,count)
            dsa_questions,total_score_dsa,new_cluster_dsa,count=mapping(grade_dsa,cluster_dsa,"DSA",cluster_rank,3,count)
            if(count < 4):
                break
            else:
                cluster_os,cluster_rank_os=find_next_cluster(cluster_rank,0)
                cluster_dbms,cluster_rank_dbms=find_next_cluster(cluster_rank,1)
                cluster_networks,cluster_rank_networks=find_next_cluster(cluster_rank,2)
                cluster_dsa,cluster_rank_dsa=find_next_cluster(cluster_rank,3)
                cluster_rank=cluster_rank_os
        new_grade=np.array([new_cluster_os,new_cluster_dbms,new_cluster_networks,new_cluster_dsa])                                                  
        return os_questions,dbms_questions,networks_questions,dsa_questions,total_score_os,total_score_dbms,total_score_networks,total_score_dsa,new_grade
