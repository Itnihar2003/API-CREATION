from rest_framework import serializers
from api.models import students
class studentserialiser(serializers.HyperlinkedModelSerializer):
    student_id=serializers.ReadOnlyField()
    class Meta:
        model = students
        fields = "__all__"

