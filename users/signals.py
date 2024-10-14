from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Manager


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return
    Profile.objects.create(user=instance)
    post_save.connect(create_profile, sender=User)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_update_manager(sender, instance, created, **kwargs):
    if instance.is_staff:
        manager, created = Manager.objects.get_or_create(user=instance)
    else:
        try:
            manager = Manager.objects.get(user=instance)
            manager.delete()
        except ObjectDoesNotExist:
            pass

