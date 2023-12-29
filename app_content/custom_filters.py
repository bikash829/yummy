from django import template

register = template.Library()

@register.filter
def custom_range(start=1,number_of_times = 1, skip=1):
    return range(start,number_of_times,skip)