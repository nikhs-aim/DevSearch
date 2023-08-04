# in app go and import signale

from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

# #@receiver(post_save,sender=Profile)
# def profileUpdated(sender,instance,created,**kwargs):
#     print('Profile Saved!')
#     print('Instance:',instance)
#     print('CREATED:',created)

# post_save.connect(profileUpdated,sender=Profile)



# def deleteUser(sender,instance,**kwargs):
#     print('Deleting User!')

# post_delete.connect(deleteUser,sender=Profile)



# when user is created instantly create a user profile for that user
def createProfile(sender,instance,created,**kwargs):
    print('created user!')
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject='Welcome to DevSearch'
        message='We are glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,

        )

post_save.connect(createProfile,sender=User)


def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created==False:
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()

        
post_save.connect(updateUser,sender=Profile)


# when user profile is deleted the user must also be deleted

def deleteUser(sender,instance,**kwargs):

    try:
        user=instance.user
        user.delete()
        print('Deleting User!')
    except:
        pass
post_delete.connect(deleteUser,sender=Profile)