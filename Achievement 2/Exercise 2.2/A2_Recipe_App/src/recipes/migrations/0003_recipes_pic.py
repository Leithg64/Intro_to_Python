# Generated by Django 4.2.6 on 2023-11-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_remove_recipes_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='pic',
            field=models.ImageField(default='no_image.svg', upload_to='recipes'),
        ),
    ]