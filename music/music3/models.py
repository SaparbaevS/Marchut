from django.db import models

class Pop(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    MUSIC = (
        ('Just Dance', 'Just Dance'),
        ('Born This Way', 'Born This Way'),
        ('Artpop', 'Artpop'),
        ('Chromatica', 'Chromatica')
    )

    favorite_music = models.CharField(max_length=50, choices=MUSIC)
    biography = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.surname}"

    def get_absolute_url(self):
        return f"/{self.pk}"


