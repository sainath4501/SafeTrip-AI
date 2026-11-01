"""
Eastern & Central India States Master Districts & Tourist Attractions
Covers Bihar (38), Chhattisgarh (33), Jharkhand (24), Madhya Pradesh (55), Odisha (30), West Bengal (23).
"""

EAST_CENTRAL_STATES = {
    # ==================== 1. BIHAR (38 Districts) ====================
    "Bihar": [
        {
            "district": "Patna", "lat": 25.5941, "lon": 85.1376, "crime_index": 26.0, "safety_tier": "LOW",
            "food": "Litti Chokha with Ghee, Sattu Paratha, Khaja & Anarsa",
            "description": "Ancient Pataliputra, imperial capital of the Magadha, Maurya, and Gupta empires on the sacred Ganges.",
            "places": [
                {"name": "Bihar Museum (World-Class Architecture)", "category": "Museum", "entry_fee": 100, "opening": "10:00", "closing": "17:00", "description": "Maki and Associates designed premier museum holding the 3rd-century BCE Didarganj Yakshi and ancient sculptures."},
                {"name": "Golghar & Gandhi Ghat River Promenade", "category": "Historical", "entry_fee": 20, "opening": "09:30", "closing": "18:00", "description": "1786 beehive-shaped pillarless granary built by British engineer John Garstin, offering panoramic Ganges views."},
                {"name": "Takht Sri Harimandir Ji Patna Sahib", "category": "Spiritual", "entry_fee": 0, "opening": "04:30", "closing": "21:30", "description": "One of the five holy Takhts in Sikhism, sacred birthplace of the tenth Sikh guru, Guru Gobind Singh Ji in 1666."},
            ]
        },
        {
            "district": "Gaya", "lat": 24.7955, "lon": 85.0002, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Gaya Tilkut (GI Tag), Anarsa, Kesaria Peda & Litti Chokha",
            "description": "Supreme spiritual center on the Phalgu River for Hindu Pind Daan rituals and home to Bodh Gaya.",
            "places": [
                {"name": "Mahabodhi Temple Complex & Sacred Bodhi Tree (UNESCO Site)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "The exact spot where Siddhartha Gautama attained Enlightenment in 531 BCE, marked by the 50-meter pyramidal temple and Vajrasana."},
                {"name": "Great Buddha 80-Foot Statue & International Monasteries", "category": "Spiritual", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Colossal seated meditation Buddha unveiled by the 14th Dalai Lama, surrounded by Thai, Japanese, and Bhutanese monasteries."},
                {"name": "Vishnupad Temple Gaya", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "1787 grey granite temple built by Rani Ahilyabai Holkar housing a 40cm footprint of Lord Vishnu on the Phalgu River."},
            ]
        },
        {
            "district": "Nalanda", "lat": 25.1367, "lon": 85.4438, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Silao Khaja (GI Tag) & Bihari Thali",
            "description": "Ancient educational center of the world, home to the UNESCO ruins of Nalanda University and Rajgir hills.",
            "places": [
                {"name": "Nalanda Mahavihara Ruins (UNESCO World Heritage Site)", "category": "Historical", "entry_fee": 40, "opening": "09:00", "closing": "17:00", "description": "5th-to-12th century ancient monastic university that taught 10,000 international scholars across Buddhist philosophy and astronomy."},
                {"name": "Vishwa Shanti Stupa & Aerial Ropeway Rajgir", "category": "Spiritual", "entry_fee": 100, "opening": "09:00", "closing": "17:00", "description": "Pure white Peace Pagoda atop Ratnagiri hill (400m) with four golden Buddha statues, accessed via single-seater chairlift."},
                {"name": "Venuvana & Gridhakuta (Vulture Peak)", "category": "Historical", "entry_fee": 20, "opening": "07:00", "closing": "18:00", "description": "Bamboo grove monastery gifted by King Bimbisara and mountain cave where Buddha preached the Heart Sutra."},
            ]
        },
        {
            "district": "Vaishali", "lat": 25.9860, "lon": 85.1275, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Vaishali Mangoes & Bihari Litti",
            "description": "The World's First Republic (Licchavi Republic), birthplace of Lord Mahavira and site of Buddha's Last Sermon.",
            "places": [
                {"name": "Ashokan Pillar & Relic Stupa Vaishali", "category": "Historical", "entry_fee": 25, "opening": "07:00", "closing": "18:00", "description": "Complete monolithic polished sandstone pillar surmounted by a single seated lion, erected by Emperor Ashoka."},
                {"name": "Kundalpur (Birthplace of Lord Mahavira)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Sacred Jain pilgrimage temple marking the birthplace of the 24th Tirthankara, Lord Mahavira, with a marble temple."},
            ]
        },
        {
            "district": "Rohtas", "lat": 24.9525, "lon": 84.0152, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Sasaram Kadhi & Sattu Dishes",
            "description": "Historic hill district on the Sone River, home to the monumental red sandstone tomb of Sher Shah Suri.",
            "places": [
                {"name": "Tomb of Sher Shah Suri (Second Taj of India - Sasaram)", "category": "Historical", "entry_fee": 25, "opening": "07:00", "closing": "18:00", "description": "122-foot majestic red sandstone octagonal mausoleum standing in the center of an artificial square lake, built in 1545."},
                {"name": "Rohtasgarh Fort (One of the Largest Forts in India)", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "Ancient 7th-century clifftop fortress spanning 42 sq km atop the Kaimur hills, fortified by Sher Shah Suri and Raja Man Singh."},
            ]
        },
        {
            "district": "West Champaran", "lat": 27.1500, "lon": 84.4500, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Champaran Meat (Ahuna Mutton in Clay Pot - GI) & Litti",
            "description": "Historic land of Gandhi's Champaran Satyagraha in 1917, home to Bihar's only tiger reserve Valmiki.",
            "places": [
                {"name": "Valmiki National Park & Tiger Reserve", "category": "Wildlife", "entry_fee": 150, "opening": "06:00", "closing": "17:00", "description": "Terai sal and elephant grass wilderness on the Gandak River along the Nepal border, sheltering tigers, rhinos, and leopards."},
            ]
        },
        {
            "district": "Bhagalpur", "lat": 25.2425, "lon": 86.9842, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Bhagalpuri Zardalu Mango (GI), Katarni Rice & Tussar Silk",
            "description": "The Silk City of India on the Ganges, famous for ancient Vikramshila University and Gangetic dolphin sanctuaries.",
            "places": [
                {"name": "Vikramshila Ancient Buddhist University Ruins", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:00", "description": "8th-century Pala dynasty learning center established by King Dharmapala, famous for Tantric Buddhism and central cruciform stupa."},
                {"name": "Vikramshila Gangetic Dolphin Sanctuary", "category": "Wildlife", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "65-kilometer protected river stretch of the Ganges dedicated to safeguarding the endangered blind South Asian river dolphin."},
            ]
        },
        {
            "district": "Darbhanga", "lat": 26.1542, "lon": 85.8918, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Mithila Makhana (Fox Nuts - GI Tag), Fish Curry & Chura Dahi",
            "description": "Cultural Capital of Mithila, celebrated for Madhubani art, royal Darbhanga palaces, and fox-nut aquaculture.",
            "places": [
                {"name": "Raj Darbhanga Royal Palace (Nargona & Anand Bagh)", "category": "Palace", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "Grand Italianate and Indo-Saracenic royal palaces of the Khandavala dynasty with private temples, libraries, and moat gardens."},
            ]
        },
        {
            "district": "Madhubani", "lat": 26.3537, "lon": 86.0740, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Mithila Thali & Fried Makhana",
            "description": "World-famous homeland of Madhubani (Mithila) painting, decorated with intricate line drawings of nature and deities.",
            "places": [
                {"name": "Mithila Madhubani Art Heritage Villages (Jitwarpur & Ranti)", "category": "Cultural", "entry_fee": 0, "opening": "09:00", "closing": "18:00", "description": "Artisan hamlets where multiple National Award-winning women artists paint vibrant natural-dye murals on home walls and handmade paper."},
            ]
        },
        {
            "district": "Bhojpur", "lat": 25.5560, "lon": 84.6603, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Bhojpuri Litti Chokha & Belgrami",
            "description": "Home of heroic 1857 freedom fighter Veer Kunwar Singh, situated on the fertile plains near Arrah.",
            "places": [
                {"name": "Veer Kunwar Singh Fort Jagdishpur", "category": "Historical", "entry_fee": 0, "opening": "08:30", "closing": "17:30", "description": "Historic ancestral fort of the 80-year-old warrior king who defeated British forces multiple times during the 1857 rebellion."},
            ]
        },
    ],

    # ==================== 2. CHHATTISGARH (33 Districts) ====================
    "Chhattisgarh": [
        {
            "district": "Bastar", "lat": 19.0740, "lon": 82.0298, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Bastar Chaprah (Red Ant Chutney), Mahua Flowers & Bamboo Shoot Curry",
            "description": "Cultural and tribal heart of Chhattisgarh, home to the Niagara of India Chitrakote Falls and Dhokra bronze crafts.",
            "places": [
                {"name": "Chitrakote Waterfalls (Niagara of India on Indravati)", "category": "Waterfall", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Horseshoe-shaped 300-meter wide thundering waterfall plunging 95 feet over rocky cliffs into the Indravati River."},
                {"name": "Tirathgarh Waterfalls & Kanger Valley National Park", "category": "Waterfall", "entry_fee": 50, "opening": "07:00", "closing": "17:00", "description": "300-foot multi-tiered white cascade inside deep sal forests, near Kotumsar subterranean limestone stalactite caves."},
                {"name": "Danteshwari Temple & Bastar Dussehra Grounds", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "14th-century temple of Goddess Danteshwari, presiding deity of the famous 75-day-long Bastar Dussehra tribal festival."},
            ]
        },
        {
            "district": "Raipur", "lat": 21.2514, "lon": 81.6296, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Chana Samosa, Faraa, Muthia & Bore Baasi",
            "description": "Capital of Chhattisgarh on the Mahanadi plains, blending ancient temples with the new smart city of Atal Nagar.",
            "places": [
                {"name": "Swami Vivekananda Sarovar (Budha Talab)", "category": "Lake", "entry_fee": 20, "opening": "06:00", "closing": "21:30", "description": "Historic lake holding a 37-foot bronze statue of Swami Vivekananda, who spent two teenage years in Raipur."},
                {"name": "Purkhauti Muktangan Cultural Open-Air Museum", "category": "Cultural", "entry_fee": 30, "opening": "09:00", "closing": "18:00", "description": "Expansive 200-acre cultural park showcasing indigenous tribal habitats, terracotta arts, and traditional folk architecture."},
            ]
        },
        {
            "district": "Bilaspur", "lat": 22.0797, "lon": 82.1409, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bilasipuri Samosa & Kosa Silk Sweets",
            "description": "High Court and Railway capital of Chhattisgarh on the Arpa River, famous for Kosa silk and ancient forts.",
            "places": [
                {"name": "Ratanpur Mahamaya Temple & Fort Ruins", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "11th-century Kalachuri dynasty temple dedicated to Goddess Mahamaya, surrounded by medieval water tanks and stone shrines."},
                {"name": "Achanakmar Tiger Reserve & Amarkantak Biosphere", "category": "Wildlife", "entry_fee": 150, "opening": "06:00", "closing": "17:30", "description": "Pristine dense sal and bamboo sanctuary connected with Kanha corridor, home to tigers, leopards, and flying squirrels."},
            ]
        },
        {
            "district": "Kabirdham", "lat": 22.0089, "lon": 81.2483, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Kawardha Jalebi & Tribal Cuisine",
            "description": "Situated at the foothills of the Maikal ranges, home to the architectural jewel Bhoramdeo Temple.",
            "places": [
                {"name": "Bhoramdeo Temple Complex (Khajuraho of Chhattisgarh)", "category": "Historical", "entry_fee": 25, "opening": "06:00", "closing": "18:30", "description": "11th-century Nagara stone temple built by the Nagwanshi kings, adorned with erotic and religious sculptures amidst Maikal hills."},
            ]
        },
        {
            "district": "Durg", "lat": 21.1904, "lon": 81.2849, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Bhilai Chaat, Durg Faraa & Chikki",
            "description": "Twin industrial and educational city with Bhilai Steel Plant, backed by the sacred Shivnath River.",
            "places": [
                {"name": "Maitri Bagh (Friendship Garden & Zoo Bhilai)", "category": "Nature", "entry_fee": 20, "opening": "09:00", "closing": "18:30", "description": "111-acre Indo-Soviet friendship park featuring musical fountains, artificial lake, toy train, and white tiger enclosures."},
            ]
        },
        {
            "district": "Dantewada", "lat": 18.9000, "lon": 81.3500, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Tribal Mahua Dishes & Red Ant Chutney",
            "description": "Ancient pilgrimage site at the confluence of the Shankhini and Dankini rivers, home to the supreme Danteshwari Shakti Peetha.",
            "places": [
                {"name": "Danteshwari Temple Dantewada (51st Shakti Peetha)", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "21:00", "description": "One of the 51 holy Shakti Peethas where Sati's tooth fell, housing a six-armed black stone deity of the Kakatiya rulers."},
            ]
        },
    ],

    # ==================== 3. JHARKHAND (24 Districts) ====================
    "Jharkhand": [
        {
            "district": "Ranchi", "lat": 23.3441, "lon": 85.3096, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Dhuska with Ghugni, Litti Chokha & Arsa Roti",
            "description": "City of Waterfalls on the Chota Nagpur plateau at 650m elevation, summer capital surrounded by rolling hills.",
            "places": [
                {"name": "Hundru Waterfalls & Subarnarekha River Gorge", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Spectacular 98-meter plunge on the Subarnarekha River falling over jagged granite rocks into a deep natural pool."},
                {"name": "Dassam Falls & Jonha Falls (Gautam Dhara)", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Scenic 144-foot tiered cascades nestled in thick deciduous forests where Lord Buddha is said to have bathed."},
                {"name": "Pahari Mandir & Tagore Hill (Rabindranath Tagore Memorial)", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "300-foot solitary hill temple dedicated to Lord Shiva and serene hilltop retreat where Jyotirindranath Tagore composed literature."},
            ]
        },
        {
            "district": "East Singhbhum", "lat": 22.8046, "lon": 86.2029, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Jamshedpur Roll, Street Puchka & South Indian Tiffin",
            "description": "The Steel City of Jamshedpur (Tatanagar), India's first planned industrial city founded by Jamsetji Tata in 1919.",
            "places": [
                {"name": "Jubilee Park & Dimna Lake", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "225-acre garden gifted by Tata Steel on its golden jubilee, featuring rose gardens, musical illuminated fountains, and a zoo."},
                {"name": "Dalma Wildlife Sanctuary (Elephant Corridor)", "category": "Wildlife", "entry_fee": 50, "opening": "07:00", "closing": "17:00", "description": "High-altitude forest range at 3,000 feet sheltering wild Asian elephants, barking deer, and the mountaintop Shiva temple."},
            ]
        },
        {
            "district": "Deoghar", "lat": 24.4826, "lon": 86.7000, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Deoghar Peda (Khowa Peda - GI) & Rabri",
            "description": "The Abode of Gods on the Mayurakshi River, world-famous for the Baidyanath Dham Jyotirlinga and Shravani Mela.",
            "places": [
                {"name": "Baidyanath Jyotirlinga Temple Complex (Baba Dham)", "category": "Temple", "entry_fee": 0, "opening": "04:00", "closing": "21:30", "description": "One of the 12 sacred Jyotirlingas, where millions of Kanwariyas walk 108km barefoot from Sultanganj carrying sacred Ganga water."},
                {"name": "Trikut Pahar & Passenger Ropeway", "category": "Adventure", "entry_fee": 150, "opening": "08:00", "closing": "17:00", "description": "Three-peaked sacred hill rising 2,470 feet with dense forests, natural hermitage caves of Sage Bamdev, and cable car."},
            ]
        },
        {
            "district": "Dhanbad", "lat": 23.7957, "lon": 86.4304, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Litti Chokha & North Indian Dhaba Food",
            "description": "Coal Capital of India, home to IIT (ISM) Dhanbad, sprawling coalfields, and Maithon Dam.",
            "places": [
                {"name": "Maithon Dam & Deer Park (Lake of the Mother)", "category": "Lake", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Massive 65-sq-km Damodar Valley reservoir with underground powerhouse, speedboats, and the ancient Kalyaneshwari temple."},
            ]
        },
        {
            "district": "Bokaro", "lat": 23.6693, "lon": 86.1511, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bokaro Street Chaat & Bengali Sweets",
            "description": "Planned steel city on the Damodar River, home to Bokaro Steel Plant, Jawaharlal Nehru Biological Park, and Garga Dam.",
            "places": [
                {"name": "Garga Dam & Jawaharlal Nehru Biological Park", "category": "Nature", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "Picturesque dam reservoir and sprawling zoological park with green lawns, boating lake, and nocturnal animal house."},
            ]
        },
        {
            "district": "Latehar", "lat": 23.7438, "lon": 84.4984, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Netarhat Pear Fruit & Forest Honey",
            "description": "Queen of Chotanagpur, high-altitude hill resort of Netarhat at 1,128m famed for glorious sunrises and Magnolia sunset.",
            "places": [
                {"name": "Netarhat Hill Station & Magnolia Sunset Point", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Serene hill plateau covered in pine and eucalyptus forests, famous for dramatic sunset views over the Koel river valley."},
                {"name": "Betla National Park & Palamu Forts", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "17:00", "description": "One of India's earliest tiger reserves with dry sal forests, housing two 16th-century Chero dynasty brick fortresses."},
            ]
        },
    ],

    # ==================== 4. MADHYA PRADESH (55 Districts) ====================
    "Madhya Pradesh": [
        {
            "district": "Bhopal", "lat": 23.2599, "lon": 77.4126, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Bhopali Gosht Korma, Poha Jalebi, Sulemani Chai & Mawa Bati",
            "description": "City of Lakes and capital of Madhya Pradesh, built over seven hills with natural lakes and Begum-era mosques.",
            "places": [
                {"name": "Upper Lake (Bhojtal) & Van Vihar National Park", "category": "Lake", "entry_fee": 30, "opening": "06:00", "closing": "19:00", "description": "11th-century artificial lake built by Raja Bhoj spanning 31 sq km, alongside the open-fenced Van Vihar safari sanctuary."},
                {"name": "Taj-ul-Masajid (Crown of Mosques - Asia's Largest)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Spectacular pink facade mosque featuring 206-foot marble-domed minarets and courtyard holding up to 175,000 worshippers."},
                {"name": "Bhimbetka Rock Shelters (UNESCO World Heritage Site)", "category": "Historical", "entry_fee": 25, "opening": "07:00", "closing": "18:00", "description": "Prehistoric rock shelters with 30,000-year-old Paleolithic and Mesolithic cave paintings of hunting and dancing scenes."},
                {"name": "Sanchi Great Stupa Complex (UNESCO World Heritage Site)", "category": "Historical", "entry_fee": 40, "opening": "06:30", "closing": "18:30", "description": "3rd-century BCE Buddhist monument commissioned by Emperor Ashoka with four carved stone toranas (gateways)."},
            ]
        },
        {
            "district": "Indore", "lat": 22.7196, "lon": 75.8577, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Indori Poha with Sev, Sarafa Night Market Dahi Vada, Bhutte Ka Kees & Garadu",
            "description": "Cleanest City in India for 7 consecutive years, commercial capital of MP famed for midnight street food at Sarafa.",
            "places": [
                {"name": "Rajwada Palace & Sarafa Midnight Food Bazaar", "category": "Palace", "entry_fee": 20, "opening": "10:00", "closing": "23:59", "description": "Seven-storey Holkar dynasty palace combining Maratha and French architecture, adjacent to the famous jewelry-turned-food bazaar."},
                {"name": "Lal Bagh Palace (Versailles of Indore)", "category": "Palace", "entry_fee": 50, "opening": "10:00", "closing": "17:00", "description": "Lavish 19th-century Holkar residence with replica gates of Buckingham Palace, Belgian crystal, and Persian carpets."},
                {"name": "Chhatri Bagh Cenotaphs & Kanch Mandir", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "19:00", "description": "Maratha royal cenotaphs on the Khan River and the dazzling all-glass Jain temple decorated with multicolored mirror mosaics."},
            ]
        },
        {
            "district": "Gwalior", "lat": 26.2183, "lon": 78.1828, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Gwalior Bedai Puri, Morena Gajak & Malpua",
            "description": "Pearl of Indian Fortresses, imperial seat of the Scindia dynasty renowned for classical Tansen music and hilltop forts.",
            "places": [
                {"name": "Gwalior Fort (Pearl of Indian Fortresses)", "category": "Fort", "entry_fee": 25, "opening": "06:00", "closing": "18:00", "description": "8th-century sandstone fortress perched 100 meters above the city, with the blue-enameled Man Mandir Palace and Teli Ka Mandir."},
                {"name": "Jai Vilas Palace & Scindia Museum", "category": "Palace", "entry_fee": 300, "opening": "10:00", "closing": "17:30", "description": "Italian-Corinthian palace holding the world's heaviest pair of chandeliers (3.5 tonnes each) and silver model dining train."},
                {"name": "Tomb of Tansen & Muhammad Ghaus", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "16th-century Mughal memorial to the legendary musical jewel of Akbar's court, venue of the annual Tansen Music Festival."},
            ]
        },
        {
            "district": "Jabalpur", "lat": 23.1815, "lon": 79.9864, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Khoya Jalebi, Dal Bafla & Poha",
            "description": "The Marble City on the Narmada River, famous for the Marble Rocks canyon of Bhedaghat and Dhuandhar falls.",
            "places": [
                {"name": "Bhedaghat Marble Rocks & Narmada Boat Safari", "category": "Nature", "entry_fee": 100, "opening": "07:00", "closing": "18:30", "description": "Dramatic 100-foot white magnesium marble river gorge carved by the Narmada River, magical under full-moon night boat rides."},
                {"name": "Dhuandhar Falls (Smoke Cascade)", "category": "Waterfall", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "98-foot thundering plunge of the Narmada River creating a perpetual misty smoke cloud, accessed by passenger ropeway."},
                {"name": "Madan Mahal Fort & Balancing Rock", "category": "Historical", "entry_fee": 0, "opening": "07:00", "closing": "18:30", "description": "11th-century Gond fortress perched atop a massive granite ridge and a geological wonder rock balanced on a tiny base."},
            ]
        },
        {
            "district": "Ujjain", "lat": 23.1765, "lon": 75.7885, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Ujjaini Sev, Poha Jalebi & Dal Bafla",
            "description": "Sacred Avantika on the holy Shipra River, venue of the Simhastha Kumbh Mela and home to Mahakaleshwar Jyotirlinga.",
            "places": [
                {"name": "Mahakaleshwar Jyotirlinga Temple & Mahakal Lok Corridor", "category": "Temple", "entry_fee": 0, "opening": "04:00", "closing": "23:00", "description": "Only south-facing (Dakshinmukhi) Jyotirlinga, world-famous for the sacred Bhasma Aarti and 900m grand Mahakal Lok corridor."},
                {"name": "Ram Ghat & Shipra River Evening Aarti", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "Ancient holy ghat where millions take sacred dips during Kumbh Mela, with sunset aartis and floating oil lamps."},
                {"name": "Kal Bhairav Temple (Deity of Wine Offerings)", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "Tantric temple dedicated to Kal Bhairav, famous for the miracle where the deity consumes liquor offered by devotees."},
            ]
        },
        {
            "district": "Chhatarpur", "lat": 24.9180, "lon": 79.5820, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Bundelkhandi Thali & Mawa Bati",
            "description": "Home to the world-renowned UNESCO World Heritage erotic stone temples of Khajuraho and Panna tiger forests.",
            "places": [
                {"name": "Khajuraho Group of Temples (Western Group - UNESCO Site)", "category": "Historical", "entry_fee": 40, "opening": "06:00", "closing": "18:00", "description": "10th-century Chandela dynasty sandstone temples featuring the magnificent Kandariya Mahadeva temple with exquisite sculptures."},
                {"name": "Panna National Park & Ken River Safari", "category": "Wildlife", "entry_fee": 300, "opening": "06:00", "closing": "17:30", "description": "Award-winning Project Tiger sanctuary with dramatic gorges, boat safaris on the Ken River, and Pandav falls."},
            ]
        },
        {
            "district": "Niwari", "lat": 25.3500, "lon": 78.6400, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Bundelkhandi Besan Kadhi & Khaja",
            "description": "Created from Tikamgarh, holding the medieval palace kingdom of Orchha along the pristine Betwa River.",
            "places": [
                {"name": "Orchha Fort Complex (Jahangir Mahal & Raja Mahal)", "category": "Palace", "entry_fee": 40, "opening": "08:00", "closing": "17:30", "description": "16th-century Bundela Rajput fortress featuring delicate jalis, chhatris, painted ceilings, and the multi-tiered Jahangir Mahal."},
                {"name": "Ram Raja Temple Orchha", "category": "Temple", "entry_fee": 0, "opening": "07:00", "closing": "22:00", "description": "The only temple in the world where Lord Rama is worshipped as a reigning King (Raja) with a daily police guard of honor."},
            ]
        },
        {
            "district": "Mandla", "lat": 22.5986, "lon": 80.3714, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Gond Tribal Dishes, Kodo-Kutki Millets & Forest Honey",
            "description": "Lush tribal heartland surrounded by the Narmada River on three sides, gateway to Kanha Tiger Reserve.",
            "places": [
                {"name": "Kanha National Park & Tiger Reserve (Rudyard Kipling Land)", "category": "Wildlife", "entry_fee": 650, "opening": "06:00", "closing": "17:30", "description": "Largest national park in MP, classic inspiration for The Jungle Book, home to the rare Hardground Barasingha and tigers."},
            ]
        },
        {
            "district": "Umaria", "lat": 23.5242, "lon": 80.8354, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Bagheli Thali & Mahua Sweets",
            "description": "Dense forest territory of the Vindhyas, home to Bandhavgarh with the highest density of Royal Bengal tigers in India.",
            "places": [
                {"name": "Bandhavgarh National Park & Ancient Hill Fort", "category": "Wildlife", "entry_fee": 750, "opening": "06:00", "closing": "17:30", "description": "World-famous tiger reserve around a 2,000-year-old cliff fort, boasting the highest probability of tiger sightings in the world."},
            ]
        },
        {
            "district": "Hoshangabad", "lat": 22.7519, "lon": 77.7289, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Pachmarhi Herbal Tea & Narmada Sweets",
            "description": "Renamed Narmadapuram, home to the sacred Sethani Ghat on the Narmada and MP's only hill station Pachmarhi.",
            "places": [
                {"name": "Pachmarhi Hill Station (Queen of Satpura)", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "High-altitude verdant plateau at 1,067m with Bee Falls, Jata Shankar cave temple, Dhoopgarh sunset peak, and pine groves."},
            ]
        },
    ],

    # ==================== 5. ODISHA (30 Districts) ====================
    "Odisha": [
        {
            "district": "Puri", "lat": 19.8135, "lon": 85.8312, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Mahaprasad (Chhappan Bhog), Khaja (GI Tag), Chenna Poda & Malpua",
            "description": "The Spiritual Capital of Odisha and one of the four sacred Char Dham on the Bay of Bengal, famous for Rath Yatra.",
            "places": [
                {"name": "Jagannath Temple Puri (Char Dham Pilgrimage)", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "12th-century Kalinga-style shrine dedicated to Lord Jagannath, Balabhadra, and Subhadra, venue of the colossal chariot festival."},
                {"name": "Konark Sun Temple (Black Pagoda - UNESCO World Heritage Site)", "category": "Historical", "entry_fee": 40, "opening": "06:00", "closing": "18:00", "description": "13th-century architectural colossus designed as a 24-wheeled chariot of Surya pulled by seven horses with erotic relief sculptures."},
                {"name": "Golden Beach Puri (Blue Flag Certified Beach)", "category": "Beach", "entry_fee": 20, "opening": "06:00", "closing": "20:00", "description": "Pristine, eco-friendly certified beach on the Bay of Bengal famous for golden sands, swimming, and Sudarsan sand art."},
            ]
        },
        {
            "district": "Khordha", "lat": 20.2961, "lon": 85.8245, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Pahal Rasgulla (GI Tag), Dalma, Machha Besara & Chenna Jhili",
            "description": "Encompassing the Temple City of Bhubaneswar, home to over 500 ancient Kalinga temples, caves, and IT parks.",
            "places": [
                {"name": "Lingaraj Temple (11th Century Kalinga Masterpiece)", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "Largest and oldest temple in Bhubaneswar, dedicated to Harihara (Shiva and Vishnu), with a 180-foot towering sandstone deula."},
                {"name": "Udayagiri and Khandagiri Jain Rock Caves", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "18:00", "description": "2nd-century BCE rock-cut caves carved for Jain monks by King Kharavela, including the double-storey Rani Gumpha and Hathigumpha."},
                {"name": "Nandankanan Zoological Park & White Tiger Safari", "category": "Wildlife", "entry_fee": 50, "opening": "08:00", "closing": "17:00", "description": "World-famous 1,000-acre zoo set in Chandaka forest, famous for breeding white tigers and endangered gharials."},
            ]
        },
        {
            "district": "Cuttack", "lat": 20.4625, "lon": 85.8828, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Dahi Vada Aloo Dum, Silver Filigree Sweets & Chenna Poda",
            "description": "The Millennium City and Silver City of India on the Mahanadi River, famed for 1,000-year-old history and Tarakasi filigree.",
            "places": [
                {"name": "Barabati Fort & Moat (14th Century)", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Historic stone citadel with an intact nine-storey palace gateway, deep water moat, and adjacent international cricket stadium."},
            ]
        },
        {
            "district": "Mayurbhanj", "lat": 21.9333, "lon": 86.7333, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Mayurbhanj Mudhi (Puffed Rice) with Mutton Curry",
            "description": "Princely tribal heartland famous for Chhau dance, waterfalls, and the UNESCO Simlipal Tiger Reserve.",
            "places": [
                {"name": "Simlipal National Park & Biosphere Reserve (UNESCO Site)", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "17:00", "description": "Vast wilderness of sal forests and waterfalls (Barehipani 399m & Joranda 150m), home to tigers, melanistic tigers, and elephants."},
            ]
        },
        {
            "district": "Ganjam", "lat": 19.3149, "lon": 84.7941, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Berhampur Achar, Papad & Chenna Poda",
            "description": "Southern coastal district home to the Olive Ridley sea turtle sanctuary at Rushikulya and Gopalpur beach.",
            "places": [
                {"name": "Gopalpur-on-Sea Heritage Beach & Lighthouse", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Historic colonial port beach with golden sands, seaside breeze, water sports, and British-era pier ruins."},
                {"name": "Rushikulya Rookery (Olive Ridley Sea Turtle Mass Nesting)", "category": "Wildlife", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "World's premier mass nesting site (Arribada) where hundreds of thousands of endangered sea turtles lay eggs on the beach."},
            ]
        },
        {
            "district": "Koraput", "lat": 18.8120, "lon": 82.7118, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Koraput Arabica Coffee & Tribal Millet Cakes",
            "description": "Highland tribal plateau in the Eastern Ghats at 900m elevation, home to Deomali, the highest peak in Odisha.",
            "places": [
                {"name": "Deomali Peak (Highest Mountain in Odisha - 1,672m)", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Breathtaking mountain peak in the Chandragiri range offering 360-degree views of deep gorges, clouds, and tribal valleys."},
                {"name": "Duduma Waterfalls (Machkund Gorge)", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Spectacular 175-meter plunge on the Machkund River amidst deep deciduous forest canyons bordering Andhra Pradesh."},
            ]
        },
        {
            "district": "Kendrapara", "lat": 20.5000, "lon": 86.4200, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Rasabali (GI Tag) & Coastal Crab Curry",
            "description": "Coastal mangrove delta district known as the mini-Amazon of India, home to Bhitarkanika National Park.",
            "places": [
                {"name": "Bhitarkanika National Park & Crocodile Sanctuary (Ramsar)", "category": "Wildlife", "entry_fee": 100, "opening": "07:00", "closing": "17:00", "description": "India's second-largest mangrove ecosystem sheltering world-record saltwater crocodiles, white crocodiles, and kingfishers."},
            ]
        },
    ],

    # ==================== 6. WEST BENGAL (23 Districts) ====================
    "West Bengal": [
        {
            "district": "Kolkata", "lat": 22.5726, "lon": 88.3639, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Kolkata Biryani with Aloo, Rosogolla (GI), Sandesh, Kathi Roll & Phuchka",
            "description": "City of Joy and cultural capital of India on the Hooghly River, home to Victoria Memorial and Howrah Bridge.",
            "places": [
                {"name": "Victoria Memorial Hall & Gardens", "category": "Heritage", "entry_fee": 50, "opening": "10:00", "closing": "17:00", "description": "White Makrana marble monument completed in 1921 blending British and Mughal elements, housing 25 galleries and royal gardens."},
                {"name": "Howrah Bridge (Rabindra Setu on Hooghly)", "category": "Historical", "entry_fee": 0, "opening": "05:00", "closing": "23:00", "description": "Iconic 1943 balanced cantilever steel bridge without nuts and bolts, carrying over 100,000 vehicles and 150,000 pedestrians daily."},
                {"name": "Dakshineswar Kali Temple & Belur Math", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Navaratna nine-spire temple on the Hooghly where Ramakrishna Paramahamsa meditated, facing the serene Belur Math."},
            ]
        },
        {
            "district": "Darjeeling", "lat": 27.0360, "lon": 88.2627, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Darjeeling Orthodox Black Tea (Champagne of Teas - GI), Momos & Thukpa",
            "description": "Queen of the Hills at 2,050m elevation, world-renowned for Darjeeling tea estates and sunrise over Kangchenjunga.",
            "places": [
                {"name": "Tiger Hill Sunrise Point (View of Kangchenjunga & Everest)", "category": "Viewpoint", "entry_fee": 50, "opening": "04:00", "closing": "07:00", "description": "World-famous dawn viewpoint (2,590m) watching the first rays of the sun illuminate the third-highest mountain peak on Earth."},
                {"name": "Darjeeling Himalayan Railway (UNESCO Toy Train)", "category": "Heritage", "entry_fee": 400, "opening": "08:00", "closing": "17:00", "description": "Historic 1881 two-foot narrow gauge steam railway climbing from New Jalpaiguri through the Batasia Loop spiral."},
                {"name": "Happy Valley Tea Estate & Factory (Est. 1854)", "category": "Nature", "entry_fee": 100, "opening": "09:00", "closing": "16:30", "description": "Second-oldest tea estate in Darjeeling spanning 177 hectares, offering guided factory processing tours and tastings."},
            ]
        },
        {
            "district": "Kalimpong", "lat": 27.0667, "lon": 88.4667, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Kalimpong Cheese, Lollipops, Momos & Tea",
            "description": "Peaceful hill station overlooking the Teesta River valley at 1,250m, famous for orchid nurseries and monasteries.",
            "places": [
                {"name": "Deolo Hill & Zang Dhok Palri Phodang Monastery", "category": "Viewpoint", "entry_fee": 20, "opening": "06:00", "closing": "18:30", "description": "Highest point in Kalimpong (1,704m) with 360-degree snow peak panoramas, paragliding, and consecrated Buddhist gompa."},
            ]
        },
        {
            "district": "South 24 Parganas", "lat": 22.1500, "lon": 88.4500, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Sundarbans Wild Honey & Fresh Hilsa Fish",
            "description": "Home to the world's largest mangrove delta, the Sundarbans, and the holy pilgrimage island of Sagar Island.",
            "places": [
                {"name": "Sundarbans National Park (UNESCO World Heritage Site)", "category": "Wildlife", "entry_fee": 100, "opening": "07:00", "closing": "17:00", "description": "World's largest mangrove forest delta on the Bay of Bengal, home of the swimming Royal Bengal Tiger and estuarine crocodiles."},
                {"name": "Gangasagar (Kapil Muni Temple on Sagar Island)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Sacred confluence where the Holy Ganges merges into the ocean, venue of the mammoth Makar Sankranti bath festival."},
            ]
        },
        {
            "district": "Purba Medinipur", "lat": 21.6266, "lon": 87.5074, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Digha Pomfret Fry, Crab Curry & Cashews",
            "description": "Premier coastal beach tourism hub of Bengal, famous for Digha, Mandarmani, and maritime traditions.",
            "places": [
                {"name": "Digha Sea Beach & Marine Aquarium", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Bengal's most popular 7km flat hard beach with sea breeze, Marine Aquarium research center, and seafood shacks."},
                {"name": "Mandarmani Drive-In Beach & Red Crabs Shoreline", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "13-kilometer motorable coastline famous for thousands of scurrying red ghost crabs and seaside beach resorts."},
            ]
        },
        {
            "district": "Bankura", "lat": 23.2323, "lon": 87.0715, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Mecha Sandesh & Bankura Horse Crafts",
            "description": "Terracotta Capital of Bengal, famous for the Bankura Terracotta Horse (national craft emblem) and Bishnupur temples.",
            "places": [
                {"name": "Bishnupur Terracotta Temples (Rasmancha & Jor Bangla)", "category": "Historical", "entry_fee": 25, "opening": "08:00", "closing": "17:30", "description": "17th-century Malla king brick temples covered in exquisite terracotta tiles depicting Mahabharata epics, and Baluchari silk."},
            ]
        },
        {
            "district": "Birbhum", "lat": 23.6700, "lon": 87.7200, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Shantiniketan Baul Sweets & Langcha",
            "description": "Land of Red Soil (Rarh), world-famous for Rabindranath Tagore's Visva-Bharati University at Shantiniketan.",
            "places": [
                {"name": "Santiniketan Visva-Bharati University (UNESCO Site)", "category": "Cultural", "entry_fee": 50, "opening": "10:00", "closing": "16:30", "description": "Open-air international university and ashram founded by Nobel Laureate Rabindranath Tagore, celebrating art and humanities."},
                {"name": "Tarapith Shakti Peetha Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Sacred Tantric pilgrimage temple dedicated to Goddess Tara on the Dwarka River, home of saint Bamakhepa."},
            ]
        },
        {
            "district": "Murshidabad", "lat": 24.1800, "lon": 88.2700, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Murshidabadi Biryani, Chenabora & Silk",
            "description": "Last independent capital of Bengal before British conquest, situated on the Bhagirathi River.",
            "places": [
                {"name": "Hazarduari Palace (Palace with 1,000 Doors)", "category": "Palace", "entry_fee": 25, "opening": "09:00", "closing": "17:00", "description": "1837 Italianate grand palace designed by Duncan Macleod with 1,000 doors (900 real, 100 false), royal armory, and silver throne."},
            ]
        },
        {
            "district": "Nadia", "lat": 23.4000, "lon": 88.5000, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Nabadwip Lal Doi & Krishnanagar Sarpuria (GI)",
            "description": "Spiritual hub on the Bhagirathi River, birthplace of Chaitanya Mahaprabhu and global ISKCON headquarters at Mayapur.",
            "places": [
                {"name": "Mayapur ISKCON Temple of the Vedic Planetarium (TOVP)", "category": "Spiritual", "entry_fee": 0, "opening": "04:30", "closing": "20:30", "description": "World's largest Vedic temple dome complex on the holy Ganges, headquartering the International Society for Krishna Consciousness."},
            ]
        },
        {
            "district": "Alipurduar", "lat": 26.4900, "lon": 89.5200, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Dooars Tea & Momos",
            "description": "Gateway to Bhutan through the Dooars, home to Jaldapara and Buxa tiger and rhino reserves.",
            "places": [
                {"name": "Jaldapara National Park (One-Horned Rhinoceros)", "category": "Wildlife", "entry_fee": 150, "opening": "06:00", "closing": "17:00", "description": "Grassland riverine forest on the Torsa River holding India's second-largest population of Great Indian One-Horned Rhinos."},
            ]
        },
        {
            "district": "Jalpaiguri", "lat": 26.5400, "lon": 88.7100, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Jalpaiguri Sweets & Dooars Tea",
            "description": "Heart of the Dooars tea gardens in North Bengal, home to Gorumara National Park.",
            "places": [
                {"name": "Gorumara National Park & Rhino Watchtowers", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "17:00", "description": "Floodplain sal forest sanctuary on the Murti River renowned for elephant safaris and one-horned rhino sightings."},
            ]
        },
    ],
}

