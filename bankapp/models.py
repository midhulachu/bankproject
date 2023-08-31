from django.db import models

# Create your models here.
class regmodel(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    email=models.EmailField()
    number=models.IntegerField()
    image=models.FileField(upload_to='bankapp/static')
    balance=models.IntegerField()
    accountnumber=models.IntegerField()



class addamount(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)
class withmoney(models.Model):
    uid=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)


# class ministatement(models.Model):
#     choice=[
#         ('withdraw','withdraw'),
#         ('deposite','deposite'),
#         ('all','all')
#     ]
#     statement=models.IntegerField(choices=choice)
class newsmodel(models.Model):
    topic=models.CharField(max_length=300)
    content=models.CharField(max_length=3000)
    date=models.DateField(auto_now=True)

class wishlist(models.Model):
    uid=models.IntegerField()
    newsid=models.IntegerField()
    topic=models.CharField(max_length=300)
    content=models.CharField(max_length=3000)
    date=models.DateField()
