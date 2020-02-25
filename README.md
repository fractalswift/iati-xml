# iati-xml



			<h2>Thought process:</h2>

				<p>Have created the homepage as a view that will automatically read
				contents from xml code lists folder. This means in the future if
				more code lists are added they can be automatically added to links. </p>

				<p>Since there are only 9 code lists in the example I have chosen to render them manually, however a similar process could be applied in the case that we wanted to regularly add more xml files to be displayed by the app.</p>
		
				<p>Have also used a base file which loops through the data handed to it by each view, since the format of each XML file is similar.</p>

				<p>Some code lists do not have a description, so in this case the model will just write "no description available". </p>
