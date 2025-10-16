from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Page

class AboutView(TemplateView):
    template_name = "pages/about.html"

class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PageList(ListView):
    model = Page
    template_name = "pages/page_list.html"
    context_object_name = "pages"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = (self.request.GET.get("q") or "").strip()
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(excerpt__icontains=q))
        return qs

class PageDetail(DetailView):
    model = Page
    template_name = "pages/page_detail.html"
    context_object_name = "page"

class PageCreate(LoginRequiredMixin, CreateView):
    model = Page
    fields = ["title", "subtitle", "content", "image"]
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("page_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Página creada correctamente.")
        return super().form_valid(form)

    

class PageUpdate(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ["title", "subtitle", "content", "image"]
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("page_list")

    def form_valid(self, form):
        messages.success(self.request, "Página actualizada correctamente.")
        return super().form_valid(form)

class PageDelete(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy("page_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Página eliminada correctamente.")
        return super().delete(request, *args, **kwargs)
