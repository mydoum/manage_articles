from django.shortcuts import render
from forms import PostForm
from django.shortcuts import redirect

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('../home', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'creation/article.html', {'form': form})