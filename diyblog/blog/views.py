from django.shortcuts import render
from django.views import generic
from .models import Blog, Blogger, Comment, Like
from .forms import CommentForm, ReplyForm, BlogForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required,login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User




# Create your views here.

def index():
    pass

class BlogListView(generic.ListView):
    model = Blog
    #paginate_by = 

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger   


class BlogCreateView(LoginRequiredMixin, CreateView):
    model= Blog
    fields = ['title', 'description',]

    def form_valid(self, form):
        print(self.request.user)
        blogger = Blogger(name = self.request.user, bio = '')
        blogger.save()
        form.instance.blogger = blogger
        return super(BlogCreateView, self).form_valid(form) 

def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.blogger = request.user
            blog.save()
            return redirect('blog-detail', pk = blog.pk)
    else:
        form = BlogForm()        
    return render(request, 'blog_form.html', {'form': form})    

class BloggerCreateView(CreateView):
    model = Blogger
    fields = '__all__'

@login_required
def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.commenter = request.user
            comment.save()
            return redirect('blog-detail', pk = pk)
    else:

        form = CommentForm()   
    return render(request, 'comment_form.html',{'blog':blog, 'form': form})     

@login_required
def reply_comment(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit = False)
            reply.comment = comment
            reply.replier = request.user
            reply.save()
            return redirect('blog-detail',pk=pk)
    else:
        form = ReplyForm()
    return render(request, 'reply_form.html', {'blog':blog, 'form': form})            


def like(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    user = request.user
    #liked_by_list = blog.likes.all()
    #session_list = request.session.get('my_list', blog.likes.all()[0].liked_by)
    #print(session_list.tolist())
    #if user not in session_list:   --not working Like object is not iterable
    like = Like(liked_by=user, post=blog)
    like.save()
    return redirect('blog-detail', pk=pk)



   


     
        
   

        