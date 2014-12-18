from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    type_of_article = (
        ('AR', 'Article'),
        ('IN', 'Incident'),
        ('RE', 'Ressource'),
        ('DI', 'Discussion'),
    )
    category = models.CharField(max_length=2, choices=type_of_article, default='AR')

    def __unicode__(self):
        return self.name


