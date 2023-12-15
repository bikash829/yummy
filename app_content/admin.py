from django.contrib import admin

from .models import SiteMenu, Section, About
# Register your models here.


# class AboutInline(admin.StackedInline):  # or use admin.TabularInline
#     model = About

# class SectionInline(admin.StackedInline):  # or use admin.TabularInline
#     model = Section
#     inlines = [AboutInline]

# class SiteMenuAdmin(admin.ModelAdmin):
#     inlines = [SectionInline]

# admin.site.register(SiteMenu, SiteMenuAdmin)

class SectionInline(admin.StackedInline):
    model = Section
    extra = 1

class SiteMenuAdmin(admin.ModelAdmin):
    inlines = [SectionInline]

admin.site.register(SiteMenu, SiteMenuAdmin)

class AboutInline(admin.StackedInline):
    model = About
    extra = 1

class SectionAdmin(admin.ModelAdmin):
    inlines = [AboutInline]

admin.site.register(Section, SectionAdmin)