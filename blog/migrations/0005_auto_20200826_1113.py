# Generated by Django 3.1 on 2020-08-26 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200826_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.FileField(upload_to=''),
        ),
    ]
