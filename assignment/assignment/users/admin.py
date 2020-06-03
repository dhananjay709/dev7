from django.contrib import admin
from users.models import User, ActivityPeriod

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('real_name', 'id')
    search_fields = ['id']

class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time')
    search_fields = ['id']


admin.site.register(User, UserAdmin)
admin.site.register(ActivityPeriod, ActivityPeriodAdmin)


