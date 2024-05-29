from django import template
register=template.Library()


def swap(value):
    return value.swapcase()

#@register.filter()
@register.filter(name='remove')# BY USING DECORATORS
def remove(value,char):
    return value.replace(char,'')

register.filter('swapcase',swap)
#register.filter('remove',remove)
register.filter('rem',remove)# DECORATORS
