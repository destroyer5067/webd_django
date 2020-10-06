#self created
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
  params={'name':'Satyam Raj','place':'Earth'}
  return render(request,'index2.html',params)

def removepunc(request):
   
    djtext=request.POST.get('text','default')
    state1=request.POST.get('x','off')
    state2=request.POST.get('x2','off')
    if state1=="on" and state2=="on":
        z=""
        a ='''[]-!"#$%&'()*+,./:;<=>?@\^_`|'''
        for char in djtext:
            if char not in a:
                z=z+char.upper()
        params={'purpose' : 'remove punctuations','analyzed':z}
        return (render(request,'analyze2.html',params))

    elif state1=="on":
        z=""
        a ='''[]-!"#$%&'()*+,./:;<=>?@\^_`|'''
        for char in djtext:
            if char not in a:
                z=z+char
    
    #print(djtext)
        params={'purpose' : 'remove punctuations','analyzed':z}
        return (render(request,'analyze2.html',params))
    elif(state2=="on"):
        z=""
        for char in djtext:
            z=z+char.upper()
        params={'purpose' : 'remove punctuations','analyzed':z}
        return (render(request,'analyze2.html',params))
    else:
        s='''<h1>
        navigation bar</h1>
        <a href="https://wynk.in/music/detailsearch/Blue?q=Blue"> fb</a><br>
        <a href="fb"> fg</a><br>
        <a href="fb"> jk</a><br>
        <a href="fb"> io</a><br>
        <a href="fb"> pl</a><br>
        <a href="fb"> qw</a><br>'''
        return(HttpResponse(s))
     

def Capitalise(request):
    return HttpResponse("Capitalise")
def newline(request):
    return HttpResponse("New line removal")
def space(request):
    return HttpResponse("Space removal")
def char(request):
    return HttpResponse("counting of char")
def proj(request):
  return render(request,'proj1.html')
