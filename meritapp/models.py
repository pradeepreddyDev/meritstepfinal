from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Header(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = "header"
        verbose_name = "header"
        verbose_name_plural = "header"

    def __str__(self):
        return self.title


class Cms(models.Model):
    subtitle = models.CharField(max_length=100)
    sub2title = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "cms"
        verbose_name = "IT Staffing"
        verbose_name_plural = "IT Staffing"

    def __str__(self):
        return self.subtitle


class Gan(models.Model):
    sub1title = models.CharField(max_length=100)
    sub2title = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')
    seconddescription = RichTextField(config_name='awesome_ckeditor')

    class Meta:
        db_table = "gan"
        verbose_name = "gan"
        verbose_name_plural = "Support and Contactus"

    def __str__(self):
        return self.sub1title


class van(models.Model):
    sub1title = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')
    sub3title = models.CharField(max_length=100)
    overview = models.TextField()

    class Meta:
        db_table = "van"
        verbose_name = "Become an Instructor"
        verbose_name_plural = "Become an Instructor"

    def __str__(self):
        return self.sub1title


class Instructor2(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')

    class Meta:
        db_table = "instructor2"
        verbose_name = "Become an Instructor - Items"
        verbose_name_plural = "Become an Instructor - Items"

    def __str__(self):
        return self.title


class Instructor3(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')

    class Meta:
        db_table = "instructor3"
        verbose_name = "Become an Instructor - OUR INSTRUCTORS"
        verbose_name_plural = "Become an Instructor - OUR INSTRUCTORS"

    def __str__(self):
        return self.title


class Cat(models.Model):
    sub1title = models.CharField(max_length=100)
    overview = models.TextField()
    sub3title = models.CharField(max_length=100)
    overview2 = models.TextField()
    overview3 = models.TextField()
    overview4 = models.TextField()
    sub4title = models.CharField(max_length=100)
    thirddescription = RichTextField(config_name='awesome_ckeditor')
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "cat"
        verbose_name = "Corporate Training"
        verbose_name_plural = "Corporate Training"

    def __str__(self):
        return self.sub1title


class Corporate1(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')

    class Meta:
        db_table = "corporate1"
        verbose_name = "Corporate_description"
        verbose_name_plural = "Corporate_description"

    def __str__(self):
        return self.title


class Corporate2(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')

    class Meta:
        db_table = "corporate2"
        verbose_name = "Clients Feedback"
        verbose_name_plural = "Clients Feedback"

    def __str__(self):
        return self.title


class Hom(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    sub1title = models.CharField(max_length=100)
    classroomtraining = models.TextField()
    onlinetraining = models.TextField()
    corporatetraining = models.TextField()
    trending = models.CharField(max_length=100)
    popular = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')
    sub4title = models.CharField(max_length=100)
    overview1 = models.TextField()
    stories = RichTextField(config_name='awesome_ckeditor')
    customername = models.CharField(max_length=100)

    class Meta:
        db_table = "hom"
        verbose_name = "Home Page CMS"
        verbose_name_plural = "Home Page CMS"

    def __str__(self):
        return self.title


class Clientimages(models.Model):
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "clientimages"
        verbose_name = "Home Client Images"
        verbose_name_plural = "Home Client Images"


class Cos(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')

    class Meta:
        db_table = "cos"
        verbose_name = "Course-about"
        verbose_name_plural = "Course-about"

    def __str__(self):
        return self.title


class Staffingimages(models.Model):
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "staffingimages"
        verbose_name = "Client staffingimages"
        verbose_name_plural = "Client staffingimages"


class Courses(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    coursefee = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    enable_popular = models.BooleanField(default=False)
    enable_trending = models.BooleanField(default=False)

    class Meta:
        db_table = "courses"
        verbose_name = "courses"
        verbose_name_plural = "courses"

    def __str__(self):
        return self.title


class Coursedetail(models.Model):
    Courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    liveprojects = models.CharField(max_length=100)
    trainingoptions = models.CharField(max_length=100)
    title3 = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')
    title4 = models.CharField(max_length=100)
    description2 = RichTextField(config_name='awesome_ckeditor')
    title5 = models.CharField(max_length=100)
    description3 = models.CharField(max_length=100)
    title6 = models.CharField(max_length=100)
    title7 = models.CharField(max_length=100)
    title8 = models.CharField(max_length=100)
    cus = models.CharField(max_length=100)

    class Meta:
        db_table = "coursedetail"
        verbose_name = "coursedetail"
        verbose_name_plural = "coursedetail"

    def __str__(self):
        return self.Courses.title + ' > ' + self.title


class Coursedetail2(models.Model):
    Courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    price = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    particulars1 = models.CharField(max_length=100)
    particulars2 = models.CharField(max_length=100)
    particulars3 = models.CharField(max_length=100)
    particulars4 = models.CharField(max_length=100)

    class Meta:
        db_table = "coursedetail2"
        verbose_name = "Course Details - MODES OF TRAINING"
        verbose_name_plural = "Course Details - MODES OF TRAINING"

    def __str__(self):
        return self.Courses.title + ' > ' + self.title


class Course_events(models.Model):
    Courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

    class Meta:
        db_table = "course_events"
        verbose_name = "Course Details - Events"
        verbose_name_plural = "Course Details - Events"

    def __str__(self):
        return self.Courses.title + ' > ' + self.title


class Courseimages(models.Model):
    Courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "courseimages"
        verbose_name = "Course Details - Trusted By Companies Worldwide_images"
        verbose_name_plural = "Course Details - Trusted By Companies Worldwide_images"

    def __str__(self):
        return self.Courses.title + ' > ' + self.title


class Coursecol(models.Model):
    Courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=100)

    class Meta:
        db_table = "coursecol"
        verbose_name = "Course Details - Faq's"
        verbose_name_plural = "Course Details - Faq's"

    def __str__(self):
        return self.Courses.title + ' > ' + self.title


class Customer(models.Model):
    Courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    customer_story = models.CharField(max_length=800)
    customer_title = models.CharField(max_length=100)

    class Meta:
        db_table = "customer"
        verbose_name = "Customer Success Stories"
        verbose_name_plural = "Customer Success Stories"

    def __str__(self):
        return self.Courses.title + ' > ' + self.title


class Fot(models.Model):
    lefttitle = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')
    righttitle = models.CharField(max_length=100)
    description2 = RichTextField(config_name='awesome_ckeditor')

    class Meta:
        db_table = "fot"
        verbose_name = "Footer"
        verbose_name_plural = "Footer"


class Blog1(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    published_by = models.CharField(max_length=100)
    description = RichTextField(config_name='awesome_ckeditor')
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = "blog1"
        verbose_name = "blog"
        verbose_name_plural = "blog"

    def __str__(self):
        return self.title


class Request(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = RichTextField(config_name='awesome_ckeditor')

    class Meta:
        db_table = "request"
        verbose_name = "Request a Free Demo Form"
        verbose_name_plural = "Request a Free Demo Form"

    def __str__(self):
        return 'Name: ' + str(self.name) + ', Email: ' + str(self.email) + ', Message: ' + str(self.message) \
               + ', Phone: ' + str(self.phone)


class Touch(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = RichTextField(config_name='awesome_ckeditor')

    class Meta:
        db_table = "touch"
        verbose_name = "Get in touch with us Form"
        verbose_name_plural = "Get in touch with us Form"

    def __str__(self):
        return 'Name: ' + str(self.name) + ', Email: ' + str(self.email) + ', Message: ' + str(self.message) \
               + ', Phone: ' + str(self.phone)


class Contact1(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = RichTextField(config_name='awesome_ckeditor')

    class Meta:
        db_table = "contact1"
        verbose_name = "Contacted Form"
        verbose_name_plural = "Contacted Form"

    def __str__(self):
        return 'Name: ' + str(self.name) + ', Email: ' + str(self.email) + ', Message: ' + str(self.message) \
               + ', Phone: ' + str(self.phone)


class Modal(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    course = models.CharField(max_length=200)

    class Meta:
        db_table = "modal"
        verbose_name = "live_demo Form"
        verbose_name_plural = "live_demo Form"

    def __str__(self):
        return 'Email: ' + str(self.email) + ', Phone: ' + str(self.phone) + ', course: ' + str(self.course)


class Homecontact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    mode = models.CharField(max_length=200)

    class Meta:
        db_table = "homecontact"
        verbose_name = "Contacted from Home page"
        verbose_name_plural = "Contacted from Home page"

    def __str__(self):
        return 'Name: ' + str(self.name) + 'Email: ' + str(self.email) + ', Phone: ' + str(self.phone) + \
               ', course: ' + str(self.course) + ', Mode: ' + str(self.mode)
