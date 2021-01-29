import graphene
from graphene_django import DjangoObjectType
from .models import Profile


class ProfileType(DjangoObjectType):

    class Meta:
        model = Profile
        fields = ('id', 'name', 'address')


class Query(graphene.ObjectType):

    profile = graphene.List(ProfileType)

    def resolve_profile(self, info):
        # add your business logic
        
        return Profile.objects.all()


schema = graphene.Schema(query=Query)
