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


admin.site.register(Slider)

admin.site.register(About)
admin.site.register(AboutList)


@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    # inlines = [AboutInline]
    verbose_name = "Why Us"
    
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False

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
