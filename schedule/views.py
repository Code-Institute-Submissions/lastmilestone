from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Comment
from .forms import CommentForm

# Create your views here.
# Create your views here.






def schedule(request):
    """ A view to show all comments, including sorting and search queries """

    comments = Comment.objects.all()
  

    
    context = {
        'comments': comments,
      
    }

    return render(request, 'schedule/schedule.html', context)


def comment_detail(request, comment_id):
    """ A view to show individual comment details """

    comment = get_object_or_404(Comment, pk=comment_id)

    context = {
        'comment': comment,
    }

    return render(request, 'schedule/comment_details.html', context)


@login_required
def add_comment(request):
    """ Add a comment to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('all_comments'))

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            messages.success(request, 'Successfully added comment!')
            return redirect(reverse('comment_detail', args=[comment.id]))
        else:
            messages.error(
                request, 'Failed to add comment. \
                    Please ensure the form is valid.')
    else:
        form = CommentForm()

    template = 'schedule/add_comment.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_comment(request, comment_id):
    """ Edit a comment in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated comment!')
            return redirect(reverse('comment_detail', args=[comment.id]))
        else:
            messages.error(
                request, 'Failed to update comment.\
                     Please ensure the form is valid.')
    else:
        form = CommentForm(instance=comment)
        messages.info(request, f'You are editing {comment.name}')

    template = 'schedule/edit_comment.html'
    context = {
        'form': form,
        'comment': comment,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """ Delete a comment from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted!')
    return redirect(reverse('all_comments'))