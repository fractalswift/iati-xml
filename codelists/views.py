from django.shortcuts import get_object_or_404, render

from .models import Display_Pages

# Create your views here.


def home(request):

    pages_list = Display_Pages.show_links()

    return render(request, 'codelists/home.html', {'pages_list': pages_list})



def test(request):

    data = Display_Pages.display_test_page()

    return render(request, 'codelists/test.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2]
        })