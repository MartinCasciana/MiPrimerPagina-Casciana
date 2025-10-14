from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Page

class AboutView(TemplateView):
    template_name = "pages/about.html"

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
    fields = ["title", "slug", "excerpt", "body", "image"]
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("page_list")
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    

class PageUpdate(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ["title", "slug", "excerpt", "body", "image"]
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("page_list")

class PageDelete(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy("page_list")
