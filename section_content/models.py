from django.db import models

from app_content.models import (
    Section
)

# Create your models here.
    
"""/
    # Slider
/"""
    
class Slider(models.Model):
    slider_image = models.ImageField(upload_to="static/img/section_image/",blank=True,max_length=191)
    slider_title = models.CharField(max_length=100,blank=True)
    slider_description = models.TextField(blank=True)
    video_link = models.TextField(blank=True)
    video_active =models.BooleanField(default=False)
    section = models.OneToOneField(Section, on_delete=models.CASCADE)

    @property
    def tab_id(self):
        return self.section.site_menu.tab_id



    def __str__(self):
        return self.section.section_name
    
    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"
"""/
    # About
/""" 

class About(models.Model):
    # about_code = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/img/section_image/",blank=True,max_length=191)
    video_link = models.TextField(blank=True)
    video_active =models.BooleanField(default=True)
    about_description = models.TextField(blank=True)
    about_description_end = models.TextField(blank=True)
    section = models.OneToOneField(Section, on_delete=models.CASCADE)

    @property
    def tab_id(self):
        return self.section.site_menu.tab_id

    
    def __str__(self):
        return self.section.section_name
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
    
class AboutList(models.Model):
    list_text = models.TextField(blank=True)
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    def __str__(self):
        return self.list_text

    class Meta:
        verbose_name = "About List"
        verbose_name_plural = "About Lis"


"""/
    # Why Us
/"""  
class WhyUs(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
   
    class Meta:
        verbose_name = "Why Us"
        verbose_name_plural = "Why Us"

    def __str__(self):
        return self.title
    
"""/
    statistics
/"""
class Statistics(models.Model):
    # number, title, section_id
    title = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):  
        return self.title
    
    class Meta:
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"

"""/
    # menu category
/"""

class MenuCategory(models.Model):                                          
    menu_category_name = models.CharField(max_length=100)
    category_id = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu_category_name
    
class MenuItem(models.Model):
    menu_item_name = models.CharField(max_length=100)
    menu_item_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=100)
    menu_item_image = models.ImageField(upload_to="static/img/menu/",blank=True,max_length=191)
    menu_item_description = models.TextField(blank=True)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu_item_name
    
class MenuIngredient(models.Model):
    ingredient_name = models.CharField(max_length=100)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient_name


"""/
    # Testimonials
/"""
class Testimonials(models.Model):
    class Ratings(models.IntegerChoices):
        BAD = 1
        AVERAGE = 2
        GOOD = 3
        VERY_GOOD = 4
        EXCELLENT = 5

    comment = models.TextField(blank=True)
    rating = models.IntegerField(choices=Ratings.choices)
    user_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    user_picture = models.ImageField(upload_to="static/img/testimonial/",blank=True,max_length=191)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

"""
    # Events 
"""
class Events(models.Model):
    event_title = models.CharField(max_length=100)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to="static/img/event/",blank=True,max_length=191)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_title
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

"""/
    # Chef
/"""

class Chef(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="static/img/chef/",blank=True,max_length=191)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
"""/
    # Booking Form Section
/"""

class BookingFormSection(models.Model):
    image = models.ImageField(upload_to="static/img/booking/",blank=True,max_length=191)
    note = models.TextField(blank=True)
    section = models.OneToOneField(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.section.section_name


"""/
    # Gallery
/"""

class Gallery(models.Model):
    image = models.ImageField(upload_to="static/img/gallery/",blank=True,max_length=191)
    note = models.CharField(max_length=250,blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name
    
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

"""/
    # Contact Us
/"""
class ContactUsPageContent(models.Model):
    map_link = models.TextField(blank=True)
    location_name = models.CharField(max_length=100,blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.location_name
    
    class Meta:
        verbose_name = "Contact Us Page Content"
        verbose_name_plural = "Contact Us Page Content"





"""/
    # Company Information
/"""
class CompanyInformation(models.Model):
    company_name = models.CharField(max_length=100)
    logo_text = models.CharField(max_length=30)
    logo_image = models.ImageField(upload_to="static/img/logo/",blank=True,max_length=191)
    address = models.CharField(max_length=250,blank=True)
    email = models.EmailField(max_length=100)
    contact_number = models.CharField(max_length=20)
    working_hours = models.CharField(max_length=100,blank=True)
    closing_date = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.company_name


