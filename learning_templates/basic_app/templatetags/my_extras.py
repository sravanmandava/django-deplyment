from django import template

register= template.Library()

@register.filter(name='cut')
def cut(value,arg):
#thhis cuts all valuesof string
    return value.replace(arg,'')



#register.filter('cut',cut)
