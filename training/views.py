from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template

from .models import Question,Adaptive_Question
from .compute import mapping
from .cluster import find_cluster
from .adaptive import find_adaptive_questions
from .final import final_mapping
from .utils import render_to_pdf

import pickle
import numpy as np
# Create your views here.

def test(request):
    sample_questions=Question.objects.all()
    return render(request,'test.html',{'questions':sample_questions})

def first(request):
    os_score=0
    dbms_score=0
    networks_score=0
    dsa_score=0    
    sample_questions=Question.objects.all()
    if request.method=='POST':
        for i in sample_questions:
            answer=request.POST.get(i.question,"")
            if(i.correct==answer):
                if(i.category=="E"):
                    if(i.subject=="OS"):
                        os_score=os_score+5
                    elif(i.subject=="DBMS"):
                        dbms_score=dbms_score+5
                    elif(i.subject=="DSA"):
                        dsa_score=dsa_score+5
                    else:
                        networks_score=networks_score+5    
                elif(i.category=="M"):
                    if(i.subject=="OS"):
                        os_score=os_score+7.5
                    elif(i.subject=="DBMS"):
                        dbms_score=dbms_score+7.5
                    elif(i.subject=="DSA"):
                        dsa_score=dsa_score+7.5
                    else:
                        networks_score=networks_score+7.5
                else:    
                    if(i.subject=="OS"):
                        os_score=os_score+10
                    elif(i.subject=="DBMS"):
                        dbms_score=dbms_score+10
                    elif(i.subject=="DSA"):
                        dsa_score=dsa_score+10
                    else:
                        networks_score=networks_score+10            
        grade=mapping(os_score,dbms_score,networks_score,dsa_score)
        cluster_center,cluster_rank=find_cluster(grade)
        request.session['cluster_rank']=cluster_rank
        request.session['current_grade_os']=grade[0]
        request.session['current_grade_dbms']=grade[1]
        request.session['current_grade_networks']=grade[2]
        request.session['current_grade_dsa']=grade[3]
        request.session['current_cluster_os']=cluster_center[0]
        request.session['current_cluster_dbms']=cluster_center[1]
        request.session['current_cluster_networks']=cluster_center[2]
        request.session['current_cluster_dsa']=cluster_center[3]
    return render(request,'training_result.html',{'center':cluster_center,'grade':grade})        

def second(request):
    grade_os=request.session.get('current_grade_os','')
    grade_dbms=request.session.get('current_grade_dbms','')
    grade_networks=request.session.get('current_grade_networks','')
    grade_dsa=request.session.get('current_grade_dsa','')
    cluster_os = request.session.get('current_cluster_os','')
    cluster_dbms = request.session.get('current_cluster_dbms','')
    cluster_networks = request.session.get('current_cluster_networks','')
    cluster_dsa = request.session.get('current_cluster_dsa','')
    cluster_rank = request.session.get('cluster_rank','')
    os_questions,dbms_questions,networks_questions,dsa_questions,total_score_os,total_score_dbms,total_score_networks,total_score_dsa,new_grade=find_adaptive_questions(grade_os,grade_dbms,grade_networks,grade_dsa,cluster_os,cluster_dbms,cluster_networks,cluster_dsa,cluster_rank)
    flag=1
    for i in os_questions:
        if i is not None:
            flag=0
    for i in dbms_questions:
        if i is not None:
            flag=0
    for i in dsa_questions:
        if i is not None:
            flag=0
    for i in networks_questions:
        if i is not None:
            flag=0        
    request.session['new_cluster_os']=new_grade[0]
    request.session['new_cluster_dbms']=new_grade[1]
    request.session['new_cluster_networks']=new_grade[2]
    request.session['new_cluster_dsa']=new_grade[3]
    
    with open('res.pkl', 'wb') as f:
                pickle.dump([os_questions,dbms_questions,networks_questions,dsa_questions.copy(),total_score_os,total_score_dbms,total_score_networks,total_score_dsa], f)
                f.close
    return render(request,'second_test.html',{'os': os_questions,'networks':networks_questions,'dbms':dbms_questions,'dsa':dsa_questions,'flag':flag})
def finalgrade(request):
    os_score=0
    dbms_score=0
    dsa_score=0
    networks_score=0
    with open('res.pkl', 'rb') as f:
            os_questions,dbms_questions,networks_questions,dsa_questions,total_score_os,total_score_dbms,total_score_networks,total_score_dsa = pickle.load(f)     
    grade_os=request.session.get('current_grade_os','')
    grade_dbms=request.session.get('current_grade_dbms','')
    grade_networks=request.session.get('current_grade_networks','')
    grade_dsa=request.session.get('current_grade_dsa','')        
    if request.method=='POST':
        for i in os_questions:
            if i is not None:
                for j in i:
                    answer=request.POST.get(j.question,"")
                    if(j.correct==answer):
                        os_score=os_score+int(j.category)
        for i in dbms_questions:
            if i is not None:
                for j in i:
                    answer=request.POST.get(j.question,"")
                    if(j.correct==answer):
                        dbms_score=dbms_score+int(j.category)
        for i in dsa_questions:
            if i is not None:
                for j in i:
                    print(j.question)
                    answer=request.POST.get(j.question,"")
                    print(j.correct)
                    print(answer)
                    if(j.correct==answer):
                        print("correct")
                        dsa_score=dsa_score+int(j.category)
        for i in networks_questions:
            if i is not None:
                for j in i:
                    answer=request.POST.get(j.question,"")
                    if(j.correct==answer):
                        networks_score=networks_score+int(j.category)
        final_grade_os=final_mapping(os_score,os_questions,total_score_os,grade_os)
        final_grade_dbms=final_mapping(dbms_score,dbms_questions,total_score_dbms,grade_dbms)
        final_grade_dsa=final_mapping(dsa_score,dsa_questions,total_score_dsa,grade_dsa)
        final_grade_networks=final_mapping(networks_score,networks_questions,total_score_networks,grade_networks)
        request.session['final_os']=final_grade_os
        request.session['final_dbms']=final_grade_dbms
        request.session['final_dsa']=final_grade_dsa
        request.session['final_networks']=final_grade_networks
    return render(request,'final.html',{'current_os':final_grade_os,'current_dbms':final_grade_dbms,'current_dsa':final_grade_dsa,'current_networks':final_grade_networks,'prev_os':grade_os,'prev_dbms':grade_dbms,'prev_dsa':grade_dsa,'prev_networks':grade_networks})

def generatepdf(request):
    name=request.session.get('name','')
    roll_number=request.session.get('rollnumber','')
    grade_os=request.session.get('current_grade_os','')
    grade_dbms=request.session.get('current_grade_dbms','')
    grade_networks=request.session.get('current_grade_networks','')
    grade_dsa=request.session.get('current_grade_dsa','')
    cluster_os = request.session.get('new_cluster_os','')
    cluster_dbms = request.session.get('new_cluster_dbms','')
    cluster_networks = request.session.get('new_cluster_networks','')
    cluster_dsa = request.session.get('new_cluster_dsa','')
    final_grade_os=request.session.get('final_os','')
    final_grade_dbms=request.session.get('final_dbms','')
    final_grade_dsa=request.session.get('final_dsa','')
    final_grade_networks=request.session.get('final_networks','')
    candidate_name=request.session.get('name','')
    candidate_number=request.session.get('rollnumber','')
    print(candidate_number)
    pdf = render_to_pdf('last_pdf.html',{'current_os':final_grade_os,'current_dbms':final_grade_dbms,'current_dsa':final_grade_dsa,'current_networks':final_grade_networks,'prev_os':grade_os,'prev_dbms':grade_dbms,'prev_dsa':grade_dsa,'prev_networks':grade_networks,'cluster_os':cluster_os,'cluster_dbms':cluster_dbms,'cluster_networks':cluster_networks,'cluster_dsa':cluster_dsa,'candidate_name':candidate_name,'candidate_number':candidate_number})
    print(pdf)
    return HttpResponse(pdf, content_type='application/pdf')
        
        
                        
                        
                            
                        
                        
                    

    

   
    
    
    
    

    
