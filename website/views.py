from django.shortcuts import render


def home(request):
	return render(request, 'index.html', {})

# def about(request):
# 	return render(request, 'about.html', {})
#
# def webdevelopment(request):
# 	return render(request, 'webdevelopment.html', {})
#
def gui(request):
	return render(request, 'gui.html', {})


def projects(request, project):
	if project == 'Favorite Quotes':
		img = 'assets/images/quotes_small.png'
		summary = "A Favorite Quotes GUI"
		description = "This project was created using Python, Tkinter, and SQLite database. \n Favorite quotes uses" \
					  "an api to grab famous quotes.  This project is fully dynamic.  When user clicks save the program" \
					  "saves that quote to the database.  When user clicks next the program displays the next quote from " \
					  "the api, when user clicks favorite the program grabs a favorotie quote from the data base. also fun" \
					  "functionality when user clicks play the program uses text to speech technology that reads the quote" \
					  "outload to the user"
		github = "https://github.com/jcawarner/favorite-quotes"
	return render(request, 'project.html', {
										'project':project,
										'img': img,
										'summary': summary,
										'description': description,
										'github':github,
										})