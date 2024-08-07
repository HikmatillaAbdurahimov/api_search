from django.db import models


class Artist(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    create_at=models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class Albom(models.Model):
    title=models.CharField(max_length=50)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Songs(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    albom=models.ForeignKey(Albom,on_delete=models.CASCADE)

    def get_queryset(self):
        return Songs.objects.order_by('id')

    def __str__(self):
        return self.title
