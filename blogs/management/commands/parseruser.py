# -*- coding: utf-8 -*-
from optparse import make_option

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
# from __future__ import unicode_literals
from django.db import models

from blogs.models import User as BlogUser, Commit
from blogs.parser import Parser


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--file_path',
            # action='store_true',
            dest='file_path',
            # default=False,
            help=''),
        )

    def handle(self, *args, **options):
        src = options.get('file_path')
        if not src:
            print u'Укажите параметр --file_path'
        parser1 = Parser()
        log = parser1.open_file(src)
        print u'файл получен'
        if log:
            commit_list = parser1.new_commit_list(log)
            for commit in commit_list:
                print commit
                if not User.objects.filter(username=commit['username']).exists():
                    new_django_user = User.objects.create(username=commit['username'], password=commit['username'])
                    new_django_user.save()
                    if not BlogUser.objects.filter(name=commit['username']).exists():
                        new_user = BlogUser.objects.create(name=commit['username'], user=new_django_user)
                        new_user.save()
                    else:
                        new_user = BlogUser.objects.get(name=commit['username'])
                        new_user.user = new_django_user
                        new_user.save()
                else:
                    new_user = BlogUser.objects.get(name=commit['username'])

                if not Commit.objects.filter(revno=commit['revno']).exists():
                    new_commit = Commit.objects.create(revno=commit['revno'], user=new_user, timestamp=commit['timestamp'])
                    new_commit.save()

