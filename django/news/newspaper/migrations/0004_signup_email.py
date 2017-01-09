# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_signup_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='email',
            field=models.EmailField(default=b'dummy@dummy.com', max_length=254),
        ),
    ]
