# Generated by Django 3.2.9 on 2021-12-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StarWarsApp', '0007_alter_personaje_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaje',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='static/images/BD'),
        ),
    ]
