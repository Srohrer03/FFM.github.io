import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './components/LandingPage';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Checkbook from './components/Checkbook';
import VendorLoyalty from './components/VendorLoyalty';
import KPISettingsToggle from './components/KPISettingsToggle';
import CapExPlanner from './components/CapExPlanner';
import TenantTicketForm from './components/TenantTicketForm';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/dashboard/checkbook" element={<Checkbook propertyId={1} />} />
        <Route path="/dashboard/loyalty" element={<VendorLoyalty />} />
        <Route path="/dashboard/kpi" element={<KPISettingsToggle />} />
        <Route path="/dashboard/capex" element={<CapExPlanner propertyId={1} />} />
        <Route path="/ticket" element={<TenantTicketForm propertyId={1} />} />
      </Routes>
    </Router>
  );
}
