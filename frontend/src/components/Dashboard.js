import React from 'react';
export default function Dashboard() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Client Dashboard</h1>
      <nav className="space-x-4">
        <a href="/dashboard/checkbook">Checkbook</a>
        <a href="/dashboard/loyalty">Vendors</a>
        <a href="/dashboard/kpi">KPI Settings</a>
        <a href="/dashboard/capex">CapEx Planner</a>
        <a href="/ticket">Submit Ticket</a>
      </nav>
    </div>
  );
}
