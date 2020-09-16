from django.db import models

class Comment(models.Model):
    
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    comment = models.TextField()
   
   
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name