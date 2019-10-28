from __future__ import unicode_literals
from .models import CustomUser

def CustomUserView(request, id):

    return render(request, 'Client/add-service.html', {'form': inwardTypesForm})
