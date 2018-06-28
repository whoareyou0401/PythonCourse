from django.contrib import admin


from t7.models import Stu,Grade


# Register your models here.
class SthInfo(admin.TabularInline):
    module = Stu
    extra = 3

class GradeAdmin(admin.ModelAdmin):
    inlines = [SthInfo]

class StuAdmin(admin.ModelAdmin):
    def is_old_man(self):
        if self.age>=18:
            return "老年人"
        else:
            return "不成熟"

    is_old_man.short_description = "大大"
    list_display = ['name','age',is_old_man]
    list_filter = ['name','age']
    search_fields = ['name']
    list_per_page = 3
    fieldsets = [
        ('基本信息',{"fields":('name','age')}),
        ('成绩', {"fields":('score',)}),
    ]


admin.site.register(Stu,StuAdmin)
# admin.site.register(Grade)