from rest_framework import serializers
from .models import Women, Article


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ("title", "cat_id")


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = "__all__" # Нельзя использоваться __all__ вместе с exclude и подобным
        exclude = ("text",)
