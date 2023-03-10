# Generated by Django 4.1.6 on 2023-02-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("personal_site", "0012_remove_article_image_articleimages_caption_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                related_name="tags",
                to="personal_site.articletags",
                verbose_name="Тэги",
            ),
        ),
    ]
