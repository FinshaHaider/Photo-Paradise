from django import forms

from .models import Gallery,Photo,Cattegory
 
    



class PhotoForm(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    category=forms.ModelChoiceField(queryset=Gallery.objects.all(),widget=forms.Select())

    

# # def upload_file(request):
# #     if request.method == 'POST':
# #         file = request.FILES['file']
# #         upload = Uploads(file=file)
# #         upload.save()
# #         return redirect('home')
# #     return render(request, 'upload.html')

# # def download_file(request, file_id):
# #     upload = Uploads.objects.get(id=file_id)
# #     response = HttpResponse(upload.file.read(), content_type=upload.file.content_type)
# #     response['Content-Disposition'] = f'attachment; filename="{upload.file.name}"'
# #     return response

# class UploadForm(forms.Form):
#     title=forms.TimeField()
#     image = forms.ImageField()
    
#     class Meta:
#         model = Uploads
#         fields = ['title','image']
    
class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title','image','category']
    

    
