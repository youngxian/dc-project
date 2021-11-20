from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance
STAGE = (
    (1, 1),
    (2, 2),
    (3, 3)
)


# Create your models here.
class RegistrationStage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stage = models.CharField(max_length=10, choices=STAGE)
    # Todo: Encode Slug Field
    slug = models.SlugField(unique=True, blank=True, null=True)
    about_me = models.TextField()
    activation_code = models.CharField(max_length=10)


def suglify_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance(instance, save=False)


pre_save.connect(suglify_pre_save, sender=RegistrationStage)


def suglify_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance(instance, save=True)


post_save.connect(suglify_post_save, sender=RegistrationStage)
