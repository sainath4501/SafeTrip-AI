"""
Northern India States Part 2: Himachal Pradesh (12), Jammu & Kashmir (20), Ladakh (2), Punjab (23), Uttarakhand (13).
"""

NORTH_STATES_PART2 = {
    # ==================== 1. HIMACHAL PRADESH (12 Districts) ====================
    "Himachal Pradesh": [
        {
            "district": "Shimla", "lat": 31.1048, "lon": 77.1734, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Himachali Siddu, Chha Gosht, Madra & Kurkuri Jalebi",
            "description": "Queen of the Hills, former British summer capital perched at 2,205m with colonial Tudor heritage and snow peaks.",
            "places": [
                {"name": "The Ridge & Christ Church Shimla", "category": "Heritage", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Iconic neo-Gothic 1857 yellow church on the open pedestrian Ridge offering panoramic Himalayan snowline vistas."},
                {"name": "Jakhoo Hill & 108-Foot Hanuman Statue", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Highest peak in Shimla (2,455m) crowned by a colossal orange statue of Lord Hanuman, accessed via modern ropeway."},
                {"name": "Kalka-Shimla Toy Train (UNESCO World Heritage)", "category": "Heritage", "entry_fee": 250, "opening": "06:00", "closing": "18:00", "description": "1903 narrow-gauge mountain railway traversing 103 tunnels, 864 bridges, and 919 curves through pine forests."},
                {"name": "Viceregal Lodge (Indian Institute of Advanced Study)", "category": "Palace", "entry_fee": 50, "opening": "09:30", "closing": "17:30", "description": "1888 English Renaissance castle built of grey sandstone, site of historic summit talks that led to Indian independence."},
            ]
        },
        {
            "district": "Kullu", "lat": 31.9579, "lon": 77.1095, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Kullu Trout Fish, Siddu, Babru & Apple Cider",
            "description": "Valley of the Gods on the Beas River, gateway to high-altitude adventure sports, Rohtang Pass, and Manali.",
            "places": [
                {"name": "Solang Valley Adventure Arena", "category": "Adventure", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "World-famous adventure bowl offering paragliding, zorbing, quad biking, and winter skiing alongside snow peaks."},
                {"name": "Hadimba Devi Ancient Wooden Temple Manali", "category": "Temple", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "1553 CE four-tiered pagoda-style cedar wood temple built by Raja Bahadur Singh in the heart of Dhungri forest."},
                {"name": "Atal Tunnel (Rohtang) & Sissu Waterfall Gateway", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "World's longest highway tunnel above 10,000 feet (9.02km), opening into the snow-covered glacial wonderland of Lahaul."},
            ]
        },
        {
            "district": "Kangra", "lat": 32.0998, "lon": 76.2691, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Kangri Dham (Khatta, Madra), Momos & Tibetan Thukpa",
            "description": "Spiritual seat of His Holiness the Dalai Lama in Dharamshala, home to the dramatic Kangra Fort and Dhauladhar mountains.",
            "places": [
                {"name": "Tsuglagkhang Complex (Dalai Lama Temple McLeod Ganj)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Spiritual heart of Little Lhasa, housing the residence of the 14th Dalai Lama, meditation halls, and Tibet Museum."},
                {"name": "HPCA Cricket Stadium Dharamshala", "category": "Viewpoint", "entry_fee": 30, "opening": "09:00", "closing": "17:30", "description": "One of the world's most scenic cricket stadiums at 1,457m elevation with snow-clad Dhauladhar peaks directly behind."},
                {"name": "Kangra Fort (Oldest Fort in the Himalayas)", "category": "Fort", "entry_fee": 40, "opening": "09:00", "closing": "18:00", "description": "Ancient 4th-century BCE Katoch dynasty cliff fortress perched at the confluence of the Banganga and Majhi rivers."},
            ]
        },
        {
            "district": "Lahaul and Spiti", "lat": 32.5535, "lon": 77.0125, "crime_index": 8.0, "safety_tier": "LOW",
            "food": "Spiti Buckwheat Pancakes, Butter Tea, Thukpa & Tsampa",
            "description": "High-altitude Himalayan cold desert, renowned for cliffside 1,000-year-old Buddhist monasteries and fossil villages.",
            "places": [
                {"name": "Key Monastery (Kye Gompa)", "category": "Spiritual", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "11th-century Tibetan fortress monastery perched at 4,166m above the Spiti River, holding ancient murals and thangkas."},
                {"name": "Chandratal Lake (Lake of the Moon - 4,300m)", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Crescent-shaped sapphire glacial lake in the Samudra Tapu plateau, surrounded by scree cliffs and high peaks."},
                {"name": "Dhankar Monastery & Fort", "category": "Historical", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Spectacular cliffside monastery precariously balanced atop a 300m high pinnacle overlooking the Spiti and Pin rivers."},
            ]
        },
        {
            "district": "Chamba", "lat": 32.5534, "lon": 76.1258, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Chamba Chukh (Spicy Chili Paste), Madra & Chamba Rumal (GI)",
            "description": "Princely valley on the Ravi River, famous for the mini-Switzerland of India Khajjiar and ancient temples.",
            "places": [
                {"name": "Khajjiar (Mini Switzerland of India)", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Rolling saucer-shaped green meadow at 1,920m surrounded by dense deodar pine forests and a central floating island lake."},
                {"name": "Dalhousie Colonial Hill Station & Panchpula", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "1854 British summer retreat spread over five hills, featuring Subhash Baoli, St. John's Church, and waterfalls."},
                {"name": "Laxmi Narayan 10th-Century Temple Complex", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "Six classical stone shikhara temples built by Sahil Varman, with wooden chhatris protecting white stone spires."},
            ]
        },
        {
            "district": "Kinnaur", "lat": 31.6510, "lon": 78.4752, "crime_index": 10.0, "safety_tier": "LOW",
            "food": "Kinnauri Golden Apples, Chilgoza (Pine Nuts) & Ogla Wine",
            "description": "Land of Fairy Tales on the Indo-Tibetan border, dominated by the sacred 6,050m Kinner Kailash peak.",
            "places": [
                {"name": "Sangla Valley & Kamru Fort", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Serene valley on the Baspa River featuring the wooden Kamru tower fort housing a revered idol of Goddess Kamakhya."},
                {"name": "Chitkul (Last Inhabited Indian Village on Indo-Tibet Border)", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Charming wooden village at 3,450m elevation beside the roaring crystal-clear Baspa River with zero crime rate."},
            ]
        },
        {
            "district": "Mandi", "lat": 31.7087, "lon": 76.9320, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Sepu Badi, Kachori & Mandi Dham",
            "description": "Varanasi of the Hills on the Beas River, holding 81 historic stone temples and the mystical floating reed lake Prashar.",
            "places": [
                {"name": "Prashar Lake & 13th-Century Pagoda Temple", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Deep blue circular alpine lake at 2,730m with a mysterious floating island that moves across the seasons."},
                {"name": "Rewalsar Sacred Lake (Lotus Lake - Tso Pema)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Holy lake venerated by Buddhists (Padmasambhava), Sikhs (Guru Gobind Singh), and Hindus (Rishi Lomas)."},
            ]
        },
        {
            "district": "Solan", "lat": 30.9045, "lon": 77.0967, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Mushroom Delicacies & Kasauli Bun Samosa",
            "description": "Mushroom City of India, home to the quiet colonial hill station of Kasauli and Mohan Shakti heritage park.",
            "places": [
                {"name": "Kasauli Heritage Hill Station & Gilbert Trail", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "19:30", "description": "Pristine cantt town at 1,900m with 1853 Christ Church, Monkey Point, and cliff-edge birdwatching trails."},
                {"name": "Mohan Shakti National Heritage Park", "category": "Heritage", "entry_fee": 30, "opening": "09:00", "closing": "17:30", "description": "Grand Vedic spiritual park nestled in the Giri River valley with life-size marble statues of rishis and deities."},
            ]
        },
        {
            "district": "Bilaspur", "lat": 31.3260, "lon": 76.7597, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Bilaspuri Makki Roti & Sarson Saag",
            "description": "Located on the banks of Govind Sagar lake, renowned for Asia's second-highest concrete gravity dam Bhakra.",
            "places": [
                {"name": "Bhakra Dam & Gobind Sagar Lake", "category": "Nature", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "Colossal 226-meter concrete gravity dam across the Sutlej River, creating India's third-largest water reservoir."},
            ]
        },
        {
            "district": "Sirmaur", "lat": 30.5599, "lon": 77.2961, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Sirmauri Patande (Himachali Pancakes) & Siddu",
            "description": "Southernmost district bordering Uttarakhand, home to Renuka Lake shaped like a reclining goddess.",
            "places": [
                {"name": "Renuka Lake & Wildlife Sanctuary (Largest Natural Lake in HP)", "category": "Lake", "entry_fee": 20, "opening": "07:00", "closing": "18:00", "description": "Sacred Ramsar freshwater lake naturally contoured like a sleeping woman, with lion safari and boat rides."},
            ]
        },
        {
            "district": "Hamirpur", "lat": 31.6862, "lon": 76.5213, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Hamirpur Dham & Makki Roti",
            "description": "Most literate district in Himachal Pradesh, famous for the cave shrine of Baba Balak Nath at Deotsidh.",
            "places": [
                {"name": "Baba Balak Nath Cave Temple Deotsidh", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Ancient natural cliff-cave shrine dedicated to immortal child-yogi Baba Balak Nath on the Dhaulagiri hill."},
            ]
        },
        {
            "district": "Una", "lat": 31.4685, "lon": 76.2708, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Una Chole & Sweet Peda",
            "description": "Gateway to Himachal Pradesh from Punjab, celebrated for the revered Shakti Peetha temple of Chintpurni.",
            "places": [
                {"name": "Maa Chintpurni Temple (Chhinnamastika Shakti Peetha)", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "One of the 51 holy Shakti Peethas, where devotees pray to Maa Chintpurni for alleviation of all worries."},
            ]
        },
    ],

    # ==================== 2. JAMMU AND KASHMIR (20 Districts) ====================
    "Jammu and Kashmir": [
        {
            "district": "Srinagar", "lat": 34.0837, "lon": 74.7973, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Kashmiri Wazwan (Rogan Josh, Gustaba, Rista), Kahwa & Noon Chai",
            "description": "Summer Capital of Jammu & Kashmir and Paradise on Earth, famed for Dal Lake houseboats and Mughal gardens.",
            "places": [
                {"name": "Dal Lake & Shikara Boat Cruises", "category": "Lake", "entry_fee": 500, "opening": "06:00", "closing": "21:00", "description": "The jewel of Kashmir: 18-sq-km lake with floating vegetable markets, carved wooden cedar houseboats, and lotus channels."},
                {"name": "Mughal Gardens (Shalimar Bagh & Nishat Bagh)", "category": "Nature", "entry_fee": 25, "opening": "09:00", "closing": "19:00", "description": "1619 CE terraced royal gardens built by Emperor Jahangir for Empress Nur Jahan, with cascading fountains and chinar trees."},
                {"name": "Shankaracharya Hilltop Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Ancient 9th-century stone Shiva temple atop a 1,000-foot hillock with 243 steps offering sweeping views of Srinagar."},
                {"name": "Indira Gandhi Memorial Tulip Garden (Asia's Largest)", "category": "Nature", "entry_fee": 60, "opening": "09:00", "closing": "18:00", "description": "30-acre terraced floral paradise on the foothills of the Zabarwan range with 1.5 million blooming tulips in spring."},
            ]
        },
        {
            "district": "Jammu", "lat": 32.7266, "lon": 74.8570, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Jammu Rajma Chawal, Kaladi Kulcha & Chocolate Barfi",
            "description": "Winter Capital of J&K and City of Temples on the Tawi River, dominated by the Bahu Fort and Raghunath Temple.",
            "places": [
                {"name": "Bahu Fort & Bagh-e-Bahu Terraced Garden", "category": "Fort", "entry_fee": 20, "opening": "06:00", "closing": "20:00", "description": "3,000-year-old historic stone fort overlooking the Tawi River, housing the revered Bawe Wali Mata Kali temple."},
                {"name": "Raghunath Temple Complex", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "One of the largest temple complexes in North India built by Maharaja Gulab Singh in 1860 with gold-leaf sanctums."},
            ]
        },
        {
            "district": "Baramulla", "lat": 34.2090, "lon": 74.3436, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Kahwa, Kashmiri Nadru Yakhni & Pulao",
            "description": "Home to the world-famous ski resort of Gulmarg, high-altitude meadows, and the Apharwat Gondola.",
            "places": [
                {"name": "Gulmarg Ski Resort & Apharwat Peak Gondola (14,000ft)", "category": "Adventure", "entry_fee": 800, "opening": "09:00", "closing": "17:00", "description": "Asia's premier winter sports paradise and highest operating cable car in the world ascending to 3,980m snowfields."},
            ]
        },
        {
            "district": "Anantnag", "lat": 33.7311, "lon": 75.1487, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Kashmiri Trout, Kahwa & Girda Bread",
            "description": "Commercial capital of South Kashmir on the Jhelum River, portal to Pahalgam and the holy Amarnath Cave.",
            "places": [
                {"name": "Pahalgam (Valley of Shepherds) & Betaab Valley", "category": "Hill Station", "entry_fee": 50, "opening": "07:00", "closing": "18:30", "description": "Picturesque mountain meadow along the crystal Lidder River, surrounded by pine forests and snow-capped peaks."},
                {"name": "Martand Sun Temple Ruins (8th Century CE)", "category": "Historical", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Colossal limestone colonnaded sun temple built by King Lalitaditya Muktapida, blending Greek and Kashmiri architecture."},
            ]
        },
        {
            "district": "Reasi", "lat": 33.0827, "lon": 74.8322, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Katra Vegetarian Thali, Dry Fruits & Apple Halwa",
            "description": "Spiritual destination in the Trikuta Mountains, base for millions of pilgrims visiting Shri Mata Vaishno Devi.",
            "places": [
                {"name": "Shri Mata Vaishno Devi Shrine Trikuta Hills", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "23:00", "description": "Holistic cave shrine located at 5,200ft, venerated by millions who undertake the 13km trek from Katra."},
                {"name": "Chenab Rail Bridge (World's Highest Railway Arch Bridge)", "category": "Heritage", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Engineering marvel 359 meters above the Chenab Riverbed (35m higher than the Eiffel Tower)."},
            ]
        },
        {
            "district": "Ganderbal", "lat": 34.2268, "lon": 74.7818, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Kahwa, Walnut Fudge & Kashmiri Harissa",
            "description": "Known as the Meadow of Gold, gateway to Sonamarg, the Sindh River, and Thajiwas glacier.",
            "places": [
                {"name": "Sonamarg (Meadow of Gold) & Thajiwas Glacier", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Spectacular alpine meadow at 2,740m on the Sindh River, portal to pony rides across ancient turquoise glaciers."},
                {"name": "Kheer Bhawani Temple (Tulmulla)", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Sacred spring shrine dedicated to Goddess Ragnya Devi, where the natural water color changes to predict future events."},
            ]
        },
        # Remaining J&K Districts (Bandipora, Budgam, Doda, Kathua, Kishtwar, Kulgam, Kupwara, Poonch, Pulwama, Rajouri, Ramban, Samba, Shopian, Udhampur)
        {
            "district": "Bandipora", "lat": 34.4225, "lon": 74.6500, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Wular Lake Fish & Lotus Stems (Nadru)",
            "description": "Home to Wular Lake, one of the largest freshwater lakes in Asia, and gateway to Gurez Valley.",
            "places": [
                {"name": "Wular Lake (Asia's Largest Natural Freshwater Lake)", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Expansive 189-sq-km wetland fed by the Jhelum River, renowned for water chestnut farming and birdlife."},
            ]
        },
        {
            "district": "Budgam", "lat": 34.0200, "lon": 74.7200, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Kashmiri Poha & Rogan Josh",
            "description": "Central valley district home to Doodhpathri (Valley of Milk) and the shrine of Sheikh Noor-ud-Din Wali.",
            "places": [
                {"name": "Doodhpathri (Valley of Milk) Mountain Meadow", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Lush grassy alpine bowl where the Shaliganga River cascades over pebbles creating frothy white milk-like waters."},
            ]
        },
        {
            "district": "Doda", "lat": 33.1458, "lon": 75.5458, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Bhaderwah Rajma Chawal & Walnut Delicacies",
            "description": "Mountainous Chenab valley district known as 'Chhota Kashmir' in Bhaderwah, famous for alpine meadows.",
            "places": [
                {"name": "Bhaderwah Valley (Chhota Kashmir)", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Picturesque hill valley at 1,600m with pine forests, Jai Valley meadow, and ancient Vasuki Nag temples."},
            ]
        },
        {
            "district": "Kathua", "lat": 32.3711, "lon": 75.5200, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Basohli Painting Heritage & Jammu Rajma",
            "description": "Gateway to Jammu & Kashmir, famous for miniature Basohli paintings and the massive Ranjit Sagar Dam.",
            "places": [
                {"name": "Ranjit Sagar Dam & Basohli Miniature Art Heritage", "category": "Lake", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Huge hydroelectric reservoir on the Ravi River, home to the Atal Setu cable-stayed bridge and Basohli art schools."},
            ]
        },
        {
            "district": "Kishtwar", "lat": 33.3100, "lon": 75.7700, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Kishtwari Saffron & Morel Mushrooms (Gucchi)",
            "description": "Land of Saffron, Sapphire, and Shraddha, surrounded by snow peaks and Kishtwar High Altitude National Park.",
            "places": [
                {"name": "Kishtwar National Park & Chowgan Ground", "category": "Wildlife", "entry_fee": 50, "opening": "07:00", "closing": "17:00", "description": "High-altitude wilderness sheltering snow leopards, Himalayan brown bears, and musk deer amidst cedar peaks."},
            ]
        },
        {
            "district": "Kulgam", "lat": 33.6450, "lon": 75.0200, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kashmiri Wazwan & Red Apples",
            "description": "The Rice Bowl of Kashmir on the Veshaw River, home to the cascading Aharbal Waterfalls.",
            "places": [
                {"name": "Aharbal Waterfalls (Niagara of Kashmir)", "category": "Waterfall", "entry_fee": 20, "opening": "08:00", "closing": "18:00", "description": "Spectacular 25-meter plunge where the Veshaw River crashes into a narrow granite gorge surrounded by fir forests."},
            ]
        },
        {
            "district": "Kupwara", "lat": 34.5300, "lon": 74.2500, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Lolab Walnut Breads & Kashmiri Tea",
            "description": "Frontier district blessed with the oval green Lolab Valley, pine ridges, and freshwater springs.",
            "places": [
                {"name": "Lolab Valley (Fruit Bowl of Kashmir)", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "25km long emerald valley dotted with walnut orchards, apple groves, and wooden village bridges."},
            ]
        },
        {
            "district": "Poonch", "lat": 33.7700, "lon": 74.1000, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Poonchi Halwa & Kashmiri Food",
            "description": "Historical border principality in the Pir Panjal ranges, holding medieval forts and the Peer Ki Gali pass.",
            "places": [
                {"name": "Poonch Fort & Noori Chamb Waterfall", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "16th-century fortress built by Raja Rustam Khan and scenic waterfall named after Mughal Empress Nur Jahan."},
            ]
        },
        {
            "district": "Pulwama", "lat": 33.8700, "lon": 74.8900, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Pampore Saffron Tea & Kashmiri Apples",
            "description": "Saffron Bowl of Kashmir, world-famous for the purple saffron fields of Pampore and ancient Avantipur ruins.",
            "places": [
                {"name": "Pampore Saffron Fields & Avantiswami Temple Ruins", "category": "Historical", "entry_fee": 25, "opening": "08:00", "closing": "18:00", "description": "Vast purple saffron crocus fields and 9th-century Avantivarman stone-carved temple dedicated to Vishnu."},
            ]
        },
        {
            "district": "Rajouri", "lat": 33.3800, "lon": 74.3000, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kalari Cheese & Rajouri Makki Roti",
            "description": "Historical valley between the Chenab and Pir Panjal, home to Mughal heritage serais along the Imperial Road.",
            "places": [
                {"name": "Chingus Sarai Mughal Waystation", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "16th-century royal resting inn where the entrails of Mughal Emperor Jahangir were buried in 1627."},
            ]
        },
        {
            "district": "Ramban", "lat": 33.2400, "lon": 75.2400, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Sanasar Trout & Dogri Food",
            "description": "Central Chenab valley district on the Jammu-Srinagar highway, home to the aerodrome meadow of Sanasar.",
            "places": [
                {"name": "Sanasar Eco Adventure Meadow", "category": "Adventure", "entry_fee": 0, "opening": "07:00", "closing": "18:30", "description": "Cup-shaped alpine meadow at 2,050m offering paragliding, hot air ballooning, and 9-hole golf course."},
            ]
        },
        {
            "district": "Samba", "lat": 32.5600, "lon": 75.1200, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Dogra Rajma Chawal & Barfi",
            "description": "Industrial and border bastion known as the Land of Warriors, famed for calico hand-printing.",
            "places": [
                {"name": "Mansar Lake & Wildlife Sanctuary", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Sacred 1-mile forest lake surrounded by mango groves, sheltering thousands of softshell turtles and carps."},
            ]
        },
        {
            "district": "Shopian", "lat": 33.7200, "lon": 74.8300, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Shopian Crisp Red Delicious Apples",
            "description": "Apple Bowl of Kashmir, historical gateway on the Mughal Road crossing through the Pir Panjal.",
            "places": [
                {"name": "Peer Ki Gali Pass (Mughal Road - 3,485m)", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "High mountain pass on the historic Mughal imperial route with alpine meadows and shrine of saint Sheikh Ahmed Karim."},
            ]
        },
        {
            "district": "Udhampur", "lat": 32.9200, "lon": 75.1400, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Kud Patisa (Soan Papdi) & Kaladi Kulcha",
            "description": "Northern Army Command headquarters, home to the scenic hill meadow of Patnitop and ancient Krimchi temples.",
            "places": [
                {"name": "Patnitop Hill Meadow & Skyview Ropeway", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Scenic plateau at 2,024m surrounded by thick deodar forests, connected by India's longest passenger ropeway at Chenani."},
                {"name": "Krimchi 9th-Century Pandava Temples", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Complex of seven classical stone shikhara temples built by Greek-influenced medieval rulers."},
            ]
        },
    ],

    # ==================== 3. LADAKH (2 Districts) ====================
    "Ladakh": [
        {
            "district": "Leh", "lat": 34.1526, "lon": 77.5771, "crime_index": 8.0, "safety_tier": "LOW",
            "food": "Ladakhi Thukpa, Tingmo, Skyu, Butter Tea & Apricot Jam",
            "description": "Land of High Passes, high-altitude desert kingdom at 3,500m famed for Pangong Tso, Nubra Valley, and monasteries.",
            "places": [
                {"name": "Pangong Tso High-Altitude Saltwater Lake (14,270ft)", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "134-km endorheic lake changing shades from turquoise to deep indigo, crossing the international border into Tibet."},
                {"name": "Nubra Valley & Hunder Double-Humped Bactrian Camels", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Valley of Flowers reached via Khardung La (17,982ft), featuring silver sand dunes and shaggy Bactrian camels."},
                {"name": "Thiksey Monastery (Mini Potala Palace)", "category": "Spiritual", "entry_fee": 30, "opening": "06:30", "closing": "18:30", "description": "12-storey whitewashed Gelugpa monastery complex crowned by a two-storey 49-foot statue of Maitreya Buddha."},
                {"name": "Leh Royal Palace & Shanti Stupa", "category": "Palace", "entry_fee": 25, "opening": "08:00", "closing": "18:30", "description": "17th-century 9-storey stone palace built by King Sengge Namgyal and white Japanese Peace Pagoda."},
            ]
        },
        {
            "district": "Kargil", "lat": 34.5539, "lon": 76.1349, "crime_index": 9.0, "safety_tier": "LOW",
            "food": "Kargil Dried Apricots, Tsampa & Butter Tea",
            "description": "Historic trade transit on the Suru River between Srinagar and Leh, home to the Dras War Memorial and Nun-Kun peaks.",
            "places": [
                {"name": "Kargil War Memorial (Dras - 2nd Coldest Inhabited Place)", "category": "Historical", "entry_fee": 0, "opening": "09:00", "closing": "18:00", "description": "Pink sandstone war memorial built by the Indian Army at the base of Tololing and Tiger Hill, honoring 1999 martyrs."},
                {"name": "Suru Valley & Nun-Kun Twin Mountain Peaks", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Breathtaking green valley with glacier-fed streams framed by the 7,135m twin massif of Nun and Kun peaks."},
            ]
        },
    ],

    # ==================== 4. PUNJAB (23 Districts) ====================
    "Punjab": [
        {
            "district": "Amritsar", "lat": 31.6340, "lon": 74.8723, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Amritsari Kulcha with Chole, Makki Di Roti, Dal Makhani & Lassi",
            "description": "Spiritual and cultural capital of Sikhism, home to the celestial Golden Temple and the patriotic Wagah Border.",
            "places": [
                {"name": "Sri Harmandir Sahib (Golden Temple - Holiest Sikh Shrine)", "category": "Spiritual", "entry_fee": 0, "opening": "03:00", "closing": "23:00", "description": "Gold-leaf gilded spiritual sanctuary situated in the Amrit Sarovar, operating the world's largest community kitchen (Langar)."},
                {"name": "Attari-Wagah Border Beating Retreat Ceremony", "category": "Heritage", "entry_fee": 0, "opening": "15:30", "closing": "18:30", "description": "Electrifying daily military flag-lowering drill conducted by the BSF and Pakistan Rangers with thousands of cheering spectators."},
                {"name": "Jallianwala Bagh National Memorial", "category": "Historical", "entry_fee": 0, "opening": "06:30", "closing": "19:30", "description": "Historic national monument commemorating the peaceful independence martyrs of the tragic 1919 massacre."},
            ]
        },
        {
            "district": "Ludhiana", "lat": 30.9010, "lon": 75.8573, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Ludhiana Tandoori Chicken, Butter Naan & Kulfi",
            "description": "The Manchester of India on the Sutlej River, premier manufacturing and textile powerhouse of Punjab.",
            "places": [
                {"name": "Punjab Agricultural University Museum (Rural Life)", "category": "Museum", "entry_fee": 20, "opening": "09:00", "closing": "17:00", "description": "Open-air ethnographic museum displaying 18th-century rural Punjabi homes, brass utensils, phulkaris, and farming tools."},
                {"name": "Lodhi Fort & Maharaja Ranjit Singh War Museum", "category": "Fort", "entry_fee": 20, "opening": "09:30", "closing": "17:00", "description": "15th-century Sikandar Lodi fortress and grand military gallery with battle tanks, uniforms, and light shows."},
            ]
        },
        {
            "district": "Jalandhar", "lat": 31.3260, "lon": 75.5762, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Jalandhari Chole Bhature, Sarson Saag & Lassi",
            "description": "World-renowned Sports Goods Manufacturing City, supplying equipment to Olympic games and Cricket World Cups.",
            "places": [
                {"name": "Devi Talab Mandir (Shakti Peetha)", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "200-year-old temple complex situated in a sacred water tank, venue of the 140-year-old Harballabh Sangeet Sammelan."},
                {"name": "Jang-e-Azadi Memorial Kartarpur", "category": "Heritage", "entry_fee": 50, "opening": "10:00", "closing": "18:00", "description": "25-acre national memorial commemorating the supreme sacrifices of Punjabi freedom fighters during the independence struggle."},
            ]
        },
        {
            "district": "Patiala", "lat": 30.3398, "lon": 76.3869, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Patiala Shahi Pulao, Tandoori Delicacies & Patiala Peg",
            "description": "The Royal City of Punjab, world-famous for the Patiala Peg, Phulkari embroidery, and the Qila Mubarak palace.",
            "places": [
                {"name": "Qila Mubarak Palace Complex & Sheesh Mahal", "category": "Palace", "entry_fee": 25, "opening": "09:00", "closing": "17:00", "description": "1763 CE Sikh palace built by Baba Ala Singh with mirror mosaics, royal armory, and the world's largest collection of royal medals."},
            ]
        },
        {
            "district": "Bathinda", "lat": 30.2110, "lon": 74.9455, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Bathinda Sarson Saag, Makki Roti & Malpua",
            "description": "One of the oldest cities in Punjab on the Malwa plateau, home to the 6th-century fortress of Qila Mubarak.",
            "places": [
                {"name": "Qila Mubarak Bathinda (Razia Sultana Fort)", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Massive 1,900-year-old brick fortress where India's first female monarch Razia Sultana was imprisoned in 1240."},
            ]
        },
        {
            "district": "Rupnagar", "lat": 30.9753, "lon": 76.5273, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Ropar Sweet Lassi & Punjabi Thali",
            "description": "Ancient Ropar on the Sutlej River, site of Harappan excavations and portal to holy Anandpur Sahib.",
            "places": [
                {"name": "Takht Sri Kesgarh Sahib (Birthplace of the Khalsa - Anandpur Sahib)", "category": "Spiritual", "entry_fee": 0, "opening": "04:00", "closing": "22:00", "description": "One of the five holy Takhts in Sikhism, where Guru Gobind Singh Ji established the Khalsa Panth in 1699 on Baisakhi."},
                {"name": "Virasat-e-Khalsa (Museum of Sikh Heritage)", "category": "Museum", "entry_fee": 0, "opening": "09:30", "closing": "16:30", "description": "Award-winning Moshe Safdie architectural masterpiece narrating 500 years of Sikh history with immersive audio-visual exhibits."},
            ]
        },
        # All other Punjab Districts (Barnala, Faridkot, Fatehgarh Sahib, Fazilka, Firozpur, Gurdaspur, Hoshiarpur, Kapurthala, Malerkotla, Mansa, Moga, Muktsar, Pathankot, SAS Nagar, SBS Nagar, Sangrur, Tarn Taran)
        {
            "district": "Fatehgarh Sahib", "lat": 30.6480, "lon": 76.3880, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Langar Prasadam & Punjabi Thali",
            "description": "Sacred Sikh pilgrimage town where the two younger sons of Guru Gobind Singh were bricked alive in 1704.",
            "places": [
                {"name": "Gurudwara Fatehgarh Sahib & Bhora Sahib", "category": "Spiritual", "entry_fee": 0, "opening": "04:00", "closing": "22:00", "description": "Revered shrine marking the martyrdom of Sahibzada Zorawar Singh and Sahibzada Fateh Singh, with gold-inlaid architecture."},
            ]
        },
        {
            "district": "Kapurthala", "lat": 31.3800, "lon": 75.3800, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Royal Patiala-Kapurthala Cuisine & Sweets",
            "description": "The Paris of Punjab, princely city celebrated for French Renaissance architecture built by Maharaja Jagatjit Singh.",
            "places": [
                {"name": "Jagatjit Palace (Inspired by Versailles) & Moorish Mosque", "category": "Palace", "entry_fee": 20, "opening": "09:00", "closing": "17:00", "description": "1908 French-style palace modeled on the Palace of Versailles and the 1930 Moroccan-styled Moorish Mosque."},
            ]
        },
        {
            "district": "Hoshiarpur", "lat": 31.5300, "lon": 75.9200, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Hoshiarpur Mangoes & Wooden Inlay Crafts",
            "description": "City of Mangoes at the Shivalik foothills, world-renowned for wooden inlay furniture and citrus groves.",
            "places": [
                {"name": "Sheesh Mahal & Dholbaha Archaeological Valley", "category": "Historical", "entry_fee": 0, "opening": "09:00", "closing": "17:30", "description": "Historic glass palace and prehistoric valley excavations dating back to the Pleistocene era in the Shivalik hills."},
            ]
        },
        {
            "district": "Gurdaspur", "lat": 32.0400, "lon": 75.4000, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Gurdaspuri Peda & Amritsari Kulcha",
            "description": "Historic border district on the Ravi and Beas rivers, where Akbar was crowned King of India in 1556.",
            "places": [
                {"name": "Takht-e-Akbari Kalanaur (Coronation Platform of Akbar)", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Brick coronation platform where the 13-year-old Mughal prince Akbar was crowned Emperor of India in 1556."},
            ]
        },
        {
            "district": "Pathankot", "lat": 32.2700, "lon": 75.6500, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Pathankot Peda & Dogra-Punjabi Food",
            "description": "Meeting point of Punjab, Himachal, and J&K, gateway to the Himalayas on the Chakki River.",
            "places": [
                {"name": "Shahpurkandi Fort & Ranjit Sagar Dam", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "16th-century fortress on the banks of the Ravi River with panoramic views of Jammu hills and Sutlej canals."},
            ]
        },
        {
            "district": "Tarn Taran", "lat": 31.4500, "lon": 74.9300, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Tarn Taran Kulcha & Lassi",
            "description": "Holy city established by Guru Arjan Dev Ji, holding the largest sarovar (water tank) of all Sikh shrines.",
            "places": [
                {"name": "Gurudwara Sri Tarn Taran Sahib", "category": "Spiritual", "entry_fee": 0, "opening": "04:00", "closing": "22:00", "description": "Majestic golden-domed Gurudwara founded in 1590 CE, featuring the world's largest rectangular sacred sarovar."},
            ]
        },
        {
            "district": "Firozpur", "lat": 30.9200, "lon": 74.6100, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Hussainiwala Border Sweets & Punjabi Food",
            "description": "Historic border town on the Sutlej, home to the National Martyrs Memorial at Hussainiwala.",
            "places": [
                {"name": "National Martyrs Memorial Hussainiwala", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:30", "description": "Sacred cremation ground of Bhagat Singh, Rajguru, and Sukhdev, featuring an evening joint border retreat ceremony."},
            ]
        },
        {
            "district": "Fazilka", "lat": 30.4000, "lon": 74.0300, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Fazilka Toba Tek Singh Sweets & Dal",
            "description": "Known as the City of Bridges, rich in Sufi shrines and the border retreat ceremony at Sadqi.",
            "places": [
                {"name": "Sadqi Joint Check Post (Indo-Pak Border Ceremony)", "category": "Cultural", "entry_fee": 0, "opening": "16:00", "closing": "18:30", "description": "Patriotic joint flag-lowering parade between BSF and Pakistan Rangers on the Fazilka-Okara international border."},
            ]
        },
        {
            "district": "Faridkot", "lat": 30.6700, "lon": 74.7500, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Faridkot Milk Cake & Punjabi Dishes",
            "description": "Named after 12th-century Sufi saint Baba Farid, royal princely capital holding Qila Mubarak.",
            "places": [
                {"name": "Qila Mubarak Faridkot & Raj Mahal", "category": "Fort", "entry_fee": 0, "opening": "09:00", "closing": "17:30", "description": "700-year-old royal fortress featuring the Sheesh Mahal painted with European motifs and Baba Farid's hermitage."},
            ]
        },
        {
            "district": "Moga", "lat": 30.8200, "lon": 75.1700, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Nestle Milk Sweets & Sarson Saag",
            "description": "Hub of agricultural machinery and dairy, birthplace of freedom fighter Lala Lajpat Rai.",
            "places": [
                {"name": "Lala Lajpat Rai Memorial Dhudike", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Memorial library and heritage village museum commemorating the Lion of Punjab, Lala Lajpat Rai."},
            ]
        },
        {
            "district": "Muktsar", "lat": 30.4800, "lon": 74.5200, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Muktsari Jutti Crafts & Punjabi Khichdi",
            "description": "Historic city of the 40 Liberated Ones (Chali Mukte), celebrated for the grand Maghi Mela festival.",
            "places": [
                {"name": "Gurudwara Sri Tuti Gandi Sahib Muktsar", "category": "Spiritual", "entry_fee": 0, "opening": "04:30", "closing": "21:30", "description": "Historic shrine commemorating the 1705 Battle of Muktsar where Guru Gobind Singh forgave the 40 martyred disciples."},
            ]
        },
        {
            "district": "Mansa", "lat": 29.9800, "lon": 75.3800, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Malwa Punjabi Thali & Lassi",
            "description": "Area of White Gold (cotton) in southern Malwa, rich in folklore and Harappan excavation mounds.",
            "places": [
                {"name": "Sardulgarh Fort & Budhlada Harappan Mounds", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Historic brick fortress on the Ghaggar River and ancient Indus Valley trade settlements."},
            ]
        },
        {
            "district": "Barnala", "lat": 30.3800, "lon": 75.5400, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Barnala Sweets & Punjabi Kadhi",
            "description": "Historic seat of the Phulkian dynasty founded by Baba Ala Singh before establishing Patiala.",
            "places": [
                {"name": "Qila Mubarak Barnala", "category": "Historical", "entry_fee": 0, "opening": "09:00", "closing": "17:30", "description": "1722 CE ancient brick citadel constructed by Baba Ala Singh, founder of the Patiala princely state."},
            ]
        },
        {
            "district": "Sangrur", "lat": 30.2500, "lon": 75.8400, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Sangrur Kulfi & Sarson Saag",
            "description": "Former capital of the princely state of Jind, renowned for the heritage Banasar Garden marble pavilion.",
            "places": [
                {"name": "Banasar Garden & Marble Baradari", "category": "Heritage", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Princely walled garden featuring an artificial lake with a white marble pleasure pavilion in the center."},
            ]
        },
        {
            "district": "Malerkotla", "lat": 30.5200, "lon": 75.8800, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Malerkotla Biryani, Halwa & Sheermal",
            "description": "Only Muslim-majority princely state in East Punjab, blessed by Guru Gobind Singh for opposing the execution of his sons.",
            "places": [
                {"name": "Mubarak Manzil Palace & Dargah Haider Sheikh", "category": "Palace", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "19th-century royal palace of the Nawabs of Malerkotla and 15th-century Sufi pilgrimage shrine."},
            ]
        },
        {
            "district": "Sahibzada Ajit Singh Nagar", "lat": 30.7046, "lon": 76.7179, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Mohali Cyber Cafes, Butter Chicken & Lassi",
            "description": "Commercial IT and cricket hub adjoining Chandigarh, home to the PCA Mohali International Cricket Stadium.",
            "places": [
                {"name": "Fateh Burj (Tallest Victory Minar in India - 328ft)", "category": "Historical", "entry_fee": 20, "opening": "09:00", "closing": "18:00", "description": "100-meter triumphal victory tower commemorating the 1710 Battle of Chappar Chiri fought by Baba Banda Singh Bahadur."},
            ]
        },
        {
            "district": "Shahid Bhagat Singh Nagar", "lat": 31.1200, "lon": 76.1200, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Khatkar Kalan Sweets & Makki Roti",
            "description": "Ancestral homeland of legendary freedom fighter Shaheed-e-Azam Bhagat Singh in Nawanshahr.",
            "places": [
                {"name": "Shaheed Bhagat Singh Memorial & Ancestral Home Khatkar Kalan", "category": "Museum", "entry_fee": 10, "opening": "09:00", "closing": "17:00", "description": "National memorial preserving the ancestral home, pen, blood-stained soil, and personal diary of Bhagat Singh."},
            ]
        },
    ],

    # ==================== 5. UTTARAKHAND (13 Districts) ====================
    "Uttarakhand": [
        {
            "district": "Dehradun", "lat": 30.3165, "lon": 78.0322, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Garhwali Kafuli, Rus, Bal Mithai & Sticky Rice",
            "description": "Capital of Uttarakhand in the Doon Valley, gateway to the Queen of Hills Mussoorie and Yoga Capital Rishikesh.",
            "places": [
                {"name": "Mussoorie Hill Station & Kempty Falls", "category": "Hill Station", "entry_fee": 50, "opening": "06:00", "closing": "19:00", "description": "Queen of the Hills at 2,000m with Camel's Back Road, Mall Road, and cascading waterfalls."},
                {"name": "Robber's Cave (Guchhupani Gorge)", "category": "Nature", "entry_fee": 35, "opening": "07:00", "closing": "18:30", "description": "Natural limestone cave gorge where an icy stream flows through narrow rock fissures, disappearing underground."},
                {"name": "Forest Research Institute (FRI World Heritage Campus)", "category": "Heritage", "entry_fee": 50, "opening": "09:00", "closing": "17:30", "description": "Colossal 1929 Greco-Roman and colonial brick architecture campus spanning 450 hectares with six forestry museums."},
            ]
        },
        {
            "district": "Haridwar", "lat": 29.9457, "lon": 78.1642, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Haridwar Aloo Puri, Mathura Peda, Rabri & Jalebi",
            "description": "Gateway to the Gods, ancient sacred city where the holy Ganga enters the Indo-Gangetic Plains from the Himalayas.",
            "places": [
                {"name": "Har Ki Pauri & Evening Ganga Aarti", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "Sacred riverfront ghat where thousands float illuminated diya lamps on the emerald Ganga amidst thunderous evening chants."},
                {"name": "Mansa Devi & Chandi Devi Hilltop Ropeway Temples", "category": "Temple", "entry_fee": 150, "opening": "06:00", "closing": "19:00", "description": "Twin Shakti shrines atop Bilwa and Neel Parvat hills, offering sweeping views of Haridwar and the Ganga canal."},
            ]
        },
        {
            "district": "Nainital", "lat": 29.3803, "lon": 79.4636, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Kumaoni Baadi, Singori & Bal Mithai",
            "description": "City of Lakes in Kumaon nestled around emerald Naini Lake, surrounded by seven lush Himalayan peaks.",
            "places": [
                {"name": "Naini Lake & Naina Devi Temple", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Eye-shaped alpine lake at 1,938m elevation with colourful yachting, pedal boats, and 51-Shakti Peetha shrine on the northern shore."},
                {"name": "Snow View Point & Nainital Aerial Ropeway", "category": "Viewpoint", "entry_fee": 300, "opening": "09:00", "closing": "17:00", "description": "Cable car ascent to 2,270m offering breath-taking panoramas of snow-capped Nanda Devi, Trishul, and Nanda Kot."},
                {"name": "Jim Corbett National Park (Oldest National Park in India)", "category": "Wildlife", "entry_fee": 200, "opening": "06:00", "closing": "17:30", "description": "Established in 1936 along the Ramganga River, world-famous for Royal Bengal tigers, wild elephants, and sal forests."},
            ]
        },
        {
            "district": "Chamoli", "lat": 30.4150, "lon": 79.3242, "crime_index": 10.0, "safety_tier": "LOW",
            "food": "Garhwali Bhatt Ki Churkani & Mandua Roti",
            "description": "Abode of Gods home to the sacred Badrinath Char Dham temple, Valley of Flowers, and Hemkund Sahib.",
            "places": [
                {"name": "Badrinath Temple (Supreme Char Dham Shrine)", "category": "Temple", "entry_fee": 0, "opening": "04:30", "closing": "21:00", "description": "Sacred 9th-century temple of Lord Vishnu situated at 3,133m on the Alaknanda River between Nar and Narayana mountain ranges."},
                {"name": "Valley of Flowers National Park (UNESCO World Heritage)", "category": "Nature", "entry_fee": 150, "opening": "07:00", "closing": "14:00", "description": "High-altitude Himalayan valley carpeted with over 500 species of wild alpine flowers (Blue Poppy, Brahmakamal) in monsoon."},
                {"name": "Auli Skiing Resort & Cable Car (Asia's Longest Ropeway)", "category": "Adventure", "entry_fee": 1000, "opening": "08:00", "closing": "16:30", "description": "Premier winter skiing slopes at 3,050m elevation facing the magnificent 7,816m summit of Nanda Devi."},
            ]
        },
        {
            "district": "Rudraprayag", "lat": 30.2858, "lon": 78.9818, "crime_index": 10.0, "safety_tier": "LOW",
            "food": "Pahaadi Gahat Ki Dal & Jhangora Kheer",
            "description": "Sacred confluence of Mandakini and Alaknanda rivers, portal to the holiest 12-Jyotirlinga temple of Kedarnath.",
            "places": [
                {"name": "Kedarnath Jyotirlinga Temple (3,584m Altitude)", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "20:30", "description": "One of the 12 sacred Jyotirlingas of Shiva, built of grey granite slabs near the Chorabari glacier in the snow peaks."},
                {"name": "Tungnath Temple (Highest Shiva Temple in the World - 3,680m)", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Highest of the Panch Kedar temples, reached by a 4km scenic rhododendron trek from Chopta overlooking Chandrashila peak."},
            ]
        },
        {
            "district": "Uttarkashi", "lat": 30.7268, "lon": 78.4354, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Uttarkashi Til Ke Laddu & Red Rice",
            "description": "Northern Himalayan district on the Bhagirathi River, home to Gangotri, Yamunotri, and Nehru Institute of Mountaineering.",
            "places": [
                {"name": "Gangotri Temple & Gaumukh Glacier Trek", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Sacred seat of Goddess Ganga at 3,100m, from where the 18km trek leads to Gaumukh, the snout of the Gangotri Glacier."},
                {"name": "Yamunotri Temple & Surya Kund Hot Springs", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Source of the sacred Yamuna River at 3,293m, featuring natural thermal sulfur pools where rice is cooked as prasadam."},
            ]
        },
        {
            "district": "Almora", "lat": 29.5971, "lon": 79.6591, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Almora Bal Mithai (GI Tag), Singori & Kumaoni Raita",
            "description": "Cultural capital of Kumaon situated on a horse-saddle ridge, celebrated for 9th-century Katyuri stone temples.",
            "places": [
                {"name": "Jageshwar Dham (Complex of 124 Stone Temples)", "category": "Historical", "entry_fee": 25, "opening": "06:00", "closing": "18:00", "description": "8th-to-12th century cluster of 124 carved stone shikhara temples nestled amidst towering deodar forests on the Jata Ganga."},
                {"name": "Kasai Devi Temple & Crank's Ridge (Van Allen Belt)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Ancient hilltop temple possessing a rare geomagnetic field identical to Stonehenge and Machu Picchu, visited by Swami Vivekananda."},
            ]
        },
        {
            "district": "Pauri Garhwal", "lat": 30.1500, "lon": 78.7800, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Garhwali Mandua Roti & Chaunsa",
            "description": "Scenic hill district overlooking the snow-capped Himalayan ranges, home to Lansdowne cantonment.",
            "places": [
                {"name": "Lansdowne Quiet Pine Hill Station", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "1887 Garhwal Rifles cantonment town at 1,706m with quiet pine trails, Tip-in-Top viewpoint, and Bhulla Lake."},
            ]
        },
        {
            "district": "Tehri Garhwal", "lat": 30.3800, "lon": 78.4800, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Tehri Gahat Ke Parathe & Local Honey",
            "description": "Home to the colossal Tehri Dam, Asia's tallest rock-fill dam, and new floating water-sport resorts.",
            "places": [
                {"name": "Tehri Dam Reservoir & Water Sports Complex", "category": "Adventure", "entry_fee": 50, "opening": "08:30", "closing": "18:00", "description": "Tallest dam in India (260m) on the Bhagirathi River, offering jet-skiing, speed-boating, and floating houseboats."},
            ]
        },
        {
            "district": "Pithoragarh", "lat": 29.5800, "lon": 80.2200, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Kumaoni Bhatia & Madua Halwa",
            "description": "Little Kashmir in the Soar Valley bordering Nepal and Tibet, gateway to Kailash Mansarovar pilgrimage.",
            "places": [
                {"name": "Munsiyari & Panchachuli Five Snow Peaks Viewpoint", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "High-altitude base (2,200m) offering dramatic close-up views of the five legendary peaks of Panchachuli."},
            ]
        },
        {
            "district": "Bageshwar", "lat": 29.8400, "lon": 79.7700, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Bageshwari Sweets & Kumaoni Dishes",
            "description": "Sacred confluence of Saryu and Gomati rivers, gateway to Pindari and Sunderdhunga glaciers.",
            "places": [
                {"name": "Bagnath Temple & Pindari Glacier Gateway", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "20:00", "description": "Ancient 1450 CE stone temple of Shiva where Sage Markandeya worshipped, at the holy Sangam."},
            ]
        },
        {
            "district": "Champawat", "lat": 29.3300, "lon": 80.0900, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Champawat Bal Mithai & Kumaoni Dal",
            "description": "Ancient capital of the Chand dynasty kings, home to Baleshwar stone temple and Mayawati Ashram.",
            "places": [
                {"name": "Baleshwar 12th-Century Carved Stone Temple", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Exquisite South-Indian influenced stone temple complex with delicate carvings constructed by Chand rulers."},
            ]
        },
        {
            "district": "Udham Singh Nagar", "lat": 28.9800, "lon": 79.4000, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Terai Basmati Rice & Punjabi Dhaba Dishes",
            "description": "The Food Bowl of Uttarakhand in the fertile Terai plains, home to Nanakmatta Sahib Gurudwara.",
            "places": [
                {"name": "Nanakmatta Sahib Gurudwara & Dam", "category": "Spiritual", "entry_fee": 0, "opening": "04:00", "closing": "21:30", "description": "Historic Sikh shrine associated with Guru Nanak Dev Ji and Guru Hargobind Ji, set beside a vast boating reservoir."},
            ]
        },
    ],
}

