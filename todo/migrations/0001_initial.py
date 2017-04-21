# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('todo', models.CharField(max_length=100)),
                ('expire_date', models.DateTimeField(auto_now_add=True)),
                ('todo_sign', models.CharField(max_length=2)),
                ('todo_priority', models.CharField(max_length=2)),
            ],
        ),
    ]
