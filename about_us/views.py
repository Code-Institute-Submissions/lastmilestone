from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Trainers
from .forms import TrainerForm
# Create your views here.




def about_us(request):
    """ A view to show individual trainer details """
    trainer = Trainers.objects.all()
    

    context = {
        'trainer': trainer,
    }

    return render(request,'about_us/about_us.html', context)

def trainer_detail(request, trainer_id):
    """ A view to show individual trainer details """

    trainer = get_object_or_404(Trainers, pk=trainer_id)

    context = {
        'trainer': trainer,
    }

    return render(request, 'about_us/trainer_details.html', context)


@login_required
def add_trainer(request):
    """ Add a trainer to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            trainer = form.save()
            messages.success(request, 'Successfully added trainer!')
            return redirect(reverse('trainer_detail', args=[trainer.id]))
        else:
            messages.error(
                request, 'Failed to add trainer. \
                    Please ensure the form is valid.')
    else:
        form = TrainerForm()

    template = 'about_us/add_trainer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_trainer(request, trainer_id):
    """ Edit a trainer in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    trainer = get_object_or_404(Trainers, pk=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated trainer!')
            return redirect(reverse('trainer_detail', args=[trainer.id]))
        else:
            messages.error(
                request, 'Failed to update trainer.\
                     Please ensure the form is valid.')
    else:
        form = TrainerForm(instance=trainer)
        messages.info(request, f'You are editing {trainer.name}')

    template = 'about_us/edit_trainer.html'
    context = {
        'form': form,
        'trainer': trainer,
    }

    return render(request, template, context)


@login_required
def delete_trainer(request, trainer_id):
    """ Delete a trainer from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    trainer = get_object_or_404(Trainers, pk=trainer_id)
    trainer.delete()
    messages.success(request, 'Trainer deleted!')
    return redirect(reverse('about_us'))