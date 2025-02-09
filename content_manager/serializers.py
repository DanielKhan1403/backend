from rest_framework import serializers
from .models import Service, PortfolioItem, PortfolioImage, TeamSection, PortfolioCategory, Video


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImage
        fields = ["image"]

class PortfolioCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioCategory
        fields = ["id", "name"]

class PortfolioItemSerializer(serializers.ModelSerializer):
    images = PortfolioImageSerializer(many=True, read_only=True)
    categories = PortfolioCategorySerializer(many=True, read_only=True)  # Отображаем категории с именами

    class Meta:
        model = PortfolioItem
        fields = ["id", "title", "description", "images", "categories"]




class TeamSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSection
        fields = "__all__"

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video_file', 'thumbnail', 'created_at']