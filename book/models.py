from django.db import models

class Book(models.Model):
    title = models.CharField(verbose_name='Введите название книги', max_length=100)
    author = models.CharField(verbose_name='Введите имя автора', max_length=100)
    description = models.TextField(verbose_name='Введите описание книги', blank=True)
    Book_Genre = (
    ('Художественная литература', 'Художественная литература'),
    ('Нехудожественная литература', 'Нехудожественная литература'),
    ('Научная фантастика', 'Научная фантастика'),
    ('Фэнтези', 'Фэнтези'),
    ('Детектив', 'Детектив'),
    ('Биография', 'Биография'),
    ('История', 'История'),
    ('Роман', 'Роман'),
    ('Триллер', 'Триллер'),
    ('Другое', 'Другое'),
    )
    genre = models.CharField(verbose_name='Введите жанр книги', choices=Book_Genre, default='Художественная литература', blank=True)
    pages = models.PositiveIntegerField(verbose_name='Введите количество страниц', default=20, null=True)
    price = models.DecimalField(verbose_name='Введите цену книги', max_digits=5, decimal_places=2)
    published_date = models.DateField(verbose_name='Введите дату публикации книги', null=True, blank=True)
    language = models.CharField(verbose_name='Введите язык книги', max_length=50, blank=True)
    publisher = models.CharField(verbose_name='Введите издательство книги', max_length=100, blank=True)
    mark = models.FloatField(verbose_name='Введите рейтинг книги', default=0.0, null=True)
    isbn = models.CharField(verbose_name='Введите ISBN книги', max_length=20, blank=True)

    def __str__(self):
        return self.title