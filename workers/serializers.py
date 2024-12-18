from rest_framework import serializers
from .models import Team, Worker

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id']


class WorkerSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Worker
        fields = ['id', 'last_name', 'team', 'salary', 'specialization']
