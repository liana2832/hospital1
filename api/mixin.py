from rest_framework import viewsets

from .permissions import RoleBasPermissionMixin, HasPermissionByAuthenticatedUserRole


class HospitalGenericViewSet(
    RoleBasPermissionMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [HasPermissionByAuthenticatedUserRole]