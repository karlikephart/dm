# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_producto',
            new_name='titulo',
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default='default value'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(default=9.99, max_digits=30, decimal_places=2),
            preserve_default=False,
        ),
    ]
