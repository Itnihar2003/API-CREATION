from django.db import models

# Create your models here.
class students(models.Model):
    student_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    qualification=models.TextField()
