from django.db import models


class SpendingInfo(models.Model):
    #id = models.AutoField(primary_key=True) #主键省略不写
    sigma = models.TextField()
    msg = models.TextField()
    class Meta:
        db_table = "SpendingInfo"  # 更改表名

class User(models.Model):
    #id = models.AutoField(primary_key=True) #主键省略不写
    name = models.TextField()
    money = models.IntegerField()
    class Meta:
        db_table = "User"  # 更改表名

class Message(models.Model):
    #id = models.AutoField(primary_key=True) #主键省略不写
    # payer = models.TextField()
    # payee = models.TextField()
    sigma = models.TextField()
    msg = models.TextField()
    class Meta:
        db_table = "Message"  # 更改表名

class Cryptocurrency(models.Model):
    #id = models.AutoField(primary_key=True) #主键省略不写
    n = models.TextField()
    e = models.TextField()
    d = models.TextField()
    value = models.IntegerField()
    class Meta:
        db_table = "Cryptocurrency"  # 更改表名