from django.shortcuts import get_object_or_404, render, redirect
from .models import PostModel, Reaction
from .forms import PostModelForm
from .forms import PostEditForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def react_to_post(request, post_id, value):
    post = get_object_or_404(PostModel, id=post_id)

    reaction, created = Reaction.objects.get_or_create(user=request.user, post=post)

    if not created:
        if reaction.value == value:
            # user clicked same reaction again → remove reaction
            reaction.delete()
        else:
            # user switched from like → dislike or vice versa
            reaction.value = value
            reaction.save()
    else:
        reaction.value = value
        reaction.save()

    return redirect("Post detail", pk=post.id)

@login_required
def index (request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('Blog post')
    else:
        form = PostModelForm()
    context = {
        'posts': posts,
        'form': form
    }

    return render (request, 'blog/index.html', context) 


@login_required
def post_detail(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    comments = post.comment_set.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user= request.user
            instance.post= post
            instance.save()
            return redirect('Post detail', pk=post.id)
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comments':comments,
        'comment_form': comment_form

    }
    return render(request, 'blog/post_detail.html', context)

@login_required
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    comments = post.comment_set.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('Post detail', pk=post.id)
    else: 
     comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,  # Ensure comments are in the context
        'comment_form': comment_form

    }
    return render(request, 'blog/post_edit.html', context)


@login_required   
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('Blog post')
    context = {
    'post': post,
    
    }
    return render(request, 'blog/post_delete.html', context)




# Create your views here.
