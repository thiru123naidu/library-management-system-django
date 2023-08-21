from django.db import models

class studentlibrary(models.Model):
    #id = models.IntegerField(primary_key=)
    student_rollnumber = models.IntegerField()
    bookid = models.IntegerField()
    issue_date = models.DateField()
    return_date = models.DateField(null=True,blank=True)
    time_period =models.DateField()
    penalty = models.IntegerField(null=True,blank=True)
    
