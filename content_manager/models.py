from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", null=True, blank=True)
    image = models.ImageField(upload_to="services/", blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return self.title


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name


class PortfolioItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название выполненной работы')
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    categories = models.ManyToManyField(PortfolioCategory, related_name="portfolio_items", verbose_name="Категории")

    def __str__(self):
        categories_str = ", ".join([category.name for category in self.categories.all()])
        return f"{self.title} - {categories_str if categories_str else 'Без категории'}"


class PortfolioImage(models.Model):
    portfolio_item = models.ForeignKey(
        PortfolioItem,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Портфолио"
    )
    image = models.ImageField(upload_to='portfolio_images/', verbose_name="Изображение")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return f"Image for {self.portfolio_item.title}"


class TeamSection(models.Model):
    photo = models.ImageField(upload_to='team_person_foto/', verbose_name='Фото сотрудника')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    name = models.CharField(max_length=100, verbose_name='Имя сотрудника')
    specialization = models.CharField(max_length=100, verbose_name='Специализация')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.specialization}'


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
