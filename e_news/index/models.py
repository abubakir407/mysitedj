from django.db import models

# Create your models here.
class NewsCategory(models.Model):
        name = models.CharField(max_length=64)
        created_at = models.DateTimeField(auto_now_add=True)

        def str(self):
            return self.name



class News(models.Model):
        title = models.CharField(max_length=255)
        content = models.TextField()
        category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)

        def str(self):
            return self.title

