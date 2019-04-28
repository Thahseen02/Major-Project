import numpy as np

#
# Grading Policy
#for 1 jump ,above 50%=higher grade and below 50%=lower grade (E->D)
#for 2 jumps, 30% -70% == one grade,above 70% == 2 grades(E->C)
#for 3 jumps, 25%-50% == 1 grade,50%-75% 2 grades, above 75% 3 grades(E->B)
#for 4 jumps, 20%-40% == 1 grade,40%-60% 2 grades, 60%-80% 2 grades, above 80% 4 grades(E->A)
#for 5 jumps, 15%-30% == 1 grade,30%-50-% 2 grades, 50%-65% 3 grades, 65%-80% 4 grades, above 80% 5 grades(E->S)

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
def decode(num):
    if(num == 0):
        string="E"
    elif(num == 1):
        string="D"
    elif(num == 2):
        string="C"
    elif(num == 3):
        string="B"
    elif(num == 4):
        string="A"
    else:
        string="S"
    return string    
def upgrade(current,mark):
    current=encode(current)
    current=current+mark
    current=decode(current)
    return current
def find_length(queryset):
    length=0
    for i in queryset:
        if i is not None:
            length=length+1
    return length        
def final_mapping(score,queryset,total,current):
    division=find_length(queryset)
    if(division==1):
        if((score/total)*100 > 50):
            final_grade=upgrade(current,1)
        else:
            final_grade=current
    elif(division==2):
        if((score/total)*100 > 30 and (score/total)*100 <= 70):
            final_grade=upgrade(current,1)
        elif((score/total)*100 > 70):
            final_grade=upgrade(current,2)
        else:
            final_grade=current
    elif(division==3):
        if((score/total)*100 > 25 and (score/total)*100 <= 50):
            final_grade=upgrade(current,1)
        elif((score/total)*100 > 50 and (score/total)*100 <= 75):
            final_grade=upgrade(current,2)
        elif((score/total)*100 > 75):
            final_grade=upgrade(current,3) 
        else:
            final_grade=current
    elif(division==4):
        if((score/total)*100 > 20  and (score/total)*100 <= 40):
            final_grade=upgrade(current,1)
        elif((score/total)*100 > 40 and (score/total)*100 <= 60):
            final_grade=upgrade(current,2)
        elif((score/total)*100 > 60 and (score/total)*100 <= 80):
            final_grade=upgrade(current,3)    
        elif((score/total)*100 > 80):
            final_grade=upgrade(current,4) 
        else:
            final_grade=current 
    elif(division==5):
        if((score/total)*100 > 15  and (score/total)*100 <= 30):
            final_grade=upgrade(current,1)
        elif((score/total)*100 > 30 and (score/total)*100 <= 50):
            final_grade=upgrade(current,2)
        elif((score/total)*100 > 50 and (score/total)*100 <= 65):
            final_grade=upgrade(current,3)
        elif((score/total)*100 > 65 and (score/total)*100 <= 80):
            final_grade=upgrade(current,4)     
        elif((score/total)*100 > 80):
            final_grade=upgrade(current,5) 
        else:
            final_grade=current
    else:
        final_grade=current
    return final_grade        
            
        
            
        
            