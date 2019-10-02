from django.conf.urls import url
from .views import InwardDocumentUploadView, InwardPendingDocumentView, login_restApi

urlpatterns = [
    url('login', login_restApi, name='restApi-login'),
    url('inward_document_upload', InwardDocumentUploadView.as_view()),
    url('inward_pending_document_list', InwardPendingDocumentView.as_view()),
]
