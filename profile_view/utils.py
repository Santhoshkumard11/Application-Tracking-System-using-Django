
from profile_view.models import Profile


def get_profile_view_model():

    name, address = [], []

    for profile in Profile.objects.all():

        name.append(profile.name)

        address.append(profile.address)

    return zip(name, address)
