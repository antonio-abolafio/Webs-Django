from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
"""from django.shortcuts import redirect"""
from .models import Page
from .forms import PageForm


# Create your views here.

class StaffRequiredMixin(object):
    """
    Este mixin require que el usuario sea miembro del staff
    """
    
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        """if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))"""
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    

class PagesListView(ListView):
    model = Page
    template_name = "pages/pages.html"
    context_object_name = "pages"
    

class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page.html"
    context_object_name = "page"

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    

@method_decorator(staff_member_required, name='dispatch')    
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    

@method_decorator(staff_member_required, name='dispatch')    
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
