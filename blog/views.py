from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment, Preference
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'blog/post_draft_list.html', {'posts':posts})


@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')


@login_required
def add_comment_to_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post 
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'blog/add_comment_to_post.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def postpreference(request, pk, userpreference):
	if request.method == "POST":
		post = get_object_or_404(Post, pk=pk)

		obj = ''

		valueobj = ''

		try:
			print("Если реакции уже были")
			print("User", request.user)
			print("Post", post.__str__())
			print(Preference.objects.all())
			obj = Preference.objects.get(user=request.user, post=post)

			valueobj = obj.value  # value of userpreference

			valueobj = int(valueobj)

			userpreference = int(userpreference)

			if valueobj != userpreference:
				obj.delete()

				upref = Preference()
				upref.user = request.user

				upref.post = post

				upref.value = userpreference
				print(userpreference)
				if userpreference == 1 and valueobj != 1:
					post.likes += 1
					post.dislikes -= 1
				elif userpreference == 2 and valueobj != 2:
					post.dislikes += 1
					post.likes -= 1

				upref.save()

				post.save()

				context = {'post': post,
						   'pk': pk}

				return render(request, 'blog/post_detail.html', context)


			elif valueobj == userpreference:
				print("Удаляем ранее поставленную реакцию.")
				obj.delete()

				if userpreference == 1:
					post.likes -= 1
				elif userpreference == 2:
					post.dislikes -= 1

				post.save()

				context = {'post': post,
						   'pk': pk}

				return render(request, 'blog/post_detail.html', context)


		except Preference.DoesNotExist:
			print("Если реакций нет.")

			upref = Preference()

			upref.user = request.user

			upref.post = post

			upref.value = userpreference

			userpreference = int(userpreference)

			if userpreference == 1:
				post.likes += 1
			elif userpreference == 2:
				post.dislikes += 1

			upref.save()

			post.save()

			context = {'post': post,
					   'pk': pk}
			obj = Preference.objects.get(user=request.user, post=post)
			print("Создали", obj)
			return render(request, 'blog/post_detail.html', context)


	else:
		post = get_object_or_404(Post, id=pk)
		context = {'post': post,
				   'pk': pk}

		return render(request, 'blog/post_detail.html', context)