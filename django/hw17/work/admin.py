from django.contrib import admin
from .models import Student



# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name','age','email','birthday')# ,'email','birthday','age'
# admin.site.register(Student)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu')# ,'email','birthday','age'
admin.site.register(Munu)


# def __str__(self):
#          return self.title
# Register your models here.
