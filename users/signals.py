# in app go and import signale

from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver



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
            name=user.first_name
        )

post_save.connect(createProfile,sender=User)


# when user profile is deleted the user must also be deleted

def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()
    print('Deleting User!')

post_delete.connect(deleteUser,sender=Profile)