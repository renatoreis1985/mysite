from django.http import HttpResponse # type: ignore
from django.views import generic # type: ignore

class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the blog index.")