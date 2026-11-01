"""
Northern India States & UTs Master Districts & Tourist Attractions
Covers Delhi (11), Chandigarh (1), Haryana (22), Himachal Pradesh (12), Jammu & Kashmir (20), Ladakh (2), Punjab (23), Rajasthan (50), Uttar Pradesh (75), Uttarakhand (13).
"""

NORTH_STATES = {
    # ==================== 1. DELHI (11 Districts) ====================
    "Delhi": [
        {
            "district": "New Delhi", "lat": 28.6139, "lon": 77.2090, "crime_index": 26.0, "safety_tier": "LOW",
            "food": "Pandara Road North Indian, Connaught Place Cafes & Chaat",
            "description": "National capital seat of the Republic of India, designed by Sir Edwin Lutyens with grand ceremonial avenues and war memorials.",
            "places": [
                {"name": "India Gate & National War Memorial", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "23:00", "description": "42-meter triumphal arch war memorial along Kartavya Path and the four concentric chakras of the National War Memorial."},
                {"name": "Rashtrapati Bhavan & Amrit Udyan", "category": "Heritage", "entry_fee": 50, "opening": "09:30", "closing": "17:30", "description": "330-acre grand presidential estate atop Raisina Hill with Mughal-influenced classical botanical gardens."},
                {"name": "Connaught Place (Rajiv Chowk)", "category": "Heritage", "entry_fee": 0, "opening": "10:00", "closing": "22:00", "description": "Colonial Georgian-style circular colonnaded arcade housing international bistros, underground Palika Bazaar, and museums."},
            ]
        },
        {
            "district": "Central Delhi", "lat": 28.6500, "lon": 77.2300, "crime_index": 28.0, "safety_tier": "LOW",
            "food": "Chandni Chowk Paranthe, Daulat Ki Chaat, Karim's Mughlai & Jalebi",
            "description": "The historic walled Mughal city of Shahjahanabad, home to red sandstone palaces, bustling bazaars, and massive mosques.",
            "places": [
                {"name": "Red Fort (Lal Qila - UNESCO World Heritage Site)", "category": "Historical", "entry_fee": 50, "opening": "09:30", "closing": "17:30", "description": "1648 octagonal red sandstone citadel built by Emperor Shah Jahan with Diwan-i-Aam, Diwan-i-Khas, and Lahori Gate."},
                {"name": "Jama Masjid (India's Largest Historic Mosque)", "category": "Spiritual", "entry_fee": 0, "opening": "07:00", "closing": "18:30", "description": "Mughal architectural wonder commissioned by Shah Jahan in 1656, holding up to 25,000 worshippers in its marble courtyard."},
                {"name": "Chandni Chowk & Paranthe Wali Gali", "category": "Cultural", "entry_fee": 0, "opening": "10:00", "closing": "21:00", "description": "Historic 17th-century moonlight bazaar planned by Princess Jahanara, famous for heritage street food and spice trading."},
            ]
        },
        {
            "district": "South Delhi", "lat": 28.5245, "lon": 77.1855, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Hauz Khas Village Cafes, Dosa & Mughlai Kebabs",
            "description": "Rich historical enclave preserving Delhi Sultanate monuments, medieval reservoirs, and chic arts villages.",
            "places": [
                {"name": "Qutub Minar & Mehrauli Archaeological Park (UNESCO Site)", "category": "Historical", "entry_fee": 40, "opening": "07:00", "closing": "18:00", "description": "72.5-meter fluted red sandstone minaret built in 1192 by Qutb-ud-din Aibak, with the 1,600-year-old rustless Iron Pillar."},
                {"name": "Lotus Temple (Bahá'í House of Worship)", "category": "Spiritual", "entry_fee": 0, "opening": "08:30", "closing": "18:00", "description": "Pure white Greek marble temple shaped like 27 petals of a blooming lotus flower, welcoming people of all faiths in silence."},
                {"name": "Hauz Khas Complex & Deer Park", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "14th-century Alauddin Khalji royal water reservoir and madrasa ruins overlooking scenic duck lakes and deer meadows."},
            ]
        },
        {
            "district": "South East Delhi", "lat": 28.5600, "lon": 77.2600, "crime_index": 25.0, "safety_tier": "LOW",
            "food": "Nizamuddin Biryani, Kebabs & Phirni",
            "description": "Home to the first garden tomb of the Indian subcontinent and world-renowned Sufi musical traditions.",
            "places": [
                {"name": "Humayun's Tomb Complex & Sunder Nursery (UNESCO Site)", "category": "Historical", "entry_fee": 40, "opening": "06:00", "closing": "18:00", "description": "1570 Charbagh garden tomb commissioned by Empress Bega Begum that directly inspired the architectural design of the Taj Mahal."},
                {"name": "Hazrat Nizamuddin Dargah & Qawwali Courtyard", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "22:30", "description": "14th-century Sufi sanctuary of saint Nizamuddin Auliya and poet Amir Khusrau, world-famed for soul-stirring Thursday qawwali music."},
            ]
        },
        {
            "district": "East Delhi", "lat": 28.6280, "lon": 77.2950, "crime_index": 25.0, "safety_tier": "LOW",
            "food": "Street Chaat, Chole Bhature & Kulfi",
            "description": "Trans-Yamuna district famous for colossal Swaminarayan Akshardham and riverside parks.",
            "places": [
                {"name": "Swaminarayan Akshardham Temple Delhi", "category": "Spiritual", "entry_fee": 0, "opening": "09:30", "closing": "20:00", "description": "100-acre pink sandstone and Italian Carrara marble temple with 234 carved pillars, 148 stone elephants, and boat rides."},
            ]
        },
        {
            "district": "North Delhi", "lat": 28.7000, "lon": 77.2100, "crime_index": 25.0, "safety_tier": "LOW",
            "food": "Kamla Nagar Chole Kulche, Chaat & University Street Eats",
            "description": "Historic northern ridge and university campus, home to British Mutiny memorials and riverside ghats.",
            "places": [
                {"name": "Northern Ridge (Kamla Nehru Ridge) & Flagstaff Tower", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Forested quartzite ridge featuring historic 1857 Mutiny Memorial, Ashokan pillar, and morning walking trails."},
            ]
        },
        {
            "district": "North West Delhi", "lat": 28.7180, "lon": 77.1400, "crime_index": 26.0, "safety_tier": "LOW",
            "food": "Pitampura Street Food, Dal Makhani & Soya Chaap",
            "description": "Bustling residential and commercial district featuring the landmark Pitampura TV Tower and Dilli Haat.",
            "places": [
                {"name": "Dilli Haat Pitampura", "category": "Cultural", "entry_fee": 30, "opening": "11:00", "closing": "22:00", "description": "Open-air rural craft bazaar and food plaza showcasing traditional state handicrafts, folk dances, and regional cuisine."},
            ]
        },
        {
            "district": "West Delhi", "lat": 28.6500, "lon": 77.1200, "crime_index": 25.0, "safety_tier": "LOW",
            "food": "Rajouri Garden Tandoori Delicacies, Chole Bhature & Amritsari Kulcha",
            "description": "Thriving shopping, culinary, and residential hub famed for Punjabi delicacies, markets, and district parks.",
            "places": [
                {"name": "District Park Paschim Vihar & Bharat Darshan Park", "category": "Nature", "entry_fee": 100, "opening": "10:00", "closing": "21:00", "description": "Eco-friendly theme park featuring replica monuments of India constructed entirely from 350 tonnes of metallic scrap waste."},
            ]
        },
        {
            "district": "South West Delhi", "lat": 28.5800, "lon": 77.0500, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Dwarka Street Food & South Indian Cafes",
            "description": "Gateway to Indira Gandhi International Airport and modern planned sub-city of Dwarka.",
            "places": [
                {"name": "National Rail Museum Chanakyapuri", "category": "Museum", "entry_fee": 50, "opening": "10:00", "closing": "17:00", "description": "11-acre outdoor museum housing India's first steam locomotive (Fairy Queen - 1855) and Maharaja royal saloons."},
            ]
        },
        {
            "district": "North East Delhi", "lat": 28.7000, "lon": 77.2700, "crime_index": 27.0, "safety_tier": "LOW",
            "food": "Seelampur Kebabs, Bedmi Puri & Halwa Nagori",
            "description": "Dense cultural and trade hub on the eastern bank of the Yamuna River with traditional street bazaars.",
            "places": [
                {"name": "Yamuna Biodiversity Park (Phase 1 & 2)", "category": "Nature", "entry_fee": 0, "opening": "09:30", "closing": "16:30", "description": "457-acre revived wetland ecology restoring natural native Yamuna floodplains, migratory bird lagoons, and herbal gardens."},
            ]
        },
        {
            "district": "Shahdara", "lat": 28.6700, "lon": 77.2900, "crime_index": 26.0, "safety_tier": "LOW",
            "food": "Shahdara Jalebi, Kachori & Kulfi",
            "description": "Historic 17th-century Mughal commercial gateway established by Shah Jahan, meaning 'Door of Kings'.",
            "places": [
                {"name": "Chhota Bazaar & Historic Gurudwara Nanak Piao", "category": "Cultural", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Historic marketplace and Sikh pilgrimage shrine where Guru Nanak Dev Ji served cool water to weary travelers in 1505."},
            ]
        },
    ],

    # ==================== 2. CHANDIGARH (1 District) ====================
    "Chandigarh": [
        {
            "district": "Chandigarh", "lat": 30.7333, "lon": 76.7794, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Chole Bhature, Butter Chicken, Lassi & Sector 17 Ice Cream",
            "description": "The City Beautiful, planned modernist garden metropolis designed by French-Swiss architect Le Corbusier.",
            "places": [
                {"name": "Nek Chand's Rock Garden (World-Famous Recycled Art)", "category": "Historical", "entry_fee": 30, "opening": "09:00", "closing": "19:00", "description": "25-acre surreal fantasy kingdom of sculptures and amphitheaters built secretly by Nek Chand entirely from urban industrial and home waste."},
                {"name": "Sukhna Lake & Walking Promenade", "category": "Lake", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "3-sq-km pristine man-made reservoir nestled at the foothills of the Shivalik hills, with solar boat cruises and migratory ducks."},
                {"name": "Capitol Complex & Open Hand Monument (UNESCO Site)", "category": "Heritage", "entry_fee": 0, "opening": "09:00", "closing": "17:00", "description": "Le Corbusier's masterwork comprising the Secretariat, High Court, Legislative Assembly, and the 28-meter rotating Open Hand metal emblem."},
                {"name": "Zakir Hussain Rose Garden (Asia's Largest)", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "30-acre botanical garden in Sector 16 boasting 1,600 distinct rose varieties and 50,000 rose bushes alongside medicinal shrubs."},
            ]
        },
    ],

    # ==================== 3. HARYANA (22 Districts) ====================
    "Haryana": [
        {
            "district": "Gurugram", "lat": 28.4595, "lon": 77.0266, "crime_index": 26.0, "safety_tier": "LOW",
            "food": "Cyber Hub Gourmet Dining, Murthal Parathas & Haryanvi Kadhi",
            "description": "Millennium City of India, gleaming corporate Fortune 500 headquarters hub, high-tech malls, and biodiversity wetlands.",
            "places": [
                {"name": "Sultanpur National Park & Bird Sanctuary", "category": "Wildlife", "entry_fee": 20, "opening": "07:00", "closing": "16:30", "description": "Ramsar wetland sanctuary home to over 250 species of winter migratory birds from Siberia and Central Asia."},
                {"name": "Cyber Hub & Kingdom of Dreams Corridor", "category": "Cultural", "entry_fee": 0, "opening": "11:00", "closing": "23:30", "description": "Premier dining, social, and entertainment amphitheater promenade with open-air global bistros and live performances."},
            ]
        },
        {
            "district": "Faridabad", "lat": 28.4089, "lon": 77.3178, "crime_index": 25.0, "safety_tier": "LOW",
            "food": "Surajkund Street Food & North Indian Thali",
            "description": "Largest city in Haryana on the Yamuna River, famous for the annual international Surajkund Crafts Mela.",
            "places": [
                {"name": "Surajkund Sun Reservoir & International Crafts Mela Grounds", "category": "Historical", "entry_fee": 20, "opening": "06:00", "closing": "18:00", "description": "10th-century semi-circular amphitheater sun stepwell built by King Surajpal of the Tomar dynasty, venue of the global crafts festival."},
                {"name": "Badkhal Lake & Aravalli Trekking Trails", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Natural reservoir nestled in the ancient Aravalli hill ranges with forested ridge walks and picnic spots."},
            ]
        },
        {
            "district": "Kurukshetra", "lat": 29.9695, "lon": 76.8783, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Haryanvi Malpua, Bajra Khichdi & Lassi",
            "description": "The Holy Land of the Mahabharata and Gita Upadesh, sacred pilgrimage center featuring monumental water tanks.",
            "places": [
                {"name": "Brahma Sarovar (Sacred Water Tank)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "One of Asia's largest man-made water tanks (1,800m x 800m), where millions take holy dips during solar eclipses."},
                {"name": "Jyotisar (Birthplace of the Bhagavad Gita)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Sacred site where Lord Krishna delivered the timeless message of the Bhagavad Gita to Arjuna under the holy Banyan Tree."},
            ]
        },
        {
            "district": "Panchkula", "lat": 30.6942, "lon": 76.8606, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Pinjore Street Food & Punjabi-Haryanvi Dishes",
            "description": "Planned Shivalik foothills satellite city, home to 17th-century Mughal terraced gardens and Morni Hills.",
            "places": [
                {"name": "Yadavindra Gardens (Pinjore Mughal Gardens)", "category": "Heritage", "entry_fee": 25, "opening": "07:00", "closing": "21:30", "description": "17th-century terraced garden built by Nawab Fidai Khan with central water channels, fountains, and Sheesh Mahal."},
                {"name": "Morni Hills & Tikkar Taal Twin Lakes", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Haryana's only hill station at 1,220m elevation, featuring boating, pine trees, and ancient forts."},
            ]
        },
        {
            "district": "Ambala", "lat": 30.3782, "lon": 76.7767, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Ambala Cloth Market Sweets & Chole Bhature",
            "description": "Twin cantonment and science city, major railway junction famous for scientific instruments and textile wholesale.",
            "places": [
                {"name": "Gurudwara Manji Sahib (Baoli Sahib)", "category": "Spiritual", "entry_fee": 0, "opening": "04:30", "closing": "21:30", "description": "Historic Sikh shrine visited by Guru Hargobind Ji and Guru Tegh Bahadur Ji, with sacred subterranean baoli."},
            ]
        },
        # All other Haryana districts (Bhiwani, Charkhi Dadri, Fatehabad, Hisar, Jhajjar, Jind, Kaithal, Karnal, Mahendragarh, Nuh, Palwal, Panipat, Rewari, Rohtak, Sirsa, Sonipat, Yamunanagar)
        {
            "district": "Hisar", "lat": 29.1492, "lon": 75.7217, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Hisar Peda & Haryanvi Bajra Roti",
            "description": "Steel City of Haryana founded by Firoz Shah Tughlaq in 1354, holding Indus Valley ruins at Rakhigarhi.",
            "places": [
                {"name": "Firoz Shah Palace Complex & Lat ki Masjid", "category": "Historical", "entry_fee": 20, "opening": "08:00", "closing": "17:30", "description": "14th-century Tughlaq royal citadel featuring the Gujri Mahal palace built for his beloved and ancient Ashokan pillar."},
                {"name": "Rakhigarhi Indus Valley Archaeological Site", "category": "Historical", "entry_fee": 0, "opening": "09:00", "closing": "17:00", "description": "Largest Harappan civilization excavation site spanning 350 hectares, revealing planned drainage, kilns, and cemeteries."},
            ]
        },
        {
            "district": "Karnal", "lat": 29.6857, "lon": 76.9905, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Basmati Rice Dishes & Doodh Jalebi",
            "description": "City of Daanveer Karna from the Mahabharata, agricultural and research center on the Grand Trunk Road.",
            "places": [
                {"name": "Karna Lake & Cantonment Church Tower", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Scenic highway lake with pedal boating and swans, where warrior Karna gave donations to the poor."},
            ]
        },
        {
            "district": "Panipat", "lat": 29.3909, "lon": 76.9635, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Panipat Pachranga Pickle & Handloom Sweets",
            "description": "City of Weavers, historic battleground where three monumental battles shaped the history of India in 1526, 1556, and 1761.",
            "places": [
                {"name": "Panipat Battle Memorial & Kabuli Bagh Mosque", "category": "Historical", "entry_fee": 20, "opening": "08:30", "closing": "17:30", "description": "1527 mosque built by Babur commemorating his victory over Ibrahim Lodhi at the First Battle of Panipat."},
                {"name": "Tomb of Bu Ali Shah Qalandar", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "21:30", "description": "14th-century Sufi shrine celebrating universal peace and brotherhood with ornate red stone jalis."},
            ]
        },
        {
            "district": "Sonipat", "lat": 28.9931, "lon": 77.0151, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Murthal Dhabas (Amrik Sukhdev White Butter Parathas)",
            "description": "Ancient Swarnaprastha on the Yamuna, worldwide famous for the 24/7 highway culinary capital of Murthal.",
            "places": [
                {"name": "Murthal Highway Culinary Oasis", "category": "Cultural", "entry_fee": 0, "opening": "00:00", "closing": "23:59", "description": "Famous 24/7 highway strip on NH-44 celebrated across North India for tandoori stuffed parathas with homemade white butter."},
                {"name": "Khwaja Khizr Tomb & Garden", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "1524 CE Ibrahim Lodi period red sandstone mausoleum set within landscaped gardens with intricate arched gateways."},
            ]
        },
        {
            "district": "Rohtak", "lat": 28.8955, "lon": 76.6066, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Rohtak Rewari (GI Tag), Gajak & Lassi",
            "description": "The Educational Capital of Haryana, famous for rewri gajak winter sweets and the ancient Tilyar Lake.",
            "places": [
                {"name": "Tilyar Lake & Tourist Complex", "category": "Lake", "entry_fee": 20, "opening": "07:00", "closing": "20:00", "description": "132-acre landscaped green recreation lake with toy train, mini-zoo, boating, and paved walking paths."},
            ]
        },
        {
            "district": "Bhiwani", "lat": 28.7830, "lon": 76.1397, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bhiwani Peda & Haryanvi Sweets",
            "description": "Known as Chhoti Kashi for its 300+ temples, and the Boxing Capital of India producing Olympic medalists.",
            "places": [
                {"name": "Star Monument (Tara Chand Maharaj Smarak)", "category": "Spiritual", "entry_fee": 0, "opening": "08:00", "closing": "19:00", "description": "Star-shaped architectural marvel built without pillars, honoring Param Sant Radhaswami guru Tara Chand Ji."},
            ]
        },
        {
            "district": "Charkhi Dadri", "lat": 28.5921, "lon": 76.2653, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Haryanvi Churma & Lassi",
            "description": "Formed from Bhiwani, famed for flexible sandstone quarries (itacolumite) found only in two places globally.",
            "places": [
                {"name": "Shyam Sarovar & Kapuri Hills", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Natural lake and Aravalli hill ranges with scenic temples and geological flexible stone reserves."},
            ]
        },
        {
            "district": "Fatehabad", "lat": 29.5160, "lon": 75.4544, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Fatehabad Sweets & North Indian Food",
            "description": "Founded by Firoz Shah Tughlaq in 1352 named after his son Fateh Khan, near Indus Valley Kunal ruins.",
            "places": [
                {"name": "Firoz Shah Tughlaq Fort & Lat (Pillar)", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "17:30", "description": "14th-century stone fort complex featuring a monolithic Ashokan pillar inscribed with Tughlaq genealogy."},
            ]
        },
        {
            "district": "Jhajjar", "lat": 28.6063, "lon": 76.6565, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Jhajjar Pottery Sweets & Haryanvi Kheer",
            "description": "Traditional pottery town home to the premier migratory waterbird haven of Bhindawas Wildlife Sanctuary.",
            "places": [
                {"name": "Bhindawas Wildlife Sanctuary & Lake (Ramsar Site)", "category": "Wildlife", "entry_fee": 20, "opening": "07:00", "closing": "17:00", "description": "Man-made wetland covering 1,000 acres, sheltering over 35,000 winter migratory waterfowl across 250 species."},
            ]
        },
        {
            "district": "Jind", "lat": 29.3160, "lon": 76.3150, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Jind Milk Sweets & Bajra Khichdi",
            "description": "Heart of Haryana founded by Pandavas, celebrated for the sacred Jayanti Devi Temple and Ranji lake.",
            "places": [
                {"name": "Jayanti Devi Temple & Rani Talab", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Ancient temple built by the Pandavas for Goddess of Victory Jayanti Devi, and a royal tank with a central temple."},
            ]
        },
        {
            "district": "Kaithal", "lat": 29.8015, "lon": 76.3997, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kaithal Sweets & Haryanvi Tiffin",
            "description": "Mythological Kapisthala (Abode of Hanuman) and final resting place of Razia Sultana, first woman ruler of Delhi.",
            "places": [
                {"name": "Tomb of Razia Sultana", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "1240 CE historic resting place of Razia Sultana, the brave 13th-century Empress of the Delhi Sultanate."},
            ]
        },
        {
            "district": "Mahendragarh", "lat": 28.2797, "lon": 76.1488, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Narnaul Sweets & Haryanvi Kadhi",
            "description": "Home to the historic heritage town of Narnaul, Birbal Ka Chhatta, and Dhosi Hill extinct volcano.",
            "places": [
                {"name": "Jal Mahal & Chor Gumbad Narnaul", "category": "Historical", "entry_fee": 20, "opening": "08:30", "closing": "17:30", "description": "1591 CE water palace built by Shah Quli Khan in the center of an artificial lake, with stone causeway bridges."},
            ]
        },
        {
            "district": "Nuh", "lat": 28.1133, "lon": 77.0151, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Mewati Pulao & Roti",
            "description": "Heart of the Mewat cultural region in the southern Aravallis, home to medieval Sheikh Musa tombs and mineral springs.",
            "places": [
                {"name": "Tomb of Sheikh Musa & Shaking Minarets", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "14th-century Dargah blending Rajput and Mughal architecture, famed for twin minarets that vibrate simultaneously."},
            ]
        },
        {
            "district": "Palwal", "lat": 28.1444, "lon": 77.3256, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Palwal Peda & Milk Sweets",
            "description": "Ancient Apelva town on the Yamuna, site where Mahatma Gandhi was first arrested on Indian soil in 1919.",
            "places": [
                {"name": "Gandhi Seva Ashram & Panchvati Temple", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Foundation stone laid by Subhas Chandra Bose in 1938 at the site of Gandhi's first arrest in independent struggle."},
            ]
        },
        {
            "district": "Rewari", "lat": 28.1920, "lon": 76.6191, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Rewari Tillewali Jutti Sweets & Kadhi",
            "description": "The Brass City of Haryana, home to India's only surviving steam locomotive heritage shed and Raja Rao Tula Ram.",
            "places": [
                {"name": "Rewari Steam Railway Heritage Shed (1893)", "category": "Heritage", "entry_fee": 20, "opening": "09:00", "closing": "17:00", "description": "Century-old working steam locomotive shed housing the Fairy Queen (1855) and Akbar steam engines featured in films."},
            ]
        },
        {
            "district": "Sirsa", "lat": 29.5349, "lon": 75.0297, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Kheer, Churma & Punjabi-Haryanvi Cuisine",
            "description": "Ancient town on the legendary dried Saraswati River, gateway between Haryana, Punjab, and Rajasthan.",
            "places": [
                {"name": "Tara Baba Kutiya & Sarsuti Temple", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Sprawling 5-acre spiritual sanctuary featuring a 71-foot high Shiva statue and peaceful prayer halls."},
            ]
        },
        {
            "district": "Yamunanagar", "lat": 30.1290, "lon": 77.2674, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Yamunanagar Sweets & North Indian Meals",
            "description": "Plywood and paper capital situated on the Yamuna, blessed with Kalesar National Park and Hathnikund Barrage.",
            "places": [
                {"name": "Kalesar National Park & Hathnikund Barrage", "category": "Wildlife", "entry_fee": 50, "opening": "06:30", "closing": "17:00", "description": "Dense sal forest park in the Shivaliks sheltering leopards, wild boars, and elephants alongside the Yamuna Barrage."},
            ]
        },
    ],
}

from app.database.states_north_part2 import NORTH_STATES_PART2
from app.database.states_north_part3 import NORTH_STATES_PART3

NORTH_STATES.update(NORTH_STATES_PART2)
NORTH_STATES.update(NORTH_STATES_PART3)

