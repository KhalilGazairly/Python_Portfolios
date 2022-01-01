from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
projectList = [
    {
        'id':'1',
        'title':'Ecommerce',
        'description':'Fully functional website'
    },
    {
        'id':'2',
        'title':'Eduction',
        'description':'part functional website for eduction'
    },
    {
        'id':'3',
        'title':'Transportaion',
        'description':'functional website for transport'
    },
    
]

def projects(request):
    name = 'Khalil'
    number = 25
    context = {'name':name, 'number':number, 'items':projectList}
    return render(request, 'projects/projects.html', context)
    # return HttpResponse('Here are our products')

def project(request,pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project':projectObj})
    # return HttpResponse('Here Single product' + ' ' +str(pk))
