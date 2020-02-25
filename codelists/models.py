from django.db import models

import os
import re


# Create your models here.


class Display_Pages(models.Model):

    def show_links():

        folder_contents = os.listdir("codelists/xml/")
        titles = []
        links =[]

        codelists_data = {}

        for row in folder_contents:
            # add in a space before capital letter and strip off the file extension
            title = re.sub( r"([A-Z])", r" \1", row[0:-4]) 
            titles.append(title)
            # convert to lowercase and change .xml for /
            link = re.sub( r".xml", r"/", row).lower()
            links.append(link)

            codelists_data[title] = link


        return codelists_data


 
 


    def display_page(xml_file):

        codelist_name = xml_file[0][0][0].text

        # Check to see if codelist has a description
        try:
            desc = [d for d in xml_file[0].iter('description')]
        except:
            desc = []

         # Create description placeholder for codelists with no description
       
        if len(desc) == 0:
            description =  "No description available."
        else:
            description = xml_file[0][1][0].text
          
            

        items_table = {}

        for row in xml_file[1]:
            
            code_number = row[0].text
            name = row[1][0].text
            items_table[code_number] = name
            

        return [codelist_name,  description, items_table]