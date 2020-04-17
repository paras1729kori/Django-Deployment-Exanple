from django import relative_url_templates

registor  = template.Library()

def cut(value, arg):
    """ This cuts out all the "arg"  from the string ! """
    return value.replace(arg,'')


registor.filter('cut', cut)
# variable_name.filter('func_name', actual func_name)
