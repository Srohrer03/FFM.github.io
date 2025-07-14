import React from 'react';

export default function Dashboard() {
  return (
    <div className="flex min-h-screen bg-gray-50">
      {/* Sidebar */}
      <nav className="w-64 h-full bg-blue-900 text-white p-6 space-y-8">
        <h2 className="text-3xl font-bold mb-6">Dashboard</h2>
        <ul className="space-y-4">
          <li>
            <a href="/dashboard/checkbook" className="hover:bg-blue-700 rounded p-2 block">Checkbook</a>
          </li>
          <li>
            <a href="/dashboard/loyalty" className="hover:bg-blue-700 rounded p-2 block">Vendors</a>
          </li>
          <li>
            <a href="/dashboard/kpi" className="hover:bg-blue-700 rounded p-2 block">KPI Settings</a>
          </li>
          <li>
            <a href="/dashboard/capex" className="hover:bg-blue-700 rounded p-2 block">CapEx Planner</a>
          </li>
          <li>
            <a href="/ticket" className="hover:bg-blue-700 rounded p-2 block">Submit Ticket</a>
          </li>
        </ul>
      </nav>
      
      {/* Main Content */}
      <main className="flex-1 p-10">
        <h1 className="text-2xl font-bold mb-8 text-blue-900">Welcome to the Client Dashboard!</h1>
        {/* Add summary cards, charts, or quick info here */}
        <div className="grid grid-cols-2 gap-8">
          <div className="bg-white shadow rounded-lg p-6">
            <h3 className="text-lg font-semibold mb-4">Checkbook Summary</h3>
            {/* Insert checkbook summary content here */}
          </div>
          <div className="bg-white shadow rounded-lg p-6">
            <h3 className="text-lg font-semibold mb-4">Vendor Stats</h3>
            {/* Insert vendor info here */}
          </div>
          {/* Add more cards as needed */}
        </div>
      </main>
    </div>
  );
}

