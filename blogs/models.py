# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=140, verbose_name=u'Имя')
    status = models.TextField(max_length=140, verbose_name=u'Статус')
    bio = models.TextField(verbose_name=u'Био')
    date_of_birth = models.DateField(verbose_name=u'Дата рождения')

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



