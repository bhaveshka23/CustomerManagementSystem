from django.db import models


class Customer(models.Model):
    Cst_id = models.AutoField(primary_key=True) 
    Cst_name = models.CharField(max_length = 100)
    Cst_contact = models.CharField(max_length = 10)
    Cst_gender = models.CharField(max_length = 1)
    Cst_dob = models.DateField()
    Cst_photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    Cst_address = models.TextField()
    Cst_department = models.CharField(max_length=100)

    def __str__(self):
        return  self.Cst_name