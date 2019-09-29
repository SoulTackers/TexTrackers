from rest_framework import serializers
from Inward.models import InwardDocument, InwardPendingDocument

class InwardDocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InwardDocument
        fields = "__all__"

class InwardPendingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InwardPendingDocument
        fields = "__all__"
