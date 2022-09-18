from .models import BatchRunModel
from rest_framework import serializers

class BatchRunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BatchRunModel
        fields = "url queries results owner id".split()
        read_only_fields = ["results"]