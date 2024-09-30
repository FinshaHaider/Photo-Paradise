from django.urls import path,include

from galleryapp import views

urlpatterns=[
     path('',views.home,name='home'),
     path('nature/',views.nature,name='nature'),
     # path('animals/',views.animals,name='animals'),
     path('background/',views.background,name='background'),
     path('snow/',views.snow,name='snow'),
     path('art/',views.art,name='art'),
     path('fantasy/',views.fantasy,name='fantasy'),
     path('forest/',views.forest,name='forest'),
     path('love/',views.love,name='love'),
     path('landscape/',views.landscape,name='landscape'),
     path('food/',views.food,name='food'),
     path('wildlife/',views.wildlife,name='wildlife'),
     path('search/',views.search,name='search'),
     path('upload_photo/',views.upload_photo,name='upload_photo'),
     # path('upload/',views.upload,name='upload'),


]
