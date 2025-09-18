from django.contrib import admin

# Register your models here.
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
    search_fields = ('user', 'rating')

