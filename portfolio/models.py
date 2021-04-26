"""
Полная база проектов
"""

from django.db import models
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field


class ProjectType(models.Model):
	title = models.CharField(
		max_length=80, 
		verbose_name='Категория проекта',
	)

	description = CKEditor5Field(
		blank=True,
		null=True,
		verbose_name='Описание', 
		config_name='extends'
	)

	def __str__(self):
		return self.title

class SystemInUse(models.Model):
	title = models.CharField(
		max_length=80, 
		verbose_name='Технологический стек',
	)

	description = CKEditor5Field(
		blank=True,
		null=True,
		verbose_name='Описание',
		config_name='extends'
	)

	def __str__(self):
		return self.title

class Project(models.Model):
	title = models.CharField(
		max_length=80, 
		verbose_name='Название',
	)

	project_type = models.ManyToManyField(ProjectType,
		blank=True,
		verbose_name='Категория проекта')

	systems_in_use = models.ManyToManyField(SystemInUse,
		blank=True,
		verbose_name='Технологический стек')

	description = CKEditor5Field(
		null=True,
		blank=True,
		verbose_name='Описание',
		config_name='extends'
	)

	area = models.IntegerField(
		null=True,
		blank=True,
		verbose_name='Площадь в квадратных метрах'
	)

	show_on_main_screen = models.BooleanField(
		default=False,
		verbose_name='Показать на главной странице'
		)

	show_in_portfolio = models.BooleanField(
		default=True,
		verbose_name='Показывать в портфолио')

	image = models.ImageField(blank=True, upload_to='%Y/%m/')

	created = models.DateTimeField(auto_now_add=True)

	updated = models.DateTimeField(auto_now=True)
	updated_by = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		on_delete=models.DO_NOTHING,
	)

	def __str__(self):
		return self.title
