# iati-xml



			Thought process:

				Have created the homepage as a view that will automatically read
				contents from xml code lists folder. This means in the future if
				more code lists are added they can be automatically added to links. 

				Since there are only 9 code lists in the example I have chosen to render them manually, however a similar process could be applied in the case that we wanted to regularly add more xml files to be displayed by the app.
		
				Have also used a base file which loops through the data handed to it by each view, since the format of each XML file is similar.

				Some code lists do not have a description, so in this case the model will just write "no description available". 
