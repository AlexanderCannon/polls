# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_desc',
            field=models.CharField(default='What is the correct answer', max_length=1000),
            preserve_default=False,
        ),
    ]
