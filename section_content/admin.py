from django.contrib import admin

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
    Testimonials,
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
admin.site.register(Slider)

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

admin.site.register(Statistics)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(MenuIngredient)
admin.site.register(Testimonials)
admin.site.register(Events)
admin.site.register(Chef)
admin.site.register(BookingFormSection)
admin.site.register(Gallery)
admin.site.register(ContactUsPageContent)
admin.site.register(CompanyInformation)
