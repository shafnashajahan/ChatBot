from django.shortcuts import render

import requests
import sys
from subprocess import run,PIPE
def button(request):
    return render(request,'index.html')
def output(request):
    data=requests.get(“https://www.google.com/“)
    print(data.text)
    data=data.text
    return render(request,'index.html',{'data':data})
def external(request):
    inp= request.POST.get('param')
    out= run([sys.executable,'//Users//user//OneDrive//miniproject//OneDrive//Desktop//LNxxxx8293-A-2--main//LNxxxx8293-A-2--main//jhalaksharma//testing_sentence.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'home.html',{'data1':out.stdout})