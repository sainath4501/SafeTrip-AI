"""
Northern India States Part 3: Rajasthan (50 Districts) and Uttar Pradesh (75 Districts).
"""

NORTH_STATES_PART3 = {
    # ==================== 1. RAJASTHAN (50 Districts) ====================
    "Rajasthan": [
        {
            "district": "Jaipur", "lat": 26.9124, "lon": 75.7873, "crime_index": 25.0, "safety_tier": "LOW",
            "food": "Dal Baati Churma, Pyaaz Kachori, Ghevar (GI) & Ker Sangri",
            "description": "The Pink City and capital of Rajasthan, UNESCO World Heritage city renowned for royal palaces and astronomical observatories.",
            "places": [
                {"name": "Amber Fort & Maota Lake (UNESCO World Heritage)", "category": "Fort", "entry_fee": 100, "opening": "08:00", "closing": "18:00", "description": "16th-century hilltop citadel featuring Sheesh Mahal (Mirror Palace), elephant corridors, and ramparts."},
                {"name": "Hawa Mahal (Palace of Winds)", "category": "Palace", "entry_fee": 50, "opening": "09:00", "closing": "17:00", "description": "Five-storey pink sandstone honeycomb facade with 953 jharokhas designed by Lal Chand Ustad in 1799."},
                {"name": "City Palace & Jantar Mantar (UNESCO World Heritage)", "category": "Historical", "entry_fee": 200, "opening": "09:30", "closing": "17:00", "description": "Grand royal residence of the Maharaja of Jaipur and 1734 astronomical stone observatory with the world's largest sundial."},
            ]
        },
        {
            "district": "Udaipur", "lat": 24.5854, "lon": 73.7125, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Udaipuri Kachori, Gatte Ki Sabzi, Mirchi Vada & Mawa Kachori",
            "description": "City of Lakes and Venice of the East, imperial capital of Mewar famed for Lake Pichola palaces and Aravalli sunsets.",
            "places": [
                {"name": "City Palace Udaipur & Lake Pichola", "category": "Palace", "entry_fee": 300, "opening": "09:30", "closing": "17:30", "description": "Rajasthan's largest royal palace complex with 11 palaces, mirror mosaics, and boat cruises to Jag Mandir."},
                {"name": "Taj Lake Palace (Jag Niwas)", "category": "Heritage", "entry_fee": 500, "opening": "09:00", "closing": "18:00", "description": "White marble luxury palace built in 1746 by Maharana Jagat Singh II, appearing to float effortlessly on Lake Pichola."},
                {"name": "Saheliyon Ki Bari & Fateh Sagar Lake", "category": "Nature", "entry_fee": 20, "opening": "09:00", "closing": "19:00", "description": "Royal garden of the maids with marble fountains, lotus pools, and the adjoining scenic lake with Nehru Island park."},
            ]
        },
        {
            "district": "Jodhpur", "lat": 26.2389, "lon": 73.0243, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Jodhpur Mirchi Vada, Pyaaz Kachori, Mawa Kachori & Makhaniya Lassi",
            "description": "The Blue City and Sun City on the edge of the Thar Desert, dominated by the colossal Mehrangarh Fort.",
            "places": [
                {"name": "Mehrangarh Fort & Museum", "category": "Fort", "entry_fee": 100, "opening": "09:00", "closing": "17:00", "description": "One of the largest fortresses in India, rising 125 meters on a perpendicular cliff, with palanquin galleries and zip-lining."},
                {"name": "Jaswant Thada (Taj Mahal of Marwar)", "category": "Historical", "entry_fee": 30, "opening": "09:00", "closing": "17:00", "description": "1899 royal white marble cenotaph built by Maharaja Sardar Singh, with carved sheets of marble that glow warmly in sunlight."},
                {"name": "Umaid Bhawan Palace & Museum", "category": "Palace", "entry_fee": 50, "opening": "09:00", "closing": "17:00", "description": "One of the world's largest private residences with 347 rooms, built of golden Chittar sandstone in Art Deco style."},
            ]
        },
        {
            "district": "Jaisalmer", "lat": 26.9157, "lon": 70.9083, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Ker Sangri, Bajra Roti, Gatte Ka Pulao & Ghotua Laddu",
            "description": "The Golden City of India in the heart of the Thar Desert, famous for its living yellow sandstone fort and sand dunes.",
            "places": [
                {"name": "Jaisalmer Fort (Sonar Qila - UNESCO World Heritage Site)", "category": "Fort", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "The world's only living fort, home to 4,000 residents, ornate Jain temples, royal palaces, and rooftop cafes."},
                {"name": "Sam Sand Dunes & Desert Safari Camp", "category": "Adventure", "entry_fee": 100, "opening": "06:00", "closing": "21:00", "description": "Rolling 60-meter high shifting golden sand dunes offering camel safaris, jeep dune bashing, and Kalbeliya folk dances under stars."},
                {"name": "Patwon Ki Haveli (Cluster of 5 Royal Mansions)", "category": "Historical", "entry_fee": 50, "opening": "09:00", "closing": "18:00", "description": "First haveli erected in Jaisalmer (1805) with 60 intricately carved sandstone balconies, jali windows, and mural ceilings."},
            ]
        },
        {
            "district": "Bikaner", "lat": 28.0229, "lon": 73.3119, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bikaneri Bhujia (GI Tag), Rasgulla & Ghevar",
            "description": "Desert trade center founded by Rao Bika in 1488, world-renowned for Bikaneri Bhujia and the unvanquished Junagarh Fort.",
            "places": [
                {"name": "Junagarh Fort & Prachina Museum", "category": "Fort", "entry_fee": 50, "opening": "10:00", "closing": "16:30", "description": "1594 CE fortress never conquered in history, showcasing Badal Mahal (Cloud Palace), mirror chambers, and gold leaf artwork."},
                {"name": "Karni Mata Temple Deshnoke (Temple of Rats)", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "Famous 600-year-old temple home to over 25,000 revered black rats (kabbas), where sighting a white rat brings supreme fortune."},
            ]
        },
        {
            "district": "Ajmer", "lat": 26.4499, "lon": 74.6399, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Ajmer Kadhi Kachori, Sohan Halwa & Biryani",
            "description": "Spiritual oasis encircled by the Aravalli hills, home to the revered Dargah of Khwaja Moinuddin Chishti and Ana Sagar Lake.",
            "places": [
                {"name": "Dargah Sharif (Khwaja Moinuddin Chishti)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "Revered 13th-century Sufi pilgrimage shrine featuring silver gates, Nizam gate, and massive cooking cauldrons (Degs)."},
                {"name": "Ana Sagar Lake & Marble Baradari Pavilions", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "12th-century artificial lake built by Arnoraja with white marble pavilions (Baradari) erected by Emperor Shah Jahan in 1637."},
                {"name": "Brahma Temple & Pushkar Sacred Lake", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "The only prominent temple in the world dedicated to Lord Brahma, situated on the sacred 52-ghat Pushkar Lake."},
            ]
        },
        {
            "district": "Chittorgarh", "lat": 24.8887, "lon": 74.6269, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Chittorgarh Dal Baati & Rajasthani Sweets",
            "description": "Symbol of Rajput valor and sacrifice, home to India's largest fort perched atop a 180-meter high hill.",
            "places": [
                {"name": "Chittorgarh Fort (Largest Fort in India - UNESCO Site)", "category": "Fort", "entry_fee": 40, "opening": "08:00", "closing": "18:00", "description": "700-acre UNESCO fortress with Vijay Stambh (Tower of Victory), Kirti Stambh, Padmini's Palace, and Gaumukh Reservoir."},
            ]
        },
        {
            "district": "Sawai Madhopur", "lat": 25.9928, "lon": 76.3713, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Guava Delicacies & Rajasthani Pulao",
            "description": "Gateway to Ranthambore, one of the world's most famous wilderness sanctuaries for wild Bengal tigers in historic ruins.",
            "places": [
                {"name": "Ranthambore National Park & Tiger Safari", "category": "Wildlife", "entry_fee": 850, "opening": "06:00", "closing": "18:00", "description": "Premier Project Tiger reserve where wild royal Bengal tigers roam naturally among 10th-century fort ruins and lakes."},
                {"name": "Ranthambore Fort & Trinetra Ganesha Temple (UNESCO Site)", "category": "Fort", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "10th-century UNESCO cliff fortress inside the national park, housing the famous three-eyed Ganesha temple."},
            ]
        },
        {
            "district": "Sirohi", "lat": 24.8826, "lon": 72.8589, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Mount Abu Rabri, Dal Baati & Khaja",
            "description": "Home to Mount Abu, Rajasthan's only hill station at 1,220m elevation, famous for the Dilwara Jain marble temples.",
            "places": [
                {"name": "Dilwara Jain Temples (World-Class Marble Carvings)", "category": "Historical", "entry_fee": 0, "opening": "12:00", "closing": "17:00", "description": "11th-to-13th century marble temples with unbelievable lace-like ceilings, translucent stone pillars, and ornamental doorways."},
                {"name": "Nakki Lake & Toad Rock (Mount Abu)", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Sacred mountain lake excavated by the gods using their fingernails (nakh), with colourful boat rides and sunset rocks."},
            ]
        },
        {
            "district": "Bharatpur", "lat": 27.2152, "lon": 77.5030, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bharatpur Mawa Sweets & Dal Kachori",
            "description": "Eastern Gateway of Rajasthan, home to the UNESCO World Heritage bird sanctuary Keoladeo National Park.",
            "places": [
                {"name": "Keoladeo Ghana National Park (UNESCO World Heritage Site)", "category": "Wildlife", "entry_fee": 75, "opening": "06:00", "closing": "18:00", "description": "World-famous wetland avifauna paradise hosting over 370 bird species, explored on quiet bicycle and rickshaw safaris."},
                {"name": "Lohagarh Fort (Iron Fort of Bharatpur)", "category": "Fort", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "18th-century impregnable Jat fortress built by Maharaja Suraj Mal, famous for withstanding British artillery assaults."},
            ]
        },
        {
            "district": "Alwar", "lat": 27.5530, "lon": 76.6346, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Alwar Kalakand (Milk Cake - GI Tag) & Kachori",
            "description": "Historic Rajput kingdom in the Aravallis, home to the Bala Quila, Sariska Tiger Reserve, and haunted Bhangarh.",
            "places": [
                {"name": "Sariska Tiger Reserve & Siliserh Lake Palace", "category": "Wildlife", "entry_fee": 150, "opening": "06:00", "closing": "17:30", "description": "Aravalli valley sanctuary home to royal Bengal tigers, leopards, and an 1845 royal lake palace with boat safaris."},
                {"name": "Bhangarh Fort Ruins (Asia's Most Haunted Citadel)", "category": "Historical", "entry_fee": 25, "opening": "06:00", "closing": "17:30", "description": "17th-century preserved ghost town and fort ruins strictly closed after sunset, famed for folklore and stone carvings."},
            ]
        },
        {
            "district": "Kota", "lat": 25.2138, "lon": 75.8648, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Kota Kachori (Hing Kachori) & Kota Doria Sarees",
            "description": "Educational and industrial powerhouse on the Chambal River, celebrated for Seven Wonders Park and Kota stone.",
            "places": [
                {"name": "Chambal Riverfront Promenade & Garh Palace", "category": "Heritage", "entry_fee": 50, "opening": "09:00", "closing": "21:00", "description": "World-class riverfront promenade with monumental ghats, world's largest stone bell, and the 17th-century royal palace."},
                {"name": "Seven Wonders Park Kota", "category": "Nature", "entry_fee": 20, "opening": "16:30", "closing": "22:00", "description": "Lakeside park on Kishore Sagar featuring miniature replicas of the Taj Mahal, Eiffel Tower, Colosseum, and Pyramids."},
            ]
        },
        # Representative districts for the remaining Rajasthan districts
        {
            "district": "Bundi", "lat": 25.4415, "lon": 75.6441, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Bundi Ladoo & Dal Baati",
            "description": "City of Stepwells (Baoris) and Rajput murals, home to the Taragarh Fort and Sukh Mahal.",
            "places": [
                {"name": "Taragarh Fort & Bundi Palace (Chitrashala Murals)", "category": "Fort", "entry_fee": 80, "opening": "08:00", "closing": "17:00", "description": "14th-century hillside fortress famous for vivid miniature fresco galleries depicting scenes from Krishna's life."},
                {"name": "Raniji ki Baori (Queen's Stepwell)", "category": "Historical", "entry_fee": 30, "opening": "09:00", "closing": "17:00", "description": "1699 CE multi-storey stepwell with 50-meter deep stone steps adorned with intricate elephant toranas and friezes."},
            ]
        },
        {
            "district": "Pali", "lat": 25.7711, "lon": 73.3234, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Ranakpur Sweets & Gulab Halwa",
            "description": "Textile center of Marwar, home to the world-renowned Ranakpur Jain temple with 1,444 marble pillars.",
            "places": [
                {"name": "Ranakpur Jain Temple (1,444 Uniquely Carved Marble Pillars)", "category": "Historical", "entry_fee": 100, "opening": "12:00", "closing": "17:00", "description": "15th-century marble temple where no two carved pillars are identical, glowing in natural light in the Aravalli valley."},
                {"name": "Om Banna Temple (Bullet Baba Shrine)", "category": "Cultural", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Unique roadside pilgrimage shrine on NH-62 dedicated to a 350cc Royal Enfield motorcycle and its owner Om Singh Rathore."},
            ]
        },
        {
            "district": "Nagaur", "lat": 27.2070, "lon": 73.7423, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Nagauri Methi (Fenugreek) & Dal Baati",
            "description": "Historic trade center celebrated for the UNESCO-awarded Ahhichatragarh Fort and the Nagaur Cattle Fair.",
            "places": [
                {"name": "Nagaur Fort (Ahichhatragarh - UNESCO Awarded)", "category": "Fort", "entry_fee": 50, "opening": "09:00", "closing": "17:30", "description": "12th-century mud-and-stone fortress restored with international awards, featuring water palaces and Mughal garden fountains."},
            ]
        },
        {
            "district": "Jhunjhunu", "lat": 28.1289, "lon": 75.3995, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Peda & Shekhawati Vegetarian Feast",
            "description": "Capital of the Shekhawati open-air art gallery, renowned for fresco-covered merchant havelis and Rani Sati temple.",
            "places": [
                {"name": "Shekhawati Painted Havelis & Rani Sati Temple", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Centuries-old Marwari merchant mansions covered in colourful frescoes, and the 400-year-old multi-marble Rani Sati temple."},
            ]
        },
        {
            "district": "Sikar", "lat": 27.6094, "lon": 75.1399, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Khatu Shyam Prasadam & Peda",
            "description": "Heart of Shekhawati, world-famous for the massive pilgrimage center of Khatu Shyam Ji.",
            "places": [
                {"name": "Khatu Shyam Ji Temple (Barbarika Shrine)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "Famous temple dedicated to Barbarika (grandson of Bhima), visited by millions during the annual Phalguna Mela."},
            ]
        },
        {
            "district": "Rajsamand", "lat": 25.0747, "lon": 73.8821, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Nathdwara Rabri, Thandai & Gatte",
            "description": "Home to the sacred Shrinathji temple in Nathdwara, Kumbhalgarh Fort with the Great Wall of India, and marble lakes.",
            "places": [
                {"name": "Kumbhalgarh Fort (Great Wall of India - 36km)", "category": "Fort", "entry_fee": 40, "opening": "09:00", "closing": "18:00", "description": "Birthplace of Maharana Pratap with the second-longest continuous defensive wall in the world (36km) and 360 temples."},
                {"name": "Nathdwara Shrinathji Temple & Statue of Belief (Viswas Swaroopam)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "20:30", "description": "Major Pushtimarg Vaishnava shrine and the 369-foot colossal sitting statue of Shiva (Statue of Belief)."},
            ]
        },
        {
            "district": "Barmer", "lat": 25.7532, "lon": 71.3967, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Bajra Roti with Garlic Chutney & Ker Sangri",
            "description": "Thar Desert district famed for block printing, wood carving, and the ancient Kiradu temple ruins.",
            "places": [
                {"name": "Kiradu Temples (Khajuraho of Rajasthan)", "category": "Historical", "entry_fee": 20, "opening": "08:00", "closing": "17:30", "description": "Five 11th-century Solanki-style stone temples with intricate erotic sculptures in the Thar desert foothills."},
            ]
        },
        {
            "district": "Dholpur", "lat": 26.7025, "lon": 77.8934, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Dholpur Peda & Milk Sweets",
            "description": "Red Sandstone Capital whose stone built the Red Fort and Rashtrapati Bhavan, on the Chambal River.",
            "places": [
                {"name": "National Chambal Sanctuary & Machkund Sacred Tank", "category": "Wildlife", "entry_fee": 100, "opening": "07:00", "closing": "17:30", "description": "Pristine river sanctuary sheltering gharials, Gangetic dolphins, and red-crowned roof turtles on boat safaris."},
            ]
        },
        {
            "district": "Jhalawar", "lat": 24.5973, "lon": 76.1611, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Jhalawar Oranges & Dal Baati",
            "description": "Princely state in Hadoti region, home to the UNESCO World Heritage water fortress Gagron Fort.",
            "places": [
                {"name": "Gagron Fort (UNESCO World Heritage Water Fortress)", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Majestic 12th-century hill-and-water fort surrounded on three sides by the Ahu and Kali Sindh rivers."},
            ]
        },
        {
            "district": "Karauli", "lat": 26.4984, "lon": 77.0229, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kaila Devi Prasadam & Peda",
            "description": "Holy city in eastern Rajasthan, renowned for the Kaila Devi temple and the grand City Palace of Karauli.",
            "places": [
                {"name": "Kaila Devi Temple & City Palace Karauli", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Sacred Shakti Peetha temple visited by millions during the Chaitra Navratri fair on the banks of the Kalisil River."},
            ]
        },
    ],

    # ==================== 2. UTTAR PRADESH (75 Districts) ====================
    "Uttar Pradesh": [
        {
            "district": "Agra", "lat": 27.1767, "lon": 78.0081, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Agra Petha (Pancchi Petha - GI Tag), Bedmi Puri & Mughlai",
            "description": "The City of the Taj Mahal on the Yamuna River, premier tourism capital of India with three UNESCO World Heritage Sites.",
            "places": [
                {"name": "Taj Mahal (UNESCO World Heritage Site & New 7 Wonders)", "category": "Historical", "entry_fee": 50, "opening": "06:00", "closing": "18:30", "description": "Ivory-white marble mausoleum commissioned in 1631 by Mughal Emperor Shah Jahan for his wife Mumtaz Mahal."},
                {"name": "Agra Fort (Red Sandstone Citadel - UNESCO Site)", "category": "Fort", "entry_fee": 50, "opening": "06:00", "closing": "18:00", "description": "Main residence of the Mughal emperors until 1638, featuring Jahangiri Mahal, Diwan-i-Khas, and Musamman Burj."},
                {"name": "Fatehpur Sikri Royal City (UNESCO Site)", "category": "Historical", "entry_fee": 50, "opening": "06:00", "closing": "18:00", "description": "16th-century ghost capital built by Akbar, featuring the monumental 54m Buland Darwaza and Salim Chishti tomb."},
                {"name": "Mehtab Bagh (Moonlight Garden Viewpoint)", "category": "Nature", "entry_fee": 25, "opening": "06:00", "closing": "18:00", "description": "Charbagh garden complex on the northern bank of the Yamuna offering the most famous reflection views of the Taj Mahal."},
            ]
        },
        {
            "district": "Varanasi", "lat": 25.3176, "lon": 82.9739, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Banarasi Paan (GI), Malaiyo, Kachori Jalebi, Tamatar Chaat & Lassi",
            "description": "Kashi, the Spiritual Capital of India and oldest continuously inhabited city in the world on the sacred Ganges.",
            "places": [
                {"name": "Kashi Vishwanath Jyotirlinga Temple & Corridor", "category": "Temple", "entry_fee": 0, "opening": "03:00", "closing": "23:00", "description": "One of the 12 sacred Jyotirlingas of Lord Shiva with golden spires, connected directly to the Ganga via a grand corridor."},
                {"name": "Dashashwamedh Ghat & Evening Maha Ganga Aarti", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "Main riverfront ghat where priests perform the synchronized multi-tiered brass lamp Ganga Aarti every sunset."},
                {"name": "Sarnath (First Sermon of Lord Buddha - Dhamek Stupa)", "category": "Historical", "entry_fee": 25, "opening": "06:00", "closing": "18:00", "description": "Sacred deer park where Siddhartha Gautama taught the Dharma; museum preserves the Lion Capital of Ashoka (National Emblem)."},
                {"name": "Assi Ghat & Sunrise Subah-e-Banaras", "category": "Cultural", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "Southernmost ghat on the confluence of Assi and Ganga, famed for early morning classical music, yoga, and boat rides."},
            ]
        },
        {
            "district": "Lucknow", "lat": 26.8467, "lon": 80.9462, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Lucknowi Biryani, Galouti Kebab, Tunday Kababi, Sheermal & Malai Paan",
            "description": "The City of Nawabs on the Gomti River, world-renowned for Tehzeeb (etiquette), Chikankari embroidery, and Awadhi cuisine.",
            "places": [
                {"name": "Bara Imambara & Bhool Bhulaiya (Labyrinth)", "category": "Historical", "entry_fee": 50, "opening": "06:00", "closing": "17:00", "description": "1784 architectural wonder built by Nawab Asaf-ud-Daula with unsupported vaulted central hall and 1,000 secret passages."},
                {"name": "Chota Imambara (Palace of Lights) & Rumi Darwaza", "category": "Historical", "entry_fee": 50, "opening": "06:00", "closing": "17:00", "description": "Ornate mausoleum with Belgian glass chandeliers, facing the 60-foot iconic Turkish Gate (Rumi Darwaza)."},
                {"name": "The British Residency Ruins (1857 Siege Memorial)", "category": "Heritage", "entry_fee": 25, "opening": "09:00", "closing": "17:00", "description": "Historic compound of buildings that withstood the 1857 Siege of Lucknow, preserved with cannonball scars and gardens."},
            ]
        },
        {
            "district": "Ayodhya", "lat": 26.7922, "lon": 82.1998, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Ayodhya Peda, Samosa Chaat & Rabri Jalebi",
            "description": "Sacred birthplace of Lord Rama on the holy Saryu River, home to the monumental Shri Ram Janmabhoomi Mandir.",
            "places": [
                {"name": "Shri Ram Janmabhoomi Mandir", "category": "Temple", "entry_fee": 0, "opening": "06:30", "closing": "21:30", "description": "Monumental pink sandstone temple built in traditional Nagara style, consecrating the sacred birthplace of Lord Rama."},
                {"name": "Hanuman Garhi Fort Temple", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "10th-century four-sided hill fortress with 76 steps, where Lord Hanuman is said to have guarded the city of Ayodhya."},
                {"name": "Ram Ki Paidi & Saryu River Ghats", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "Series of riverside steps on the Saryu River, venue of the Guinness World Record Deepotsav festival with millions of earthen lamps."},
            ]
        },
        {
            "district": "Prayagraj", "lat": 25.4358, "lon": 81.8463, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Allahabadi Guava (Surkha), Loknath Chaat, Kachori & Lassi",
            "description": "Ancient Prayag at the Triveni Sangam of Ganga, Yamuna, and Saraswati, venue of the world-famed Kumbh Mela.",
            "places": [
                {"name": "Triveni Sangam & Maha Kumbh Mela Grounds", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Sacred confluence where the pale yellow Ganga meets the blue Yamuna, site of the largest human spiritual gathering on Earth."},
                {"name": "Allahabad Fort & Akshayavat (Indestructible Banyan Tree)", "category": "Fort", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "1583 sandstone fortress built by Emperor Akbar at the Sangam, protecting the sacred immortal banyan tree and Patalpuri temple."},
                {"name": "Anand Bhavan & Swaraj Bhavan (Nehru Ancestral Home)", "category": "Museum", "entry_fee": 70, "opening": "09:30", "closing": "17:00", "description": "Two-storey mansion where Motilal Nehru and Jawaharlal Nehru lived, center of strategy for the Indian National Congress."},
            ]
        },
        {
            "district": "Mathura", "lat": 27.4924, "lon": 77.6737, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Mathura Peda (GI Tag), Makhan Mishri, Bedmi Puri & Jalebi",
            "description": "Brajbhoomi, sacred birthplace of Lord Krishna on the Yamuna, famous worldwide for Holi and Janmashtami.",
            "places": [
                {"name": "Shri Krishna Janmasthan Temple Complex", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "Sacred prison cell (Garbha Griha) where Lord Krishna was born to Devaki and Vasudeva in ancient Mathura."},
                {"name": "Vishram Ghat & Yamuna Aarti", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Central riverfront ghat where Lord Krishna rested after slaying the tyrant king Kansa, celebrated for evening aarti."},
                {"name": "Prem Mandir & Bankey Bihari Temple (Vrindavan)", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "21:30", "description": "54-acre Italian white marble temple in Vrindavan with musical fountain and the beloved Bankey Bihari shrine."},
            ]
        },
        {
            "district": "Jhansi", "lat": 25.4484, "lon": 78.5685, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bundelkhandi Kadhi, Thali & Peda",
            "description": "Gateway to Bundelkhand, synonymous with the courage of Rani Lakshmibai (Rani of Jhansi) during the 1857 rebellion.",
            "places": [
                {"name": "Jhansi Fort (Rani Jhansi Ka Qila)", "category": "Fort", "entry_fee": 25, "opening": "07:00", "closing": "18:00", "description": "17th-century granite fortress atop Bangira hill with 22 bastions, from where Rani Lakshmibai jumped on horseback during siege."},
                {"name": "Rani Mahal & Government Museum", "category": "Palace", "entry_fee": 25, "opening": "09:30", "closing": "17:30", "description": "Palace residence of Rani Lakshmibai featuring colourful floral murals and collection of Chandela sculptures."},
            ]
        },
        {
            "district": "Kanpur Nagar", "lat": 26.4499, "lon": 80.3319, "crime_index": 25.0, "safety_tier": "LOW",
            "food": "Thaggu Ke Laddu, Badnam Kulfi & Kanpur Chaat",
            "description": "The Leather City of the World on the Ganga, historic industrial hub and center of the 1857 independence revolt at Bithoor.",
            "places": [
                {"name": "Bithoor Sacred Ghats & Brahmavart Teerth", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Sacred spot on the Ganga where Lord Brahma created mankind and Valmiki composed the Ramayana, launchpad of 1857 revolt."},
            ]
        },
        {
            "district": "Gorakhpur", "lat": 26.7606, "lon": 83.3732, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Gorakhpuri Khaja, Peda & North Indian Food",
            "description": "Headquarters of the Gorakhnath Nath tradition and Gita Press, the world's largest publisher of Hindu religious texts.",
            "places": [
                {"name": "Gorakhnath Temple (Nath Panth Headquarters)", "category": "Temple", "entry_fee": 0, "opening": "04:00", "closing": "21:30", "description": "Sprawling 52-acre temple monastery dedicated to yogi Guru Gorakhnath, venue of the month-long Khichdi Mela on Makar Sankranti."},
                {"name": "Gita Press Heritage Architecture", "category": "Heritage", "entry_fee": 0, "opening": "09:00", "closing": "17:30", "description": "Founded in 1923, printing over 410 million copies of the Bhagavad Gita and Ramcharitmanas with art gallery."},
            ]
        },
        {
            "district": "Kushinagar", "lat": 26.7410, "lon": 83.8890, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Tibetan Momos, Thukpa & Eastern UP Sweets",
            "description": "One of the four major Buddhist pilgrimage destinations, where Gautama Buddha attained Parinirvana in 483 BCE.",
            "places": [
                {"name": "Parinirvana Temple & 6-Meter Reclining Buddha", "category": "Historical", "entry_fee": 25, "opening": "06:00", "closing": "18:00", "description": "Monolithic 6.1m red sandstone statue of reclining Buddha carved in 5th century CE, depicting Buddha's entry into Mahaparinirvana."},
                {"name": "Ramabhar Stupa (Cremation Site of Lord Buddha)", "category": "Historical", "entry_fee": 25, "opening": "06:00", "closing": "18:00", "description": "Large brick dome stupa standing 15 meters high where Lord Buddha was cremated by the Malla chieftains."},
            ]
        },
        {
            "district": "Lakhimpur Kheri", "lat": 27.9467, "lon": 80.7781, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kheri Rice Sweets & Awadhi Cuisine",
            "description": "Largest district in Uttar Pradesh along the Nepal border, home to Dudhwa National Park.",
            "places": [
                {"name": "Dudhwa National Park & Tiger Reserve", "category": "Wildlife", "entry_fee": 300, "opening": "06:00", "closing": "17:30", "description": "Vast Terai sal forest and swamp grassland sheltering royal Bengal tigers, Indian one-horned rhinos, and swamp deer (Barasingha)."},
            ]
        },
        {
            "district": "Chitrakoot", "lat": 25.1764, "lon": 80.8660, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Bundelkhandi Mawa Sweets & Puri Sabzi",
            "description": "The Hills of Many Wonders in the Vindhyas, where Lord Rama, Sita, and Lakshmana spent eleven of their fourteen exile years.",
            "places": [
                {"name": "Ramghat on Mandakini River & Kamadgiri Hill", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Sacred ghat where saint Tulsidas had darshan of Lord Rama, and the 5km holy parikrama path around Kamadgiri."},
            ]
        },
        {
            "district": "Meerut", "lat": 28.9845, "lon": 77.7064, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Meerut Gajak, Nan Khatai & Rewari",
            "description": "Sports Goods City and cradle of the 1857 Indian Independence Revolt, home to the Augurnath Temple.",
            "places": [
                {"name": "Augharnath Temple (Kali Paltan Mandir - 1857 Revolt Site)", "category": "Historical", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Ancient Shiva temple where Indian soldiers (sepoys) gathered and sparked the 1857 revolt against the East India Company."},
            ]
        },
        {
            "district": "Gautam Buddha Nagar", "lat": 28.5355, "lon": 77.3910, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Noida Cyber Dining, Chaat & North Indian",
            "description": "Modern planned commercial and IT powerhouse of Noida and Greater Noida, featuring bird sanctuaries and sports cities.",
            "places": [
                {"name": "Okhla Bird Sanctuary & Yamuna River Wetlands", "category": "Wildlife", "entry_fee": 30, "opening": "07:00", "closing": "17:30", "description": "Ramsar wetland haven situated where the Yamuna enters UP, hosting over 300 species of migratory and native waterbirds."},
            ]
        },
        {
            "district": "Shravasti", "lat": 27.5100, "lon": 81.9900, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Local Kheer & Poha",
            "description": "Ancient Kosala kingdom capital where Lord Buddha spent 24 monsoon retreats and performed twin miracles.",
            "places": [
                {"name": "Jetavana Monastery & Anathapindika Stupa", "category": "Historical", "entry_fee": 25, "opening": "06:00", "closing": "18:00", "description": "Sacred monastery gifted to Buddha by merchant Anathapindika, featuring the sacred Anandabodhi Tree and Gandhakuti (fragrant hut)."},
            ]
        },
        {
            "district": "Mirzapur", "lat": 25.1460, "lon": 82.5690, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Mirzapur Carpet Crafts & Baati Chokha",
            "description": "Carpet and brassware hub in the Vindhyachal hills on the Ganga, home to the sacred Vindhyavasini Shakti Peetha.",
            "places": [
                {"name": "Vindhyavasini Devi Temple Vindhyachal", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "Celebrated Shakti Peetha located on the banks of the Ganga where the goddess is revered as Mahishasuramardini."},
            ]
        },
        {
            "district": "Aligarh", "lat": 27.8974, "lon": 78.0880, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Aligarh Biscuit, Barfi & Mughlai Dishes",
            "description": "City of Locks, home to the historic Aligarh Muslim University (AMU) founded by Sir Syed Ahmad Khan in 1875.",
            "places": [
                {"name": "Aligarh Fort (Baangh-e-Zamir) & AMU Heritage Quad", "category": "Historical", "entry_fee": 0, "opening": "08:30", "closing": "17:30", "description": "16th-century fortress surrounded by deep moats and the grand Indo-Saracenic buildings of Aligarh Muslim University."},
            ]
        },
        {
            "district": "Bareilly", "lat": 28.3670, "lon": 79.4304, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Bareilly Zari Crafts & Seekh Kebabs",
            "description": "Nath Nagari on the Ramganga River, renowned worldwide for Zari-Zardozi embroidery and cane furniture.",
            "places": [
                {"name": "Alakhnath Temple & Bareilly Nath Temples", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Ancient headquarters of the Naga Sanyasi order, part of the seven historic Shiva shrines surrounding Bareilly."},
            ]
        },
        {
            "district": "Saharanpur", "lat": 29.9671, "lon": 77.5510, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Saharanpur Mangoes & Wood Carvings",
            "description": "Wood Carving City on the Shivalik border, celebrated for teakwood artisanal furnishings and Shakumbhari Devi.",
            "places": [
                {"name": "Shakumbhari Devi Temple Shivalik Hills", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Famous 51-Shakti Peetha shrine situated in a mountain torrent valley 40km from Saharanpur in the Shivalik foothills."},
            ]
        },
        {
            "district": "Pilibhit", "lat": 28.6300, "lon": 79.8000, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Pilibhit Flutes (Bansuri) & Rice Dishes",
            "description": "The Flute City of India (Bansuri Nagari), producing 95% of India's bamboo flutes, home to Pilibhit Tiger Reserve.",
            "places": [
                {"name": "Pilibhit Tiger Reserve & Chuka Beach Resort", "category": "Wildlife", "entry_fee": 150, "opening": "06:00", "closing": "17:30", "description": "Terai forest tiger sanctuary on the Sharda Sagar dam reservoir, featuring tree-houses and eco-tourism cottages."},
            ]
        },
        {
            "district": "Jaunpur", "lat": 25.7464, "lon": 82.6837, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Jaunpuri Imarti (GI Tag) & Beni Ram Sweets",
            "description": "Shiraz of the East on the Gomti River, medieval Sharqi sultanate capital famed for Atala Mosque and Shahi Bridge.",
            "places": [
                {"name": "Shahi Bridge (Akbari Bridge - 1568) & Atala Masjid", "category": "Historical", "entry_fee": 0, "opening": "07:00", "closing": "18:30", "description": "16-arch Mughal bridge with pillared shops built by Munim Khan and 1408 Sharqi stone mosque with grand pylons."},
            ]
        },
    ],
}

