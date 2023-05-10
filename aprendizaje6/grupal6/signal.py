from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def agregar_grupo(sender, instance, **kwargs):
    post_save.disconnect(agregar_grupo, sender=sender)
    if instance.is_superuser: instance.groups.add(Group.objects.get(name='administrador'))
    elif instance.is_staff: instance.groups.add(Group.objects.get(name='staff'))
    else: instance.groups.add(Group.objects.get(name='normal'))

    if instance.is_superuser and not instance.is_staff: instance.is_staff = True
    
    instance.save()
    post_save.connect(agregar_grupo, sender=sender)

   