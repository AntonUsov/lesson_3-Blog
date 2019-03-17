# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=140, verbose_name=u'Имя',  null=True)
    status = models.TextField(max_length=140, verbose_name=u'Статус',  null=True)
    bio = models.TextField(verbose_name=u'Био',  null=True)
    date_of_birth = models.DateField(verbose_name=u'Дата рождения', null=True)
    user = models.ForeignKey(User, verbose_name=u'Пользователь Django')

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    text = models.TextField(verbose_name=u'Текст')
    pub_date = models.DateTimeField(verbose_name=u'Дата публикации')
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = u'Заметка'
        verbose_name_plural = u'Заметки'

    def __unicode__(self):
        return self.title


class Commit(models.Model):
    revno = models.IntegerField(verbose_name=u'№ ревизии', null=True)
    timestamp = models.DateTimeField(verbose_name=u'Дата коммита')
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = u'Коммит'
        verbose_name_plural = u'Коммиты'


