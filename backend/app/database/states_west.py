"""
Western India States Master Districts & Tourist Attractions
Covers Goa (2), Gujarat (33), Maharashtra (36).
"""

WEST_STATES = {
    # ==================== 1. GOA (2 Districts) ====================
    "Goa": [
        {
            "district": "North Goa", "lat": 15.4989, "lon": 73.8278, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Goan Fish Curry Rice, Prawn Balchão, Bebinca & Feni",
            "description": "Vibrant coastal hub famous for golden beaches, water sports, Portuguese colonial forts, and nightlife.",
            "places": [
                {"name": "Fort Aguada & 1864 Portuguese Lighthouse", "category": "Fort", "entry_fee": 25, "opening": "09:30", "closing": "18:00", "description": "17th-century Portuguese fortress overlooking the Arabian Sea and Sinquerim Beach, with fresh water storage cisterns."},
                {"name": "Basilica of Bom Jesus (UNESCO World Heritage Site)", "category": "Spiritual", "entry_fee": 0, "opening": "09:00", "closing": "18:30", "description": "1605 Baroque Jesuit church housing the sacred mortal remains of Saint Francis Xavier in Old Goa."},
                {"name": "Baga & Calangute Beach Coastal Strip", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "23:00", "description": "Iconic energetic shoreline featuring parasailing, jet-skiing, beach shacks, and live seaside music."},
                {"name": "Anjuna Beach & Wednesday Flea Market", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Scenic red rocky cove renowned for alternative music, bohemian flea markets, and sunset gatherings."},
            ]
        },
        {
            "district": "South Goa", "lat": 15.2736, "lon": 73.9582, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Goan Pork Vindaloo, Sanna, Crab Xec Xec & Bebinca",
            "description": "Peaceful tropical paradise with white-sand beaches, cascading jungle waterfalls, and spice plantations.",
            "places": [
                {"name": "Dudhsagar Waterfalls (Sea of Milk)", "category": "Waterfall", "entry_fee": 100, "opening": "08:00", "closing": "16:30", "description": "Four-tiered 310m thundering waterfall in Bhagwan Mahaveer Sanctuary, where railway trains pass across the falls."},
                {"name": "Palolem & Agonda Crescent Beaches", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Idyllic crescent bay with calm shallow waters, dolphin-spotting cruises, and quiet beach huts."},
                {"name": "Cabo de Rama Fort & Cliff Beach", "category": "Fort", "entry_fee": 0, "opening": "09:00", "closing": "17:30", "description": "Historic cliffside coastal fort named after Lord Rama, offering 360-degree views of the turquoise Arabian Sea."},
            ]
        },
    ],

    # ==================== 2. GUJARAT (33 Districts) ====================
    "Gujarat": [
        {
            "district": "Ahmedabad", "lat": 23.0225, "lon": 72.5714, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Gujarati Thali, Khaman Dhokla, Fafda Jalebi & Handvo",
            "description": "India's first UNESCO World Heritage City, textile capital on the Sabarmati River rich in Pols and Stepwells.",
            "places": [
                {"name": "Sabarmati Ashram (Gandhi Smarak Sangrahalaya)", "category": "Historical", "entry_fee": 0, "opening": "08:30", "closing": "18:30", "description": "Mahatma Gandhi's peaceful riverside headquarters from 1917–1930, launch point of the historic Dandi Salt March."},
                {"name": "Adalaj Stepwell (Rudabai Stepwell)", "category": "Historical", "entry_fee": 25, "opening": "08:00", "closing": "18:00", "description": "1499 CE five-storey subterranean stepwell with Solanki stone pillars and octagonal shafts carved with floral reliefs."},
                {"name": "Sidi Saiyyed Mosque & Tree of Life Jali", "category": "Historical", "entry_fee": 0, "opening": "07:00", "closing": "19:00", "description": "1573 mosque celebrated for its intricate carved stone lattice windows depicting the intertwining Tree of Life."},
                {"name": "Sabarmati Riverfront Promenade", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Modern 11km pedestrian waterfront with flower gardens, Atal pedestrian bridge, speedboats, and cycling paths."},
            ]
        },
        {
            "district": "Kachchh", "lat": 23.2420, "lon": 69.6669, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Kutchi Dabeli, Gulab Pak & Bajra No Rotlo with Ringna No Oro",
            "description": "India's largest district, home to the Great Rann white salt desert, Rann Utsav, and artisan villages.",
            "places": [
                {"name": "Great Rann of Kutch White Salt Desert (Dhordo)", "category": "Nature", "entry_fee": 100, "opening": "06:00", "closing": "20:00", "description": "World's largest seasonal salt marsh turning into an endless blinding white expanse, magical under full moon nights."},
                {"name": "Aina Mahal & Prag Mahal Bhuj", "category": "Palace", "entry_fee": 50, "opening": "09:00", "closing": "17:30", "description": "18th-century Palace of Mirrors crafted by Ramsinh Malam and Italian-Gothic Prag Mahal with a 45m clock tower."},
                {"name": "Dholavira Harappan City (UNESCO World Heritage Site)", "category": "Historical", "entry_fee": 25, "opening": "08:00", "closing": "18:00", "description": "Ancient 5,000-year-old Indus Valley metropolis famous for water harvesting reservoirs, citadel, and stone inscriptions."},
            ]
        },
        {
            "district": "Gir Somnath", "lat": 20.9012, "lon": 70.3667, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Kathiyawadi Thali, Sev Tameta & Magas",
            "description": "Spiritual coastal district home to the first Jyotirlinga Somnath and the Asiatic Lion territory of Gir.",
            "places": [
                {"name": "Somnath Jyotirlinga Temple & Triveni Sangam", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "21:30", "description": "First among the twelve sacred Shiva Jyotirlingas, overlooking the Arabian Sea with evening light & sound shows."},
                {"name": "Gir National Park & Devalia Safari Park", "category": "Wildlife", "entry_fee": 800, "opening": "06:00", "closing": "17:00", "description": "The only natural habitat on Earth of the Asiatic Lion (Panthera leo persica), spanning dry teak scrub forests."},
            ]
        },
        {
            "district": "Devbhumi Dwarka", "lat": 22.2442, "lon": 68.9685, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Dwarkadhish Prasadam, Farsan & Kadhi Khichdi",
            "description": "Ancient pilgrimage capital of Lord Krishna, one of the four sacred Char Dham and Sapta Puri holy cities.",
            "places": [
                {"name": "Dwarkadhish Temple (Jagat Mandir)", "category": "Temple", "entry_fee": 0, "opening": "06:30", "closing": "21:30", "description": "2,200-year-old 5-storey limestone temple supported by 72 pillars on the Gomti River confluence with the Arabian Sea."},
                {"name": "Beyt Dwarka Island & Sudama Setu", "category": "Spiritual", "entry_fee": 20, "opening": "07:00", "closing": "18:30", "description": "Sacred island believed to be Krishna's royal residence, reached by scenic ferry boats across coral reefs."},
                {"name": "Shivrajpur Beach (Blue Flag Certified)", "category": "Beach", "entry_fee": 30, "opening": "08:00", "closing": "18:30", "description": "Pristine white sand beach with international Blue Flag eco-certification, scuba diving, and clear turquoise waters."},
            ]
        },
        {
            "district": "Narmada", "lat": 21.8700, "lon": 73.5500, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Kevadia Gujarati Thali & Roasted Corn",
            "description": "Home to the colossal Statue of Unity, Sardar Sarovar Dam, and lush Satpura-Vindhyachal river valleys.",
            "places": [
                {"name": "Statue of Unity (World's Tallest Statue - 182m)", "category": "Heritage", "entry_fee": 150, "opening": "08:00", "closing": "18:00", "description": "182-meter bronze colossus of Sardar Vallabhbhai Patel with high-speed elevators, viewing gallery, and laser show."},
                {"name": "Sardar Sarovar Dam & Valley of Flowers", "category": "Nature", "entry_fee": 50, "opening": "09:00", "closing": "18:00", "description": "Third-highest concrete dam in India on the Narmada River surrounded by 24-acre colorful floral gardens."},
            ]
        },
        {
            "district": "Patan", "lat": 23.8500, "lon": 72.1167, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Patan Patola Handloom & Gujarati Sweets",
            "description": "Medieval capital of the Solanki rulers, world-famous for the UNESCO Rani ki Vav and double-ikat Patola silk.",
            "places": [
                {"name": "Rani ki Vav (The Queen's Stepwell - UNESCO World Heritage)", "category": "Historical", "entry_fee": 40, "opening": "08:00", "closing": "18:00", "description": "11th-century inverted subterranean temple stepwell featuring over 500 principal sculptures and 1,000 minor reliefs (on ₹100 note)."},
                {"name": "Patan Patola Silk Heritage Weaving Museum", "category": "Cultural", "entry_fee": 50, "opening": "09:00", "closing": "18:00", "description": "Museum preserving the 900-year-old double-ikat weaving tradition where natural dyes remain bright for centuries."},
            ]
        },
        {
            "district": "Junagadh", "lat": 21.5222, "lon": 70.4579, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Kesar Mangoes, Kathiyawadi Undhiyu & Bajra No Rotlo",
            "description": "Ancient fortress city at the base of Mount Girnar, holding Ashokan rock edicts and Nawabi palaces.",
            "places": [
                {"name": "Uparkot Fort & 3rd-Century Buddhist Caves", "category": "Fort", "entry_fee": 25, "opening": "08:00", "closing": "18:00", "description": "Ancient 319 BCE citadel with 20m high ramparts, Adi Kadi Vav stepwell, and Mauryan rock-cut monasteries."},
                {"name": "Girnar Hill & Ropeway (Asia's Longest Temple Ropeway)", "category": "Viewpoint", "entry_fee": 700, "opening": "06:00", "closing": "18:00", "description": "Holy mountain ascending 10,000 steps to ancient Jain and Dattatreya shrines, connected by a 2.3km cable car."},
                {"name": "Mahabat Maqbara Palace Mausoleum", "category": "Historical", "entry_fee": 0, "opening": "09:00", "closing": "17:30", "description": "1892 Indo-Islamic architectural marvel with spiraling minarets, French gothic arches, and silver gates."},
            ]
        },
        {
            "district": "Vadodara", "lat": 22.3072, "lon": 73.1812, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Sev Usal, Bhakarwadi & Poha",
            "description": "Cultural capital of Gujarat ruled by the Gaekwad Maratha dynasty, famed for magnificent palaces and museums.",
            "places": [
                {"name": "Laxmi Vilas Palace (Four Times the Size of Buckingham Palace)", "category": "Palace", "entry_fee": 250, "opening": "10:00", "closing": "17:00", "description": "1890 Indo-Saracenic royal residence of Maharaja Sayajirao Gaekwad III with European stained glass, mosaics, and armory."},
                {"name": "Champaner-Pavagadh Archaeological Park (UNESCO World Heritage)", "category": "Historical", "entry_fee": 40, "opening": "08:30", "closing": "17:30", "description": "Complete unexcavated medieval Hindu-Muslim city dating from the 8th to 14th century, topped by Kalika Mata Temple."},
            ]
        },
        {
            "district": "Surat", "lat": 21.1702, "lon": 72.8311, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Surati Locho, Ghari, Ponk & Undhiyu",
            "description": "Diamond City and Silk City of the World on the Tapi River, culinary haven celebrated for Locho and sweets.",
            "places": [
                {"name": "Dumas Beach & Black Sand Shoreline", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Popular urban beach on the Arabian Sea with unique black volcanic sand and famous food stalls for hot bhajiyas."},
                {"name": "Surat Castle (Old Fort)", "category": "Fort", "entry_fee": 20, "opening": "10:00", "closing": "18:00", "description": "16th-century fortress built by Khudawand Khan on the Tapi River to defend against Portuguese sea invaders."},
            ]
        },
        {
            "district": "Rajkot", "lat": 22.3039, "lon": 70.8022, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Rajkot Peda, Chikki, Kathiyawadi Thali & Ice Gola",
            "description": "Heart of Saurashtra where Mahatma Gandhi spent his childhood, rich in handicrafts, silversmithing, and engines.",
            "places": [
                {"name": "Kaba Gandhi No Delo (Mahatma Gandhi Childhood Residence)", "category": "Historical", "entry_fee": 0, "opening": "09:00", "closing": "18:00", "description": "Traditional Saurashtra townhouse where Gandhi lived, now housing a gallery of photographs and spinning charkha."},
                {"name": "Rotary Dolls Museum & Pradhyuman Zoological Park", "category": "Museum", "entry_fee": 30, "opening": "09:30", "closing": "17:30", "description": "Unique international museum exhibiting over 1,600 traditional dolls from 102 nations and adjacent safari zoo."},
            ]
        },
        {
            "district": "Bhavnagar", "lat": 21.7645, "lon": 72.1519, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bhavnagari Gathiya, Bateta Vada & Peda",
            "description": "Princely port city on the Gulf of Khambhat, gateway to the sacred 863 marble temples of Palitana.",
            "places": [
                {"name": "Palitana Shatrunjaya Hill Temple Complex", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "World's only mountain with over 863 intricately carved white marble Jain temples, climbing 3,800 stone steps."},
                {"name": "Velavadar Blackbuck National Park", "category": "Wildlife", "entry_fee": 100, "opening": "06:30", "closing": "17:30", "description": "Grassland savannah sanctuary home to thousands of leaping blackbucks, Indian wolves, and striped hyenas."},
            ]
        },
        {
            "district": "Porbandar", "lat": 21.6417, "lon": 69.6293, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Porbandari Khaja & Fresh Coastal Seafood",
            "description": "Birthplace of Mahatma Gandhi on the Arabian Sea, featuring white sandstone colonial architecture.",
            "places": [
                {"name": "Kirti Mandir (Birthplace of Mahatma Gandhi)", "category": "Historical", "entry_fee": 0, "opening": "07:30", "closing": "19:00", "description": "79-foot memorial temple adjoining the three-storey 1869 ancestral Haveli where Mahatma Gandhi was born."},
                {"name": "Chowpati Beach & Marine Promenade", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Clean coastal promenade popular for sunset walking, flamingos, and gentle sea breezes."},
            ]
        },
        {
            "district": "Dang", "lat": 20.8560, "lon": 73.7140, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Nagali Roti (Ragi), Wild Bamboo Sprouts & Dang Forest Honey",
            "description": "Lush tribal forest district in the Sahyadris, home to Gujarat's only hill station Saputara and Gira waterfalls.",
            "places": [
                {"name": "Saputara Hill Station & Table Ground", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Tranquil plateau at 1,000m with Saputara Lake boating, passenger ropeway, sunset points, and tribal museum."},
                {"name": "Gira Waterfalls", "category": "Waterfall", "entry_fee": 20, "opening": "08:00", "closing": "17:30", "description": "150-foot seasonal waterfall dropping into the Ambika River amidst dense bamboo and teak forests."},
            ]
        },
        # All other Gujarat Districts (Amreli, Anand, Aravalli, Banaskantha, Bharuch, Botad, Chhota Udaipur, Dahod, Gandhinagar, Jamnagar, Kheda, Mahisagar, Mehsana, Morbi, Navsari, Panchmahal, Sabarkantha, Surendranagar, Tapi, Valsad)
        {
            "district": "Gandhinagar", "lat": 23.2156, "lon": 72.6369, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Gujarati Snacks & Masala Chai",
            "description": "The Green Capital of Gujarat, planned garden city on the Sabarmati home to the grand Akshardham complex.",
            "places": [
                {"name": "Akshardham Temple & Musical Water Show", "category": "Spiritual", "entry_fee": 0, "opening": "09:30", "closing": "20:00", "description": "Sprawling 23-acre pink sandstone temple complex with sculpted pillars, gardens, and Sat-Chit-Anand water show."},
                {"name": "Indroda Dinosaur and Fossil Park", "category": "Nature", "entry_fee": 30, "opening": "08:00", "closing": "18:00", "description": "India's own Jurassic Park, second-largest dinosaur egg hatchery in the world with life-size dinosaur models and zoo."},
            ]
        },
        {
            "district": "Jamnagar", "lat": 22.4707, "lon": 70.0577, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kachori, Ghughra & Dry Fruit Kachori",
            "description": "Jewel of Kathiawar, princely Solanki city renowned for brassware, bandhani tie-dye, and marine parks.",
            "places": [
                {"name": "Marine National Park (Gulf of Kutch)", "category": "Wildlife", "entry_fee": 150, "opening": "08:00", "closing": "17:00", "description": "India's first marine sanctuary with 42 islands, where visitors can walk through coral reefs at low tide without diving."},
                {"name": "Lakhota Lake & Palace Museum", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "18:00", "description": "19th-century island fortress in the center of Ranmal Lake housing medieval weaponry and pottery."},
            ]
        },
        {
            "district": "Mehsana", "lat": 23.5880, "lon": 72.3693, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Mehsana Buffalo Milk Sweets & Gujarati Thali",
            "description": "Dairy and oil capital famed for the 1,000-year-old Sun Temple of Modhera and stepwells.",
            "places": [
                {"name": "Sun Temple Modhera & Surya Kund", "category": "Historical", "entry_fee": 25, "opening": "07:00", "closing": "18:00", "description": "1026 CE Solanki architectural masterpiece with a stepped reservoir adorned with 108 miniature shrines and evening illumination."},
            ]
        },
        {
            "district": "Valsad", "lat": 20.6100, "lon": 72.9300, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Valsad Alphonso Mangoes (Hafoos) & Coastal Farsan",
            "description": "Southern coastal district with fruit orchards, quiet beaches, and the sacred fire temple of Udvada.",
            "places": [
                {"name": "Tithal Beach & Swaminarayan Temple", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Famous black-sand coastline facing the Arabian Sea, featuring palm groves and the ornate seaside stone temple."},
                {"name": "Udvada Atash Behram (Zoroastrian Fire Temple)", "category": "Spiritual", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Oldest continuously burning Zoroastrian sacred fire in the world (consecrated in 1742 CE) by Parsi settlers."},
            ]
        },
        {
            "district": "Amreli", "lat": 21.6032, "lon": 71.2221, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Amreli Peda & Kathiyawadi Rotla",
            "description": "Agricultural Saurashtra district home to Gir lions and the historic Rajmahal palace.",
            "places": [
                {"name": "Dhari Ambardi Lion Safari Park", "category": "Wildlife", "entry_fee": 150, "opening": "08:00", "closing": "17:00", "description": "Protected reserve near the Shetrunji River offering dedicated open-jeep sightings of Asiatic lions in scrubland."},
            ]
        },
        {
            "district": "Anand", "lat": 22.5645, "lon": 72.9289, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Amul Ice Cream, Cheese Delicacies & Gujarati Thali",
            "description": "Milk Capital of India, birthplace of the White Revolution (Operation Flood) and home to Amul Dairy headquarters.",
            "places": [
                {"name": "Amul Dairy Museum & Chocolate Factory", "category": "Museum", "entry_fee": 20, "opening": "10:00", "closing": "17:00", "description": "Museum honoring Dr. Verghese Kurien showcasing the history of cooperative dairy farming in India."},
            ]
        },
        {
            "district": "Aravalli", "lat": 23.5412, "lon": 73.1812, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Shamlaji Sweets & Rajasthani-Gujarati Fusion Meals",
            "description": "Border district of rolling Aravalli hills, home to the sacred 11th-century Shamlaji Vishnu shrine.",
            "places": [
                {"name": "Shamlaji Vishnu Temple (Gadadhar Swamy)", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "11th-century white sandstone temple on the Meshwo River featuring exquisitely carved friezes of musicians and elephants."},
            ]
        },
        {
            "district": "Banaskantha", "lat": 24.1724, "lon": 72.4346, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Ambaji Mohanthal (GI Tag) & Gujarati Farsan",
            "description": "Northern border district in the Aravallis, home to the major Shakti Peetha temple of Ambaji.",
            "places": [
                {"name": "Ambaji Mata Temple & Gabbar Hill Ropeway", "category": "Spiritual", "entry_fee": 0, "opening": "07:00", "closing": "21:00", "description": "One of the 51 holy Shakti Peethas with no physical idol, venerating the sacred gold-inscribed Viso Yantra."},
            ]
        },
        {
            "district": "Bharuch", "lat": 21.7051, "lon": 72.9959, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bharuchi Salted Peanuts (Khari Sing) & Parsi Cuisine",
            "description": "Ancient seaport of Barygaza on the Narmada River, famous for salt-roasted peanuts and the Golden Bridge.",
            "places": [
                {"name": "Golden Bridge over Narmada River", "category": "Heritage", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Historic 1881 iron bridge built by the British to connect Ankleshwar to Bharuch across the mighty Narmada."},
            ]
        },
        {
            "district": "Botad", "lat": 22.1704, "lon": 71.6669, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Salangpur Prasadam & Kathiyawadi Meals",
            "description": "Spiritual town renowned worldwide for the Kashtbhanjan Dev Hanuman Temple at Salangpur.",
            "places": [
                {"name": "Shree Kashtbhanjan Dev Hanumanji Temple Salangpur", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "21:00", "description": "Revered temple established by Gopalanand Swami, with a 54-foot giant King of Salangpur bronze statue."},
            ]
        },
        {
            "district": "Chhota Udaipur", "lat": 22.3108, "lon": 74.0118, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Rathwa Tribal Dishes & Mahua Drink",
            "description": "Tribal princely district famed for vivid ritualistic Pithora wall paintings and palace heritage.",
            "places": [
                {"name": "Pithora Tribal Art Galleries & Kusum Vilas Palace", "category": "Cultural", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "Traditional Rathwa tribal villages creating ritualistic horse and deity wall paintings, alongside 1920s royal palaces."},
            ]
        },
        {
            "district": "Dahod", "lat": 22.8360, "lon": 74.2560, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Kharagpur Roti & Gujarati Dhokla",
            "description": "Eastern tribal gateway where Mughal Emperor Aurangzeb was born, bordered by Madhya Pradesh.",
            "places": [
                {"name": "Fort of Aurangzeb (Gadhi)", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "17th-century fortress constructed by Mughal Emperor Shah Jahan to commemorate the birth of Aurangzeb in 1618."},
            ]
        },
        {
            "district": "Kheda", "lat": 22.7533, "lon": 72.6842, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Dakor Gota (GI Tag) & Gujarati Kadhi",
            "description": "Tobacco and agricultural land on the Shedhi River, home to the sacred Ranchhodraiji Temple of Dakor.",
            "places": [
                {"name": "Dakor Ranchhodraiji Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "1772 CE temple housing the revered black stone idol of Lord Krishna, brought from Dwarka by devotee Bodana."},
            ]
        },
        {
            "district": "Mahisagar", "lat": 23.1672, "lon": 73.6558, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Kharva Fish & Rotla",
            "description": "Scenic district along the Mahi River, rich in natural geothermal sulphur springs and forest camps.",
            "places": [
                {"name": "Kadana Dam & Reservoir", "category": "Nature", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Impressive earthen-masonry dam on the Mahi River surrounded by forested hillocks and bird habitats."},
            ]
        },
        {
            "district": "Morbi", "lat": 22.8173, "lon": 70.8377, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Morbi Gathiya & Pedas",
            "description": "Ceramic and Clock Capital of India on the Machchhu River, renowned for European-style palaces.",
            "places": [
                {"name": "Mani Mandir (Willingdon Secretariat)", "category": "Palace", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "1935 royal courtyard palace built with Jaipur stone, arched colonnades, and central temple."},
            ]
        },
        {
            "district": "Navsari", "lat": 20.9467, "lon": 72.9520, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Parsi Dhansak & Dandi Salt Crystals",
            "description": "Twin city of Surat, historic cradle of Parsi culture in India and terminal site of the Dandi Salt March.",
            "places": [
                {"name": "National Salt Satyagraha Memorial (Dandi Beach)", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "20:00", "description": "Memorial commemorating Mahatma Gandhi's 1930 historic salt march with 80 bronze life-size statues of satyagrahis."},
            ]
        },
        {
            "district": "Panchmahal", "lat": 22.7758, "lon": 73.6149, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Godhra Fafda & Farsan",
            "description": "Forested hill district home to the UNESCO World Heritage monuments of Champaner and Pavagadh hill.",
            "places": [
                {"name": "Pavagadh Mahakali Hill Temple & Ropeway", "category": "Spiritual", "entry_fee": 170, "opening": "06:00", "closing": "19:00", "description": "Sacred Shakti Peetha temple atop an 800m volcanic crag, connected by modern passenger ropeway cable cars."},
            ]
        },
        {
            "district": "Sabarkantha", "lat": 23.6033, "lon": 72.9639, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Himatnagar Gathiya & Gujarati Thali",
            "description": "North Gujarat hill district on the Sabarmati tributary, famous for Polo Forest archaeological ruins.",
            "places": [
                {"name": "Polo Forest & 15th-Century Temple Ruins", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Ancient forested valley along the Harnav River concealing 15th-century Jain and Hindu stone temple ruins."},
            ]
        },
        {
            "district": "Surendranagar", "lat": 22.7284, "lon": 71.6372, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Wadhwan Sing Bhujia & Peda",
            "description": "Gateway of Saurashtra famed for the colorful Tarnetar folk fair and historic stepwells of Wadhwan.",
            "places": [
                {"name": "Tarnetar Trinetreshwar Mahadev Temple", "category": "Cultural", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Ancient Shiva temple venue of the vibrant annual Tarnetar Fair featuring traditional Saurashtra folk dance and embroidered umbrellas."},
            ]
        },
        {
            "district": "Tapi", "lat": 21.2882, "lon": 73.4326, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Vyara Rice Dishes & Tapi Fish",
            "description": "Forest-covered tribal district on the Tapi River, home to the massive Ukai Dam and wildlife sanctuaries.",
            "places": [
                {"name": "Ukai Dam (Vallabh Sagar Reservoir)", "category": "Nature", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Second-largest reservoir in Gujarat across the Tapi River, surrounded by forested hills and boating waters."},
            ]
        },
    ],

    # ==================== 3. MAHARASHTRA (36 Districts) ====================
    "Maharashtra": [
        {
            "district": "Mumbai City", "lat": 18.9220, "lon": 72.8347, "crime_index": 28.0, "safety_tier": "LOW",
            "food": "Vada Pav, Pav Bhaji, Bombay Duck & Irani Maska Bun",
            "description": "The Financial Capital of India, colonial Victorian Gothic marvel on the Arabian Sea with iconic sea views.",
            "places": [
                {"name": "Gateway of India & Taj Mahal Palace Hotel", "category": "Heritage", "entry_fee": 0, "opening": "05:00", "closing": "23:00", "description": "Colonial 1924 basalt arch overlooking Mumbai Harbor, facing the historic 1903 Taj Mahal Palace luxury landmark."},
                {"name": "Marine Drive Promenade (Queen's Necklace)", "category": "Viewpoint", "entry_fee": 0, "opening": "05:00", "closing": "23:30", "description": "3.6-kilometer C-shaped coastal boulevard creating a glittering pearl-necklace curve of streetlights by night."},
                {"name": "Chhatrapati Shivaji Maharaj Terminus (CSMT - UNESCO Site)", "category": "Historical", "entry_fee": 0, "opening": "05:00", "closing": "23:00", "description": "Victorian Gothic architectural masterpiece completed in 1888 with stone domes, stained glass, and gargoyles."},
                {"name": "Elephanta Caves & Monolithic Trimurti (UNESCO Site)", "category": "Historical", "entry_fee": 40, "opening": "09:30", "closing": "17:30", "description": "6th-century rock-cut basalt island cave temple complex featuring the famous 20-foot three-headed Shiva Trimurti."},
            ]
        },
        {
            "district": "Mumbai Suburban", "lat": 19.1136, "lon": 72.8697, "crime_index": 26.0, "safety_tier": "LOW",
            "food": "Juhu Bhel Puri, Sev Puri & Frankie",
            "description": "The entertainment and Bollywood heartbeat of India, home to Arabian Sea beaches and national parks.",
            "places": [
                {"name": "Juhu Beach & Bollywood Star Homes Belt", "category": "Beach", "entry_fee": 0, "opening": "05:00", "closing": "23:00", "description": "Famous suburban beach celebrated for sunset strolls, Mumbai street chaat stalls, and celebrity residences."},
                {"name": "Sanjay Gandhi National Park & Kanheri Caves", "category": "Nature", "entry_fee": 64, "opening": "07:30", "closing": "17:30", "description": "104-sq-km wilderness inside a metropolis, sheltering 109 rock-cut Buddhist caves dating from the 1st century BCE."},
                {"name": "Bandra Bandstand Promenade & Bandra Fort", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Sea-facing promenade overlooking the Bandra-Worli Sea Link and Castella de Aguada Portuguese fort ruins."},
            ]
        },
        {
            "district": "Pune", "lat": 18.5204, "lon": 73.8567, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Misal Pav, Puran Poli, Bakarwadi & Puneri Poha",
            "description": "The Oxford of the East and cultural capital of the Maratha Empire, set in the Sahyadri mountains.",
            "places": [
                {"name": "Shaniwar Wada Palace Fortress", "category": "Historical", "entry_fee": 25, "opening": "09:30", "closing": "17:30", "description": "1732 CE seat of the Peshwa rulers of the Maratha Empire, known for massive teak doors and sound & light shows."},
                {"name": "Aga Khan Palace & Gandhi Memorial", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Italian-arched palace where Mahatma Gandhi and Kasturba Gandhi were interned during the 1942 Quit India movement."},
                {"name": "Sinhagad Fort (Lion's Fort)", "category": "Fort", "entry_fee": 20, "opening": "06:00", "closing": "18:00", "description": "Historic Sahyadri cliff fortress conquered by Tanaji Malusare in 1670, famous for cool winds and pithla bhakri."},
                {"name": "Dagdusheth Halwai Ganpati Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "22:30", "description": "Beloved Ganesha temple in the heart of Pune visited by hundreds of thousands during the annual Ganeshotsav festival."},
            ]
        },
        {
            "district": "Aurangabad", "lat": 19.8762, "lon": 75.3433, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Naan Qalia, Paithani Silk Sweets & Hurda",
            "description": "Renamed Chhatrapati Sambhajinagar, tourism capital of Maharashtra home to world-renowned UNESCO caves.",
            "places": [
                {"name": "Ajanta Caves (UNESCO World Heritage Site)", "category": "Historical", "entry_fee": 40, "opening": "09:00", "closing": "17:30", "description": "30 rock-cut Buddhist monument caves dating from 2nd century BCE to 480 CE, famous worldwide for master frescoes."},
                {"name": "Ellora Caves & Kailasa Monolithic Temple (UNESCO Site)", "category": "Historical", "entry_fee": 40, "opening": "06:00", "closing": "18:00", "description": "Cave 16 Kailasa: world's largest single rock-cut megalith excavated top-down from a single basalt cliff face."},
                {"name": "Bibi Ka Maqbara (Taj of the Deccan)", "category": "Historical", "entry_fee": 25, "opening": "08:00", "closing": "20:00", "description": "1668 CE marble mausoleum commissioned by Prince Azam Shah in memory of his mother Dilras Banu Begum."},
                {"name": "Daulatabad Fort (Devagiri Impregnable Citadel)", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "18:00", "description": "12th-century hill citadel with deep subterranean moats, dark labyrinth passages (Andhari), and the 110-foot Chand Minar."},
            ]
        },
        {
            "district": "Nashik", "lat": 19.9975, "lon": 73.7898, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Misal Pav (Kat Kirr), Grapes & Sula Wine",
            "description": "Wine Capital of India and sacred Kumbh Mela city on the Godavari River, steeped in Ramayana lore.",
            "places": [
                {"name": "Trimbakeshwar Jyotirlinga Shiva Temple", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "21:00", "description": "Sacred 12-Jyotirlinga shrine at the foot of Brahmagiri Mountain, source of the Godavari River, with three-faced linga."},
                {"name": "Panchavati & Sita Gufa (Ramayana Hermitage)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Sacred five banyan trees and cave hermitage where Lord Rama, Sita, and Lakshmana stayed in Dandakaranya."},
                {"name": "Sula Vineyards & Tasting Cellar", "category": "Nature", "entry_fee": 400, "opening": "11:30", "closing": "21:00", "description": "Pioneering Indian winery estate in the rolling Sahyadri valleys offering vineyard tours, barrel rooms, and tastings."},
            ]
        },
        {
            "district": "Kolhapur", "lat": 16.7050, "lon": 74.2433, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kolhapuri Tambda-Pandhra Rassa, Mutton Sukka & Kolhapuri Chappals (GI)",
            "description": "Historic royal city of Chhatrapati Shahu Maharaj, world-famous for wrestling, leather chappals, and Mahalakshmi.",
            "places": [
                {"name": "Mahalakshmi (Amba Bai) Temple", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "7th-century Chalukyan Shakti Peetha where sunrays illuminate the idol during Kiranotsav twice each year."},
                {"name": "Panhala Hill Fort", "category": "Fort", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Largest fort in the Deccan rising 845m above sea level, closely linked with Chhatrapati Shivaji and Tarabai."},
                {"name": "New Palace (Shree Chhatrapati Shahu Museum)", "category": "Palace", "entry_fee": 50, "opening": "09:30", "closing": "17:30", "description": "Black polished stone palace combining Jain, Hindu, and British styles, showcasing royal Maratha weaponry."},
            ]
        },
        {
            "district": "Raigad", "lat": 18.2346, "lon": 73.4428, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Alibaug Fresh Fish Thali, Solkadhi & Coconut Poha",
            "description": "Cradle of the Maratha Empire and capital of Chhatrapati Shivaji Maharaj, flanked by sandy Konkan beaches.",
            "places": [
                {"name": "Raigad Fort (Capital of the Maratha Empire)", "category": "Fort", "entry_fee": 25, "opening": "08:00", "closing": "18:00", "description": "Gibraltar of the East: historic mountain fortress where Chhatrapati Shivaji Maharaj was crowned in 1674, reached by ropeway."},
                {"name": "Alibaug Beach & Kolaba Sea Fort", "category": "Beach", "entry_fee": 20, "opening": "06:00", "closing": "18:30", "description": "Pristine coastal town facing a 17th-century island fortress that can be walked to during low tide."},
                {"name": "Murud-Janjira Impregnable Island Sea Fort", "category": "Fort", "entry_fee": 50, "opening": "07:00", "closing": "18:00", "description": "Oval island fortress surrounded entirely by the Arabian Sea, famous for withstanding Dutch, British, and Portuguese sieges."},
            ]
        },
        {
            "district": "Ratnagiri", "lat": 16.9902, "lon": 73.3120, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Ratnagiri Alphonso Mangoes, Modak & Fish Curry",
            "description": "Heart of the Konkan coastline, birthplace of Lokmanya Tilak and world-famous for Alphonso mangoes and sea cliffs.",
            "places": [
                {"name": "Ganpatipule Beach & Swayambhu Ganpati Temple", "category": "Beach", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "400-year-old self-manifested Ganesha shrine on silver sands, backed by verdant hillocks facing the Arabian Sea."},
                {"name": "Ratnadurg Fort & 1867 Marine Lighthouse", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:30", "description": "Horseshoe-shaped coastal citadel surrounded by ocean on three sides, with Bhagwati Temple and panoramic sunset cliffs."},
            ]
        },
        {
            "district": "Sindhudurg", "lat": 16.1133, "lon": 73.7144, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Malvani Fish Curry, Kombdi Vade & Amsul Kadhi",
            "description": "Coastal eco-paradise established by Shivaji Maharaj, famous for scuba diving, fortresses, and Malvani cuisine.",
            "places": [
                {"name": "Sindhudurg Sea Fort (Kurte Island)", "category": "Fort", "entry_fee": 50, "opening": "08:00", "closing": "17:30", "description": "Masterpiece of naval architecture built in 1664 by Shivaji Maharaj with 3km of 30-foot walls resting on rocky ocean reef."},
                {"name": "Tarkarli Beach & Coral Reef Scuba Diving", "category": "Beach", "entry_fee": 500, "opening": "07:00", "closing": "18:00", "description": "Crystal-clear waters where the Karli River meets the Arabian Sea, renowned for snorkeling and dolphin spotting."},
                {"name": "Amboli Hill Station (Cherrapunji of Maharashtra)", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Misty Sahyadri hill station at 690m elevation receiving 7,500mm of rain, with cascading waterfalls and biodiversity."},
            ]
        },
        {
            "district": "Satara", "lat": 17.6805, "lon": 73.9997, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Satara Kandi Peda (GI Tag) & Pithla Bhakri",
            "description": "Historic Maratha capital situated amidst Sahyadri peaks, home to the UNESCO World Heritage Kaas Plateau.",
            "places": [
                {"name": "Kaas Plateau Valley of Flowers (UNESCO World Heritage Site)", "category": "Nature", "entry_fee": 100, "opening": "07:00", "closing": "18:00", "description": "Volcanic laterite plateau transforming into a vibrant carpet of 850+ species of wild orchids and flowers every post-monsoon."},
                {"name": "Thoseghar Waterfalls & Chalkewadi Windmill Plateau", "category": "Waterfall", "entry_fee": 20, "opening": "08:00", "closing": "17:30", "description": "Spectacular 500-meter drop cascade falling into deep forested ravines, alongside rolling windmills."},
                {"name": "Ajinkyatara Fort (Fortress of the Invincible)", "category": "Fort", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "16th-century hill fort perched 1,000m above Satara town offering panoramic views of the Sahyadri mountains."},
            ]
        },
        {
            "district": "Thane", "lat": 19.2183, "lon": 72.9781, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Thane Street Chaat & Maharashtrian Thali",
            "description": "The City of Lakes adjoining Mumbai, terminus of India's first passenger railway in 1853.",
            "places": [
                {"name": "Upvan Lake & Yeoor Hills (Sanjay Gandhi Reserve Edge)", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Scenic recreational lake set against Yeoor hills, hosting the annual Sanskruti Arts Festival and musical fountain."},
            ]
        },
        {
            "district": "Ahmednagar", "lat": 19.0952, "lon": 74.7480, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Shirdi Prasadam, Hurda & Maharashtrian Meals",
            "description": "Historic Nizam Shahi fortress town and home to Shirdi, the global pilgrimage center of Sai Baba.",
            "places": [
                {"name": "Shirdi Sai Baba Samadhi Temple", "category": "Spiritual", "entry_fee": 0, "opening": "04:00", "closing": "22:30", "description": "One of India's most visited spiritual shrines, preserving the holy Samadhi Mandir and Dwarkamai of saint Sai Baba."},
                {"name": "Shani Shingnapur (Village of Doorless Houses)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "Famous village where houses have no doors or locks, centered around a self-manifested black stone Shani deity."},
                {"name": "Ahmednagar Fort", "category": "Fort", "entry_fee": 20, "opening": "09:00", "closing": "17:00", "description": "15th-century oval stone fort where Jawaharlal Nehru was imprisoned in 1942 and wrote 'The Discovery of India'."},
            ]
        },
        {
            "district": "Nagpur", "lat": 21.1458, "lon": 79.0882, "crime_index": 25.0, "safety_tier": "LOW",
            "food": "Nagpur Orange Barfi, Saoji Mutton & Tarri Poha",
            "description": "Orange City and Winter Capital of Maharashtra, geographical center of India marked by the Zero Mile Stone.",
            "places": [
                {"name": "Deekshabhoomi Sacred Buddhist Stupa", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Asia's largest hollow Buddhist dome stupa where Dr. B.R. Ambedkar embraced Buddhism with 600,000 followers in 1956."},
                {"name": "Pench Tiger Reserve & Forest Safari", "category": "Wildlife", "entry_fee": 400, "opening": "06:00", "closing": "17:30", "description": "The real Jungle Book territory that inspired Rudyard Kipling, sheltering royal Bengal tigers and leopards."},
                {"name": "Futala Lake Promenade & Musical Fountains", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Bhusawal-built historic lake with colored fountains, paved promenades, and evening street food bistros."},
            ]
        },
        {
            "district": "Solapur", "lat": 17.6599, "lon": 75.9064, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Solapuri Chutney (Shenga Chutney), Jowar Bhakri & Solapuri Chadar",
            "description": "Textile and handloom center on the Karnataka border, gateway to the sacred Vithoba temple of Pandharpur.",
            "places": [
                {"name": "Pandharpur Vithoba (Vitthal Rukmini) Temple", "category": "Temple", "entry_fee": 0, "opening": "04:00", "closing": "23:00", "description": "Supreme pilgrimage center of the Varkari tradition on the Chandrabhaga River, celebrating the annual Ashadhi Ekadashi Dindi."},
                {"name": "Siddheshwar Temple & Bhuikot Lake Fort", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "Unique water fortress built in the 14th century in the center of an island lake dedicated to saint Siddharameshwar."},
            ]
        },
        # Remaining Maharashtra Districts (Akola, Amravati, Beed, Bhandara, Buldhana, Chandrapur, Dhule, Gadchiroli, Gondia, Hingoli, Jalgaon, Jalna, Latur, Nanded, Nandurbar, Osmanabad, Palghar, Parbhani, Sangli, Wardha, Washim, Yavatmal)
        {
            "district": "Buldhana", "lat": 20.5300, "lon": 76.1800, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Buldhana Peda & Vidarbha Thali",
            "description": "Home to the world-famous Lonar Crater Lake, created by a hyper-velocity meteorite impact 52,000 years ago.",
            "places": [
                {"name": "Lonar Meteorite Crater Lake (National Geo-Heritage Site)", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "World's only hyper-velocity meteorite impact crater in basaltic rock, creating a saline-alkaline lake surrounded by 1,000-year-old temples."},
            ]
        },
        {
            "district": "Chandrapur", "lat": 19.9615, "lon": 79.2961, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Saoji Cuisine & Jowar Bhakri",
            "description": "The City of Black Gold (coal) and premier wildlife kingdom, home to the tiger haven of Tadoba.",
            "places": [
                {"name": "Tadoba-Andhari Tiger Reserve", "category": "Wildlife", "entry_fee": 750, "opening": "06:00", "closing": "18:00", "description": "Oldest and largest national park in Maharashtra, famous for having one of the highest tiger densities in India."},
            ]
        },
        {
            "district": "Amravati", "lat": 20.9320, "lon": 77.7523, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Amravati Girmity & Vidarbha Saoji",
            "description": "Historic temple city of Goddess Ambadevi, gateway to the cool Satpura hill resort of Chikhaldara.",
            "places": [
                {"name": "Chikhaldara Hill Station & Melghat Tiger Reserve", "category": "Hill Station", "entry_fee": 50, "opening": "06:00", "closing": "18:30", "description": "Only coffee-growing hill station in Vidarbha (1,118m) featuring deep viewpoints and the adjoining tiger reserve."},
            ]
        },
        {
            "district": "Nanded", "lat": 19.1383, "lon": 77.3210, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Nanded Tahari & Guru Ka Langar",
            "description": "Major Sikh pilgrimage center on the Godavari River, home to Takht Sachkhand Sri Hazur Abchalnagar Sahib.",
            "places": [
                {"name": "Hazur Sahib Gurudwara (Takht Sachkhand)", "category": "Spiritual", "entry_fee": 0, "opening": "04:00", "closing": "22:00", "description": "One of the five Takhts in Sikhism, where Guru Gobind Singh Ji spent his final days in 1708, with gold-plated domes."},
            ]
        },
        {
            "district": "Palghar", "lat": 19.6967, "lon": 72.7699, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Dahanu Gholvad Chikus (GI) & Konkan Fish Curry",
            "description": "Coastal tribal district north of Mumbai, famed for GI-tagged Bordi chiku orchards, Warli art, and sea forts.",
            "places": [
                {"name": "Kelva Beach & Shirgaon Sea Fort", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Expansive 8km sandy beach lined with surrender casuarina trees and 16th-century Maratha sea watchtowers."},
                {"name": "Jawhar Hill Station & Jai Vilas Palace", "category": "Hill Station", "entry_fee": 30, "opening": "09:00", "closing": "17:30", "description": "Tribal hill station known as the Mahabaleshwar of Thane, celebrated for authentic Warli painting workshops."},
            ]
        },
        {
            "district": "Wardha", "lat": 20.7453, "lon": 78.6022, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Wardha Khadi Cotton Sweets & Maharashtrian Meals",
            "description": "Historic nerve center of India's independence movement, home to Mahatma Gandhi's Sevagram Ashram.",
            "places": [
                {"name": "Sevagram Ashram (Mahatma Gandhi National Residence)", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Village ashram established by Gandhi in 1936 where crucial independence decisions were formulated."},
                {"name": "Vishwa Shanti Stupa (World Peace Pagoda)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Pure white cylindrical Buddhist stupa built by Japanese monks atop a hillock, promoting global non-violence."},
            ]
        },
        {
            "district": "Jalgaon", "lat": 21.0077, "lon": 75.5626, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Jalgaon Bharit (Smoked Brinjal) & Shev Bhaji",
            "description": "Banana City of India, contributing over two-thirds of Maharashtra's bananas, near Ajanta Caves.",
            "places": [
                {"name": "Mehrun Lake & Padmalaya Temple Complex", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Historic lake famed for natural water lilies and adjacent dual-Ganesha pilgrimage shrine."},
            ]
        },
        {
            "district": "Osmanabad", "lat": 18.1856, "lon": 76.0420, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Dharashiv Peda & Jowar Bhakri",
            "description": "Renamed Dharashiv, famous for the revered Tuljabhavani Temple in Tuljapur and 6th-century rock caves.",
            "places": [
                {"name": "Tuljapur Tuljabhavani Temple", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "Patron deity of Chhatrapati Shivaji Maharaj, one of the 51 sacred Shakti Peethas located in the Balaghat hills."},
            ]
        },
        {
            "district": "Sangli", "lat": 16.8524, "lon": 74.5815, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Sangli Turmeric, Grapes & Bhel",
            "description": "Turmeric City on the Krishna River, major sugar belt and home to Chandoli National Park.",
            "places": [
                {"name": "Chandoli National Park (UNESCO World Heritage Site)", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "17:30", "description": "Pristine Sahyadri Tiger Reserve reserve around Vasant Sagar Reservoir, home to tigers and leopards."},
            ]
        },
        {
            "district": "Beed", "lat": 18.9891, "lon": 75.7601, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Beed Peda & Kathiyawadi Meals",
            "description": "Historic Marathwada town home to the ancient Parli Vaijnath Jyotirlinga and water temples.",
            "places": [
                {"name": "Parli Vaijnath Jyotirlinga Temple", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "One of the twelve sacred Jyotirlinga shrines perched on a hill slope, constructed with black stone by Rani Ahilyabai Holkar."},
            ]
        },
        {
            "district": "Gondia", "lat": 21.4554, "lon": 80.1961, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Rice Poha & Forest Honey",
            "description": "Rice City of Vidarbha, surrounded by lakes and the tiger-rich Navegaon-Nagzira reserve.",
            "places": [
                {"name": "Navegaon National Park & Bird Sanctuary", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "17:30", "description": "Picturesque hill reservoir sanctuary sheltering over 200 species of migratory and resident birds."},
            ]
        },
        {
            "district": "Bhandara", "lat": 21.1714, "lon": 79.6548, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Brass Metal Handicrafts & Vidarbha Thali",
            "description": "Brass City of Maharashtra on the Wainganga River, celebrated for over 3,000 natural lakes.",
            "places": [
                {"name": "Koka Wildlife Sanctuary", "category": "Wildlife", "entry_fee": 50, "opening": "06:30", "closing": "17:30", "description": "Natural deciduous forest corridor connected with Navegaon-Nagzira, home to wild dogs and tigers."},
            ]
        },
        {
            "district": "Latur", "lat": 18.4088, "lon": 76.5604, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Latur Roasted Gram & Jowar Roti",
            "description": "Historical trading capital of the Rashtrakuta kings, home to subterranean Kharosa caves and Udgir Fort.",
            "places": [
                {"name": "Udgir Fort & Samadhi of Swami Sadashivrao", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Historic fort where the 1760 Battle of Udgir was fought between the Marathas and the Nizam of Hyderabad."},
            ]
        },
        {
            "district": "Hingoli", "lat": 19.7188, "lon": 77.1477, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Marathwada Jowar Bhakri & Chutney",
            "description": "Pilgrimage destination in Marathwada, home to the 8th Jyotirlinga Aundha Nagnath.",
            "places": [
                {"name": "Aundha Nagnath Jyotirlinga Temple", "category": "Temple", "entry_fee": 0, "opening": "04:30", "closing": "21:30", "description": "Ancient 8th Jyotirlinga shrine believed to have been founded by the Pandavas, with ornate Hemadpanthi stone carvings."},
            ]
        },
        {
            "district": "Akola", "lat": 20.7002, "lon": 77.0082, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Cotton Belt Sweets & Dal Baati",
            "description": "Cotton City on the Morna River, guarded by the impregnable Satpura fortress of Narnala.",
            "places": [
                {"name": "Narnala Fort (Shahnoor Fort)", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "17:30", "description": "10th-century hill fortress spanning three hills in the Satpura ranges, housing the 15th-century Mahakali gate."},
            ]
        },
        {
            "district": "Washim", "lat": 20.1098, "lon": 77.1352, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Vidarbha Meals & Peda",
            "description": "Ancient Vatsagulma capital of the Vakataka dynasty, rich in sacred teerth ponds and Jain temples.",
            "places": [
                {"name": "Shirpur Jain Temple (Antariksha Parshvanath)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Ancient Jain temple revered for the floating idol of Lord Parshvanath suspended slightly above the ground."},
            ]
        },
        {
            "district": "Yavatmal", "lat": 20.3888, "lon": 78.1204, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Teak Wood Crafts & Vidarbha Thali",
            "description": "Lush forest district of eastern Vidarbha, home to the tiger haven of Tipeshwar.",
            "places": [
                {"name": "Tipeshwar Wildlife Sanctuary", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "17:00", "description": "Fast-growing tiger reserve in the Yavatmal hills, offering thrilling open-jeep wildlife safaris."},
            ]
        },
        {
            "district": "Gadchiroli", "lat": 20.1800, "lon": 79.9900, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Tribal Bamboo Dishes & Wild Honey",
            "description": "Dense forest and teak kingdom bordering Chhattisgarh, celebrated for Markanda temples.",
            "places": [
                {"name": "Markanda Shiva Temple Complex (Khajuraho of Vidarbha)", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Cluster of 24 exquisitely carved 8th-century stone temples on the Wainganga River, showcasing Hemadpanthi architecture."},
            ]
        },
        {
            "district": "Dhule", "lat": 20.9042, "lon": 74.7749, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Khandeshi Shev Bhaji & Jowar Roti",
            "description": "Khandesh commercial hub on the Panzara River, famous for Laling hill fort and Rajwade historical museum.",
            "places": [
                {"name": "Laling Fort & Hilltop Viewpoint", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "14th-century Faruqi sultanate hill fortress guarding the ancient pass between Gujarat and the Deccan."},
            ]
        },
        {
            "district": "Nandurbar", "lat": 21.3697, "lon": 74.2403, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Khandeshi Thali & Toranmal Corn",
            "description": "Northwestern tribal district in the Satpuras, home to the cool Toranmal hill station and Yashavant Lake.",
            "places": [
                {"name": "Toranmal Hill Station & Lotus Lake (Kamal Talao)", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "High-altitude plateau at 1,150m in the Satpura range, covered in natural lotus ponds and Sita Khai gorges."},
            ]
        },
        {
            "district": "Parbhani", "lat": 19.2644, "lon": 76.7749, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Marathwada Jowar Bhakri & Peda",
            "description": "Historical territory on the Godavari River, home to Sufi Hazrat Turabul Haq Dargah and Mudgaleshwar.",
            "places": [
                {"name": "Hazrat Turabul Haq Dargah", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "21:30", "description": "18th-century Sufi shrine celebrating annual multi-faith Urs gatherings fostering unity and harmony."},
            ]
        },
        {
            "district": "Jalna", "lat": 19.8347, "lon": 75.8816, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Sweet Lime (Mosambi) & Maharashtrian Meals",
            "description": "Steel and seed capital of Maharashtra, birthplace of saint-poet Samarth Ramdas at Jamb Samarth.",
            "places": [
                {"name": "Matsyodari Devi Temple & Ambad Fort", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Ancient hilltop shrine shaped like a fish (Matsya), overlooking the historic fortified town of Ambad."},
            ]
        },
    ],
}
