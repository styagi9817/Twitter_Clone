from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Post

# def index(render):
#     return HttpResponse('HELLO')

from .forms import PostForm
# from .forms import UpdateForm
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.


def index(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.all().order_by('-created_at')
    # Tweet.objects.order_by('created_at').reverse().all()[:20]

    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


# def edit(request, post_id):
#     post = Post.objects.get(id=post_id)
#     form = PostForm(instance=post)
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         else:
#             return HttpResponseRedirect(form.errors.as_json())
#     # Show editting screen
#     return render(request, 'edit.html',
#                   {'tweet': post, 'form': form})

def update_tweet(request, pk):
    tweet = Post.objects.get(id=pk)
    form = PostForm(instance=tweet)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'edit.html', context)


def postLikeAdd(request, post_id):

    post = Post.objects.get(id=post_id)

    new_like_count = post.like_count + 1
    post.like_count = new_like_count

    print(post.like_count)
    post.save()

    return HttpResponseRedirect('/')
