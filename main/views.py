from django.shortcuts import render
# import os
# print(os. getcwd())
# Create your views here.
import json

with open('./anim.json', 'r') as file_obj:
    my_family = json.load(file_obj)
my_family["families"].append({'id': 3, 'name' : 'mammal' })
my_family["families"].append({'id': 4, 'name' : 'reptile' })
my_family["families"].append({'id': 5, 'name' : 'insect' })
my_family["families"].append({'id': 6, 'name' : 'arachnid' })
my_family["families"].append({'id': 7, 'name' : 'amphibian' })
my_family['animals'].append({'id': 4, 'name' : 'fly','legs':4,'weight':.034,'height': .003,'speed': 2, 'family':5 })
my_family['animals'].append({'id': 5, 'name' : 'lizard','legs':4,'weight':7.2,'height': 1.2,'speed': 6, 'family':4 })
my_family['animals'].append({'id': 7, 'name' : 'frog','legs':4,'weight':2.2,'height': .5,'speed': 3, 'family':7})

# print(my_family) 

def homepage(request):
   
    context = {'hi': my_family}
    # context = my_family['families'][0]
    return render(request,'index.html',context)

def family(request,num):
    lst =[]
    for anim in my_family['animals']:
        if anim['family'] == num:
            lst.append(anim['name'])
    context = {'fam': lst,'num':num}
    return render(request,'family.html',context)

def animal(request,num):
    
    anim = my_family['animals'][num]
        
    context = {'anim': anim,'num':num}
    return render(request,'animal.html',context)
