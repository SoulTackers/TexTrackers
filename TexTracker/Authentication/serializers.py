from rest_framework import serializers
from Inward.models import InwardDocument

class InwardDocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InwardDocument
        fields = "__all__"
