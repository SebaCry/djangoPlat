from django.http import HttpResponse
from django.urls import path
from . import views
from .models import Profile, Author


# def author_view(request, id):
#     author = Author.objects.get(id = id)
#     profile = Profile.objects.get(id = author.pk)

#     return HttpResponse(f'{author.name} - {profile.website} - {profile.biography}')

urlpatterns = [
    # path("listado/", views.my_test_view),
    path("listado/", views.CarListView.as_view()),
    path("detalle/<int:id>", views.my_view),

    # path("autor/<int:id>", author_view)
]
