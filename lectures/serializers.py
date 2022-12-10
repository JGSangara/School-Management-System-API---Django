from rest_framework.serializers import ModelSerializer
from .models import Lecture

class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'slides_url')