from typing import Optional
from django.contrib import admin
from django.http import HttpRequest
from blog import models
from django.contrib import messages

# default admin site 변경
class BlogAdminArea(admin.AdminSite):
    # default admin site overriding
    site_header = 'Blog Admin Area'
    login_template = 'blog/admin/login.html' # override

class TestAdminPermissions(admin.ModelAdmin): 
    def has_add_permission(self, request: HttpRequest) -> bool:
        # return super().has_add_permission(request)
        if request.user.groups.filter(name='editors').exists():
            return True
        return False
    
    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        # return super().has_change_permission(request, obj=obj)

        return False
    
    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        if obj != None and request.POST.get('action') == 'delete_selected':
            messages.add_message(request, messages.ERROR,(
                "I really hope you are sure about this!"
            ))
    
        return True

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        # return super().has_view_permission(request, obj=obj)
        return True
    
blog_site = BlogAdminArea(name='BlogAdmin')
blog_site.register(models.Category)
blog_site.register(models.Post, TestAdminPermissions)
admin.site.register(models.Post)

# - --------------------------------------------------------------
# Form으로 field 편집하기
#
# from blog import models
# from django import forms
#
# class PostForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs) -> None:
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['title'].help_text = 'New Help Text'
    
#     class Meta:
#         model = models.Post
#         exclude = ('',) or exclude = ('slug',)
    
# class PostFormAdmin(admin.ModelAdmin):
#     form = PostForm

# admin.site.register(models.Post, PostFormAdmin)


#---------------------------------------------------------------
# 데이터 추가할 때 입력할 필드만 보여주고, fieldsets으로 그룹지음

# TEXT = 'Some text that we can include'

# class PostAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ('Section 1', {
#             'fields': ('title', 'excerpt', ('author', 'slug'),),
#             'description': f'{TEXT}',
#         }),
#         ('section 2',{
#             'fields':('status',),
#             'classes': ('wide',),
#         }),
#     )

# admin.site.register(models.Post, PostAdmin)

# ------------------------------------------------------
# negative 방식으로 model 등록.

# import django.apps

# models = django.apps.apps.get_models()
# print(models)
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

# admin.site.unregister(django.contrib.auth.models.Group)

#---------------------------------------------------------
# 데코레이터

# from blog import models

# # Register your models here.

# @admin.register(models.Post)
# class PostAdmin(admin.ModelAdmin):
#     fields = ['title', 'author']

# ----------------------------------------------------------

# class PostAdmin(admin.ModelAdmin):
#     fields = ['title', 'author']


# admin.site.register(models.Post, PostAdmin)
# admin.site.register(models.Category)

#-----------------------------------------------------------
# default admin site 변경
# class BlogAdminArea(admin.AdminSite):
#     # default admin site overriding
#     site_header = 'Blog Admin Area'
    
# blog_site = BlogAdminArea(name='BlogAdmin')
# blog_site.register(models.Post)

