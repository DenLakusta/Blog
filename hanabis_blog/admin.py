from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from django import forms
from .models import Tag, Post, Author, Reviews, Category

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from hanabis_blog.models import Post




class PostAdminForm(forms.ModelForm):
    body = forms.CharField(label= "Post Body", widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ["title"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ["title"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'get_image')
    list_display_links = ["name"]
    readonly_fields = ('get_image',)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
    get_image.short_description = "Image"

# class ImageAuth(admin.StackedInline):
#     model = Author
#     extra = 1
#

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'parent', 'post', 'date_pub')
    readonly_fields = ('name', 'email')
    list_display_links = ["name"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'draft', 'get_image')
    list_display_links = ["title",]
    list_filter = ['tags', 'date_pub']
    search_fields = ['title', 'tags__title']
    actions = ['publish', 'unpublish']
    inlines = [ReviewInline, ]#ImageAuth
    save_on_top = True
    save_as = True
    form = PostAdminForm
    list_editable = ('draft',)
    # fields = (('tags', 'date_pub', 'auth'), )
    fieldsets = (
        (None, {
           "fields":("body", "image")
        }),
        (None, {
           "fields":(("title", "slug"),)
        }),
        ("Options", {
            "classes":("collapse",),
           "fields":(("tags", "date_pub", "auth", "draft"),)
        }),
    )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Image"

    def unpublish(self, request, queryset):
        """unbublish"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 record was updated"
        else:
            message_bit = f"{row_update} records was updated"
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """publish"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 record was updated"
        else:
            message_bit = f"{row_update} records was updated"
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Publish post'
    publish.allowed_permissions = ('change', )
    unpublish.short_description = 'Unpublish post'
    unpublish.allowed_permissions = ('change',)



admin.site.site_title = "Django Hanabis Engine"
admin.site.site_header = "Django Hanabis Engine"