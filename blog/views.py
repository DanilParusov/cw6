from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic


from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(generic.ListView):
    model = Blog
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        queryset = queryset.order_by('-data_creating')
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')
    extra_context = {
        'title': 'Написать статью'
    }

    def form_valid(self, form):
        if form.is_valid():
            fields = form.save(commit=False)
            fields.autor = self.request.user
            fields.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')
    extra_context = {
        'title': 'Редактировать статью'
    }


class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    extra_context = {
        'title': 'Удалить статью'
    }

