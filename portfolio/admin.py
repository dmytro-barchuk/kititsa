from django.contrib import admin
from .models import Project, ProjectType, SystemInUse

admin.site.register(ProjectType)
admin.site.register(SystemInUse)


class ProjectAdmin(admin.ModelAdmin):
	list_display = [
		'title', 
		# 'area',
		'show_on_main_screen',
		'show_in_portfolio',
		]

	list_editable = [
		'show_on_main_screen',
		'show_in_portfolio',
		]

	# list_filter = ['updated', 'area']

	class Meta:
		model = Project
admin.site.register(Project, ProjectAdmin)


