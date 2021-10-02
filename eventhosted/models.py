from django.db import models

# Create your models here.
class eventdetails(models.Model):
    """docstring for eventdetails."""
    name = models.CharField(max_length=200)
    summary = models.TextField()
    date = models.DateTimeField()
    banner = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name

class PostImage(models.Model):
    post = models.ForeignKey(eventdetails, default=None, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.post.name
