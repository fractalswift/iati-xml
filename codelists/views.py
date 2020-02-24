from django.shortcuts import get_object_or_404, render

from .models import Display_Pages

import os

import xml.etree.ElementTree as ET




folder_contents = os.listdir("codelists/xml/")

xml_list = []

for row in folder_contents:

    tree = ET.parse(f'codelists/xml/{row}')
    root = tree.getroot()
    xml_list.append(root)





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


def gazetteerAgency(request):

    data = Display_Pages.display_page(xml_list[0])

    return render(request, f'codelists/gazateeragency.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2]
        })

def documentCategory(request):

    data = Display_Pages.display_page(xml_list[1])

    return render(request, f'codelists/documentcategory.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2]
        })




