from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='images/', blank=True, null=True) 
    passwd = models.CharField(max_length=200)
    nickname = models.CharField(max_length=45)
    tel = models.CharField(max_length=20)
    birth = models.CharField(max_length=8)
    sex = models.CharField(max_length=1)
    schoolPassType=models.CharField(max_length=20)
    student_id = models.CharField(max_length=45)
    school = models.CharField(max_length=45)
    department = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    intro_title = models.CharField(max_length=100, null=False)
    intro_body = models.CharField(max_length=200, null=False)
    role = models.IntegerField()
    createdTime = models.DateTimeField(auto_now_add=True)
 
