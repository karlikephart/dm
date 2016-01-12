# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_auto_20160104_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_rebajas',
            field=models.DecimalField(default=6.99, null=True, max_digits=100, decimal_places=2, blank=True),
        ),
    ]
