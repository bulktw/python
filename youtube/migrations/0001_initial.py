# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aollowlist',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('employeeid', models.CharField(max_length=10)),
                ('employeedept', models.CharField(max_length=10)),
                ('employeename', models.TextField()),
                ('purpose', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='data created')),
            ],
        ),
    ]
