from django.contrib.auth.models import User
from django.db.models.signals import post_save
# signal nomi, post_delete, post_init, post_migrate degan signallar ham bor
from django.dispatch import receiver
# @receiver(<signal_nomi>, **kwargs)

from .models import Profile


@receiver(post_save, sender=User) # Agar User modelga biror bir ozgartirish kiritilsa
def create_profile(sender, instance, created, **kwargs):
    """
    yani biror user yaratilganda nimadir amallar bajarishimiz uchun
    """
    if created: # yani rostan ham biror user create bolsa yani yaratilsa
        Profile.objects.create(user=instance) # osha yaratilgan userni biz instance orqali belgilab olyapmiz


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    bu holda esa biz sazdat emas shunchaki ozgartirganda qiladigan amallarimizni yozamiz
    """
    instance.profile.save() # instance bu yerda ozgartirish kiritilgan user object
