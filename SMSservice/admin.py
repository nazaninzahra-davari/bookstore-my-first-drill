from django.contrib import admin

# Register your models here.
class SmsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'message')
    list_filter = ('phone', 'email', 'message')
    search_fields = ('phone', 'email', 'message')
    list_per_page = 50

