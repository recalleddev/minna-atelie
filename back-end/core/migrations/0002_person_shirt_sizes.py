# Generated by Django 3.0.3 on 2020-02-23 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='shirt_sizes',
            field=models.CharField(choices=[('s', 'small'), ('m', 'medium'), ('l', 'large')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]