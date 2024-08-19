from django.urls import path
from .views import home
from django.urls import include

app_name = 'recipes'  

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('sales.urls'))
]