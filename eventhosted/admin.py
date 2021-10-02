from django.contrib import admin

from .models import eventdetails, PostImage
# Register your models here.

class PostImageAdmin(admin.StackedInline):
    model=PostImage

@admin.register(eventdetails)
class eventdetailsAdmin(admin.ModelAdmin):
    inLines = [PostImageAdmin]

    class Meta:
        model = eventdetails

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
