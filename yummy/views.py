from django.shortcuts import render

from app_content.models import (
    SiteMenu, 
    Section
    )
from section_content.models import (
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

def index(request):

    context = {
        'site_menu': SiteMenu.objects.all(),
        'section': Section.objects.all(),
        'slider': Slider.objects.all(),
        'about': About.objects.all(),
        'about_list': AboutList.objects.all(),
        'why_us': WhyUs.objects.all(),
        'statistics': Statistics.objects.all(),
        'menu_category': MenuCategory.objects.all(),
        'menu_item': MenuItem.objects.all(),
        'menu_ingredient': MenuIngredient.objects.all(),
        'testimonials': Testimonials.objects.all(),
        'events': Events.objects.all(),
        'chef': Chef.objects.all(),
        'booking_form_section': BookingFormSection.objects.all(),
        'gallery': Gallery.objects.all(),
        'contact_us_page_content': ContactUsPageContent.objects.all(),
        'company_information': CompanyInformation.objects.all(),
    }

    return render(request,'layouts/_base.html',context)