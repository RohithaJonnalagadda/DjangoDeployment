from django.db import models
class emp_table(models.Model):
    eid=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=30)
    emp_salary=models.FloatField()
