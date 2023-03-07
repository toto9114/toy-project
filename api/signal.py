from django.dispatch import receiver
from django.db.models.signals import post_save
from api.models import Profile
from django.contrib.auth.models import User


def generate_profile_name(user: User):
    return f'user_{user.id}'


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    instance = kwargs['instance']
    if kwargs['created']:
        Profile(user=instance, name=generate_profile_name(instance)).save()
