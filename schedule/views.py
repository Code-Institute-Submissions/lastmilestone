from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Comment
from .forms import CommentForm


def schedule(request):
    """ A view to show all comments """
    if request.user:

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
    if not request.user:
        messages.error(request, 'Sorry, only logged in user can do that.')
        return redirect(reverse('all_comments'))

    if request.method == 'POST':

        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():

            comment = form.save()
            comment.created_by = request.user

            messages.success(request, 'Successfully added note!')
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
    if not request.user:
        messages.error(request, 'Sorry, only logged in user can do that.')
        return redirect(reverse('all_comments'))

    comment = get_object_or_404(Comment, pk=comment_id,)

    if request.method == 'POST':

        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated note!')
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
    if not request.user:
        messages.error(request, 'Sorry, only logged in user can do that.')
        return redirect(reverse('all_comments'))

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'Note deleted!')
    return redirect(reverse('all_comments'))
