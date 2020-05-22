from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
#Now we use class based views such as list views, detail views, update and delete views etc
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView #Similar to detail view
)
#we cannot use decorators on class based views as we did for profile, instead we use Mixins
#another mixin to restrict user to edit theirs posts only
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#add is to far left of post create view
# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'linuxls/home.html', context)
#context is used to pass information into the template


class PostListView(ListView):
    model = Post
    template_name = 'linuxls/home.html'
    context_object_name = 'posts' #otherwise class view will use 'objects' variable
    ordering =['-date_posted'] #change the ordering of the posts
    paginate_by = 4

#list and order post by user
class UserPostListView(ListView):
    model = Post
    template_name = 'linuxls/user_posts.html'
    context_object_name = 'posts' #otherwise class view will use 'objects' variable
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
#we will use default class url pattern and use default 'objects' variable

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
#we need to provide the fields only
#date posted will update automatically
    fields = ['title', 'content', 'videoURL']
#to add the author for the new post and get rid of integrity error we wil define a function (Need to overwrite the form valid method)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)# just runnign form valid mehtod on parent class, it runs anyway, we are setting author before it rans
#same as PostCreateView
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content', 'videoURL']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#with user mixin, we can create a method called test_func that mixin will run in order to see that user passed certain conditions
    def test_func(self):
        post =   self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/' # this will redirect to home page after deletion of the post
    def test_func(self):
        post =   self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,'linuxls/about.html')

def fundamentals(request):
    return render(request,'linuxls/fundamentals.html')

def rhcsa(request):
    return render(request,'linuxls/rhcsa.html')
