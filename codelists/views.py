from django.shortcuts import get_object_or_404, render

from .models import Display_Pages

import os

import xml.etree.ElementTree as ET


# Import filenames from xml codelists folder for
# to pass to models for generating page content


folder_contents = os.listdir("codelists/xml/")

xml_list = []

for row in folder_contents:

    tree = ET.parse('codelists/xml/' + str(row))
    root = tree.getroot()
    xml_list.append(root)





def home(request):


    codelists_data = Display_Pages.show_links()

    return render(request, 'codelists/home.html', {"codelists_data": codelists_data} )




def gazetteerAgency(request):

    # Hand to models to parse xml content

    data = Display_Pages.display_page(xml_list[0])

    return render(request, 'codelists/gazetteeragency.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2],
        })

def documentCategory(request):

    data = Display_Pages.display_page(xml_list[1])

    return render(request, 'codelists/documentcategory.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2],
        })

def activityDateType(request):

    data = Display_Pages.display_page(xml_list[2])

    return render(request, 'codelists/activitydatetype.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2]
        })

def budgetStatus(request):

    data = Display_Pages.display_page(xml_list[3])

    return render(request, 'codelists/budgetstatus.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2]
        })


def relatedActivityType(request):

    data = Display_Pages.display_page(xml_list[5])

    return render(request, 'codelists/relatedactivitytype.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2]
        })


def budgetType(request):

    data = Display_Pages.display_page(xml_list[6])

    return render(request, 'codelists/budgettype.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2]
        })


def transactionType(request):

    data = Display_Pages.display_page(xml_list[7])

    return render(request, 'codelists/transactiontype.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2]
        })


def organisationRole(request):

    data = Display_Pages.display_page(xml_list[8])

    return render(request, 'codelists/organisationrole.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2]
        })

    
def activityStatus(request):

    data = Display_Pages.display_page(xml_list[4])

    return render(request, 'codelists/activitystatus.html', {
        'name': data[0],
        'description': data[1],
        'items_table': data[2]
        })



# Possible extension for future

def renderCodelist(request, codelist_name):

    codelist = get_object_or_404(Display_Pages.display_page(xml_list[8]), YOUR_ITEM_FIELD_NAME=item_name)

    pass


