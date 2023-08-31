
import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout
# Create your views here.
def register(request):
    if request.method =='POST':
        a=regform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['firstname']
            ln=a.cleaned_data['lastname']
            un=a.cleaned_data['username']
            p=a.cleaned_data['password']
            cp=a.cleaned_data['confirmpassword']
            e=a.cleaned_data['email']
            n=a.cleaned_data['number']
            ac=int('15'+str(n))
            im=a.cleaned_data['image']
            a = regmodel.objects.all()
            for i in a:
                if (un == i.username or e == i.email):
                    return HttpResponse('allready esixt')
            else:
                if (p == cp):
                 b=regmodel(firstname=fn,lastname=ln,username=un,password=p,email=e,number=n,accountnumber=ac,image=im,balance=0)
                 b.save()
                 subject='your account has been created'
                 message=f'your new account number is {ac}'
                 email_from='dakshithmidhun7@gmail.com'
                 email_to=e
                 send_mail(subject,message,email_from,[email_to])
                 return redirect(login)
                else:
                   return HttpResponse('password incorrect')
        else:
            return HttpResponse('registration failed')
    return render(request,'userregister.html')

def login(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['username']
            p=a.cleaned_data['password']
            b=regmodel.objects.all()
            for i in b:
                if i.username==un and i.password==p:
                    request.session['id']=i.id
                    return redirect(profile)
            else:
                return redirect(login)

    return render(request,'loginuser.html')
def profile(request):
   try:
    id1=request.session['id']
    a=regmodel.objects.get(id=id1)
    img=str(a.image).split('/')[-1]
    return render(request,'bankprofile.html',{'a':a,'img':img})
   except:
       return redirect(login)
def edit(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.username = request.POST.get('username')
        a.password = request.POST.get('password')
        a.email=request.POST.get('email')
        a.number=request.POST.get('number')
        a.save()
        return redirect(profile)
    return render(request,'edit.html',{'a':a})

def imageedit(request, id):
        a = regmodel.objects.get(id=id)
        img = str(a.image).split('/')[-1]
        if request.method == 'POST':
            if request.FILES.get('image') == None:
                a.save()
            else:
                a.image = request.FILES['image']
                a.save()
            a.save()
            return redirect(profile)

        return render(request, 'imageedit.html', {'a': a, 'img': img})

def addmoney(request,id):
    x=regmodel.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount') #withot form
        password = request.POST.get('password')
        request.session['am'] = am
        request.session['ac']=x.accountnumber
        if password == x.password:
            x.balance+=int(am)
            x.save()
            b=addamount(amount=am,uid=request.session['id'])
            b.save()
            return redirect(success)
        else:
            return HttpResponse('failed')
    return render(request,'addamount.html')
def success(request):
    am=request.session['am']
    id=request.session['id']
    a=regmodel.objects.get(id=id)
    return render(request,'adddisplay.html',{'am':am,'a':a})
def widrawmoney(request,id):
    x=regmodel.objects.get(id=id)
    if request.method=='POST':
        am = request.POST.get('amount')  # withot form
        request.session['am'] = am
        request.session['ac'] = x.accountnumber
        password = request.POST.get('password')
        if password == x.password:
         if(x.balance>=int(am)):
            x.balance -= int(am)
            x.save()
            b=withmoney(amount=am,uid=request.session['id'])
            b.save()
            return redirect(widrawdisplay)

         else:
            return HttpResponse('insufficientbalance')
        else:
            return HttpResponse('password incorrect')

    return render(request,'withdrawamount.html')
def widrawdisplay(request):
    am=request.session['am']
    ac=request.session['ac']
    return render(request,'withdrawdisplay.html',{'am':am,'ac':ac})


def checkbalance(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        request.session['balance']=a.balance
        request.session['ac']=a.accountnumber
        password=request.POST.get('password')
        if password==a.password:
            return redirect(checkbalance1)
        else:
            return HttpResponse('wrong passsword')
    return render(request,'checkbalance.html')
def checkbalance1(request):
    ac=request.session['ac']
    balance=request.session['balance']
    return render(request,'checkbalance1.html',{'ac':ac,'balance':balance})

def statement(request,id):
    a=regmodel.objects.get(id=id)
    password = request.POST.get('password')
    choice=request.POST.get('statement')
    if request.method=='POST':
        if password == a.password:

            if choice=='deposit':
                return redirect(depdisplay)
            elif choice=='withdraw':
                return redirect(withdisplay)
        else:
            return HttpResponse('PASSSWORD ERROR')
    return render(request, 'ministatement.html')
def depdisplay(request):
    x=addamount.objects.all() #fetchall
    id=request.session['id']
    return render(request,'depdisp.html',{'x':x,'id':id})

def withdisplay(request):
    x=withmoney.objects.all()
    id = request.session['id']
    return render(request,'withdisp.html',{'x':x,'id':id})
def news(request):
    if request.method=='POST':
        a=newsform(request.POST)
        if a.is_valid():
            top=a.cleaned_data['topic']
            con=a.cleaned_data['content']
            b=newsmodel(topic=top,content=con)
            b.save()
            return redirect(newsdisplay)
        else:
            return HttpResponse('failed')
    return render(request,'newsfeed.html')
def newsdisplay(request):
    a=newsmodel.objects.all()
    return render(request,'adminnewsfeeddisplay.html',{'a':a})
def adminlogin(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['username']
            p=a.cleaned_data['password']
            b=regmodel.objects.all()
            for i in b:
                if i.username==un and i.password==p:
                    request.session['id']=i.id
                    return redirect(profile)
            else:
                return redirect(login)

    return render(request,'login.html')
def index(request):
    return render(request,'firstpage.html')
def admin(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            username=a.cleaned_data['username']
            password=a.cleaned_data['password']
            User=authenticate(request,username=username,password=password)
            if User is not None:
                return render(request,'admindisplay.html')
            else:
                return HttpResponse('login failed')
    return render(request,'adminlogin.html')
def adminnewsdelete(request,id):
    a=newsmodel.objects.get(id=id)
    a.delete()
    return redirect(newsdisplay)
def adminnewsedit(request,id):
    a=newsmodel.objects.get(id=id)
    if request.method=='POST':
        a.topic=request.POST.get('topic')
        a.content=request.POST.get('content')
        a.save()
        return redirect(newsdisplay)
    return render(request,'newsfeededit.html',{'a':a})
def display(request):
        a = newsmodel.objects.all()
        return render(request, 'newsdisplay1.html', {'a': a})
def wish(request,id):
    a=newsmodel.objects.get(id=id)
    a1=wishlist.objects.all()
    for i in a1:
        if i.newsid==a.id and i.uid==request.session['id']:
            return HttpResponse('Item already in wishlist')
    b=wishlist(topic=a.topic,content=a.content,date=a.date,newsid=a.id,uid=request.session['id'])
    b.save()
    return HttpResponse('added')
def wishlistview(request):
    a=wishlist.objects.all()
    id=request.session['id']
    return render(request,'wishlistview.html',{'a':a,'id':id})
def logoutt(request):
    logout(request)
    return redirect(index)
# def forgetpassword(request):
#     a=regmodel.objects.all()
#     if request.method == 'POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         for i in a:
#             if (i.username == username):
#                 a.password=password
#                 b=regmodel(firstname=i.firstname,lastname=i.lastname,username=i.username,password=password,email=i.email,number=i.number,accountnumber=i.accountnumber,image=i.image,balance=i.balance)
#                 b.save()
#                 return HttpResponse('success')
#         else:
#           return HttpResponse('incorrect username')
#     return render(request,'forgetpassword.html')


def forgot_password(request):
    a=regmodel.objects.all()
    if request.method=='POST':
        em=request.POST.get('email')
        ac=request.POST.get('accountnumber')
        for i in a:
            if(i.email==em and i.accountnumber==int(ac)):
                id=i.id
                subject="password change"
                message=f"http://127.0.0.1:8000/bankapp/change_password/{id}"
                frm='dakshithmidhun7@gmail.com'
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("check email")
        else:
            return HttpResponse("sorry")
    return render(request,'forgotpassword.html')
def change(request):
    return render(request,'change.html')
def change_password(request,id):
    a=regmodel.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pin')
        p2=request.POST.get('rpin')
        if p1==p2:
            a.password=p1
            a.save()
            return HttpResponse('password changed')
        else:
            return HttpResponse('sorry')
    return render(request,'change.html')
# def moneytransferhtml(request):
#     return render(request,'moneytransfer.html')
def moneytransfer(request):
    id1=request.session['id']
    a=regmodel.objects.get(id=id1)
    b=regmodel.objects.all()
    if request.method == 'POST':
        acn = request.POST.get('username')
        acno = request.POST.get('accountnumber')
        am=request.POST.get('amount')
        for i in b:
            if i.accountnumber==int(acno) and i.username==acn:
                if (a.balance >= int(am)):
                    a.balance-=int(am)
                    a.save()
                    i.balance+=int(am)
                    i.save()
                    return HttpResponse('success')
                else:
                    return HttpResponse('Not Sufficient balance')
        else:
                   return HttpResponse('wrong')
    return render(request,'moneytrans.html')
def moneytransferdisplay(request):
    id=request.session['id']
    a=moneymodel.objects.all(id=id)
    return render(request,'moneytransfer.html',{a})
def profilebank(request):
    return render(request,'bankprofile.html')


