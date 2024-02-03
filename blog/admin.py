from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('start_date','category', 'created_on')
    summernote_fields = ('description')

    #  def approve_posts(self, request, queryset):
    #    queryset.update(approved=True)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name', 'email', 'body']
 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
