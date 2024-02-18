from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_draft = models.BooleanField(default=False)  # Add this field

    def __str__(self):
        return self.title

