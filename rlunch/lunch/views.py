from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Talk
from .forms import TalkForm


class TalkDetailView(DetailView):

    model = Talk
    template_name = 'lunch/talk_detail.html'


class TalkListView(ListView):

    model = Talk
    template_name = 'lunch/talk_list.html'


class TalkCreate(CreateView):

    model = Talk
    template_name = 'lunch/talk_create.html'
    form_class = TalkForm


class TalkUpdate(UpdateView):

    model = Talk
    form_class = TalkForm
    template_name = 'lunch/talk_create.html'
