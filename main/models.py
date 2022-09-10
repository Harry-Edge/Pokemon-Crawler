from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    api_id = models.IntegerField()
    is_legendary = models.BooleanField(default=False)
    is_mythical = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Pokemon'
