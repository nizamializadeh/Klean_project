from django.contrib import admin
from .models import Carusel, Service,Project,Category,Blog,Comment, Tag


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status', 
        'updated_at',
    )
    
    list_filter = ('status',  )
    list_editable = (
        'title',
        'status', 
    )



# class ProductAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#     list_display = (
#         'pk',
#         'title',
#         'cover_image',
#         'price',
#         'stock',
#         'slug',
#         'is_home',
#         'status', 
#         'updated_at',
#     )
#     list_filter = ('status', )
#     list_editable = (
#         'title',
#         'is_home',
#         'status', 
#     )
admin.site.register(Carusel)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
