from django.db import models

# Create your models here.
class SiteMenu(models.Model):
    tab_name = models.CharField(max_length=100)
    active_status = models.BooleanField(default=False)
    notes = models.TextField()

    def __str__(self):
        return self.tab_name


class Section(models.Model):
    section_name = models.CharField(max_length=100)
    section_title = models.CharField(max_length=100)
    # section_backgroud_name = models.CharField(max_length=191)
    # backgroud_location = models.CharField(max_length=191)
    section_background_photo = models.ImageField(upload_to="cars")
    bg_color = models.CharField(max_length=20)
    notes = models.TextField()
    site_menu = models.OneToOneField(SiteMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.section_name
    

class About(models.Model):
    image_title = models.CharField(max_length=50)
    image_text = models.CharField(max_length=100)
    about_description = models.TextField()
    about_description_end = models.TextField()
    section = models.OneToOneField(Section, on_delete=models.CASCADE)

    
