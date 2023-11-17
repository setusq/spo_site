from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Professions(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Professions._meta.fields]

class Skills(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Skills._meta.fields]

class Questions(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    score = models.PositiveIntegerField(verbose_name="Очки")
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE, verbose_name="Навык", related_name="SkillsQuestions")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Questions._meta.fields]


class Model_prof(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    professions = models.ForeignKey(Professions, on_delete=models.PROTECT, verbose_name="Профессия")
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE, verbose_name="Навык", related_name="SkillsProf")
    score = models.PositiveIntegerField(verbose_name="Очки")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Модельная профессия"
        verbose_name_plural = "Модельные профессии"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Model_prof._meta.fields]
    
class Blank(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    image_full = models.ImageField(upload_to='blank/%Y/%m/%d', blank=True, verbose_name="Изображение")
    image_one = models.ImageField(upload_to='blank/%Y/%m/%d', blank=True, verbose_name="Изображение")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Бланк"
        verbose_name_plural = "Бланки"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Blank._meta.fields]
    
class Human(models.Model):
    title = models.TextField(max_length=50, verbose_name="Название")
    avatar = models.ImageField(upload_to='human/%Y/%m/%d', blank=True, verbose_name="Аватар")
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")

    class Meta:
        ordering = ["-title"]
        verbose_name = "Человек"
        verbose_name_plural = "Человечки"

    def __str__(self):
        return self.title
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                for field in Blank._meta.fields]
       