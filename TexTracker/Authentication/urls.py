from django.conf.urls import url
from .views import InwardDocumentUploadView, InwardPendingDocumentView, abc


urlpatterns = [
    # url('login', login_restApi, name='restApi-login'),
    url('inward_document_upload', InwardDocumentUploadView.as_view()),
    url('inward_pending_document_list', abc.as_view()),
]
