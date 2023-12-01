from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse


def cfg_assets_root(request):

    if request.user.is_authenticated:
        if request.user.groups.filter(name='Управляющий').exists():
            sidebar = [

                {
                    'name': 'пакет 1',
                    'color': 'text-danger',
                     'children': [
                         {'name': 'Машинки', 'url': reverse('car:MyCar')},
                    ]
                },
                {
                    'name': 'пакет 2',
                    'color': 'text-warning',
                    'children': [
                        {'name': 'Вертолеты', 'url': reverse('helicopter:MyHelicopter')},
                    ]
                },
                {
                    'name': 'Анкета',
                    'color': 'text-warning',
                    'children': [
                        {'name': 'Профессии', 'url': reverse('anketa:professions')},
                        {'name': 'Скиллы', 'url': reverse('anketa:skills')},
                        {'name': 'Вопросы', 'url': reverse('anketa:questions')},
                        {'name': 'Модельная профессия', 'url': reverse('anketa:model_prof')},
                        {'name': 'Бланк', 'url': reverse('anketa:blank')},
                        {'name': 'Люди', 'url': reverse('anketa:human')},
                    ]
                },
                                {
                    'name': 'Сертификат',
                    'color': 'text-success',
                    'children': [
                        {'name': 'Сертификат', 'url': reverse('testik:Sertif')},
                    ]
                },
                
            ]
        else: sidebar = [{
            'name': 'пакет 2',
            'color': 'text-warning',
            'children': [
                {'name': 'Вертолеты', 'url': reverse('helicopter:MyHelicopter')},
            ]
            }]
    else: sidebar = []

    return { 'ASSETS_ROOT' : settings.ASSETS_ROOT, 'SIDEBAR':  sidebar}

