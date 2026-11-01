import React, { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import {
  ShieldCheck,
  MapPin,
  Calendar,
  Train,
  AlertTriangle,
  FileText,
  Cpu,
  LayoutDashboard,
  User,
  LogOut,
  LogIn,
  UserPlus,
  Sparkles,
  Menu,
  X,
  ChevronRight,
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useTrip } from '../context/TripContext';

export default function Navbar() {
  const { user, logout } = useAuth();
  const { customTripBasket } = useTrip();
  const location = useLocation();
  const navigate = useNavigate();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  // Close mobile drawer on route changes
  useEffect(() => {
    setMobileMenuOpen(false);
  }, [location.pathname]);

  // Lock body scroll when mobile drawer is open
  useEffect(() => {
    if (mobileMenuOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [mobileMenuOpen]);

  // Close drawer on Escape key
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') setMobileMenuOpen(false);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const primaryNavItems = [
    { to: '/', label: 'Home', icon: Sparkles },
    { to: '/planner', label: 'AI Trip Planner', icon: Calendar, badge: 'Smart' },
    { to: '/map', label: 'Interactive Map', icon: MapPin },
    { to: '/transport', label: 'Transport & Metro', icon: Train },
    { to: '/safety', label: 'Safety AI', icon: ShieldCheck },
    { to: '/incidents', label: 'Incidents', icon: AlertTriangle },
    { to: '/pdf', label: 'PDF Hub', icon: FileText },
    { to: '/ml-dashboard', label: 'ML Research', icon: Cpu },
    { to: '/admin', label: 'Admin', icon: LayoutDashboard },
  ];

  const isActive = (path) => {
    if (path === '/') return location.pathname === '/';
    return location.pathname.startsWith(path);
  };

  return (
    <>
      <header className="sticky top-0 z-50 transition-all duration-300">
        {/* Accent Glow Line along top edge */}
        <div className="h-[2px] w-full bg-gradient-to-r from-cyan-500 via-sky-400 to-indigo-500 shadow-[0_0_10px_rgba(56,189,248,0.7)]" />

        {/* Main Navbar Bar with Glassmorphic Backdrop */}
        <div className="bg-slate-950/85 backdrop-blur-xl border-b border-white/[0.08] text-white shadow-xl shadow-black/20">
          <div className="max-w-7xl mx-auto px-4 sm:px-6">
            <div className="flex items-center justify-between h-16 gap-3">
              
              {/* Brand Logo */}
              <Link to="/" className="flex items-center gap-3 group shrink-0 select-none">
                <div className="relative">
                  <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-cyan-400 via-sky-500 to-blue-600 flex items-center justify-center shadow-lg shadow-sky-500/25 ring-1 ring-white/20 group-hover:scale-105 group-hover:shadow-sky-400/40 transition-all duration-300">
                    <ShieldCheck className="w-5 h-5 text-white drop-shadow" />
                  </div>
                  {/* Subtle live radar ping */}
                  <span className="absolute -top-1 -right-1 flex h-2.5 w-2.5">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500 border border-slate-950"></span>
                  </span>
                </div>

                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-extrabold text-lg tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-300 bg-clip-text text-transparent group-hover:brightness-110 transition">
                      SafeTrip <span className="bg-gradient-to-r from-sky-400 to-cyan-300 bg-clip-text text-transparent">AI</span>
                    </span>
                    <span className="inline-flex items-center px-1.5 py-0.5 rounded-full text-[9px] font-bold tracking-wide uppercase bg-sky-500/10 text-sky-300 border border-sky-500/30 backdrop-blur-sm">
                      India
                    </span>
                  </div>
                  <p className="text-[10px] text-slate-400 tracking-wide font-medium hidden sm:block">
                    Plan Smarter • Travel Safer
                  </p>
                </div>
              </Link>

              {/* Desktop Nav Links - Clean & Uniform without arbitrary highlighting (DESKTOP >= 1280px) */}
              <nav className="hidden xl:flex items-center gap-1">
                {primaryNavItems.map((item) => {
                  const Icon = item.icon;
                  const active = isActive(item.to);
                  return (
                    <Link
                      key={item.to}
                      to={item.to}
                      className={`relative flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl text-xs font-medium transition-all duration-200 group ${
                        active
                          ? 'bg-gradient-to-r from-sky-500/20 via-cyan-500/15 to-blue-500/20 text-sky-200 border border-sky-400/30 shadow-[0_0_15px_rgba(56,189,248,0.2)] font-semibold'
                          : 'text-slate-300 hover:text-white hover:bg-white/[0.06] border border-transparent'
                      }`}
                    >
                      <Icon
                        className={`w-3.5 h-3.5 transition-colors duration-200 ${
                          active
                            ? 'text-sky-400'
                            : 'text-slate-400 group-hover:text-sky-300'
                        }`}
                      />
                      <span>{item.label}</span>
                      
                      {item.badge && !active && (
                        <span className="text-[9px] px-1 py-0.2 rounded bg-sky-500/20 text-sky-300 font-bold border border-sky-500/30">
                          {item.badge}
                        </span>
                      )}

                      {/* Active bottom micro-glow pill */}
                      {active && (
                        <span className="absolute bottom-0 left-1/2 -translate-x-1/2 w-4 h-[2px] bg-sky-400 rounded-full shadow-[0_0_8px_#38bdf8]" />
                      )}
                    </Link>
                  );
                })}
              </nav>

              {/* Right Side: Trip Basket + Auth/Profile + Mobile Hamburger */}
              <div className="flex items-center gap-2 sm:gap-3">
                {/* Trip Basket Button */}
                {customTripBasket.length > 0 && (
                  <button
                    onClick={() => navigate('/planner')}
                    className="relative flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-gradient-to-r from-emerald-500/15 to-teal-500/15 border border-emerald-500/30 text-emerald-300 text-xs font-semibold hover:bg-emerald-500/25 hover:border-emerald-500/50 hover:shadow-[0_0_15px_rgba(16,185,129,0.25)] transition-all duration-200"
                  >
                    <Calendar className="w-3.5 h-3.5 text-emerald-400" />
                    <span className="hidden sm:inline">Trip Basket</span>
                    <span className="px-1.5 py-0.5 rounded-full bg-emerald-500 text-slate-950 text-[10px] font-extrabold shadow-sm">
                      {customTripBasket.length}
                    </span>
                  </button>
                )}

                {/* User State (Desktop & Tablet >= 768px: hidden on mobile < md to prevent navbar overflow) */}
                {user ? (
                  <div className="hidden md:flex items-center gap-2">
                    <Link
                      to="/dashboard"
                      className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900/90 hover:bg-slate-850 border border-slate-700/80 hover:border-slate-600 text-xs font-medium text-slate-200 shadow-inner transition-all duration-200 group"
                    >
                      <div className="w-6 h-6 rounded-lg bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center text-[11px] font-bold text-white shadow-sm ring-1 ring-white/20">
                        {user.full_name ? user.full_name[0].toUpperCase() : 'U'}
                      </div>
                      <span className="max-w-[100px] truncate text-slate-100 font-semibold hidden md:inline">
                        {user.full_name}
                      </span>
                      <span
                        className={`px-1.5 py-0.5 rounded-md text-[9px] font-bold tracking-wider uppercase ${
                          user.role === 'ADMIN'
                            ? 'bg-amber-400/15 text-amber-300 border border-amber-400/30 shadow-[0_0_8px_rgba(251,191,36,0.2)]'
                            : 'bg-sky-400/15 text-sky-300 border border-sky-400/30'
                        }`}
                      >
                        {user.role}
                      </span>
                    </Link>

                    <button
                      onClick={() => {
                        logout();
                        navigate('/');
                      }}
                      title="Logout"
                      className="p-2 rounded-xl bg-slate-900/90 hover:bg-rose-500/20 hover:text-rose-300 hover:border-rose-500/30 text-slate-400 border border-slate-700/80 transition-all duration-200"
                    >
                      <LogOut className="w-4 h-4" />
                    </button>
                  </div>
                ) : (
                  <div className="hidden md:flex items-center gap-2">
                    <Link
                      to="/login"
                      className="flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-white/[0.04] hover:bg-white/[0.08] text-slate-200 hover:text-white border border-white/10 hover:border-white/20 text-xs font-semibold backdrop-blur-sm transition-all duration-200"
                    >
                      <LogIn className="w-3.5 h-3.5 text-sky-400" />
                      <span>Login</span>
                    </Link>
                    <Link
                      to="/register"
                      className="flex items-center gap-1.5 px-4 py-1.5 rounded-xl bg-gradient-to-r from-sky-500 via-blue-600 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white text-xs font-bold shadow-lg shadow-sky-500/25 hover:shadow-sky-400/40 hover:scale-[1.02] active:scale-[0.98] border border-white/20 transition-all duration-200"
                    >
                      <UserPlus className="w-3.5 h-3.5" />
                      <span className="hidden sm:inline">Sign Up</span>
                    </Link>
                  </div>
                )}

                {/* Mobile & Tablet Hamburger Toggle Button */}
                <button
                  type="button"
                  onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                  className="xl:hidden p-2 rounded-xl bg-slate-900/80 hover:bg-slate-800 active:bg-slate-700 text-slate-200 hover:text-white border border-slate-700/80 shadow-md transition-all duration-200 cursor-pointer min-w-[42px] min-h-[42px] flex items-center justify-center shrink-0"
                  aria-label={mobileMenuOpen ? 'Close Navigation Menu' : 'Open Navigation Menu'}
                  aria-expanded={mobileMenuOpen}
                >
                  {mobileMenuOpen ? (
                    <X className="w-6 h-6 text-sky-400" />
                  ) : (
                    <Menu className="w-6 h-6 text-slate-200" />
                  )}
                </button>
              </div>

            </div>
          </div>

          {/* Secondary Tablet/Laptop Quick Horizontal Scroll Bar (when screen is < 1280px but >= 768px) */}
          <div className="hidden md:flex xl:hidden items-center gap-1 overflow-x-auto px-4 py-2 border-t border-white/[0.06] bg-slate-900/60 no-scrollbar">
            {primaryNavItems.map((item) => {
              const Icon = item.icon;
              const active = isActive(item.to);
              return (
                <Link
                  key={item.to}
                  to={item.to}
                  className={`flex items-center gap-1.5 px-3 py-1 rounded-xl text-xs font-medium whitespace-nowrap transition-all duration-200 ${
                    active
                      ? 'bg-sky-500/20 text-sky-300 border border-sky-500/30 font-semibold'
                      : 'text-slate-300 hover:text-white hover:bg-white/[0.06]'
                  }`}
                >
                  <Icon className="w-3.5 h-3.5 text-sky-400" />
                  <span>{item.label}</span>
                </Link>
              );
            })}
          </div>
        </div>
      </header>

      {/* Professional Slide-over Navigation Drawer for Mobile/Tablet (< 1280px) */}
      {/* Placed outside header to escape backdrop-filter containing block constraint */}
      {mobileMenuOpen && (
        <div className="xl:hidden fixed inset-0 z-[9999] flex justify-end">
          {/* Backdrop with smooth blur and fade - clicking outside closes drawer */}
          <div
            onClick={() => setMobileMenuOpen(false)}
            className="fixed inset-0 bg-slate-950/80 backdrop-blur-sm transition-opacity duration-300 animate-fadeIn"
            aria-hidden="true"
          />

          {/* Drawer Container */}
          <aside
            className="relative z-10 w-[85vw] max-w-sm h-full h-[100dvh] bg-slate-950 border-l border-white/10 shadow-2xl flex flex-col justify-between overflow-y-auto overscroll-contain animate-slideLeft"
            aria-label="Mobile Navigation Drawer"
          >
            {/* Drawer Top / Header */}
            <div>
              <div className="p-4 border-b border-white/[0.08] flex items-center justify-between">
                <Link
                  to="/"
                  onClick={() => setMobileMenuOpen(false)}
                  className="flex items-center gap-2.5"
                >
                  <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-cyan-400 via-sky-500 to-blue-600 flex items-center justify-center shadow-lg shadow-sky-500/25 ring-1 ring-white/20">
                    <ShieldCheck className="w-5 h-5 text-white drop-shadow" />
                  </div>
                  <div>
                    <span className="font-extrabold text-base tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-300 bg-clip-text text-transparent">
                      SafeTrip <span className="bg-gradient-to-r from-sky-400 to-cyan-300 bg-clip-text text-transparent">AI</span>
                    </span>
                    <span className="ml-1.5 inline-flex items-center px-1.5 py-0.5 rounded-full text-[9px] font-bold tracking-wide uppercase bg-sky-500/10 text-sky-300 border border-sky-500/30">
                      India
                    </span>
                  </div>
                </Link>

                {/* Dedicated Close Button */}
                <button
                  type="button"
                  onClick={() => setMobileMenuOpen(false)}
                  className="p-2 rounded-xl bg-white/[0.06] hover:bg-white/[0.12] active:bg-white/[0.18] text-slate-300 hover:text-white border border-white/10 transition cursor-pointer min-w-[38px] min-h-[38px] flex items-center justify-center"
                  aria-label="Close Navigation Menu"
                >
                  <X className="w-5 h-5 text-sky-400" />
                </button>
              </div>

              {/* Auth Actions inside Drawer (Login & Register or User Info) */}
              <div className="p-4 border-b border-white/[0.08] bg-slate-900/50">
                {user ? (
                  <div className="space-y-3">
                    <div className="flex items-center justify-between gap-2">
                      <div className="flex items-center gap-2.5 min-w-0">
                        <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center text-sm font-bold text-white shadow-sm ring-1 ring-white/20 shrink-0">
                          {user.full_name ? user.full_name[0].toUpperCase() : 'U'}
                        </div>
                        <div className="min-w-0">
                          <p className="text-xs font-bold text-white truncate">
                            {user.full_name || 'Traveler'}
                          </p>
                          <p className="text-[11px] text-slate-400 truncate">
                            {user.email}
                          </p>
                        </div>
                      </div>
                      <span
                        className={`px-2 py-0.5 rounded-md text-[9px] font-bold tracking-wider uppercase shrink-0 ${
                          user.role === 'ADMIN'
                            ? 'bg-amber-400/15 text-amber-300 border border-amber-400/30'
                            : 'bg-sky-400/15 text-sky-300 border border-sky-400/30'
                        }`}
                      >
                        {user.role}
                      </span>
                    </div>

                    <div className="grid grid-cols-2 gap-2 pt-1">
                      <Link
                        to="/dashboard"
                        onClick={() => setMobileMenuOpen(false)}
                        className="flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 active:bg-slate-600 text-slate-200 text-xs font-semibold border border-white/10 transition text-center"
                      >
                        <User className="w-3.5 h-3.5 text-sky-400" />
                        <span>Dashboard</span>
                      </Link>
                      <button
                        type="button"
                        onClick={() => {
                          logout();
                          setMobileMenuOpen(false);
                          navigate('/');
                        }}
                        className="flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl bg-rose-500/15 hover:bg-rose-500/25 active:bg-rose-500/35 text-rose-300 text-xs font-semibold border border-rose-500/30 transition text-center"
                      >
                        <LogOut className="w-3.5 h-3.5" />
                        <span>Logout</span>
                      </button>
                    </div>
                  </div>
                ) : (
                  <div className="space-y-2">
                    <p className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-2">
                      Account Access
                    </p>
                    <div className="grid grid-cols-2 gap-2">
                      <Link
                        to="/login"
                        onClick={() => setMobileMenuOpen(false)}
                        className="flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-xl bg-white/[0.06] hover:bg-white/[0.12] active:bg-white/[0.18] text-white text-xs font-bold border border-white/15 transition text-center min-h-[44px]"
                      >
                        <LogIn className="w-4 h-4 text-sky-400" />
                        <span>Login</span>
                      </Link>
                      <Link
                        to="/register"
                        onClick={() => setMobileMenuOpen(false)}
                        className="flex items-center justify-center gap-1.5 py-2.5 px-3 rounded-xl bg-gradient-to-r from-sky-500 via-blue-600 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white text-xs font-bold shadow-lg shadow-sky-500/25 border border-white/20 transition text-center min-h-[44px]"
                      >
                        <UserPlus className="w-4 h-4" />
                        <span>Register</span>
                      </Link>
                    </div>
                  </div>
                )}

                {/* Trip Basket Shortcut if items exist */}
                {customTripBasket.length > 0 && (
                  <Link
                    to="/planner"
                    onClick={() => setMobileMenuOpen(false)}
                    className="mt-3 flex items-center justify-between p-2.5 rounded-xl bg-emerald-500/15 border border-emerald-500/30 text-emerald-300 text-xs font-bold"
                  >
                    <div className="flex items-center gap-2">
                      <Calendar className="w-4 h-4 text-emerald-400" />
                      <span>Custom Trip Basket</span>
                    </div>
                    <span className="px-2 py-0.5 rounded-full bg-emerald-500 text-slate-950 text-[10px] font-extrabold">
                      {customTripBasket.length} places
                    </span>
                  </Link>
                )}
              </div>

              {/* Primary Navigation Links */}
              <div className="p-3 space-y-1">
                <p className="px-3 pt-2 pb-1 text-[10px] font-extrabold text-slate-500 uppercase tracking-wider">
                  Explore & Plan
                </p>
                {primaryNavItems.map((item) => {
                  const Icon = item.icon;
                  const active = isActive(item.to);
                  return (
                    <Link
                      key={item.to}
                      to={item.to}
                      onClick={() => setMobileMenuOpen(false)}
                      className={`flex items-center justify-between px-3.5 py-3 rounded-xl text-xs font-semibold transition min-h-[44px] ${
                        active
                          ? 'bg-gradient-to-r from-sky-500/20 to-blue-500/10 text-sky-300 border border-sky-500/30 font-bold shadow-[0_0_15px_rgba(56,189,248,0.15)]'
                          : 'text-slate-300 hover:text-white hover:bg-white/[0.05] active:bg-white/[0.1] border border-transparent'
                      }`}
                    >
                      <div className="flex items-center gap-3">
                        <div
                          className={`p-1.5 rounded-lg ${
                            active
                              ? 'bg-sky-500/20 text-sky-400'
                              : 'bg-white/[0.04] text-slate-400'
                          }`}
                        >
                          <Icon className="w-4 h-4" />
                        </div>
                        <span>{item.label}</span>
                        {item.badge && (
                          <span className="text-[9px] px-1.5 py-0.5 rounded bg-sky-500/20 text-sky-300 font-bold border border-sky-500/30">
                            {item.badge}
                          </span>
                        )}
                      </div>
                      <ChevronRight
                        className={`w-4 h-4 ${
                          active ? 'text-sky-400' : 'text-slate-600'
                        }`}
                      />
                    </Link>
                  );
                })}
              </div>
            </div>

            {/* Drawer Bottom Info */}
            <div className="p-4 border-t border-white/[0.08] bg-slate-900/60 text-center pb-8">
              <p className="text-[11px] text-slate-400 font-medium">
                SafeTrip AI • Intelligent Indian Tourism
              </p>
              <p className="text-[10px] text-slate-500 mt-0.5">
                Plan Smarter • Travel Safer • 28 States & 8 UTs
              </p>
            </div>
          </aside>
        </div>
      )}

      {/* Modern Floating Dock Bottom Bar for Mobile Phones (Strictly Hidden on Desktop) */}
      <nav className="md:hidden fixed bottom-3 left-3 right-3 z-40 max-w-md mx-auto bg-slate-950/95 backdrop-blur-2xl border border-white/10 rounded-2xl shadow-2xl shadow-black/70 px-2 py-1 flex items-center justify-around">
        {[
          { to: '/', label: 'Home', icon: Sparkles },
          { to: '/planner', label: 'Planner', icon: Calendar },
          { to: '/safety', label: 'Safety', icon: ShieldCheck },
          { to: '/map', label: 'Map', icon: MapPin },
          { to: user ? '/dashboard' : '/login', label: user ? 'Profile' : 'Login', icon: User },
        ].map((m) => {
          const Icon = m.icon;
          const active = isActive(m.to);
          return (
            <Link
              key={m.to}
              to={m.to}
              className={`flex-1 min-w-0 min-h-[44px] relative flex flex-col items-center justify-center gap-0.5 py-1 px-1 rounded-xl text-[10px] font-semibold transition-all duration-200 ${
                active
                  ? 'text-sky-400 scale-105'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <Icon className="w-4 h-4 shrink-0" />
              <span className="truncate max-w-full">{m.label}</span>
              {active && (
                <span className="w-1 h-1 rounded-full bg-sky-400 shadow-[0_0_6px_#38bdf8] mt-0.5" />
              )}
            </Link>
          );
        })}
      </nav>
    </>
  );
}
