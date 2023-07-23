from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=100, verbose_name="company name")
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Advertisement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default="")
    position_title = models.CharField(max_length=100)
    publication_date = models.DateField()
    job_description = models.TextField(max_length=5000)
    job_requirements = models.TextField(max_length=5000, blank=True)
    salary_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    work_mode = models.CharField(max_length=100)
    required_driving_categories = models.CharField(
        max_length=20,
        choices=[
            ('A', 'A'), 
            ('B', 'B'),
            ('BE', 'BE'), 
            ('C1', 'C1'),
            ('C1E', 'C1E'), 
            ('C', 'C'),
            ('CE', 'CE'),
            ('D1', 'D1'),
            ('D1E', 'D1E'),
            ('D', 'D'),
            ('DE', 'DE'),
        ],
    )
    work_location = models.CharField(max_length=100)
    start_date = models.DateField()
    contract_duration = models.CharField(
        max_length=100,
        choices=[('Permanent', 'Na stałe'), ('Contract', 'Zlecenie')],
    )

    def __str__(self):
        return self.position_title