from rest_framework import generics
from apis.models.bill_models import BillDetail
from apis.serializers.bill_serializer import BillDetailSerializer

class FetchBillDetailView(generics.ListAPIView):
    serializer_class = BillDetailSerializer

    def get_queryset(self):
        queryset = BillDetail.objects.all()
        return queryset
    
    
