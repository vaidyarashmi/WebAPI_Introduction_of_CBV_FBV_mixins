from django.shortcuts import render
from django.http import HttpResponse
import json 
from django.http import JsonResponse
from django.views.generic import View
from testapp.mixins import HttpResMixins
# Create your views here.
class Json_CBV(HttpResMixins,View):
    def get(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'this is from get'})
        return self.render_to_http_response(json_data)
    def post(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'this is from post'})
        return self.render_to_http_response(json_data)
    def put(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'this is from put'})
        return self.render_to_http_response(json_data)
    def patch(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'this is from patch'})
        return self.render_to_http_response(json_data)
    def delete(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'this is from delete'})
        return self.render_to_http_response(json_data)
    
def emp_data_view(request):
    emp_data={
        'eno':100,
        'ename':'raj',
        'esal':1000,
        'eaddr':'pune'
    }
    resp=f"<h1> Employee number : {emp_data['eno']}<br> Employee Name : {emp_data['eno']} <br> Employee salary : {emp_data['esal']}<br> Employee address :{emp_data['eaddr']} </h1>"
    return HttpResponse(resp)

def emp_data_jsonview(request):
    emp_data = {
        'eno':100,
        'ename':'raj',
        'esal':1000,
        'eaddr':'pune'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

def emp_data_jsonview_using_jsonres(request):
    emp_data = {
        'eno':100,
        'ename':'raj',
        'esal':1000,
        'eaddr':'pune'
    }
    return JsonResponse(emp_data)