from django.views.generic import TemplateView, ListView
from .models import Item, ParentCategory


class Index(TemplateView):
    template_name = 'items/list.html'


class ItemList(ListView):
    model = Item
    paginate_by = 6
    ordering = ['-id']
    template_name = 'items/list.html'

    def get_queryset(self):
        queryset = super(ItemList, self).get_queryset()
        slug = self.kwargs.get('slug')
        if slug:
            queryset = queryset.filter(category__slug=slug)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context: dict = super(ItemList, self).get_context_data(**kwargs)
        context.update({"parent_categories": ParentCategory.objects.all()})
        return context
