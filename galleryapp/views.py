from django.shortcuts import  render,redirect
from .models import Gallery,Photo,Cattegory
from .forms import PhotoUploadForm
# Create your views here.

def home(request):
    
    return render(request, 'home.html')


def nature(request):

    photo = Photo.objects.filter(category=5)
    return render(request, 'nature.html', {'photo': photo})

def wildlife(request):
    photo = Photo.objects.filter(category=9)
    return render(request,'wildlife.html', {'photo': photo})

def art(request):
    photo = Photo.objects.filter(category=8)
    return render(request,'art.html', {'photo': photo})
def snow(request):
    photo = Photo.objects.filter(category=6)
    return render(request,'snow.html', {'photo': photo})
def background(request):
    photo = Photo.objects.filter(category=2)
    return render(request,'background.html', {'photo': photo})

def fantasy(request):
    photo = Photo.objects.filter(category=7)
    return render(request,'fantasy.html', {'photo': photo})
def landscape(request):
    photo = Photo.objects.filter(category=4)
    return render(request,'landscape.html', {'photo': photo})
def forest(request):
    photo = Photo.objects.filter(category=3)
    return render(request,'forest.html', {'photo': photo})
def love(request):
    photo = Photo.objects.filter(category=10)
    return render(request,'love.html', {'photo': photo})

def food(request):
    return render(request,'food.html')

def upload_photo(request):
    form = PhotoUploadForm()
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('home')
        else:
            return render(request, 'user_upload.html', {'form': form})
    else:
        return render(request, 'user_upload.html', {'form': form})

def gallery(request):
    gallery = Gallery.objects.all()
    return render (request, 'gallery.html', {'gallery': gallery})

def search(request):
    if request.GET:
        search=request.GET.get('search')
        search=search.lower()
        if search=='nature':
            photo = Photo.objects.filter(category=5)
            return render(request,'nature.html',{'photo':photo})
        elif search=='art':
            photo = Photo.objects.filter(category=8)
            return render(request,'art.html',{'photo':photo})
        elif search=='snow':
            photo = Photo.objects.filter(category=6)
            return render(request,'snow.html',{'photo':photo})
        elif search=='background':
            photo = Photo.objects.filter(category=2)
            return render(request,'background.html',{'photo':photo})
        elif search=='wildlife':
            photo = Photo.objects.filter(category=9)
            return render(request,'wildlife.html',{'photo':photo})
        elif search=='fantasy':
            photo = Photo.objects.filter(category=7)
            return render(request,'fantasy.html',{'photo':photo})
        elif search=='landscape':
            photo = Photo.objects.filter(category=4)
            return render(request,'landscape.html',{'photo':photo})
        elif search=='forest':
            photo = Photo.objects.filter(category=3)
            return render(request,'forest.html',{'photo':photo})
        
        else:
            return render(request,'search.html',{'search':search})
    else:
        return render(request,'home.html')
        





# def search(request):
#     cattegory=Cattegory
#     if request.GET:
#         search_query = request.GET.get('search')
#         search_query = search_query.lower()

#         pages_mapping = {
#             'nature': 'nature.html',
#             'art': 'art.html',
#             'snow': 'snow.html',
#             'background': 'background.html',
#             'wildlife': 'wildlife.html',
#             'fantasy': 'fantasy.html',
#             'landscape': 'landscape.html',
#             'forest': 'forest.html',
#         }

#         # Check if the search term is in the predefined pages
#         if search_query in pages_mapping:
#             return render(request, pages_mapping[search_query])
#         else:
#             return render(request, 'search.html', {'search': search_query})
#     else:
#         return render(request, 'home.html')
        
        
        

    
    
         
    
# def uploads(request):
#     upload=Uploads.objects.all()
#     return render(request, 'upload.html',{'upload':upload})
