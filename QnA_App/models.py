from django.db import models

class PDF(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class QAHistory(models.Model):
    pdf = models.ForeignKey(PDF, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    asked_at = models.DateTimeField(auto_now_add=True)
