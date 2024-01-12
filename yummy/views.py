from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import messages
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

# from reservation.forms import ReservationForm
from section_content.forms import ContactForm, ReservationForm


def index(request):

    context = {
        'site_menu': SiteMenu.objects.all(),
        'section': Section.objects.all(),
        # 'slider': Slider.objects.get(section__id = (Section.objects.get(site_menu__id = (SiteMenu.objects.get(tab_id = 'hero').id)).id)),
        'slider': Slider.objects.get(section__site_menu__tab_id='hero'),
        # 'about': About.objects.all(),
        # 'about': About.objects.get(section__id = (Section.objects.get(site_menu__id = (SiteMenu.objects.get(tab_id = 'about').id)).id)),
        'about': About.objects.get(section__site_menu__tab_id='about'),
        'about_list': AboutList.objects.all(),
        'why_us': {
            'section': Section.objects.get(pk=9),
            'list' : WhyUs.objects.all(),
        }, 
        'statistics': {
            'section': Section.objects.get(pk=10),
            'statistics_detail' : Statistics.objects.all(),
        },
        # 'menu_category': MenuCategory.objects.all(),
        'menu' : {
            'section' : Section.objects.get(site_menu__tab_id='menu'),
            'tab_id' : 'menu',
            'menu_category': MenuCategory.objects.filter(section__site_menu__tab_id='menu'),
            'menu_item': MenuItem.objects.all(),
            'menu_ingredient': MenuIngredient.objects.all(),
            },
        # Testimonials Data 

        'testimonial': {
                'section' :  Section.objects.get(pk=11),
                'clients_testimonial' : Testimonials.objects.all(),
        },
        

        # Events Data

        'events': {
            'section' : Section.objects.get(site_menu__tab_id='events'),
            'tab_id' : 'events',
            'event_contents': Events.objects.all(),
        },
        # 'events': Events.objects.all(),
        
        # Chef Data
        'chefs': {
            'section' : Section.objects.get(site_menu__tab_id='chefs'),
            'tab_id' : 'chefs',
            'chef_infos': Chef.objects.all(),
        },


        # Booking Form Section Data
        'booking_form_section': {
            'section' : Section.objects.get(site_menu__tab_id = 'book-a-table'),
        },
        # 'booking_form_section': BookingFormSection.objects.all(),


        'gallery': Gallery.objects.all(),
        'contact_us_page_content': ContactUsPageContent.objects.all(),
        'company_information': CompanyInformation.objects.get(pk=1),

        # 'reservation_form': ReservationForm(),
        # Reservation form =================================
        'reservation_form': ReservationForm(),
    }

    # menu = SiteMenu.objects.get(tab_id = 'hero')
    # section = Section.objects.get(site_menu__id = (menu.id))
    # slider = Slider.objects.get(section__id = (section.id))

    # print(f"slider: {menu.__dict__}")
    # print(f"section: {section.__dict__}")    
    # print(f"section: {slider.__dict__}")    
    # print(f"section: {context['menu_category'].__dict__}")

    return render(request,'layouts/_base.html',context)


"""/
    # Reservation form =================================
/"""
def reservation_form(request):

    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            # process the data in form.cleaned_data as required
            # 
            reservation_form.save()
            return HttpResponse("Reservation form submitted successfully")
    context = {
        'reservation_form': ReservationForm(),
    }
    return render(request,'layouts/_base.html',context)