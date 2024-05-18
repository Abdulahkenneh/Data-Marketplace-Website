from django.shortcuts import render

# Create your views here.

def homepage(request):

    return render(request,template_name='university/homepage.html')

def education_view(request):

    return render(request,template_name='university/education_view.html')

def research_view(request):

    return render(request,template_name='university/research_view.html')


def innovations_view(request):

    return render(request,template_name='university/innovations_view.html')



def admission_view(request):

    return render(request,template_name='university/admission_view.html')


def campuslife_view(request):

    return render(request,template_name='university/campuslife_view.html')


def news_view(request):

    return render(request,template_name='university/news_view.html')



def alumni_view(request):
    return render(request, template_name='university/alumni_view.html')
