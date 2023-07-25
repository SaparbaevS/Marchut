from django.db import models

class Rok(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    MUSIC = (
        ('Cry of Love', 'Cry of Love'),
        ('Rainbow Bridge', 'Rainbow Bridge'),
        ('The Eternal Fire', 'The Eternal Fire'),
        ('War Heroes', 'War Heroes')
    )

    favorite_music = models.CharField(max_length=50, choices=MUSIC)
    biography = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.surname}"

    def get_absolute_url(self):
        return f"/{self.pk}"
