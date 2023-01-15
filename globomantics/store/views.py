from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
#from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator
from django.views.generic import View, TemplateView, ListView

# Create your views here.
def index(request):
    return HttpResponse("store front coming soon")

def detail(request):
    return HttpResponse("store front detail pages coming soon")

# #@csrf_exempt
# @require_http_methods(["GET"])
# @cache_page(900)
# def electronics(request):
#     items = ("item 1", "item 2", "item 3", "item 4")
#     if request.method == 'GET':
#         paginator = Paginator(items, 2)
#         pages = request.GET.get('page', 1)
#         try:
#             items = paginator.page(pages)
#         except PageNotAnInteger:
#             items = paginator.page(1)
#         return render(request, 'store/list.html', {'items': items})
#     return HttpResponse("store front electronics pages coming soon")

class ElectronicsView(View):
    def get(self, request):
        items = ("item 1", "item 2", "item 3", "item 4", "item 5", "item 6")
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        self.process()
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        
        response = render(request, 'store/list.html', {'items': items})

        if request.COOKIES.get('visits'):
            value = int(request.COOKIES.get('visits'))
            print("Getting Cookie")
            response.set_cookie('visits', value + 1)
        else:
            value = 1
            print ("setting cookie")
            response.set_cookie('visits', value)
        
        return response
    
    def process(self):
        print("We are processing Electronics")

class ElectronicsView2(TemplateView):
    template_name = 'store/list.html'
    def get_context_data(self, **kwargs):
        items = ("item 1", "item 2", "item 3", "item 4", "item 5", "item 6")
        context = {'items': items}
        return context

class ElectronicsView3(ListView):
    template_name = 'store/list.html'
    queryset = ("item 1", "item 2", "item 3", "item 4", "item 5", "item 6")
    context_object_name = 'items'
    paginate_by = 2

class ComputersView(ElectronicsView):
    # def process(self):
    #     print("We are processing Computers")
    pass
    
class MobileView():
    # def process(self):
    #     print("We are processing Mobile Phones")
    pass

class EquipmentView(MobileView, ComputersView):
    pass