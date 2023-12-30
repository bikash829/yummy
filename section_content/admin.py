from django.contrib import admin
from django.http.request import HttpRequest

# Register your models here.
from .models import (
    Slider,
    About,
    AboutList,
    WhyUs,
    Statistics,
    MenuCategory,
    MenuItem,
    MenuIngredient,
    Testimonials, #***
    Events,
    Chef,
    BookingFormSection,
    Gallery,
    ContactUsPageContent,
    CompanyInformation,
)

"""/
    # Slider
/"""
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    # list_display = ('get_section_name','title','description','active_status',)

    def has_add_permission(self, request):
        return False
"""/
    # About us
/"""
# admin.site.register(About)
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('get_section_name','video_active',)

    def get_section_name(self, obj):
        return obj.section.section_name
    # get_section_name.short_description = 'Section Name'

"""/
    # About us list
/"""
admin.site.register(AboutList)

"""/
    # Why us
/"""
@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    # inlines = [AboutInline]
    list_display = ('get_section_name','title','icon',)

    def get_section_name(self, obj):
        return obj.section.section_name

    verbose_name = "Why Us"
    max_whyus_records = 3  # Set the maximum number of records
    
    # This will help you to disbale add functionality
    # def has_add_permission(self, request):
    #     return False

    # # This will help you to disable delete functionaliyt
    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_add_permission(self, request):
    # Check if the number of existing records is less than the maximum allowed
        if WhyUs.objects.count() >= self.max_whyus_records:
            return False
        return super().has_add_permission(request)


"""/
    # Statistics
/"""
# admin.site.register(Statistics)
@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    # inlines = [AboutInline]
    list_display = ('title','number',)
    max_records = 3

    def has_add_permission(self, request):
    # Check if the number of existing records is less than the maximum allowed
        if Statistics.objects.count() >= self.max_records:
            return False
        return super().has_add_permission(request)

    # def get_section_name(self, obj):
    #     return obj.section.section_name
    
    # def has_delete_permission(self, request, obj=None):
    #     return False
"""/ 
    Our Menu 
/"""
@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('menu_category_name', 'category_id')
# admin.site.register(MenuCategory)
    
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('menu_item_name', 'menu_category', 'menu_item_price')


@admin.register(MenuIngredient)
class MenuIngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient_name', 'menu_item')
    
"""/
    # Testimonials
/"""
admin.site.register(Testimonials)

"""/
    # Events
/"""
admin.site.register(Events)
    
"""/
    # Chef
/"""
admin.site.register(Chef)
        
"""/
    # Booking Form Section
/"""
admin.site.register(BookingFormSection)
    
"""/
    # Gallery
/"""
admin.site.register(Gallery)
        
"""/
    # Contact Us Page Content
/"""
admin.site.register(ContactUsPageContent)
            
"""/
    # Company Information
/"""
admin.site.register(CompanyInformation)
