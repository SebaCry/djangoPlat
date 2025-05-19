from django.http import HttpResponse
from django.urls import path
# from . import views
from .models import Profile, Author

def my_view(request,*args, **kwargs):
    print(args, kwargs)
    return HttpResponse("")

# def author_view(request, id):
#     author = Author.objects.get(id = id)
#     profile = Profile.objects.get(id = author.pk)

#     return HttpResponse(f'{author.name} - {profile.website} - {profile.biography}')

    



urlpatterns = [
    path("listado/", my_view),
    path("detalle/<int:id>", my_view),
    # path("autor/<int:id>", author_view)
]
