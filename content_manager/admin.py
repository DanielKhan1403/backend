from django.contrib import admin
from .models import PortfolioItem, PortfolioImage, Service, TeamSection, PortfolioCategory, Video


# Register your models here.



class PortfolioImageInline(admin.TabularInline):  # Или admin.StackedInline для вертикального отображения
    model = PortfolioImage
    extra = 1  # Количество пустых форм для загрузки новых изображений

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]
    list_display = ['title', 'description']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
    search_fields = ("title",)

@admin.register(TeamSection)
class TeamSectionAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization")
    search_fields = ("name", "specialization")


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'video_file', 'thumbnail')
    search_fields = ('title', 'description')