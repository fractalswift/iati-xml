from django.db import models

import os


import xml.etree.ElementTree as ET


tree = ET.parse('codelists/xml/GazetteerAgency.xml')
root = tree.getroot()

# Create your models here.


class Display_Pages(models.Model):

    def show_links():

        folder_contents = os.listdir("codelists/xml/")

        return folder_contents


    def display_page(xml_doc):


        return(f'This would be the page for {xml_doc} and the root tage is {root.tag}')


 
    def display_test_page():

        codelist_name = root[0][0][0].text
        description = root[0][1][0].text

        items_table = []

        for row in root[1]:
            
            code_number = row[0].text
            name = row[1][0].text
            items_table.append([code_number, name])
            

        return [codelist_name,  description, items_table]