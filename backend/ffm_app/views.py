from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from datetime import date
from decimal import Decimal
from .models import CheckbookTransaction, ClientKPISettings, CapitalExpenditureForecast, VendorPerformance, TenantTicket
from .serializers import CheckbookTransactionSerializer, ClientKPISettingsSerializer, CapExForecastSerializer, VendorPerformanceSerializer, TenantTicketSerializer

class MonthlyCheckbookLedger(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, property_id):
        month_start = date.today().replace(day=1)
        txns = CheckbookTransaction.objects.filter(property__id=property_id, date__gte=month_start)
        balance = Decimal('10000.00')
        rows = []
        for t in txns.order_by('date'):
            delta = t.amount if t.type=='credit' else -t.amount
            balance += delta
            rows.append({'date':t.date,'description':t.description,'amount':t.amount,'type':t.type,'source':t.source,'balance':balance})
        return Response({'starting_budget':Decimal('10000.00'),'transactions':rows,'ending_balance':balance})

class ClientKPISettingsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        obj,_ = ClientKPISettings.objects.get_or_create(client=request.user)
        return Response(ClientKPISettingsSerializer(obj).data)
    def post(self, request):
        obj,_ = ClientKPISettings.objects.get_or_create(client=request.user)
        ser = ClientKPISettingsSerializer(obj,data=request.data,partial=True)
        if ser.is_valid(): ser.save(); return Response(ser.data)
        return Response(ser.errors, status=400)

class CapExForecastView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=CapExForecastSerializer
    def get_queryset(self):
        return CapitalExpenditureForecast.objects.filter(property__client=self.request.user)

class VendorLoyaltyDashboard(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        stats = VendorPerformance.objects.filter(property__client=request.user)
        return Response(VendorPerformanceSerializer(stats,many=True).data)

class SubmitTenantTicket(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        ser = TenantTicketSerializer(data=request.data)
        if ser.is_valid(): ser.save(); return Response({'message':'Ticket submitted successfully'})
        return Response(ser.errors, status=400)
