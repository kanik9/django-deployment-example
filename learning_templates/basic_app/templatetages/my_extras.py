from django import template

register  = template.Library()


"""
Method 2 :By using Decaroter

@register.filter(name='cut')

"""
def cut(value,arg):
    """
        This  cuts out all values of "arg" from the string!
    """
    return vlue.replace(arg,'')

# Method 1 : traditional method
register.filter('cut',cut)