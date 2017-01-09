# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='last_name',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
