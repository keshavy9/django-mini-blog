from django.shortcuts import render
from django.views import generic
from .models import Blog, Blogger, Comment, Like
from .forms import CommentForm, ReplyForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required,login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

class BlogCreateView(CreateView):
    model= Blog
    fields = '__all__'

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
    like = Like(liked_by=user, post=blog)
    like.save()
    return redirect('blog-detail', pk=pk)


     
        
   

        