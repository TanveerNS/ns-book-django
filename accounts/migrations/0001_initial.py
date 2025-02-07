# Generated by Django 5.1.6 on 2025-02-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('language', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('format', models.CharField(max_length=50)),
            ],
        ),
    ]
