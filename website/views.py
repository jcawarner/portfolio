from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


def home(request):
	return render(request, 'index.html', {})


def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['jcaprogramming2012@gmail.com'], fail_silently=False)
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
		return redirect('success')


	return render(request, 'contact.html', {'form': form})



def success(request):
	return HttpResponse('Success! Thank you for your message.')


def gui(request):
	return render(request, 'gui.html', {})

def website(request):
	return render(request, 'website.html', {})


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


def freelancing_projects(request, freelancing_project):
	if freelancing_project == 'sbadmin':
		img = 'assets/images/sb_admin_big_mainpage.png'
		img_1 = 'assets/images/sb_admin_servers.png'
		img_2 = 'assets/images/sb_admin_stack_crud.png'
		img_3 = 'assets/images/sb_admin_aws_crud.png'
		summary = "Database Integration Freelance Project"
		service_page = "Services Page"
		stack_crud = "Stack Form Updating the Database"
		aws_crud = "AWS Form Updating the Database"
		description = """This project was created with Python and Django.  This project included Database integraton, template rendering and CRUD operations"""
		service_desc = "Database integration and displaying on a table on the website also hyperlink to update the database"
		stack_desc = "Simple form to update the database"
		aws_desc = "More complex form to update the database on the entire aws entries"
		github = "https://github.com/jcawarner/favorite-quotes"
	return render(request, 'freelance_projects.html', {
										'project':freelancing_project,
										'img': img,
										'img_1':img_1,
										'img_2': img_2,
										'img_3': img_3,
										'summary': summary,
										'service': service_page,
										'stack': stack_crud,
										'aws': aws_crud,
										'description': description,
										'service_desc': service_desc,
										'stack_desc': stack_desc,
										'aws_desc': aws_desc,
										'github':github,
										})

