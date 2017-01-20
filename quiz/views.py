from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
import models
from models import Quetion,User,Userrecord,Quizdetails

# Create your views here.
def first(request):
    return TemplateResponse(request,'addQuiz.html')

def test(request,qid):
    type = request.session['type']
    if type == "Teacher" or type == "Quizzer":
        return render(request, 'addQ.html', {'Name': models.Quizdetails.objects.get(idquiz = qid).name, 'id': qid})
    else:
        Q =models.Quizdetails.objects.get(idquiz = qid)
        Qname =Q.name
        timeLimit = int(Q.timelimit)*60
        return HttpResponse(render(request, 'QuizPage.html', {'data': Quetion.objects.filter(idquiz = qid) , 'Name' :Qname ,'timeLimit' :timeLimit}))

def showQuiz(request):
    return HttpResponse(render(request, 'showQuiz.html', {'data': models.Quizdetails.objects.all()}))

def addQuiz(request):
    if request.method == 'GET':
        data = request.GET
        date = data['Date']
        name = data['Name']
        time = data['Time']
        subject = data['subject']
        timeLimit = data['timeLimit']
        total = data['total']
        try:
            entry = models.Quizdetails.objects.get(name = name)
            if entry.creator == "Amit":
                entry.timelimit = timeLimit
                entry.subject =subject
                entry.total = total
                entry.date =date
                entry.time = time
                entry.save()
        except  models.Quizdetails.DoesNotExist:
            s = models.Quizdetails( creator = "Amit",timelimit =timeLimit, subject = subject,   total = total,
                            name = name, date = date,time = time)  # Field name made lowercas
            s.save()

        return render(request, 'addQ.html', { 'Name' : name , 'id' : models.Quizdetails.objects.get(name = name).idquiz})


def addQ(request):
    if request.method == 'GET':
        data = request.GET
        name = data['Name']
        id = data['id']
        Que = data['Que']
        A = data['A']
        B = data['B']
        C = data['C']
        D = data['D']
        ans  =data['ans']
        total = data['total']
        s = Quetion(idquiz = id,q_d=Que,a=A,b=B,c=C,d =D,ans=ans,marks=total)
        s.save()
        return render(request, 'addQ.html',{ 'Name': name, 'id': id})

def login(request):
    request.session.flush()
    return TemplateResponse(request, 'login.html')
def signup(request):
    request.session.flush()
    return TemplateResponse(request, 'signup.html')

def signout(request):
    request.session.flush()
    return TemplateResponse(request, 'login.html')

def auth(request):
    u = request.GET['user']
    p = request.GET['pass']
    try:
            user =User.objects.get(name = u)
            if p == user.password:
                request.session['user'] = user.name
                request.session['type'] =user.type
                request.session['uid'] = user.iduser
                return HttpResponse(render(request, 'showQuiz.html', {'data': models.Quizdetails.objects.all()}))
            else:
                return TemplateResponse(request, 'login.html')
    except User.DoesNotExist:
        return TemplateResponse(request, 'login.html')

def register(request):
    u = request.GET['user']
    p = request.GET['pass']
    t = request.GET['type']
    try:
        user = User(name = u,password = p,type=t)
        user.save()
        return TemplateResponse(request, 'login.html')
    except Exception:
        return TemplateResponse(request, 'signup.html')

def marking(request):
    data = request.GET
    u = request.session['user']
    score=0
    idQ = 0
    for i in data.keys():
        S = Quetion.objects.get(idquetion=i)
        if S.ans == data[i]:
            score += int(S.marks)
        idQ = S.idquiz
    user = User.objects.get(name = u)
    S = Userrecord(idquiz = idQ,iduser=user.iduser,score=score)
    S.save()
    return HttpResponse(render(request, 'Report.html', {'data': Userrecord.objects.filter(iduser=user.iduser)}))


def getAns(request,question):
    try:
        S = Quetion.objects.get(idquetion=question)
        return JsonResponse(
            {'status': 200, 'ans' : S.ans})

    except Quetion.DoesNotExist:
        return JsonResponse({'status': 404})

def reporting(request):
    t = request.session['type']
    uname = request.session['user']
    uid = request.session['uid']
    if t == "Teacher" or t == "Quizzer":
        m = Quizdetails.objects.all()
        a = []
        for i in m:
            a.append(i.idquiz)
        return HttpResponse(render(request, 'Qreport.html', {'data':Quetion.objects.all() ,'score' :Userrecord.objects.all() }))
    else:
        return HttpResponse(render(request, 'Report.html', {'data': Userrecord.objects.filter(iduser=uid)}))

