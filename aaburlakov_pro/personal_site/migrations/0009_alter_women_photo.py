# Generated by Django 4.1.6 on 2023-02-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("personal_site", "0008_women_slug_alter_article_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="women",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="photos/%Y/%m/%d/"
            ),
        ),
    ]
