from django.contrib import admin
from videos.models import Movie, Customer


# Register your models here.


# In the admin page, we can change the view of any model by adding few attributes as shown below.
class MovieAdmin(admin.ModelAdmin):  # Inherit the class from "model-admin" class.
    
    # Use the attribute "fields" to change the order of the fields.
    fields = ["length", "title", "release_year"]

    # add "search_fields" attribute to the model to search a movie using the particular fields.
    search_fields = ["length", "title"]

    # add "list_filter" attibute to see the filters in the right side.
    list_filter = ["release_year", "length", "title"]

    # just create "list_display" attribute to view the required fields in the model.
    list_display = ["title", "length", "release_year"]

    # create "list_editable" attribute to add the fields which are editable in-place. Be careful since everybody can edit and change the values in the table.
    # item present in the "list_display[0]" can not be mentioned in the "list_editable" list.
    list_editable = ["release_year", "length"]


admin.site.register(Movie, MovieAdmin)  # register the "model-admin" with the original model.
admin.site.register(Customer)

