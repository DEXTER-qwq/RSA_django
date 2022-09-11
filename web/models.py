from django.db import models


class SpendingInfo(models.Model):
    sigma = models.TextField()
    msg = models.TextField()
    class Meta:
        db_table = "SpendingInfo"  # 更改表名