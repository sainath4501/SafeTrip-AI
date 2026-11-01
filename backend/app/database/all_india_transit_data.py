"""
Comprehensive Indian Metro Stations & City Bus Transit Knowledge Base
Covers all operational Metro Networks and Central Bus Transit Hubs across India.
"""

ALL_INDIA_METRO_STATIONS = [
    # ==================== 1. DELHI NCR (DMRC + NOIDA + GURGAON) ====================
    # Yellow Line
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Rajiv Chowk Mega Interchange", "line": "Yellow & Blue Line", "color": "#facc15", "lat": 28.6328, "lon": 77.2195, "is_interchange": True, "lines": "Yellow Line, Blue Line", "attractions": "Connaught Place, Janpath, Central Park"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "New Delhi Railway Station Metro", "line": "Yellow & Airport Express", "color": "#facc15", "lat": 28.6431, "lon": 77.2223, "is_interchange": True, "lines": "Yellow Line, Airport Express", "attractions": "New Delhi Railway Station, Paharganj"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Chandni Chowk", "line": "Yellow Line", "color": "#facc15", "lat": 28.6578, "lon": 77.2303, "is_interchange": False, "lines": "Yellow Line", "attractions": "Chandni Chowk, Old Delhi Railway Station, Gurudwara Sis Ganj"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Kashmere Gate Mega Interchange", "line": "Yellow, Red & Violet Line", "color": "#facc15", "lat": 28.6675, "lon": 77.2285, "is_interchange": True, "lines": "Yellow, Red, Violet", "attractions": "ISBT Kashmere Gate, St. James Church"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Central Secretariat", "line": "Yellow & Violet Line", "color": "#facc15", "lat": 28.6147, "lon": 77.2119, "is_interchange": True, "lines": "Yellow, Violet", "attractions": "India Gate, Rashtrapati Bhavan, Kartavya Path, National Museum"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Hauz Khas Interchange", "line": "Yellow & Magenta Line", "color": "#facc15", "lat": 28.5432, "lon": 77.2065, "is_interchange": True, "lines": "Yellow, Magenta", "attractions": "Hauz Khas Village, Deer Park, IIT Delhi"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Qutab Minar", "line": "Yellow Line", "color": "#facc15", "lat": 28.5135, "lon": 77.1858, "is_interchange": False, "lines": "Yellow Line", "attractions": "Qutub Minar Archaeological Complex, Mehrauli Archaeological Park"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Patel Chowk", "line": "Yellow Line", "color": "#facc15", "lat": 28.6232, "lon": 77.2140, "is_interchange": False, "lines": "Yellow Line", "attractions": "Metro Museum, Gurudwara Bangla Sahib, Jantar Mantar"},
    # Violet Line
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Lal Qila (Red Fort)", "line": "Violet Line", "color": "#8b5cf6", "lat": 28.6565, "lon": 77.2390, "is_interchange": False, "lines": "Violet Line", "attractions": "Red Fort (Lal Qila), Meena Bazaar"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Jama Masjid", "line": "Violet Line", "color": "#8b5cf6", "lat": 28.6508, "lon": 77.2355, "is_interchange": False, "lines": "Violet Line", "attractions": "Jama Masjid, Matia Mahal Food Street"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Delhi Gate", "line": "Violet Line", "color": "#8b5cf6", "lat": 28.6405, "lon": 77.2405, "is_interchange": False, "lines": "Violet Line", "attractions": "Feroz Shah Kotla, Ambedkar Stadium"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "ITO", "line": "Violet Line", "color": "#8b5cf6", "lat": 28.6292, "lon": 77.2415, "is_interchange": False, "lines": "Violet Line", "attractions": "Pragati Maidan, Supreme Court, Doll Museum"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "JLN Stadium", "line": "Violet Line", "color": "#8b5cf6", "lat": 28.5865, "lon": 77.2345, "is_interchange": False, "lines": "Violet Line", "attractions": "Jawaharlal Nehru Stadium, Sunder Nursery, Humayun's Tomb"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Kalkaji Mandir Interchange", "line": "Violet & Magenta Line", "color": "#8b5cf6", "lat": 28.5502, "lon": 77.2588, "is_interchange": True, "lines": "Violet, Magenta", "attractions": "Lotus Temple (Bahá'í House of Worship), Kalkaji Mandir, Nehru Place"},
    # Blue Line
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Akshardham", "line": "Blue Line", "color": "#3b82f6", "lat": 28.6181, "lon": 77.2785, "is_interchange": False, "lines": "Blue Line", "attractions": "Swaminarayan Akshardham Temple"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Mandi House Interchange", "line": "Blue & Violet Line", "color": "#3b82f6", "lat": 28.6258, "lon": 77.2340, "is_interchange": True, "lines": "Blue, Violet", "attractions": "National School of Drama, Copernicus Marg, National Gallery of Modern Art"},
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "Supreme Court (Pragati Maidan)", "line": "Blue Line", "color": "#3b82f6", "lat": 28.6215, "lon": 77.2435, "is_interchange": False, "lines": "Blue Line", "attractions": "Bharat Mandapam, Supreme Court of India, National Crafts Museum"},
    # Airport Express, Gurugram & Noida
    {"city": "Delhi", "network": "Delhi Metro (DMRC)", "station": "IGI Airport Terminal 3", "line": "Airport Express Line", "color": "#f97316", "lat": 28.5562, "lon": 77.0855, "is_interchange": False, "lines": "Airport Express", "attractions": "Indira Gandhi International Airport T3"},
    {"city": "Gurugram", "network": "Rapid Metro Gurgaon", "station": "Cyber City (DLF Phase 2)", "line": "Rapid Metro & Yellow Line", "color": "#06b6d4", "lat": 28.4945, "lon": 77.0890, "is_interchange": True, "lines": "Rapid Metro, Yellow", "attractions": "DLF CyberHub, Horizon Center"},
    {"city": "Noida", "network": "Delhi & Noida Metro", "station": "Botanical Garden Interchange", "line": "Blue & Magenta Line", "color": "#3b82f6", "lat": 28.5645, "lon": 77.3340, "is_interchange": True, "lines": "Blue, Magenta", "attractions": "Noida Golf Course, Great India Place, Worlds of Wonder"},
    {"city": "Noida", "network": "Noida Metro (NMRC)", "station": "Noida Sector 51 / 52 Interchange", "line": "Aqua Line & Blue Line", "color": "#06b6d4", "lat": 28.5815, "lon": 77.3685, "is_interchange": True, "lines": "Aqua Line, Blue Line", "attractions": "Noida City Centre, Sector 50 Markets"},

    # ==================== 2. MUMBAI (METRO + SUBURBAN HUBS) ====================
    {"city": "Mumbai", "network": "Mumbai Metro & Suburban", "station": "CSMT (Chhatrapati Shivaji Maharaj Terminus)", "line": "Central Suburban & Aqua Line 3", "color": "#dc2626", "lat": 18.9400, "lon": 72.8354, "is_interchange": True, "lines": "Central Railway, Harbour Line, Aqua Line 3", "attractions": "CSMT UNESCO Building, Crawford Market, Marine Drive"},
    {"city": "Mumbai", "network": "Mumbai Metro & Suburban", "station": "Churchgate Terminal", "line": "Western Suburban & Aqua Line 3", "color": "#2563eb", "lat": 18.9352, "lon": 72.8272, "is_interchange": True, "lines": "Western Railway, Aqua Line 3", "attractions": "Marine Drive, Wankhede Stadium, Gateway of India"},
    {"city": "Mumbai", "network": "Mumbai Metro (MMRDA)", "station": "Ghatkopar Interchange", "line": "Line 1 (Blue) & Central Suburban", "color": "#0284c7", "lat": 19.0865, "lon": 72.9080, "is_interchange": True, "lines": "Metro Line 1, Central Railway", "attractions": "R City Mall, Eastern Suburbs connectivity"},
    {"city": "Mumbai", "network": "Mumbai Metro (MMRDA)", "station": "Andheri Interchange", "line": "Line 1 (Blue) & Western Suburban", "color": "#0284c7", "lat": 19.1197, "lon": 72.8464, "is_interchange": True, "lines": "Metro Line 1, Western Railway", "attractions": "Lokhandwala, Western Express Highway"},
    {"city": "Mumbai", "network": "Mumbai Metro (MMRDA)", "station": "DN Nagar Interchange", "line": "Line 1 & Line 2A (Yellow)", "color": "#0284c7", "lat": 19.1305, "lon": 72.8285, "is_interchange": True, "lines": "Line 1, Line 2A", "attractions": "Juhu Beach, Andheri West, Link Road"},
    {"city": "Mumbai", "network": "Mumbai Metro (MMRDA)", "station": "Gundavali (Western Express Highway)", "line": "Line 7 (Red) & Line 1", "color": "#ef4444", "lat": 19.1155, "lon": 72.8550, "is_interchange": True, "lines": "Line 1, Line 7", "attractions": "Chhatrapati Shivaji Maharaj International Airport T2"},
    {"city": "Mumbai", "network": "Mumbai Metro (MMRDA)", "station": "BKC (Bandra Kurla Complex)", "line": "Aqua Line 3 Underground", "color": "#06b6d4", "lat": 19.0665, "lon": 72.8685, "is_interchange": True, "lines": "Line 3 Aqua", "attractions": "Bandra Kurla Complex, Jio World Drive, US Consulate"},
    {"city": "Mumbai", "network": "Mumbai Metro (MMRDA)", "station": "Cuffe Parade Terminal", "line": "Aqua Line 3 Underground", "color": "#06b6d4", "lat": 18.9165, "lon": 72.8220, "is_interchange": False, "lines": "Line 3 Aqua", "attractions": "Colaba, Gateway of India, World Trade Centre, Taj Mahal Palace"},
    {"city": "Mumbai", "network": "Mumbai Metro (MMRDA)", "station": "Versova Terminal", "line": "Line 1 (Blue)", "color": "#0284c7", "lat": 19.1315, "lon": 72.8160, "is_interchange": False, "lines": "Line 1", "attractions": "Versova Beach, Juhu, Seven Bungalows"},
    {"city": "Mumbai", "network": "Mumbai Metro (MMRDA)", "station": "Marol Naka Interchange", "line": "Line 1 & Aqua Line 3", "color": "#0284c7", "lat": 19.1120, "lon": 72.8870, "is_interchange": True, "lines": "Line 1, Line 3 Aqua", "attractions": "Andheri East Corporate Hub, Airport Road"},
    {"city": "Mumbai", "network": "Mumbai Metro (MMRDA)", "station": "Dadar Central Interchange", "line": "Western & Central Suburban Junction", "color": "#2563eb", "lat": 19.0178, "lon": 72.8428, "is_interchange": True, "lines": "Western Railway, Central Railway", "attractions": "Siddhivinayak Temple, Shivaji Park, Dadar Flower Market"},

    # ==================== 3. BANGALORE (NAMMA METRO - BMRCL) ====================
    {"city": "Bangalore", "network": "Namma Metro (BMRCL)", "station": "Nadaprabhu Kempegowda (Majestic) Mega Interchange", "line": "Purple & Green Line", "color": "#7c3aed", "lat": 12.9757, "lon": 77.5728, "is_interchange": True, "lines": "Purple Line, Green Line", "attractions": "KSR Bengaluru City Railway Station, Kempegowda Bus Station (BMTC/KSRTC)"},
    {"city": "Bangalore", "network": "Namma Metro (BMRCL)", "station": "Dr. B.R. Ambedkar Vidhana Soudha", "line": "Purple Line", "color": "#7c3aed", "lat": 12.9795, "lon": 77.5925, "is_interchange": False, "lines": "Purple Line", "attractions": "Vidhana Soudha, High Court of Karnataka (Attara Kacheri), Cubbon Park"},
    {"city": "Bangalore", "network": "Namma Metro (BMRCL)", "station": "Cubbon Park", "line": "Purple Line", "color": "#7c3aed", "lat": 12.9810, "lon": 77.5995, "is_interchange": False, "lines": "Purple Line", "attractions": "Cubbon Park, Chinnaswamy Stadium, Visvesvaraya Industrial & Technological Museum"},
    {"city": "Bangalore", "network": "Namma Metro (BMRCL)", "station": "MG Road Interchange", "line": "Purple Line", "color": "#7c3aed", "lat": 12.9756, "lon": 77.6066, "is_interchange": True, "lines": "Purple Line, Pink Line (u/c)", "attractions": "MG Road Boulevard, Brigade Road, Commercial Street"},
    {"city": "Bangalore", "network": "Namma Metro (BMRCL)", "station": "Indiranagar", "line": "Purple Line", "color": "#7c3aed", "lat": 12.9784, "lon": 77.6385, "is_interchange": False, "lines": "Purple Line", "attractions": "100 Feet Road, Indiranagar Food & Dining District"},
    {"city": "Bangalore", "network": "Namma Metro (BMRCL)", "station": "Whitefield (Kadugodi)", "line": "Purple Line", "color": "#7c3aed", "lat": 12.9965, "lon": 77.7610, "is_interchange": False, "lines": "Purple Line", "attractions": "ITPL, International Tech Park Bangalore, Satya Sai Ashram"},
    {"city": "Bangalore", "network": "Namma Metro (BMRCL)", "station": "Lalbagh", "line": "Green Line", "color": "#16a34a", "lat": 12.9465, "lon": 77.5800, "is_interchange": False, "lines": "Green Line", "attractions": "Lalbagh Botanical Garden (West Gate), Basavanagudi, MTR"},
    {"city": "Bangalore", "network": "Namma Metro (BMRCL)", "station": "KR Market (Krishna Rajendra Market)", "line": "Green Line", "color": "#16a34a", "lat": 12.9615, "lon": 77.5745, "is_interchange": False, "lines": "Green Line", "attractions": "Bangalore Fort, Tipu Sultan's Summer Palace, KR Flower Market"},
    {"city": "Bangalore", "network": "Namma Metro (BMRCL)", "station": "Yeshwanthpur", "line": "Green Line", "color": "#16a34a", "lat": 13.0235, "lon": 77.5505, "is_interchange": True, "lines": "Green Line, Indian Railways", "attractions": "Yeshwanthpur Junction Railway Station, ISKCON Temple Bangalore"},
    {"city": "Bangalore", "network": "Namma Metro (BMRCL)", "station": "Banashankari Interchange", "line": "Green Line & TTMC", "color": "#16a34a", "lat": 12.9150, "lon": 77.5735, "is_interchange": True, "lines": "Green Line, BMTC TTMC", "attractions": "Banashankari Amma Temple, Kanakapura Road"},

    # ==================== 4. AHMEDABAD & GANDHINAGAR (GUJARAT METRO - GMRC) ====================
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Old High Court Mega Interchange", "line": "North-South & East-West Corridor", "color": "#dc2626", "lat": 23.0385, "lon": 72.5695, "is_interchange": True, "lines": "Red Line (North-South), Blue Line (East-West)", "attractions": "Income Tax Circle, Ashram Road, Sabarmati Riverfront Walkway"},
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Sabarmati Railway Station Metro", "line": "North-South (Red Line)", "color": "#dc2626", "lat": 23.0825, "lon": 72.5855, "is_interchange": True, "lines": "Red Line, High-Speed Bullet Train Hub", "attractions": "Sabarmati Ashram (Gandhi Smarak), Sabarmati Junction, D-Cabin"},
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Ranip BRTS & Metro Hub", "line": "North-South (Red Line)", "color": "#dc2626", "lat": 23.0725, "lon": 72.5780, "is_interchange": True, "lines": "Red Line, Ranip BRTS Central Hub", "attractions": "Ranip Central GSRTC Bus Terminal, Sabarmati Ashram"},
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Motera Stadium (Narendra Modi Stadium)", "line": "North-South (Red Line)", "color": "#dc2626", "lat": 23.0915, "lon": 72.5975, "is_interchange": False, "lines": "Red Line", "attractions": "Narendra Modi Cricket Stadium, Motera"},
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Gheekanta (Old City Wall)", "line": "East-West (Blue Line)", "color": "#2563eb", "lat": 23.0275, "lon": 72.5865, "is_interchange": False, "lines": "Blue Line", "attractions": "Sidi Saiyyed Mosque & Tree of Life Jali, Bhadra Fort, Teen Darwaza"},
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Kalupur Railway Station Metro", "line": "East-West (Blue Line)", "color": "#2563eb", "lat": 23.0265, "lon": 72.6005, "is_interchange": True, "lines": "Blue Line, Indian Railways Central", "attractions": "Ahmedabad Central Railway Station, Jhulta Minar (Shaking Minarets)"},
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Kankaria East", "line": "East-West (Blue Line)", "color": "#2563eb", "lat": 23.0115, "lon": 72.6065, "is_interchange": False, "lines": "Blue Line", "attractions": "Kankaria Lakefront, Nagina Wadi, Balvatika, Kamla Nehru Zoo"},
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Gujarat University", "line": "East-West (Blue Line)", "color": "#2563eb", "lat": 23.0360, "lon": 72.5450, "is_interchange": False, "lines": "Blue Line", "attractions": "Gujarat University, Navrangpura, LD Museum of Indology"},
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Paldi", "line": "North-South (Red Line)", "color": "#dc2626", "lat": 23.0145, "lon": 72.5645, "is_interchange": False, "lines": "Red Line", "attractions": "National Institute of Design (NID), Sanskar Kendra, Tagore Memorial Hall"},
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Thaltej Gam", "line": "East-West (Blue Line)", "color": "#2563eb", "lat": 23.0535, "lon": 72.5050, "is_interchange": False, "lines": "Blue Line", "attractions": "SG Highway, Science City Road, Acropolis Mall"},
    {"city": "Ahmedabad", "network": "Gujarat Metro (GMRC)", "station": "Apparel Park Depot", "line": "East-West (Blue Line)", "color": "#2563eb", "lat": 23.0180, "lon": 72.6235, "is_interchange": False, "lines": "Blue Line", "attractions": "Kankaria East Industrial Hub, Khokhra"},
    {"city": "Gandhinagar", "network": "Gujarat Metro (GMRC)", "station": "Dandi Kutir / Mahatma Mandir", "line": "Gandhinagar Extension", "color": "#16a34a", "lat": 23.2185, "lon": 72.6315, "is_interchange": False, "lines": "Gandhinagar Metro", "attractions": "Dandi Kutir Museum, Mahatma Mandir Convention Centre, Central Vista"},
    {"city": "Gandhinagar", "network": "Gujarat Metro (GMRC)", "station": "Akshardham / Sector 1", "line": "Gandhinagar Extension", "color": "#16a34a", "lat": 23.2325, "lon": 72.6540, "is_interchange": False, "lines": "Gandhinagar Metro", "attractions": "Swaminarayan Akshardham Temple Gandhinagar, Sector 28 Botanical Garden"},
    {"city": "Gandhinagar", "network": "Gujarat Metro (GMRC)", "station": "GNLU / GIFT City Metro", "line": "GIFT City Branch", "color": "#16a34a", "lat": 23.1610, "lon": 72.6650, "is_interchange": True, "lines": "GIFT City Feeder", "attractions": "Gujarat International Finance Tec-City (GIFT City), Gujarat National Law University"},

    # ==================== 5. KOLKATA (KOLKATA METRO) ====================
    {"city": "Kolkata", "network": "Kolkata Metro", "station": "Esplanade Mega Interchange", "line": "Blue (North-South) & Green (East-West)", "color": "#2563eb", "lat": 22.5645, "lon": 88.3515, "is_interchange": True, "lines": "Blue Line, Green Line, Purple Line", "attractions": "New Market, Curzon Park, Shahid Minar, Eden Gardens"},
    {"city": "Kolkata", "network": "Kolkata Metro", "station": "Howrah Railway Station Underwater Metro", "line": "Green Line (Underwater Hooghly Corridor)", "color": "#16a34a", "lat": 22.5835, "lon": 88.3425, "is_interchange": True, "lines": "Green Line, Eastern & South Eastern Railways", "attractions": "Howrah Bridge, Howrah Railway Station (Deepest Metro Station in India)"},
    {"city": "Kolkata", "network": "Kolkata Metro", "station": "Park Street", "line": "Blue Line", "color": "#2563eb", "lat": 22.5515, "lon": 88.3510, "is_interchange": False, "lines": "Blue Line", "attractions": "Park Street Dining, Asiatic Society, St. Xavier's, Indian Museum"},
    {"city": "Kolkata", "network": "Kolkata Metro", "station": "Maidan / Victoria Memorial", "line": "Blue Line", "color": "#2563eb", "lat": 22.5445, "lon": 88.3495, "is_interchange": False, "lines": "Blue Line", "attractions": "Victoria Memorial, Kolkata Maidan, St. Paul's Cathedral, Race Course"},
    {"city": "Kolkata", "network": "Kolkata Metro", "station": "Dakshineswar Terminal", "line": "Blue Line", "color": "#2563eb", "lat": 22.6555, "lon": 88.3575, "is_interchange": False, "lines": "Blue Line", "attractions": "Dakshineswar Kali Temple, Vivekananda Setu"},
    {"city": "Kolkata", "network": "Kolkata Metro", "station": "Kalighat", "line": "Blue Line", "color": "#2563eb", "lat": 22.5185, "lon": 88.3465, "is_interchange": False, "lines": "Blue Line", "attractions": "Kalighat Kali Temple, Rashbehari Avenue"},
    {"city": "Kolkata", "network": "Kolkata Metro", "station": "Salt Lake Sector V", "line": "Green Line", "color": "#16a34a", "lat": 22.5765, "lon": 88.4345, "is_interchange": False, "lines": "Green Line", "attractions": "Salt Lake IT Hub, Nicco Park, Nalban Boating Park"},
    {"city": "Kolkata", "network": "Kolkata Metro", "station": "Sealdah Railway Station Metro", "line": "Green Line", "color": "#16a34a", "lat": 22.5680, "lon": 88.3715, "is_interchange": True, "lines": "Green Line, Eastern Railway Sealdah", "attractions": "Sealdah Central Railway Junction, College Street Book Market"},

    # ==================== 6. CHENNAI (CHENNAI METRO - CMRL) ====================
    {"city": "Chennai", "network": "Chennai Metro (CMRL)", "station": "Puratchi Thalaivar Dr. M.G.R. Central", "line": "Blue & Green Line", "color": "#0284c7", "lat": 13.0827, "lon": 80.2755, "is_interchange": True, "lines": "Blue Line, Green Line, Southern Railway", "attractions": "Chennai Central Railway Station, Ripon Building, Victoria Public Hall"},
    {"city": "Chennai", "network": "Chennai Metro (CMRL)", "station": "High Court / Fort St. George", "line": "Blue Line", "color": "#0284c7", "lat": 13.0885, "lon": 80.2875, "is_interchange": False, "lines": "Blue Line", "attractions": "Madras High Court, Fort St. George Museum, Marina Beach (North)"},
    {"city": "Chennai", "network": "Chennai Metro (CMRL)", "station": "Government Estate (Marina Beach)", "line": "Blue Line", "color": "#0284c7", "lat": 13.0675, "lon": 80.2745, "is_interchange": False, "lines": "Blue Line", "attractions": "Marina Beach, Anna Memorial, MGR Memorial, Chepauk Stadium"},
    {"city": "Chennai", "network": "Chennai Metro (CMRL)", "station": "AG-DMS / Thousand Lights", "line": "Blue Line", "color": "#0284c7", "lat": 13.0475, "lon": 80.2485, "is_interchange": False, "lines": "Blue Line", "attractions": "Kapaleeshwarar Temple (Mylapore), Semmozhi Poonga Botanical Garden"},
    {"city": "Chennai", "network": "Chennai Metro (CMRL)", "station": "CMBT (Koyambedu Bus Terminal)", "line": "Green Line", "color": "#16a34a", "lat": 13.0685, "lon": 80.2055, "is_interchange": False, "lines": "Green Line", "attractions": "Chennai Mofussil Bus Terminus (CMBT), Koyambedu Wholesale Market"},
    {"city": "Chennai", "network": "Chennai Metro (CMRL)", "station": "Chennai International Airport", "line": "Blue Line", "color": "#0284c7", "lat": 12.9805, "lon": 80.1645, "is_interchange": False, "lines": "Blue Line", "attractions": "Kamaraj Domestic & Anna International Airport Terminals"},
    {"city": "Chennai", "network": "Chennai Metro (CMRL)", "station": "Guindy", "line": "Blue Line", "color": "#0284c7", "lat": 13.0085, "lon": 80.2135, "is_interchange": True, "lines": "Blue Line, Suburban Railway", "attractions": "Guindy National Park, Snake Park, Race Course"},

    # ==================== 7. HYDERABAD (HYDERABAD METRO - HMRL) ====================
    {"city": "Hyderabad", "network": "Hyderabad Metro (HMRL)", "station": "Ameerpet Mega Interchange", "line": "Red & Blue Line", "color": "#dc2626", "lat": 17.4375, "lon": 78.4485, "is_interchange": True, "lines": "Red Line, Blue Line", "attractions": "Ameerpet Commercial Hub, Begumpet"},
    {"city": "Hyderabad", "network": "Hyderabad Metro (HMRL)", "station": "MG Bus Station (MGBS) Interchange", "line": "Red & Green Line", "color": "#dc2626", "lat": 17.3785, "lon": 78.4835, "is_interchange": True, "lines": "Red Line, Green Line", "attractions": "Mahatma Gandhi Central Bus Station, Charminar (1.8 km), Salar Jung Museum"},
    {"city": "Hyderabad", "network": "Hyderabad Metro (HMRL)", "station": "Raidurg (HITEC City)", "line": "Blue Line", "color": "#2563eb", "lat": 17.4415, "lon": 78.3785, "is_interchange": False, "lines": "Blue Line", "attractions": "HITEC City, Cyber Towers, Durgam Cheruvu Cable Bridge, Mindspace"},
    {"city": "Hyderabad", "network": "Hyderabad Metro (HMRL)", "station": "Nampally (Hyderabad Deccan)", "line": "Red Line", "color": "#dc2626", "lat": 17.3915, "lon": 78.4715, "is_interchange": False, "lines": "Red Line", "attractions": "Hyderabad Deccan Railway Station, Public Gardens, Telangana State Archaeology Museum"},
    {"city": "Hyderabad", "network": "Hyderabad Metro (HMRL)", "station": "Secunderabad East & Parade Ground", "line": "Blue & Green Line", "color": "#2563eb", "lat": 17.4415, "lon": 78.5015, "is_interchange": True, "lines": "Blue Line, Green Line", "attractions": "Secunderabad Railway Junction, Clock Tower, Parade Ground"},
    {"city": "Hyderabad", "network": "Hyderabad Metro (HMRL)", "station": "Assembly", "line": "Red Line", "color": "#dc2626", "lat": 17.3985, "lon": 78.4680, "is_interchange": False, "lines": "Red Line", "attractions": "Telangana State Legislative Assembly, Public Gardens"},

    # ==================== 8. JAIPUR (JAIPUR METRO - JMRC) ====================
    {"city": "Jaipur", "network": "Jaipur Metro (JMRC)", "station": "Badi Chaupar (Walled City Heritage)", "line": "Pink Line", "color": "#ec4899", "lat": 26.9240, "lon": 75.8265, "is_interchange": False, "lines": "Pink Line", "attractions": "Hawa Mahal, City Palace, Jantar Mantar, Johari Bazaar"},
    {"city": "Jaipur", "network": "Jaipur Metro (JMRC)", "station": "Chhoti Chaupar", "line": "Pink Line", "color": "#ec4899", "lat": 26.9225, "lon": 75.8195, "is_interchange": False, "lines": "Pink Line", "attractions": "Tripolia Gate, Chandpole Gate, Bapu Bazaar"},
    {"city": "Jaipur", "network": "Jaipur Metro (JMRC)", "station": "Sindhi Camp Central Bus Stand", "line": "Pink Line", "color": "#ec4899", "lat": 26.9230, "lon": 75.7985, "is_interchange": True, "lines": "Pink Line, ISBT Sindhi Camp", "attractions": "Sindhi Camp RSRTC Central Bus Terminus, Station Road"},
    {"city": "Jaipur", "network": "Jaipur Metro (JMRC)", "station": "Jaipur Junction Railway Station", "line": "Pink Line", "color": "#ec4899", "lat": 26.9195, "lon": 75.7895, "is_interchange": True, "lines": "Pink Line, Indian Railways", "attractions": "Jaipur Central Railway Station"},
    {"city": "Jaipur", "network": "Jaipur Metro (JMRC)", "station": "Civil Lines", "line": "Pink Line", "color": "#ec4899", "lat": 26.9085, "lon": 75.7815, "is_interchange": False, "lines": "Pink Line", "attractions": "Raj Bhavan, Chief Minister's Residence, Jacob Road"},
    {"city": "Jaipur", "network": "Jaipur Metro (JMRC)", "station": "Mansarovar Terminal", "line": "Pink Line", "color": "#ec4899", "lat": 26.8770, "lon": 75.7535, "is_interchange": False, "lines": "Pink Line", "attractions": "Mansarovar Colony, City Park Jaipur"},

    # ==================== 9. KOCHI (KOCHI METRO - KMRL) ====================
    {"city": "Kochi", "network": "Kochi Metro (KMRL)", "station": "Maharaja's College / MG Road", "line": "Line 1", "color": "#0ea5e9", "lat": 9.9715, "lon": 76.2845, "is_interchange": False, "lines": "Line 1", "attractions": "Maharaja's College, Marine Drive Walkway, Subhash Bose Park"},
    {"city": "Kochi", "network": "Kochi Metro (KMRL)", "station": "Vyttila Mobility Hub", "line": "Line 1 & Water Metro", "color": "#0ea5e9", "lat": 9.9675, "lon": 76.3205, "is_interchange": True, "lines": "Line 1, Water Metro, KSRTC Bus Hub", "attractions": "Vyttila Mobility Hub, Kochi Water Metro Terminal"},
    {"city": "Kochi", "network": "Kochi Metro (KMRL)", "station": "Edapally (Lulu Mall)", "line": "Line 1", "color": "#0ea5e9", "lat": 10.0245, "lon": 76.3085, "is_interchange": False, "lines": "Line 1", "attractions": "Lulu International Shopping Mall, St. George Forane Church"},
    {"city": "Kochi", "network": "Kochi Metro (KMRL)", "station": "Ernakulam South Railway Station", "line": "Line 1", "color": "#0ea5e9", "lat": 9.9685, "lon": 76.2915, "is_interchange": True, "lines": "Line 1, Indian Railways", "attractions": "Ernakulam Junction (South) Railway Station"},
    {"city": "Kochi", "network": "Kochi Metro (KMRL)", "station": "Aluva Terminal", "line": "Line 1", "color": "#0ea5e9", "lat": 10.1085, "lon": 76.3535, "is_interchange": True, "lines": "Line 1, Airport Bus Shuttle", "attractions": "Aluva Manappuram, Periyar River, Cochin Airport Feeder"},

    # ==================== 10. PUNE (PUNE METRO - MAHAMETRO) ====================
    {"city": "Pune", "network": "Pune Metro (MahaMetro)", "station": "Civil Court Mega Interchange", "line": "Purple & Aqua Line", "color": "#7c3aed", "lat": 18.5285, "lon": 73.8550, "is_interchange": True, "lines": "Line 1 Purple, Line 2 Aqua", "attractions": "District Court, Shivajinagar, COEP Ground"},
    {"city": "Pune", "network": "Pune Metro (MahaMetro)", "station": "Pune Central Railway Station", "line": "Aqua Line", "color": "#06b6d4", "lat": 18.5280, "lon": 73.8740, "is_interchange": True, "lines": "Aqua Line, Indian Railways", "attractions": "Pune Junction Railway Station, Inox Multiplex"},
    {"city": "Pune", "network": "Pune Metro (MahaMetro)", "station": "Deccan Gymkhana & Sambhaji Park", "line": "Aqua Line", "color": "#06b6d4", "lat": 18.5175, "lon": 73.8445, "is_interchange": False, "lines": "Aqua Line", "attractions": "FC Road (Fergusson College Road), Sambhaji Park, JM Road"},
    {"city": "Pune", "network": "Pune Metro (MahaMetro)", "station": "Swargate Terminal", "line": "Purple Line Underground", "color": "#7c3aed", "lat": 18.5015, "lon": 73.8580, "is_interchange": True, "lines": "Purple Line, PMPML/MSRTC Stand", "attractions": "Swargate Central Bus Stand, Saras Baug, Peshwe Park"},
    {"city": "Pune", "network": "Pune Metro (MahaMetro)", "station": "Ramwadi (Airport Road)", "line": "Aqua Line", "color": "#06b6d4", "lat": 18.5520, "lon": 73.9140, "is_interchange": False, "lines": "Aqua Line", "attractions": "Viman Nagar, Phoenix Marketcity, Aga Khan Palace (~2 km)"},

    # ==================== 11. LUCKNOW (LUCKNOW METRO - UPMRC) ====================
    {"city": "Lucknow", "network": "Lucknow Metro (UPMRC)", "station": "Hazratganj", "line": "Red Line", "color": "#e11d48", "lat": 26.8525, "lon": 80.9440, "is_interchange": False, "lines": "Red Line", "attractions": "Hazratganj Shopping Market, GPO, Begum Hazrat Mahal Park"},
    {"city": "Lucknow", "network": "Lucknow Metro (UPMRC)", "station": "Charbagh Railway Station", "line": "Red Line", "color": "#e11d48", "lat": 26.8325, "lon": 80.9230, "is_interchange": True, "lines": "Red Line, Northern & North Eastern Railways", "attractions": "Lucknow Charbagh Railway Junction"},
    {"city": "Lucknow", "network": "Lucknow Metro (UPMRC)", "station": "Alambagh Bus Terminal", "line": "Red Line", "color": "#e11d48", "lat": 26.8165, "lon": 80.9085, "is_interchange": True, "lines": "Red Line, UPSRTC Terminal", "attractions": "Alambagh Central Inter-State Bus Stand"},
    {"city": "Lucknow", "network": "Lucknow Metro (UPMRC)", "station": "Chaudhary Charan Singh Airport", "line": "Red Line", "color": "#e11d48", "lat": 26.7645, "lon": 80.8840, "is_interchange": False, "lines": "Red Line", "attractions": "Lucknow International Airport (Amausi)"},

    # ==================== 12. AGRA (AGRA METRO - UPMRC) ====================
    {"city": "Agra", "network": "Agra Metro (UPMRC)", "station": "Taj East Gate", "line": "Priority Corridor", "color": "#f59e0b", "lat": 27.1725, "lon": 78.0515, "is_interchange": False, "lines": "Yellow Line", "attractions": "Taj Mahal (East Gate), Shilpgram Cultural Complex"},
    {"city": "Agra", "network": "Agra Metro (UPMRC)", "station": "Captain Shubham Gupta (Fatehabad Road)", "line": "Priority Corridor", "color": "#f59e0b", "lat": 27.1635, "lon": 78.0410, "is_interchange": False, "lines": "Yellow Line", "attractions": "Fatehabad Road Hotel Corridor, TDI Mall"},
    {"city": "Agra", "network": "Agra Metro (UPMRC)", "station": "Agra Fort (Jama Masjid)", "line": "Priority Corridor", "color": "#f59e0b", "lat": 27.1815, "lon": 78.0210, "is_interchange": True, "lines": "Yellow Line, Indian Railways", "attractions": "Agra Fort UNESCO Site, Jama Masjid Agra, Agra Fort Railway Station"},
    {"city": "Agra", "network": "Agra Metro (UPMRC)", "station": "Mankameshwar Mandir", "line": "Priority Corridor", "color": "#f59e0b", "lat": 27.1850, "lon": 78.0160, "is_interchange": False, "lines": "Yellow Line", "attractions": "Mankameshwar Ancient Temple, Rawatpara Market"},

    # ==================== 13. NAGPUR (MAHA METRO) ====================
    {"city": "Nagpur", "network": "Nagpur Metro (MahaMetro)", "station": "Sitabuldi Mega Interchange", "line": "Orange & Aqua Line", "color": "#f97316", "lat": 21.1465, "lon": 79.0835, "is_interchange": True, "lines": "Orange Line (North-South), Aqua Line (East-West)", "attractions": "Sitabuldi Fort, Zero Mile Stone, Maharajbagh Zoo"},
    {"city": "Nagpur", "network": "Nagpur Metro (MahaMetro)", "station": "Nagpur Railway Station", "line": "Aqua Line", "color": "#06b6d4", "lat": 21.1520, "lon": 79.0910, "is_interchange": True, "lines": "Aqua Line, Indian Railways Central", "attractions": "Nagpur Central Railway Junction"},
    {"city": "Nagpur", "network": "Nagpur Metro (MahaMetro)", "station": "Airport Station", "line": "Orange Line", "color": "#f97316", "lat": 21.0935, "lon": 79.0620, "is_interchange": False, "lines": "Orange Line", "attractions": "Dr. Babasaheb Ambedkar International Airport"},

    # ==================== 14. KANPUR (KANPUR METRO - UPMRC) ====================
    {"city": "Kanpur", "network": "Kanpur Metro (UPMRC)", "station": "IIT Kanpur", "line": "Orange Line", "color": "#f97316", "lat": 26.5125, "lon": 80.2335, "is_interchange": False, "lines": "Orange Line", "attractions": "Indian Institute of Technology Kanpur (IITK)"},
    {"city": "Kanpur", "network": "Kanpur Metro (UPMRC)", "station": "Moti Jheel", "line": "Orange Line", "color": "#f97316", "lat": 26.4780, "lon": 80.3150, "is_interchange": False, "lines": "Orange Line", "attractions": "Moti Jheel Park & Lake, Municipal Corporation"},
    {"city": "Kanpur", "network": "Kanpur Metro (UPMRC)", "station": "Rawatpur Interchange", "line": "Orange Line", "color": "#f97316", "lat": 26.4860, "lon": 80.2985, "is_interchange": True, "lines": "Orange Line, Indian Railways", "attractions": "Rawatpur Railway Station, JK Temple (~2 km)"},
]

ALL_INDIA_BUS_STOPS = [
    # ==================== 1. DELHI NCR ====================
    {"city": "Delhi", "stop": "Kashmere Gate ISBT Central Terminal", "operator": "DTC & Inter-State", "routes": "ISBT 101, 205, 501, 801, Airport Feeder", "lat": 28.6675, "lon": 77.2285, "landmark": "Kashmere Gate Metro & ISBT"},
    {"city": "Delhi", "stop": "Sarai Kale Khan ISBT & Hazrat Nizamuddin Stand", "operator": "DTC & UPSRTC", "routes": "301, 411, 427, 543, Outer Ring Road Mudrika", "lat": 28.5885, "lon": 77.2580, "landmark": "Hazrat Nizamuddin Railway Station"},
    {"city": "Delhi", "stop": "Anand Vihar ISBT & Railway Station DTC Hub", "operator": "DTC & Inter-State", "routes": "214, 534, 543A, 85, Express Corridors", "lat": 28.6475, "lon": 77.3155, "landmark": "Anand Vihar Railway & Metro Station"},
    {"city": "Delhi", "stop": "India Gate Kartavya Path DTC Stop", "operator": "DTC", "routes": "335, 405, 505, 725, Heritage Shuttle", "lat": 28.6129, "lon": 77.2295, "landmark": "India Gate & National War Memorial"},
    {"city": "Delhi", "stop": "Red Fort Netaji Subhash Marg Terminal", "operator": "DTC", "routes": "118, 214, 403, 753, 901", "lat": 28.6562, "lon": 77.2410, "landmark": "Red Fort (Lal Qila) & Jama Masjid"},
    {"city": "Delhi", "stop": "Shivaji Stadium & Connaught Circus DTC Hub", "operator": "DTC Central", "routes": "181, 340, 522, 604, 781, Airport Shuttle", "lat": 28.6295, "lon": 77.2145, "landmark": "Connaught Place & Gurudwara Bangla Sahib"},

    # ==================== 2. MUMBAI ====================
    {"city": "Mumbai", "stop": "Mumbai Central ST Bus Depot", "operator": "BEST & MSRTC", "routes": "123, 125, 134, 168, Inter-District Shivneri", "lat": 18.9695, "lon": 72.8195, "landmark": "Mumbai Central Railway Station"},
    {"city": "Mumbai", "stop": "Dadar Asiad & Swami Vivekanand TT Circle", "operator": "BEST & MSRTC", "routes": "1, 25, 66, 172, Dadar-Pune Asiad Express", "lat": 19.0185, "lon": 72.8435, "landmark": "Dadar Central & Western Interchange"},
    {"city": "Mumbai", "stop": "Gateway of India / Regal Cinema BEST Depot", "operator": "BEST", "routes": "111, 112, 124, 132, AC Feeder 108", "lat": 18.9235, "lon": 72.8325, "landmark": "Gateway of India & Colaba Causeway"},
    {"city": "Mumbai", "stop": "CSMT / Fort Heritage Bus Stand", "operator": "BEST", "routes": "14, 69, 103, 121, 137, Fort Circular", "lat": 18.9415, "lon": 72.8365, "landmark": "Chhatrapati Shivaji Maharaj Terminus"},
    {"city": "Mumbai", "stop": "Bandra Kurla Complex (BKC) City Bus Terminal", "operator": "BEST", "routes": "BKC-1, BKC-2, 310, 312, 318 AC", "lat": 19.0665, "lon": 72.8685, "landmark": "Bandra Kurla Complex"},
    {"city": "Mumbai", "stop": "Borivali Station West BEST Depot", "operator": "BEST & MSRTC", "routes": "202, 203, 205, National Park AC Feeder", "lat": 19.2295, "lon": 72.8575, "landmark": "Borivali Railway Station & Sanjay Gandhi National Park"},

    # ==================== 3. BANGALORE ====================
    {"city": "Bangalore", "stop": "Kempegowda (Majestic) Bus Station Central", "operator": "BMTC & KSRTC", "routes": "V-335E, 500D, 365, 401K, KIA Airport Shuttles", "lat": 12.9775, "lon": 77.5715, "landmark": "City Railway Station & Majestic Metro"},
    {"city": "Bangalore", "stop": "Shivajinagar BMTC Bus Terminus", "operator": "BMTC", "routes": "138, 290, 305, 314, Cantonment Express", "lat": 12.9855, "lon": 77.6045, "landmark": "Commercial Street & Russell Market"},
    {"city": "Bangalore", "stop": "Shantinagar KSRTC/BMTC TTMC Hub", "operator": "BMTC & KSRTC", "routes": "340, 342, 348, Airavat Club Class Stand", "lat": 12.9555, "lon": 77.5955, "landmark": "Lalbagh Botanical Garden (Double Road)"},
    {"city": "Bangalore", "stop": "Yeshwanthpur TTMC Bus Terminal", "operator": "BMTC", "routes": "250, 252, 401, 500, Ring Road Volvos", "lat": 13.0245, "lon": 77.5495, "landmark": "Yeshwanthpur Junction Railway Station"},
    {"city": "Bangalore", "stop": "Banashankari BMTC TTMC Bus Hub", "operator": "BMTC", "routes": "12, 215, 600, South Bangalore Express", "lat": 12.9155, "lon": 77.5735, "landmark": "Banashankari Metro & Temple"},

    # ==================== 4. AHMEDABAD & GANDHINAGAR ====================
    {"city": "Ahmedabad", "stop": "Ranip Central GSRTC & BRTS Hub", "operator": "AMTS, BRTS & GSRTC", "routes": "BRTS Line 1, AMTS 58, 62, 70, Express Intercity", "lat": 23.0725, "lon": 72.5780, "landmark": "Sabarmati Ashram & Ranip Metro"},
    {"city": "Ahmedabad", "stop": "Gita Mandir Central ST Bus Terminal", "operator": "GSRTC State Transport", "routes": "Intercity Gujarat State Express, 101, 151", "lat": 23.0125, "lon": 72.5895, "landmark": "ST Central Depot, Astodia Gate"},
    {"city": "Ahmedabad", "stop": "Lal Darwaja City Bus Terminal", "operator": "AMTS", "routes": "AMTS 1, 3, 5, 22, 31, 40, Heritage Feeder", "lat": 23.0245, "lon": 72.5785, "landmark": "Sidi Saiyyed Mosque, Bhadra Fort"},
    {"city": "Ahmedabad", "stop": "Kalupur Railway Station AMTS Stand", "operator": "AMTS & BRTS", "routes": "10, 13, 44, 46, BRTS Corridor 2", "lat": 23.0275, "lon": 72.6015, "landmark": "Ahmedabad Central Railway Junction"},
    {"city": "Ahmedabad", "stop": "Kankaria Lakefront Bus Stand", "operator": "AMTS", "routes": "AMTS 18, 24, 72, 85, Kankaria Circuit", "lat": 23.0075, "lon": 72.6025, "landmark": "Kankaria Lakefront & Zoo"},
    {"city": "Ahmedabad", "stop": "Iscon Cross Road BRTS Terminal", "operator": "BRTS & AMTS", "routes": "BRTS Line 1, 151, SG Highway AC Volvos", "lat": 23.0285, "lon": 72.5065, "landmark": "SG Highway, Iscon Mega Mall"},
    {"city": "Gandhinagar", "stop": "Gandhinagar Central ST Bus Depot (Sector 11)", "operator": "GSRTC & VTCOS City Bus", "routes": "1, 2, 7, Gandhinagar-Ahmedabad Express Shuttle", "lat": 23.2165, "lon": 72.6415, "landmark": "Sector 11 Pathika Ashram, Vidhan Sabha"},

    # ==================== 5. KOLKATA ====================
    {"city": "Kolkata", "stop": "Esplanade / Dharmatala Central Bus Terminus", "operator": "WBTC & CSTC", "routes": "S-12, AC-1, C-8, E-1, Howrah Shuttle", "lat": 22.5655, "lon": 88.3525, "landmark": "New Market & Esplanade Metro"},
    {"city": "Kolkata", "stop": "Howrah Station Mega Bus Stand", "operator": "WBTC", "routes": "24, 39, 44, 52, 71, Mini-Bus Terminus", "lat": 22.5845, "lon": 88.3415, "landmark": "Howrah Railway Station & Hooghly River"},
    {"city": "Kolkata", "stop": "Karunamoyee International Bus Terminal (Salt Lake)", "operator": "WBTC & Inter-State", "routes": "AC-24, V-1, S-9, Dhaka International Volvos", "lat": 22.5845, "lon": 88.4215, "landmark": "Salt Lake Central Park & Karunamoyee Metro"},
    {"city": "Kolkata", "stop": "Babughat Inter-State Bus Stand", "operator": "WBTC & Private", "routes": "Digha, Bakkhali, Sundarbans Tourist Volvos", "lat": 22.5685, "lon": 88.3425, "landmark": "Babughat Ferry Ghat, Eden Gardens"},

    # ==================== 6. CHENNAI ====================
    {"city": "Chennai", "stop": "CMBT (Koyambedu Central Mofussil Stand)", "operator": "MTC & SETC", "routes": "101, 102, 114, 570, Inter-State SETC", "lat": 13.0685, "lon": 80.2055, "landmark": "CMBT Metro & Koyambedu Market"},
    {"city": "Chennai", "stop": "Broadway Central Bus Stand (Parrys Corner)", "operator": "MTC", "routes": "1, 6, 11, 21, 29C, Beach Corridors", "lat": 13.0895, "lon": 80.2885, "landmark": "High Court & Fort St. George"},
    {"city": "Chennai", "stop": "T. Nagar (Panagal Park) Bus Terminus", "operator": "MTC", "routes": "47A, 5E, 12B, 19B, 49", "lat": 13.0415, "lon": 80.2345, "landmark": "T. Nagar Ranganathan Shopping Street"},
    {"city": "Chennai", "stop": "Kilambakkam (KCBT Centenary Terminus)", "operator": "SETC & MTC", "routes": "Southern Express Volvos, 70V, 114K", "lat": 12.8655, "lon": 80.0815, "landmark": "New South Tamil Nadu Integrated Terminal"},

    # ==================== 7. HYDERABAD ====================
    {"city": "Hyderabad", "stop": "Mahatma Gandhi Bus Station (MGBS Imlibun)", "operator": "TSRTC & Inter-State", "routes": "100, 200, 216, 218, Garuda AC Volvos", "lat": 17.3785, "lon": 78.4835, "landmark": "MGBS Metro Interchange & Musi River"},
    {"city": "Hyderabad", "stop": "Jubilee Bus Station (JBS Secunderabad)", "operator": "TSRTC", "routes": "1, 10, 24, 25S, 86, Rajiv Rahadari Express", "lat": 17.4485, "lon": 78.4985, "landmark": "JBS Metro Station & Secunderabad"},
    {"city": "Hyderabad", "stop": "Koti Central Bus Terminus", "operator": "TSRTC", "routes": "1Z, 2Z, 65, 83, 115, Charminar Shuttle", "lat": 17.3885, "lon": 78.4845, "landmark": "Osmania Medical College & Koti Markets"},

    # ==================== 8. JAIPUR ====================
    {"city": "Jaipur", "stop": "Sindhi Camp ISBT Central Bus Terminus", "operator": "JCTSL & RSRTC", "routes": "1, 3, 5, 9, RSRTC Goldline / Superfast", "lat": 26.9230, "lon": 75.7985, "landmark": "Sindhi Camp Metro Station"},
    {"city": "Jaipur", "stop": "Badi Chaupar City Palace Bus Stand", "operator": "JCTSL", "routes": "Route 1A, 2, 7, Pink Heritage Shuttle", "lat": 26.9240, "lon": 75.8265, "landmark": "Hawa Mahal, City Palace, Johari Bazaar"},
    {"city": "Jaipur", "stop": "Narayan Singh Circle RSRTC Stand", "operator": "RSRTC Intercity", "routes": "Delhi, Agra, Bharatpur, Ajmer Volvos", "lat": 26.8995, "lon": 75.8175, "landmark": "Sawai Man Singh Hospital, Tonk Road"},

    # ==================== 9. PUNE ====================
    {"city": "Pune", "stop": "Swargate Central MSRTC & PMPML Hub", "operator": "PMPML & MSRTC", "routes": "1, 2, 8, 24, 100, Shivneri Asiad Stand", "lat": 18.5015, "lon": 73.8580, "landmark": "Swargate Metro & Saras Baug"},
    {"city": "Pune", "stop": "Shivajinagar ST Bus Stand", "operator": "PMPML & MSRTC", "routes": "3, 11, 28, 36, Mumbai Superfast Volvos", "lat": 18.5315, "lon": 73.8525, "landmark": "Shivajinagar Railway Station"},
    {"city": "Pune", "stop": "Pune Central Railway Station PMPML Stand", "operator": "PMPML", "routes": "Station-Katraj, Station-Nigdi, Hinjawadi IT Feeder", "lat": 18.5290, "lon": 73.8735, "landmark": "Pune Junction Railway Station"},

    # ==================== 10. KOCHI ====================
    {"city": "Kochi", "stop": "Vyttila Mobility Hub KSRTC Terminal", "operator": "KSRTC & Private City", "routes": "Airport Shuttle, K-Bus, High Court Ferry Feeder", "lat": 9.9675, "lon": 76.3205, "landmark": "Kochi Metro Vyttila & Water Metro"},
    {"city": "Kochi", "stop": "Kaloor Bus Stand & Stadium Terminal", "operator": "KSRTC & City Bus", "routes": "Fort Kochi Circuit, Aluva Route, Menaka Stand", "lat": 9.9975, "lon": 76.2945, "landmark": "Jawaharlal Nehru International Stadium"},
    {"city": "Kochi", "stop": "Fort Kochi Bus Stand (Customs Jetty)", "operator": "City Bus & Private", "routes": "Fort Kochi-Ernakulam South, Mattancherry Circuit", "lat": 9.9665, "lon": 76.2415, "landmark": "Chinese Fishing Nets & St. Francis Church"},

    # ==================== 11. AGRA ====================
    {"city": "Agra", "stop": "Idgah Central Bus Stand", "operator": "UPSRTC & City Bus", "routes": "Agra-Mathura, Agra-Jaipur, Taj Mahal AC Shuttles", "lat": 27.1635, "lon": 77.9945, "landmark": "Idgah Railway Station & Cantt"},
    {"city": "Agra", "stop": "Bijli Ghar / Agra Fort Bus Stand", "operator": "UPSRTC City Electric", "routes": "Fort-Taj Circuit, Fatehabad Road Feeder", "lat": 27.1825, "lon": 78.0195, "landmark": "Agra Fort & Jama Masjid"},
    {"city": "Agra", "stop": "ISBT Agra (Transport Nagar)", "operator": "UPSRTC Inter-State", "routes": "Delhi-Agra Yamuna Expressway Volvos, Lucknow AC", "lat": 27.2285, "lon": 77.9625, "landmark": "NH-19 Delhi-Agra Highway Hub"},

    # ==================== 12. VARANASI ====================
    {"city": "Varanasi", "stop": "Varanasi Cantt Central Roadways Stand", "operator": "UPSRTC & City Electric", "routes": "Cantt-Godowlia, Sarnath Circuit, Kashi Vishwanath Feeder", "lat": 25.3285, "lon": 82.9865, "landmark": "Varanasi Junction Cantt Railway Station"},
    {"city": "Varanasi", "stop": "Godowlia Chauraha E-Transit Hub", "operator": "Varanasi City Transit", "routes": "Dashashwamedh Ghat Shuttle, Kashi Vishwanath Electric", "lat": 25.3095, "lon": 83.0075, "landmark": "Dashashwamedh Ghat & Kashi Vishwanath Temple"},
    {"city": "Varanasi", "stop": "Sarnath Archeological Complex Bus Stand", "operator": "Varanasi City Electric", "routes": "Sarnath-Cantt E-Bus, Dhamek Stupa Shuttle", "lat": 25.3815, "lon": 83.0235, "landmark": "Dhamek Stupa & Sarnath Museum"},

    # ==================== 13. GOA ====================
    {"city": "Goa", "stop": "Panaji Kadamba Central Bus Stand", "operator": "KTC (Kadamba)", "routes": "Panaji-Margao, Panaji-Calangute, Airport Express EV", "lat": 15.4955, "lon": 73.8345, "landmark": "Panaji City Center & Mandovi River"},
    {"city": "Goa", "stop": "Margao KTC Bus Stand", "operator": "KTC", "routes": "Margao-Colva, Margao-Panaji, South Goa Express", "lat": 15.2865, "lon": 73.9685, "landmark": "Margao Railway Junction & Colva Road"},
    {"city": "Goa", "stop": "Calangute Beach Bus Stand", "operator": "KTC & Private", "routes": "Calangute-Panaji, Baga-Anjuna Feeder", "lat": 15.5415, "lon": 73.7585, "landmark": "Calangute Beach & Baga Road"},
    {"city": "Goa", "stop": "Mapusa KTC Bus Stand", "operator": "KTC", "routes": "North Goa Beaches (Vagator, Morjim, Arambol)", "lat": 15.5985, "lon": 73.8165, "landmark": "Mapusa Friday Market"},

    # ==================== 14. MYSORE ====================
    {"city": "Mysore", "stop": "City Bus Stand (CBS / KR Circle)", "operator": "KSRTC City (Mitra)", "routes": "Route 201, 202, 150, Chamundi Hill Shuttle", "lat": 12.3085, "lon": 76.6535, "landmark": "Mysore Palace & Devaraja Market"},
    {"city": "Mysore", "stop": "Suburb Central KSRTC Bus Stand", "operator": "KSRTC Intercity", "routes": "Mysore-Bengaluru Airavat Express, Ooty Circuit", "lat": 12.3165, "lon": 76.6575, "landmark": "St. Philomena's Cathedral & Bengaluru Road"},
    {"city": "Mysore", "stop": "Chamundi Hill Bus Stand", "operator": "KSRTC Mitra City", "routes": "201, 201A Chamundeshwari Temple Shuttle", "lat": 12.2745, "lon": 76.6715, "landmark": "Chamundeshwari Temple & Nandi Statue"},

    # ==================== 15. AMRITSAR ====================
    {"city": "Amritsar", "stop": "Amritsar Central ISBT Bus Stand", "operator": "PUNBUS & PRTC", "routes": "Golden Temple Heritage E-Shuttle, Delhi-Amritsar AC Volvos", "lat": 31.6245, "lon": 74.8895, "landmark": "Amritsar ISBT Terminal"},
    {"city": "Amritsar", "stop": "Golden Temple Heritage Street Shuttle", "operator": "Amritsar City E-Bus", "routes": "Station-Heritage Walk Free Shuttle", "lat": 31.6210, "lon": 74.8765, "landmark": "Golden Temple (Harmandir Sahib) & Jallianwala Bagh"},

    # ==================== 16. CHANDIGARH ====================
    {"city": "Chandigarh", "stop": "ISBT Sector 43 Central Bus Terminal", "operator": "CTU & Inter-State", "routes": "Shimla, Manali, Delhi, Punjab Volvos", "lat": 30.7225, "lon": 76.7445, "landmark": "Sector 43 ISBT Terminal"},
    {"city": "Chandigarh", "stop": "ISBT Sector 17 City Center Terminal", "operator": "CTU", "routes": "Sukhna Lake Shuttle, Rock Garden Tourist Bus", "lat": 30.7415, "lon": 76.7825, "landmark": "Sector 17 Plaza & Capitol Complex"},

    # ==================== 17. SHIMLA & MANALI ====================
    {"city": "Shimla", "stop": "Shimla ISBT Tutikandi New Bus Stand", "operator": "HRTC & Inter-State", "routes": "Delhi-Shimla Himsuta Volvos, Chandigarh Express", "lat": 31.0885, "lon": 77.1525, "landmark": "Tutikandi Bypass ISBT"},
    {"city": "Shimla", "stop": "Shimla Old Bus Stand (Cart Road)", "operator": "HRTC Local", "routes": "Mall Road Lift Feeder, Kufri Shuttle", "lat": 31.1035, "lon": 77.1715, "landmark": "Mall Road Lift, The Ridge"},
    {"city": "Manali", "stop": "Manali Private & HRTC Volvo Bus Stand", "operator": "HRTC & Private Volvos", "routes": "Delhi-Manali Himsuta, Solang Valley E-Bus", "lat": 32.2415, "lon": 77.1895, "landmark": "Mall Road Manali & Beas River"},

    # ==================== 18. SRINAGAR ====================
    {"city": "Srinagar", "stop": "TRC Srinagar (Tourist Reception Centre Stand)", "operator": "JKSRTC & Tourist Cabs", "routes": "Gulmarg, Pahalgam, Sonamarg Tourist Shuttles", "lat": 34.0725, "lon": 74.8215, "landmark": "Dal Lake Dalgate, Tourist Reception Centre"},
    {"city": "Srinagar", "stop": "Batamaloo General Bus Stand", "operator": "JKSRTC Local", "routes": "Lal Chowk, Hazratbal, Boulevard Feeder", "lat": 34.0715, "lon": 74.7915, "landmark": "Lal Chowk & Civil Secretariat"},

    # ==================== 19. UDAIPUR ====================
    {"city": "Udaipur", "stop": "Udaipur Central Bus Stand (Udiapole)", "operator": "RSRTC & Private", "routes": "Ahmedabad, Jaipur, Mount Abu Goldline Express", "lat": 24.5775, "lon": 73.7015, "landmark": "Udiapole & Udaipur City Railway Station"},
    {"city": "Udaipur", "stop": "Chetak Circle City Bus Stand", "operator": "Udaipur City Bus", "routes": "City Palace, Lake Pichola, Saheliyon Ki Bari Feeder", "lat": 24.5935, "lon": 73.6895, "landmark": "Chetak Circle & Fatehsagar Lake"},

    # ==================== 20. GUWAHATI ====================
    {"city": "Guwahati", "stop": "ISBT Betkuchi Central Bus Terminus", "operator": "ASTC & Inter-State", "routes": "Shillong, Kaziranga, Tezpur, Silchar Volvos", "lat": 26.1145, "lon": 91.7315, "landmark": "National Highway 27 Betkuchi"},
    {"city": "Guwahati", "stop": "Paltan Bazaar ASTC Bus Stand", "operator": "ASTC", "routes": "Kamakhya Temple Shuttle, Airport Feeder", "lat": 26.1815, "lon": 91.7515, "landmark": "Guwahati Central Railway Station"},

    # ==================== 21. PATNA ====================
    {"city": "Patna", "stop": "ISBT Pataliputra (Bairiya) Bus Terminal", "operator": "BSRTC & Inter-State", "routes": "Gaya, Nalanda, Rajgir, Varanasi AC Volvos", "lat": 25.5685, "lon": 85.2015, "landmark": "Bairiya New Integrated ISBT Patna"},
    {"city": "Patna", "stop": "Gandhi Maidan Central Bus Stand", "operator": "BSRTC City Electric", "routes": "Patna Junction, Golghar, Takht Sri Patna Sahib Shuttle", "lat": 25.6175, "lon": 85.1445, "landmark": "Gandhi Maidan & Golghar"},

    # ==================== 22. BHOPAL & INDORE ====================
    {"city": "Bhopal", "stop": "ISBT Habibganj (Rani Kamlapati) Terminal", "operator": "BCLL & Inter-State", "routes": "Indore, Ujjain, Jabalpur AC Intercity", "lat": 23.2195, "lon": 77.4425, "landmark": "Rani Kamlapati World-Class Railway Station"},
    {"city": "Indore", "stop": "Sarwate Central Bus Stand", "operator": "AICTSL & Intercity", "routes": "Ujjain Mahakal Shuttle, Bhopal Superfast, Omkareshwar Feeder", "lat": 22.7145, "lon": 75.8695, "landmark": "Indore Junction Railway Station"},
]
