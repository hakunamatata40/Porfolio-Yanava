from django.contrib import admin
from .models import Project, Education, Experience, Skill

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at')
    list_filter = ('technology', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')
    list_filter = ('institution', 'start_date')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date')
    list_filter = ('company', 'start_date')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category',)
    ordering = ('category', 'name')

admin.site.site_header = "Administration du Portfolio"
admin.site.site_title = "Portfolio Admin"