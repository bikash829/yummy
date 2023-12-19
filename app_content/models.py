from django.db import models

# Create your models here.
class SiteMenu(models.Model):
    tab_name = models.CharField(max_length=100)
    active_status = models.BooleanField(default=False)
    tab_id = models.CharField(max_length=100,blank=True,unique=True)
    notes = models.TextField(blank=True)

    

    def __str__(self):
        return self.tab_name

"""/
    # Section
/"""
class Section(models.Model):
    section_name = models.CharField(max_length=100)
    section_title = models.CharField(max_length=100,blank=True)
    section_background_photo = models.ImageField(upload_to="static/img/section_background/",blank=True,max_length=191)
    bg_color = models.CharField(max_length=20,blank=True)
    notes = models.TextField(blank=True)
    site_menu = models.OneToOneField(SiteMenu, on_delete=models.CASCADE, null = True , blank=True)

    def __str__(self):
        return self.section_name
    

# """/
#     # Section
# /"""
# class Section(models.Model):
#     section_name = models.CharField(max_length=100)
#     section_title = models.CharField(max_length=100,blank=True)
#     section_background_photo = models.ImageField(upload_to="static/img/section_background/",blank=True,max_length=191)
#     bg_color = models.CharField(max_length=20,blank=True)
#     notes = models.TextField(blank=True)
#     site_menu = models.OneToOneField(SiteMenu, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.section_name




# """/
#     # Contact Us Form Question from users
# /"""

# class ContactUsMessage(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     subject = models.CharField(max_length=100)
#     message = models.TextField()

#     def __str__(self):
#         return self.name
