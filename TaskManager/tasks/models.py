from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    status = models.CharField(max_length=50)
    poster = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title +"-----"+ self.status +"-----"+ str(self.created_at)