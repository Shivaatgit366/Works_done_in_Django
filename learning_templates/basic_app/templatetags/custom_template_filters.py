# here we will create functions which will be used as the "template filters" in our html files.
# we should create a python package inside the application folder.
# we should register the functions.
# then we can use the custom functions as the template filters.


from django import template
# django template is the package we should use.
# Library is the class from django template.

register = template.Library()  # an object is created from django template library class.
# this object helps to register the function for the filter.

"""
def remove(value, character):  # value means the context dictionary value.
    
    # example: "Hello world"
    # all the "o" will be removed from the string content.

    return value.replace(character, "")



# register the function for the filter using register object.
# give the name for the filter, then give the function name.
register.filter("to_remove", remove)

"""


# using decorator we can do the same thing.
# remove = register.filter(remove)

@register.filter(name="to_remove")
def remove(value, character):  # value means the context dictionary value.
    """
    example: "Hello world"
    all the "o" will be removed from the string content.
    """
    return value.replace(character, "")

