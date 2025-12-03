print("view page!!!")
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
    #return HttpResponse("Hell,this is first django project")
    #return HttpResponse("<h1 style='color:pink;'>Hell,this is first django project</h1>")
# Create your views here.

def text_response(req):
    return HttpResponse("Hello",content_type="textplain")

'''def html_response(request):
    html="<h1>Welcome to my django site</h1><p>this is html</>"
    return HttpResponse(html,content_type="text/html")
'''
#def my_render(req):
    #return render(req,'my_render.html')
'''def my_render(req):
    data={
        'name':'sneha',
          'age':37,
          'quali':'M.tech' }
    return render(req,'my_render.html',data)'''
def my_json(req):
    data={'active1':True,
          'active':False,
          '''active''':None
          }   
    return JsonResponse(data)

def my_redirect(req):
    return redirect("https://www.linkedin.com/in/")
    return redirect('language')

def my_redirect(req):
    url=reverse('my_redirect')
    data=urlencode({'name':'neeraj','age':37})
    return redirect(f'{url}{data}')

def my_redirect2(req):
    print("Hello")
    print(req.method)
    print(req.GET)