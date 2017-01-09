# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_signup_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='first_name',
            field=models.CharField(max_length=120, unique=True, null=True, blank=True),
        ),
    ]
