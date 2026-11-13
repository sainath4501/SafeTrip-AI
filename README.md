# 🇮🇳 SafeTrip AI – Intelligent Indian Tourism Safety & Trip Planning System

<p align="center">
  <img src="https://img.shields.io/badge/Project-MCA%20Final%20Year-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Domain-AI%20%7C%20ML%20%7C%20Tourism-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi" />
</p>

<p align="center">
  <b>An AI-Powered Indian Tourism Safety, Recommendation and Intelligent Trip Planning Platform</b>
</p>

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [AI & Machine Learning Models](#-ai--machine-learning-models)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [Application URLs](#-application-urls)
- [Demo Accounts](#-demo-accounts)
- [API Documentation](#-api-documentation)
- [End-to-End Testing](#-end-to-end-testing)
- [Future Enhancements](#-future-enhancements)
- [Disclaimer](#-disclaimer)

---

## 🌍 Project Overview

**SafeTrip AI** is an intelligent, AI-based Indian tourism safety, recommendation, and trip planning system developed as an MCA Final-Year Major Project.

The platform combines Artificial Intelligence, Machine Learning, Geospatial Technologies, and modern web development to provide tourists with a centralized solution for discovering destinations, evaluating travel risks, planning personalized itineraries, and identifying safer travel routes.

Unlike conventional travel platforms that primarily focus on hotel and ticket bookings, SafeTrip AI emphasizes **tourist safety, intelligent recommendations, real-time weather awareness, crowd prediction, local transportation, and explainable AI-based decision-making.**

### 📊 Project Highlights

| Component | Coverage |
|---|---|
| Indian States & Union Territories | 36 |
| Tourist Districts | 84+ |
| Tourist Places | 309+ |
| Supervised ML Models | 4 |
| Recommendation Factors | 8 |
| Safety Risk Factors | 6 |
| Database Tables | 22 |
| PDF Processing Pipeline | 9 Steps |
| Trip Planning | Day-wise Intelligent Scheduling |

---

## ❗ Problem Statement

Tourists traveling across India frequently face challenges due to fragmented travel information and a lack of centralized safety-oriented planning systems.

Existing travel applications generally concentrate on accommodation, ticket booking, and destination discovery while providing limited integration of:

- Real-time weather-related travel risks.
- Tourist crowd congestion and crowd predictions.
- Local crime, scam, and incident awareness.
- Night-time travel vulnerability.
- Safer route recommendations.
- Local Metro, Bus, Auto, and Cab transportation.
- Intelligent day-wise itinerary generation.
- Personalized recommendations based on tourist preferences.

**SafeTrip AI addresses these challenges** by integrating tourism information, machine learning predictions, geospatial analysis, safety intelligence, and automated trip planning into a single web application.

---

## 🎯 Project Objectives

1. Develop a centralized Indian tourism database covering all 28 States and 8 Union Territories.
2. Implement four supervised Machine Learning models using Scikit-Learn.
3. Develop an explainable hybrid recommendation engine.
4. Generate optimized day-wise tourist itineraries.
5. Implement a six-factor AI-powered safety assessment engine.
6. Compare shortest-distance and AI-recommended safer routes.
7. Estimate local and intercity transportation costs.
8. Implement PDF-based tourism dataset ingestion and validation.
9. Generate downloadable PDF travel itineraries.
10. Provide secure authentication and role-based administrative access.

---

## 🚀 Key Features

### 1. 🇮🇳 All-India Tourism Discovery

- Coverage of 28 States and 8 Union Territories.
- 84+ tourist districts.
- 309+ tourist destinations.
- Historical monuments, beaches, hill stations, religious destinations, and nature attractions.
- Smart natural-language destination search.
- Destination details, categories, and tourism information.

### 2. 🤖 AI-Powered Place Recommendation

An explainable hybrid recommendation engine ranks tourist destinations based on eight configurable factors.

**Key capabilities:**
- Personalized destination recommendations.
- Configurable recommendation weights (`w1` to `w8`).
- Content-based recommendation.
- Weighted ranking algorithm.
- Human-readable "Why Recommended?" explanations.

### 3. 🗓️ Intelligent Day-Wise Trip Planner

Automatically generates optimized travel itineraries based on user preferences.

**Features:**
- Geo-clustering of nearby tourist attractions.
- Day-wise destination grouping.
- Opening and closing hour validation.
- Breakfast, lunch, and dinner scheduling.
- Attraction-to-attraction distance calculation.
- Transportation cost estimation.
- Daily travel timeline generation.
- Budget and traveler-based planning.

### 4. 🛡️ Six-Factor AI Safety Engine

Evaluates travel safety using six independent risk dimensions.

| Risk Factor | Description |
|---|---|
| Weather Risk | Rainfall and adverse weather conditions |
| Crowd Risk | Tourist congestion and footfall |
| Time-of-Day Risk | Daytime and night-time travel risks |
| Route Risk | Road and accident-related risks |
| Location Safety | Destination-level safety indicators |
| Scam/Incident Risk | Crime, scam, and incident-related indicators |

**Safer Alternative System:**

When elevated risks are detected, the application can recommend:

- Safer indoor attractions.
- Alternative destinations.
- Daytime visiting schedules.
- Recommended morning travel windows.
- Lower-risk travel options.

### 5. 🗺️ AI-Based Route Comparison

Uses NetworkX, OSRM, Leaflet, and OpenStreetMap technologies.

| Route | Description |
|---|---|
| Route A | Shortest-distance route |
| Route B | AI-weighted safer route |

**Features:**
- Interactive map visualization.
- Route distance comparison.
- Estimated travel duration.
- Route risk evaluation.
- Alternative route recommendations.
- Visual route comparison.

### 6. 🚆 Local Transportation & Fare Estimation

Provides estimated transportation options between tourist destinations.

**Supported transportation:**
- Metro.
- Public Bus.
- Auto Rickshaw.
- Taxi / Cab.
- Intercity Train.
- Flight.

> **Note:** Formula-based transportation prices are explicitly identified as Estimated Data and should not be interpreted as live fare quotations.

### 7. 📄 PDF Dataset Ingestion & Validation

A nine-step PDF processing and administrative approval pipeline powered by `pypdf`.

**Pipeline capabilities:**
1. PDF upload.
2. PDF document validation.
3. Text extraction.
4. Structured record identification.
5. Data parsing.
6. Coordinate validation.
7. Record preview and inline editing.
8. Administrative approval.
9. Database insertion.

The pipeline validates Indian geographical coordinate boundaries before accepting tourism records.

### 8. 📑 PDF Itinerary Export

Generate downloadable multi-page PDF travel plans using ReportLab.

**PDF includes:**
- Trip summary.
- Tourist destination details.
- Day-wise itinerary.
- Travel timeline.
- Estimated budget breakdown.
- Transportation information.
- Emergency helpline numbers.

### 9. 🔐 Authentication & Admin Dashboard

Secure user authentication and role-based access control.

**Tourist/User:**
- Register and log in.
- Discover destinations.
- Generate AI-based itineraries.
- Save tourist places.
- Download PDF itineraries.
- Report travel incidents.

**Administrator:**
- Manage tourist destinations.
- Approve uploaded PDF datasets.
- Manage tourism records.
- Monitor ML model performance.
- Retrain machine learning models.
- Access administrative dashboards.

---

## 🧠 AI & Machine Learning Models

SafeTrip AI implements four supervised Machine Learning models using Scikit-Learn.

### Machine Learning Algorithms

| Algorithm | Description |
|---|---|
| Random Forest | Ensemble-based classification |
| Decision Tree | Tree-based classification |
| Logistic Regression | Linear classification model |

All three algorithms are benchmarked using five-fold cross-validation.

The selected models are serialized into `.pkl` files for inference.

### Four Trained ML Models

| Model | Purpose | Serialized File |
|---|---|---|
| Crowd Prediction | Predict tourist crowd levels | `crowd_model.pkl` |
| Weather Risk | Assess weather-related activity risks | `weather_risk_model.pkl` |
| Scam Risk | Estimate scam and incident risk | `scam_risk_model.pkl` |
| Route Risk | Evaluate road and route safety | `route_risk_model.pkl` |

### AI vs Algorithmic Implementation

For academic transparency, SafeTrip AI distinguishes supervised machine learning from deterministic algorithms and hybrid scoring methods.

| Module | Implementation |
|---|---|
| Crowd Prediction | Supervised Machine Learning |
| Weather Risk | Supervised ML + Safety Rules |
| Scam Risk | Supervised Machine Learning |
| Route Risk | Supervised Machine Learning |
| Place Recommendation | Explainable Hybrid Weighted Scoring |
| Safe Route Analysis | NetworkX Multi-Objective Pathfinding |
| Trip Scheduling | Spatial Geo-Clustering + Scheduling Constraints |
| Transport Fare | Distance-Based Tariff Estimation |

---

## 🏗️ System Architecture

SafeTrip AI follows a modular full-stack architecture.

```text
                 SAFETRIP AI
                      |
          +-----------+-----------+
          |                       |
      FRONTEND                 BACKEND
          |                       |
    React 19 + Vite          FastAPI Server
          |                       |
    Tailwind CSS             REST API Routers
    Leaflet Maps                  |
          |            +----------+----------+
          |            |          |          |
          |          Auth      Tourism     Safety
          |            |          |          |
          |            +----------+----------+
          |                       |
          |              AI / ML ENGINE
          |                       |
          |          +------------+------------+
          |          |            |            |
          |       Prediction   Recommendation Routing
          |          Models       Engine      Engine
          |          (.pkl)
          |                       |
          |                 SQLite Database
          |                    (22 Tables)
          |                       |
          +-----------------------+
```

---

## 🛠️ Technology Stack

### Frontend

| Technology | Purpose |
|---|---|
| React 19 | User interface |
| Vite | Frontend development server |
| Tailwind CSS | Responsive styling |
| Leaflet | Interactive maps |
| OpenStreetMap | Map data |
| JavaScript | Application logic |

### Backend

| Technology | Purpose |
|---|---|
| Python 3.10+ | Backend programming |
| FastAPI | REST API development |
| SQLAlchemy | ORM and database management |
| SQLite | Relational database |
| Uvicorn | ASGI server |
| PyJWT | Authentication |
| PBKDF2-SHA256 | Password hashing |

### AI & Machine Learning

| Technology | Purpose |
|---|---|
| Scikit-Learn | Machine Learning |
| Random Forest | Classification |
| Decision Tree | Classification |
| Logistic Regression | Classification |
| NetworkX | Graph-based routing |
| NumPy | Numerical operations |
| Pandas | Dataset processing |

### Geospatial & External Services

| Technology | Purpose |
|---|---|
| OSRM | Route geometry and routing |
| OpenStreetMap | Geographic mapping |
| Leaflet | Route visualization |
| Open-Meteo | Weather information |

### PDF Processing

| Library | Purpose |
|---|---|
| pypdf | PDF text extraction |
| ReportLab | PDF generation |

---

## 📁 Project Structure

```text
ProjectCapstone/
│
├── Dataset/
│   ├── India Tourism Structured JSON Dataset/
│   ├── Indian Crime Dataset (NCRB Derived)/
│   ├── Indian Road Accident Dataset (2022–2025)/
│   ├── Rainfall in India (1901–2015)/
│   ├── Tourist Footfall Dataset/
│   └── SafeTrip_AI_Indian_Tourism_Safety_Dataset.pdf
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── places.py
│   │   │   ├── recommendations.py
│   │   │   ├── safety_transport.py
│   │   │   └── admin_ml_pdf.py
│   │   │
│   │   ├── database/
│   │   │   ├── db.py
│   │   │   ├── schema.sql
│   │   │   └── seed.py
│   │   │
│   │   ├── ml/
│   │   │   ├── pipeline.py
│   │   │   └── predictor.py
│   │   │
│   │   ├── models/
│   │   │   └── entities.py
│   │   │
│   │   ├── pdf/
│   │   │   ├── parser.py
│   │   │   └── generator.py
│   │   │
│   │   ├── recommendation/
│   │   │   └── engine.py
│   │   │
│   │   ├── routing/
│   │   │   └── engine.py
│   │   │
│   │   ├── safety/
│   │   │   └── engine.py
│   │   │
│   │   ├── weather/
│   │   │   └── service.py
│   │   │
│   │   ├── utils/
│   │   │   ├── security.py
│   │   │   └── validators.py
│   │   │
│   │   ├── config.py
│   │   └── main.py
│   │
│   ├── models/
│   ├── requirements.txt
│   └── run.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── context/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── ml/
│   └── models/
│       ├── crowd_model.pkl
│       ├── weather_risk_model.pkl
│       ├── scam_risk_model.pkl
│       └── route_risk_model.pkl
│
├── data/
│   ├── safetrip_ai.db
│   └── pdf_datasets/
│
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites

Install the following software before running the project.

- Python 3.10 or above.
- Node.js 18 or above.
- npm.
- Git.
- Visual Studio Code (recommended).

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/SafeTrip-AI.git
```

Navigate to the project directory:

```bash
cd SafeTrip-AI
```

### Step 2: Start the Backend

Open a terminal and execute:

```powershell
cd backend
```

Create a virtual environment:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
python run.py
```

**Backend server:**

```text
http://localhost:8000
```

**Swagger API documentation:**

```text
http://localhost:8000/docs
```

### Step 3: Start the Frontend

Open a second terminal:

```powershell
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the React development server:

```bash
npm run dev
```

**Frontend application:**

```text
http://localhost:5173
```

### Step 4: Access the Application

Open your browser and visit:

```text
http://localhost:5173
```

The frontend communicates with the FastAPI backend through REST APIs.

> **Important:** Ensure that the backend is running before accessing features that require API communication. Configure the frontend API base URL and external service settings according to your environment.

### Alternative: Docker Deployment

If Docker and Docker Compose configurations are included in the repository, run:

```bash
docker compose up --build -d
```

---

## 🔗 Application URLs

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend | http://localhost:8000 |
| Swagger Documentation | http://localhost:8000/docs |
| ReDoc Documentation | http://localhost:8000/redoc |

---

## 🔐 Demo Accounts

The following demo credentials are intended for local development and demonstration.

| Role | Email | Password |
|---|---|---|
| Tourist / User | `user@safetrip.ai` | `user123` |
| System Admin | `admin@safetrip.ai` | `admin123` |

### Tourist Capabilities

- AI-powered trip planning.
- Destination discovery.
- Save tourist destinations.
- Download PDF itineraries.
- Submit incident reports.

### Administrator Capabilities

- Manage tourist destinations.
- Approve PDF datasets.
- Access ML model evaluation.
- Retrain machine learning models.
- Manage administrative records.

> **Security Warning:** Demo credentials must never be used in a production deployment. Replace default passwords, configure secure secrets, and apply appropriate access controls.

---

## 📡 API Documentation

SafeTrip AI uses modular REST API endpoints developed with FastAPI.

| API Module | Responsibility |
|---|---|
| `/api/auth` | Registration, login, user authentication |
| `/api/places` | States, districts, destinations, smart search |
| `/api/recommendations` | AI recommendations and trip planning |
| `/api/safety_transport` | Safety assessment, routes, transport |
| `/api/admin_ml_pdf` | Admin operations, ML evaluation, PDF processing |

Explore and test the APIs using Swagger UI:

```text
http://localhost:8000/docs
```

---

## 🧪 End-to-End Testing & Viva Demonstration

The following test cases demonstrate the major application workflows.

### Test Case 1: Natural Language Smart Search

**Input:**
```text
Historical places in Delhi
```

**Expected Result:**
- Extracts the category: Historical.
- Extracts the location: Delhi.
- Displays matching tourist destinations.
- Shows available safety and crowd information.

### Test Case 2: Three-Day Delhi Trip Planning

**Input:**
- Destination: Delhi.
- Duration: 3 Days.
- Budget: ₹15,000.
- Travelers: 2.

**Expected Itinerary:**

| Day | Tourist Destinations |
|---|---|
| Day 1 | India Gate, Rashtrapati Bhavan, National War Memorial, Connaught Place |
| Day 2 | Red Fort, Jama Masjid, Chandni Chowk, Humayun's Tomb |
| Day 3 | Qutub Minar, Lotus Temple, Akshardham |

### Test Case 3: Opening Hours & Timeline Validation

Verify that:
- Breakfast is scheduled at 08:00.
- Attractions are scheduled within configured opening hours.
- Lunch breaks are included.
- Travel time is considered.
- A safe return is included in the daily itinerary.

### Test Case 4: Weather & Safety Risk Evaluation

**Test Inputs:**
- Activity: Trekking / Beach.
- Visit Time: 22:30.
- Weather: Adverse conditions.

**Expected Result:**
- Elevated risk assessment.
- Safer alternative suggestions.
- Indoor attraction recommendations.
- Suggested daytime visiting windows.

### Test Case 5: Shortest vs AI Safe Route

**Source:** India Gate.

**Destination:** Red Fort.

**Expected Result:**
- Route A: Shortest-distance route.
- Route B: AI-weighted safer route.
- Interactive Leaflet map.
- Distance and duration comparison.
- Route risk information.

### Test Case 6: Transportation Fare Estimation

Verify transportation options:
- Metro.
- Bus.
- Auto.
- Cab.
- Train.
- Flight.

All formula-generated prices must be labeled as Estimated Data.

### Test Case 7: Privacy-Preserving Incident Reporting

**Input:** Scam incident report.

**Expected Result:**
- Incident stored in the database.
- Anonymous public display.
- Incident information incorporated into the relevant risk assessment.

### Test Case 8: PDF Dataset Ingestion

**Action:** Parse ProjectCapstone PDF Dataset.

**Expected Result:**
- PDF extraction.
- Structured data validation.
- Coordinate verification.
- Inline editing.
- Administrative approval.
- Database insertion after approval.

### Test Case 9: PDF Itinerary Generation

**Action:** Download Full PDF Itinerary.

**Expected Result:**
A multi-page PDF containing:
- Trip summary.
- Budget breakdown.
- Daily schedule.
- Tourist destinations.
- Transportation notes.
- Emergency contact information.

### Test Case 10: Machine Learning Dashboard

Verify:
- Accuracy.
- Precision.
- Recall.
- F1-Score.
- Confusion Matrix.
- Feature Importance.
- Model comparison.

Evaluate Random Forest, Decision Tree, and Logistic Regression across all four ML prediction tasks.

---

## 📞 Important Indian Emergency Helplines

| Service | Helpline |
|---|---|
| National Emergency Response | 112 |
| Tourist Helpline | 1363 |
| Women Helpline | 1091 |

> Emergency numbers and service availability should be independently verified before travel.

---

## 🔮 Future Enhancements

- Mobile application using React Native.
- Multilingual AI travel assistant.
- Live public transportation integration.
- Real-time tourist density monitoring.
- Advanced deep learning-based safety prediction.
- SOS emergency assistance.
- Voice-based destination search.
- Personalized AI travel chatbot.
- Integration with government tourism APIs.
- Advanced geospatial heatmaps.

---

## ⚠️ Disclaimer

SafeTrip AI is an academic and research-oriented tourism assistance platform.

- Machine Learning predictions are estimates and are not guarantees of safety.
- Crime and incident datasets may have reporting and coverage limitations.
- Route risk assessments depend on available data and model assumptions.
- Transportation fares generated using formulas are estimates, not confirmed live prices.
- External APIs may have availability and coverage limitations.
- Tourists should verify official weather alerts, transportation information, opening hours, and local safety advisories before traveling.

**SafeTrip AI should be used as a decision-support system and not as a replacement for official emergency services or government safety advisories.**

---

## 👨‍💻 Project Information

**Project Name:** SafeTrip AI

**Project Type:** MCA Final-Year Major Project

**Project Domain:** Artificial Intelligence, Machine Learning, Geoinformatics & Smart Indian Tourism

**Backend:** Python, FastAPI, SQLAlchemy

**Frontend:** React 19, Vite, Tailwind CSS

**Database:** SQLite

**Machine Learning:** Scikit-Learn

**Mapping:** Leaflet, OpenStreetMap, OSRM, NetworkX

**PDF Processing:** pypdf, ReportLab

---

## ⭐ Support

If you find this project interesting or useful, please consider giving the repository a ⭐ on GitHub.

<p align="center">
  <b>SafeTrip AI – Travel Smart. Travel Safe. Explore India. 🇮🇳</b>
</p>
