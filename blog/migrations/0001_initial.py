# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('data_criado', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_publicado', models.DateTimeField(blank=True, null=True)),
                ('autori', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
