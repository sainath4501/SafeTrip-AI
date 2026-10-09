import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { TripProvider } from './context/TripContext';
import Navbar from './components/Navbar';

import LandingPage from './pages/LandingPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import ExploreIndiaPage from './pages/ExploreIndiaPage';
import PlaceDetailsPage from './pages/PlaceDetailsPage';
import TripPlannerPage from './pages/TripPlannerPage';
import InteractiveMapPage from './pages/InteractiveMapPage';
import TransportPlannerPage from './pages/TransportPlannerPage';
import SafetyDashboardPage from './pages/SafetyDashboardPage';
import IncidentReportPage from './pages/IncidentReportPage';
import PdfManagerPage from './pages/PdfManagerPage';
import UserDashboardPage from './pages/UserDashboardPage';
import AdminDashboardPage from './pages/AdminDashboardPage';
import MlDashboardPage from './pages/MlDashboardPage';

export default function App() {
  return (
    <AuthProvider>
      <TripProvider>
        <Router>
          <div className="min-h-screen flex flex-col bg-slate-50 text-slate-900">
            <Navbar />
            <main className="flex-1">
              <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/register" element={<RegisterPage />} />
                <Route path="/explore" element={<ExploreIndiaPage />} />
                <Route path="/places/:id" element={<PlaceDetailsPage />} />
                <Route path="/planner" element={<TripPlannerPage />} />
                <Route path="/trip-planner" element={<TripPlannerPage />} />
                <Route path="/recommendations" element={<TripPlannerPage />} />
                <Route path="/map" element={<InteractiveMapPage />} />
                <Route path="/transport" element={<TransportPlannerPage />} />
                <Route path="/safety" element={<SafetyDashboardPage />} />
                <Route path="/incidents" element={<IncidentReportPage />} />
                <Route path="/pdf" element={<PdfManagerPage />} />
                <Route path="/pdf-manager" element={<PdfManagerPage />} />
                <Route path="/dashboard" element={<UserDashboardPage />} />
                <Route path="/admin" element={<AdminDashboardPage />} />
                <Route path="/ml-dashboard" element={<MlDashboardPage />} />
              </Routes>
            </main>

            <footer className="bg-slate-950 text-slate-400 border-t border-slate-800 py-8 mt-16">
              <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs">
                <div>
                  <span className="font-extrabold text-white">SafeTrip AI</span> — An Intelligent AI-Based Indian Tourism Safety, Recommendation & Trip Planning System (MCA Major Project)
                </div>
                <div className="flex items-center gap-4">
                  <span>36 States & UTs</span>
                  <span>•</span>
                  <span>4 Scikit-Learn .pkl Models</span>
                  <span>•</span>
                  <span>Emergency: 112 / 1363</span>
                </div>
              </div>
            </footer>
          </div>
        </Router>
      </TripProvider>
    </AuthProvider>
  );
}
