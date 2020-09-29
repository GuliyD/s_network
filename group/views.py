from django.shortcuts import render, HttpResponse
from .models import GroupModel
from .forms import CreateGroupForm
from django.contrib.auth.decorators import login_required


@login_required
def group_view(request, group_name):
    try:
        group = GroupModel.objects.get(name=group_name)
    except GroupModel.DoesNotExist:
        return HttpResponse('group does not exist')
    works = group.works.all()
    return render(request, 'group/group.html', {'group': group, 'works': works})


@login_required
def create_group_view(request):
    if request.POST:
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('group_name')
            request.user.user_groups.create(name=name)
            return HttpResponse('created')
    else:
        form = CreateGroupForm()
    return render(request, 'group/create_group.html', {'form': form})