from django.db import models


class SpendingInfo(models.Model):
    #id = models.AutoField(primary_key=True) #主键省略不写
    sigma = models.TextField()
    msg = models.TextField()
    class Meta:
        db_table = "SpendingInfo"  # 更改表名