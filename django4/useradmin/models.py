from django.db import models

# Create your models here.
class role(models.Model):
    rolename = models.TextField(max_length=200)
    class Meta():
        db_table = 'role'
class userInfo(models.Model):
    username = models.TextField(max_length=200)
    password = models.TextField(max_length=200)
    gender = models.TextField(max_length=10)
    hrole = models.ForeignKey(role(),on_delete=models.CASCADE)
    class Meta():
        db_table = 'userinfo'
    def showname(self):
        return self.username