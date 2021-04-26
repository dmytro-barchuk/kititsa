"""
Приложение для отображения всех средств связи
Задумка в том, чтобы если есть иконка - показывать ее
Поля не ограничены, т.к. специализированные поля делать 
под максимум 10 записей - нецелесообразно
"""

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class ContactInfo(models.Model):
	title = models.CharField(
		max_length=30, 
		verbose_name='Название средства связи',
	)

	icon = models.ImageField(
		upload_to="",
		blank=True,
		null=True,
	)

	contact = models.CharField(
		max_length=150, 
		verbose_name='Сам контакт',
	)

	def __str__(self):
		return self.title

class HelloSection(models.Model):
	text=CKEditor5Field('Текст приветствия', config_name='extends')

	def __str__(self):
		return "Текст на главной странице"

class AboutSection(models.Model):
	text=CKEditor5Field('Текст About', config_name='extends')

	def __str__(self):
		return self.text[:50]