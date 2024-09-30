from django.contrib import admin
from .models import Gallery,Photo,Cattegory
# Register your models here.

admin.site.register(Gallery)
admin.site.register(Cattegory)
admin.site.register(Photo)