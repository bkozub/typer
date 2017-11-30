from rest_framework import serializers

from typer_app.models import Ski_Jumper, Competition


class SkyJumperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ski_Jumper
        fields = ('pk','name', 'surname', 'nationality', 'photo')

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.ReadOnlyField(source='location.location')
    class Meta:
        model = Competition
        fields = ('pk','date', 'location', 'status')






