from django.urls import path
from .views import MonthlyCheckbookLedger, ClientKPISettingsView, CapExForecastView, VendorLoyaltyDashboard, SubmitTenantTicket

urlpatterns = [
    path('checkbook/<int:property_id>/', MonthlyCheckbookLedger.as_view()),
    path('client/kpi-settings/', ClientKPISettingsView.as_view()),
    path('client/capex/', CapExForecastView.as_view()),
    path('vendor/loyalty/', VendorLoyaltyDashboard.as_view()),
    path('tenant/ticket/', SubmitTenantTicket.as_view()),
]
