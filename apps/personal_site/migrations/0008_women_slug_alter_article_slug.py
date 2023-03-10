# Generated by Django 4.1.6 on 2023-02-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("personal_site", "0007_alter_women_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="women",
            name="slug",
            field=models.SlugField(max_length=100, null=True, verbose_name="URL-путь"),
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(
                max_length=80, null=True, unique=True, verbose_name="Путь URL"
            ),
        ),
    ]
