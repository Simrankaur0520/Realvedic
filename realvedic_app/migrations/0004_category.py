# Generated by Django 4.1.5 on 2023-01-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realvedic_app', '0003_remove_product_data_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('category_colour', models.TextField()),
                ('category_image', models.ImageField(upload_to='path/', verbose_name='img')),
            ],
        ),
    ]
