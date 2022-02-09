from rest_framework import serializers

from . import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = (
            "id",
            "student_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "major",
            "college",
            "notes",
        )
