from django.db import models

class Jazz(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    MUSIC = (
        ("Hello Dolly", 'Hello Dolly'),
        ("Jazz Festival", 'Jazz Festival'),
        ("In Stuttgart", 'In Stuttgart'),
        ("What a Wonderful World", 'What a Wonderful World'),
    )

    favorite_music = models.CharField(max_length=50, choices=MUSIC)
    biography = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.surname}"

    def get_absolute_url(self):
        return f"/{self.pk}"
