from django.db import models

# Create your models here.


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery_images/')
    category=models.CharField(max_length=200)

    def __str__(self):
        return self.title
 

class Cattegory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photo_images/')
    category = models.ForeignKey(Cattegory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


    

    
    
# class Uploads(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='upload_images/')
    
#     def __str__(self):
#         return self.title
    
    
    
        
    