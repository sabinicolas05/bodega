from rest_framework.routers import DefaultRouter
from apps.registro.api.views import RegisViewSet

router_regis = DefaultRouter()
router_regis.register(prefix="registro", basename="registro", viewset=RegisViewSet)