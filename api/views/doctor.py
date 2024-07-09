from ..filters import DoctorFilterSet
from ..mixin import HospitalGenericViewSet
from ..models import Doctor, Patient

from rest_framework import mixins
from rest_framework.response import Response
from ..serializers.doctor import (DoctorListSerializer, DoctorRetrieveSerializer, DoctorCreateSerializer,
                                  DoctorUpdateSerializer)
from ..serializers.patient import PatientListSerializer
from django_filters.rest_framework import DjangoFilterBackend


class DoctorView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):

    lookup_field = 'id'

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'specialization']
    filterset_class = DoctorFilterSet

    def get_action_permission(self):
        if self.action in('list', 'retrieve'):
            self.action_permissions = ['view_doctor', ]
        elif self.action == 'list_patient':
            self.action_permissions = ['view_patient', ]

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.all()

        return Doctor.objects.all()

    def list_patient(self, request, id):
        queryset = self.get_queryset().filter(visits__doctor_id=id)

        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)