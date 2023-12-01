from django.db import models
from django.contrib.auth.models import User
from mysite.anketa.models import *

class Answers(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    users = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь", related_name="SkillsUser")
    skills = models.ForeignKey(Skills, on_delete=models.PROTECT, verbose_name="Навык", related_name="SkillsAns")
    score = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-title"]
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Answers._meta.fields]

class Sertif(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    users = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Пользователь", related_name="SertifUser")
    blank = models.ForeignKey(Blank, on_delete=models.PROTECT, verbose_name="Бланк", related_name="BlankSertif")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    filled_sertif = models.ImageField(upload_to='serif/%Y/%m/%d', blank=True, verbose_name="Заполненный сертификат")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Sertif._meta.fields]