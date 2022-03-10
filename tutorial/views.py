from django.shortcuts import redirect
from django.views import generic
from django.db.models import Q
from tutorial.models import Post

# Create your views here.
def index(request):
    return redirect('tutorial_list')

class TutorialListView(generic.ListView):
    model = Post
    template_name = 'tutorial/tutorial_list.html'

    def get_queryset(self):
        return Post.objects.filter(status=1)[:20]

class TutorialDetailView(generic.DetailView):
    model = Post
    template_name = 'tutorial/tutorial_detail.html'

class SearchView(generic.ListView):
    model = Post
    template_name = 'tutorial/tutorial_list.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) & status = 1)[:20]