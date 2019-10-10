from rest_framework import serializers
from Inward.models import InwardDocument, InwardPendingDocument

class InwardDocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InwardDocument
        fields = "__all__"

class InwardPendingDocumentSerializer(serializers.ModelSerializer):
    client_name = serializers.ReadOnlyField(source='inward.inward_client_id.client_name')
    employee_name = serializers.ReadOnlyField(source='inward.inward_employeeid.employee_name')
    inward_date = serializers.ReadOnlyField(source='inward.inward_date')
    inward_return_period = serializers.ReadOnlyField(source='inward.inward_returnperiod')
    inward_type = serializers.ReadOnlyField(source='inward.inward_type')
    inward_post = serializers.ReadOnlyField(source='inward.inward_posttype')
    doc_status = serializers.ReadOnlyField(source='inward.inward_uploadfilestatus')
    class Meta:
        model = InwardPendingDocument
        fields = ("__all__") #"id", "client_name", "employee_name") #"__all__"
