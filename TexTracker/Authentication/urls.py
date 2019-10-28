from django.conf.urls import url
from .views import login_restApi, InwardDocumentUploadView


urlpatterns = [
    url('login', login_restApi, name='restApi-login'),
    url('inward_document_upload', InwardDocumentUploadView.as_view()),
]
