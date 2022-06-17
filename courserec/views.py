from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting
import json
import os
import pickle
dir_path = os.path.dirname(os.path.realpath(__file__))


print("Directory path: {}".format(dir_path))

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")



def recommends(request):
    return render(request,'sajan.html')

import math
import pandas as pd
import pickle
model=pickle.load(open('bta_model.pkl','rb+'))
def predict(request):
     if request.method=='POST':       
        temp={}
        temp['age']=int(request.POST.get('age'))  
        temp['gender']=int(request.POST.get('gender'))
        temp['duration']=int(request.POST.get('duration'))
        temp['structure']=int(request.POST.get('structure'))
        temp['job']=int(request.POST.get('job'))
        temp['categories']=int(request.POST.get('categories'))      
        testdata=pd.DataFrame({'x':temp}).transpose()
        scoreval=model.predict(testdata)[0]
        return render(request,'result.html',{'result':scoreval})

def load_data():
    output_json = json.load(open("courserec/BTA Data.json"))
    specialization_name_map = output_json['specialization_name_map']
    course_recommendations = output_json['course_recommendations']
    course_descriptions = output_json['course_descriptions']
    course_difficulties = output_json['course_difficulties']
    course_durations = output_json['course_durations']
    course_Structure = output_json['course_Structure']
    course_Pre_Requisites = output_json['course_Pre_Requisites']
    course_Hardware = output_json['course_Hardware']
    ret = (specialization_name_map, course_recommendations, course_descriptions, course_difficulties,course_durations,course_Structure,course_Pre_Requisites,course_Hardware)
    return ret

def recommend(request):
    #Input: request with user input.
    #Output: Recommendations page with class suggestions.
    specialization = request.POST['spec']
    specialization_name_map, course_recommendations, course_descriptions, course_difficulties,course_durations,course_Structure,course_Pre_Requisites ,course_Hardware= load_data()
    spec_list_str = ", ".join(course_recommendations[specialization])
    table = []
    for course in course_recommendations[specialization]:
        for difficulty in ["Easy", "Medium", "Hard"]:
            if course in course_difficulties[difficulty]:
                break
            table.append("{}: {} - ({}) - ({}) - ({}) - ({}) - ({})".format(course, course_descriptions[course], difficulty,course_durations[course],course_Structure[course],course_Pre_Requisites[course],course_Hardware[course]))
            
        print("CUSTOM LOG MSG. Requested: {}".format(specialization))
    new_context = {"spec" : specialization_name_map[specialization],
                   "courses" : spec_list_str,
                   "table" : table}
    
    
    return render(request, "recommendations.html", context=new_context)
    

def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})


