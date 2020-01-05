from django.contrib import admin
from djapp.models import coursesData
# Register your models here.
class AdminCourseData(admin.ModelAdmin):
    list_display = ['course_no','course_name','trainer_name',
                    'start_date','start_time','trainer_exp']
admin.site.register(coursesData,AdminCourseData)