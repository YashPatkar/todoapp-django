from django.db import models

# Create your models here.
class Note(models.Model):
    name=models.CharField(max_length=200)
    note=models.TextField(null=False)

    def __str__(self) -> str:
        return f'ID: {{self.id}} --- Name: {{self.name}}'