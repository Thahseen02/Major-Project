from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template

from .forms import InputForm
from .predict import predict_result
from .utils import render_to_pdf
import pickle as pickle
import numpy as np
import os

# Create your views here.
def index(request):
    return render(request,'home.html')

def predict(request):      
    return render(request,'enter_details.html',{'form':InputForm},)

def result(request):
    tier_one=np.array(["Oracle","Microsoft","Amazon","MorganStanley","Tesco","Nutanix","AppDynamics"])
    tier_two=np.array(["JPMorgan","Qualcomm","Cisco","GeneralElectric","SAP","SocietyGeneral","Cavium"])
    tier_three=np.array(["Sandvine","Target","Exxon","DeutscheBank","Micro Focus","Informatica","Tally Solutions","C Dot","Dell","Pathpartner","Factset","OneConvergence","SchniderElectricals","Amadeus","CGI","Wipro","Thermofisher","Oracle Finance","PayTM","Infosys"])
    tier=np.zeros(25,dtype=str)
    if request.method=='POST':
        form=InputForm(request.POST)
    if form.is_valid():
        form = form.save()
        result=predict_result(form.gender,form.cgpa,form.school_grade,form.internship,form.os,form.networks,form.dbms,form.dsa)
        request.session['name']=form.user_name
        request.session['rollnumber']=form.roll_number
        request.session['cgpa']=form.cgpa
        request.session['os']=form.os
        request.session['networks']=form.networks
        request.session['dsa']=form.dsa
        request.session['dbms']=form.dbms
        request.session['school_grade']=form.school_grade
        if(result==1):
            tier=tier_one
        elif(result==2):
            tier=tier_two
        else:
            tier=tier_three
        request.session['tier']=int(result[0])    
    return render(request,'result.html',{'result':result,'tier':tier})
def generatepdf(request):
    tier_one=np.array(["Oracle","Microsoft","Amazon","MorganStanley","Tesco","Nutanix","AppDynamics"])
    tier_two=np.array(["JPMorgan","Qualcomm","Cisco","GeneralElectric","SAP","SocietyGeneral","Cavium"])
    tier_three=np.array(["Sandvine","Target","Exxon","DeutscheBank","Micro Focus","Informatica","Tally Solutions","C Dot","Dell","Amadeus","CGI","Thermofisher","Oracle Finance"])
    name=request.session.get('name','')
    roll_number=request.session.get('rollnumber','')
    cgpa=request.session.get('cgpa','')
    os=request.session.get('os','')
    networks=request.session.get('networks','')
    dsa=request.session.get('dsa','')
    dbms=request.session.get('dbms','')
    school_grade=request.session.get('school_grade','')
    result=request.session.get('tier','')
    if(result==1):
            tier=tier_one
    elif(result==2):
            tier=tier_two
    else:
            tier=tier_three
    print(tier)        
    pdf = render_to_pdf('predict_pdf.html',{'name':name,'roll_number':roll_number,'os':os,'networks':networks,'dsa':dsa,'dbms':dbms,'school_grade':school_grade,'cgpa':cgpa,'tier':tier,'result':result})
    print(pdf)
    return HttpResponse(pdf, content_type='application/pdf')

