from django.urls import path
from django.views.generic import TemplateView
from .views import ProjectListView

urlpatterns = [
	# # path('', TemplateView.as_view(
	# 	template_name = "index.html")
	# 	),
	path('', ProjectListView.as_view()),
] 