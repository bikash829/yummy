from django.contrib import admin

from .models import (
    SiteMenu, 
    Section
    )
# Register your models here.



class SectionInline(admin.StackedInline):
    model = Section
    # inlines = [AboutInline]



@admin.register(SiteMenu)
class MenuAdmin(admin.ModelAdmin):
    # list_display = ('tab_name', 'section_name', 'notes')
    inlines = [SectionInline]

    list_display = ('tab_name', 'get_section_name','active_status','tab_id','id')
    readonly_fields = ('tab_id',)
    ordering = ('id',)
    

    def get_section_name(self, obj):
        # Assuming the SiteMenu has a related Section
        section = Section.objects.get(site_menu=obj)
        return section.section_name if section else ''

    get_section_name.short_description = 'Section Name'

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False




@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    # inlines = [AboutInline]
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False
    

