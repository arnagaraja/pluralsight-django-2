from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
#from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return HttpResponse("store front coming soon")

def detail(request):
    return HttpResponse("store front detail pages coming soon")

#@csrf_exempt
@require_http_methods(["GET"])
@cache_page(900)
def electronics(request):
    items = ("item 1", "item 2", "item 3", "item 4")
    if request.method == 'GET':
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, 'store/list.html', {'items': items})
    return HttpResponse("store front electronics pages coming soon")