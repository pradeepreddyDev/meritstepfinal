from django.shortcuts import render, redirect
from meritapp.forms import RequestForm, TouchForm, Contact1Form, ModalForm, HomecontactForm

from meritapp.models import Cms, Gan, van, Cat, Hom, Fot, Cos, Staffingimages, Instructor2, Instructor3, Corporate1, \
    Corporate2, Courses, Coursedetail, Coursedetail2, Course_events, Courseimages, Coursecol, Customer, Header, \
    Clientimages, Blog1


def index(request):
    index = Hom.objects.get(id=1)
    footer = Fot.objects.get(id=1)
    popular_course = Courses.objects.filter(enable_popular=True)
    trending_course = Courses.objects.filter(enable_trending=True)
    clientimages = Clientimages.objects.all()
    blog1 = Blog1.objects.all()
    return render(request, "index.html", {'index': index, 'footer': footer, 'clientimages': clientimages,
                                          'popular_course': popular_course, 'trending_course': trending_course,
                                          'blog1': blog1})


def courses(request):
    courses = Cos.objects.get(id=1)
    courses1 = Courses.objects.all()
    footer = Fot.objects.get(id=1)
    header = Header.objects.get(id=1)
    return render(request, "courses.html", {'courses': courses, 'courses1': courses1, 'footer': footer,
                                            'header': header})


def course_details(request, id):
    coursedetail = Coursedetail.objects.get(Courses_id=id)
    coursedetail2 = Coursedetail2.objects.filter(Courses_id=id)
    course_events = Course_events.objects.filter(Courses_id=id)
    courseimages = Courseimages.objects.filter(Courses_id=id)
    coursecol = Coursecol.objects.filter(Courses_id=id)
    customer = Customer.objects.filter(Courses_id=id)
    footer = Fot.objects.get(id=1)
    return render(request, "course_details.html", {'coursedetail': coursedetail, 'coursedetail2': coursedetail2,
                                                   'course_events': course_events, 'courseimages': courseimages,
                                                   'coursecol': coursecol, 'customer': customer, 'footer': footer})


def corporate(request):
    courses = Cos.objects.get(id=3)
    corporate = Cat.objects.get(id=1)
    corporate1 = Corporate1.objects.all()
    corporate2 = Corporate2.objects.all()
    footer = Fot.objects.get(id=1)
    header = Header.objects.get(id=2)
    courses1 = Courses.objects.all()
    return render(request, "corporate.html", {'courses': courses, 'corporate': corporate, 'corporate1': corporate1,
                                              'corporate2': corporate2, 'footer': footer, 'header': header,
                                              'courses1': courses1})


def instructor(request):
    courses = Cos.objects.get(id=3)
    instructor = van.objects.get(id=1)
    instructor2 = Instructor2.objects.all()
    instructor3 = Instructor3.objects.all()
    footer = Fot.objects.get(id=1)
    header = Header.objects.get(id=3)
    courses1 = Courses.objects.all()
    return render(request, "instructor.html", {'courses': courses, 'instructor': instructor, 'instructor2': instructor2,
                                               'instructor3': instructor3, 'footer': footer, 'header': header,
                                               'courses1': courses1})


def support(request):
    courses = Cos.objects.get(id=3)
    support = Gan.objects.get(id=1)
    footer = Fot.objects.get(id=1)
    header = Header.objects.get(id=4)
    courses1 = Courses.objects.all()
    return render(request, "support.html", {'courses': courses, 'support': support, 'footer': footer, 'header': header,
                                            'courses1': courses1})


def staffing(request):
    courses = Cos.objects.get(id=3)
    staffing = Cms.objects.get(id=1)
    staffingimages = Staffingimages.objects.all()
    footer = Fot.objects.get(id=1)
    header = Header.objects.get(id=6)
    courses1 = Courses.objects.all()
    return render(request, "staffing.html", {'courses': courses, 'staffing': staffing, 'staffingimages': staffingimages, 'footer': footer,
                                             'header': header, 'courses1': courses1})


def blog(request):
    footer = Fot.objects.get(id=1)
    header = Header.objects.get(id=5)
    blog1 = Blog1.objects.all()
    courses1 = Courses.objects.all()
    return render(request, "blog.html", {'footer': footer, 'header': header, 'blog1': blog1, 'courses1': courses1})


def blog_detail(request):
    footer = Fot.objects.get(id=1)
    header = Header.objects.get(id=8)
    blog1 = Blog1.objects.all()
    courses1 = Courses.objects.all()
    return render(request, "blog_detail.html", {'footer': footer, 'header': header, 'blog1': blog1,
                                                'courses1': courses1})


def contact(request):
    contact = Gan.objects.get(id=2)
    footer = Fot.objects.get(id=1)
    header = Header.objects.get(id=7)
    courses1 = Courses.objects.all()
    return render(request, "contact.html",
                  {'contact': contact, 'footer': footer, 'header': header, 'courses1': courses1})


def send(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('contact/')
    else:
        return render(request, "meritapp/request.html")


def send1(request):
    if request.method == "POST":
        form = TouchForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    else:
        return render(request, "meritapp/csection.html")


def contact1(request):
    if request.method == "POST":
        form = Contact1Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('contact/')
    else:
        return render(request, "meritapp/contact.html")


def modal(request):
    if request.method == "POST":
        form = ModalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('contact/')
    else:
        return render(request, "meritapp/models.html")


def homecontact(request):
    if request.method == "POST":
        form = HomecontactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('contact/')
    else:
        return render(request, "meritapp/models.html")
