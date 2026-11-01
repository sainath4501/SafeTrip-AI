"""
South India States Master Districts & Tourist Attractions
Covers all 5 Southern States: Andhra Pradesh (26), Karnataka (31), Kerala (14), Tamil Nadu (38), Telangana (33).
"""

SOUTH_STATES = {
    # ==================== 1. ANDHRA PRADESH (26 Districts) ====================
    "Andhra Pradesh": [
        {
            "district": "Visakhapatnam", "lat": 17.6868, "lon": 83.2185, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Bamboo Chicken, Pulihora & Coastal Fish Curry",
            "description": "City of Destiny, premier port city featuring golden beaches, naval submarine museums, and Eastern Ghats hills.",
            "places": [
                {"name": "Ramakrishna Beach & INS Kurusura Submarine Museum", "category": "Beach", "entry_fee": 40, "opening": "09:00", "closing": "20:30", "description": "South India's historic submarine museum on RK Beach showcasing a decommissioned Soviet-built submarine."},
                {"name": "Kailasagiri Hilltop Park & Ropeway", "category": "Viewpoint", "entry_fee": 50, "opening": "09:00", "closing": "20:00", "description": "Scenic hilltop garden overlooking the Bay of Bengal with giant Shiva-Parvathi statues and cable car."},
                {"name": "Simhachalam Varaha Narasimha Temple", "category": "Temple", "entry_fee": 0, "opening": "07:00", "closing": "19:00", "description": "11th-century medieval Kalinga-style hilltop shrine dedicated to Lord Narasimha, bathed in sandalwood paste."},
                {"name": "Rushikonda Beach & Watersports", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Blue Flag certified beach known for golden sands, windsurfing, speed boating, and swimming."},
            ]
        },
        {
            "district": "Tirupati", "lat": 13.6288, "lon": 79.4192, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Tirupati Laddu Prasadam, Dosa & Filter Coffee",
            "description": "World-famous spiritual pilgrimage capital nestled at the foothills of the sacred Seshachalam Hills.",
            "places": [
                {"name": "Sri Venkateswara Swamy Temple Tirumala", "category": "Temple", "entry_fee": 0, "opening": "04:00", "closing": "23:00", "description": "The world's most visited sacred hilltop temple situated on the seven peaks of Seshachalam hills."},
                {"name": "Chandragiri Fort & Raja Mahal", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "11th-century Vijayanagara royal fortress and palace with sound & light show and archaeology museum."},
                {"name": "Sri Padmavathi Ammavari Temple Tiruchanur", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Holy temple of Goddess Padmavathi, divine consort of Lord Venkateswara, featuring the sacred Padma Sarovaram tank."},
            ]
        },
        {
            "district": "Alluri Sitharama Raju", "lat": 18.3273, "lon": 82.8775, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Araku Arabica Coffee & Bongu Chicken (Bamboo Chicken)",
            "description": "Lush forested Eastern Ghats tribal valley famed for cool climate, coffee plantations, and million-year-old caves.",
            "places": [
                {"name": "Borra Caves", "category": "Nature", "entry_fee": 80, "opening": "10:00", "closing": "17:00", "description": "Spectacular million-year-old limestone karstic caves filled with natural stalactites and stalagmites."},
                {"name": "Araku Valley Coffee Plantations & Tribal Museum", "category": "Museum", "entry_fee": 40, "opening": "09:00", "closing": "18:00", "description": "Scenic hill valley showcasing indigenous tribal lifestyle, organic coffee estates, and handicrafts."},
                {"name": "Katiki Waterfalls", "category": "Waterfall", "entry_fee": 30, "opening": "08:00", "closing": "17:00", "description": "Majestic 50-foot natural waterfall originating from the Gosthani River amidst deep evergreen forests."},
            ]
        },
        {
            "district": "Anakapalli", "lat": 17.6913, "lon": 83.0039, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Anakapalli Jaggery Sweets & Andhra Thali",
            "description": "Known as the Jaggery Capital of South India, rich in ancient Buddhist rock-cut monasteries and countryside beauty.",
            "places": [
                {"name": "Bojjannakonda Buddhist Rock Caves", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "4th-century BCE monolithic Buddhist caves, stupas, and viharas carved out of twin sandstone hills."},
                {"name": "Kondakarla Ava Bird Sanctuary & Lake", "category": "Nature", "entry_fee": 20, "opening": "07:00", "closing": "18:00", "description": "Serene freshwater lake and avian haven with traditional palm-log boat rides and migratory birds."},
            ]
        },
        {
            "district": "Ananthapuramu", "lat": 14.6819, "lon": 77.6006, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Rayalaseema Ragi Sangati, Natu Kodi & Groundnut Chutney",
            "description": "Historic crossroads of the Vijayanagara Empire featuring medieval hill fortresses and giant banyan trees.",
            "places": [
                {"name": "Gooty Hill Fort", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Ancient shell-shaped hill citadel rising 300 meters above the plains, fortified by Vijayanagara and Maratha kings."},
                {"name": "Thimmamma Marrimanu Giant Banyan", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Guinness World Record banyan tree covering over 5 acres with hundreds of prop roots."},
            ]
        },
        {
            "district": "Annamayya", "lat": 13.9870, "lon": 78.7520, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Madanapalle Tomato Curry & Rayalaseema Pulao",
            "description": "Named after saint-poet Tallapaka Annamacharya, home to the cool Horsley Hills and historic forts.",
            "places": [
                {"name": "Horsley Hills Station (Ooty of Andhra)", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Charming hill station at 1,265m elevation with eucalyptus groves, Gali Bandalu windy rocks, and viewpoints."},
                {"name": "Gurramkonda Fort", "category": "Fort", "entry_fee": 20, "opening": "09:00", "closing": "17:00", "description": "Historic 500-foot granite hill fortress with Rangin Mahal, built during Vijayanagara and Golconda rule."},
            ]
        },
        {
            "district": "Bapatla", "lat": 15.9042, "lon": 80.4674, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Chirala Handloom Sweets & Coastal Fish Fry",
            "description": "Coastal beach tourism and agricultural hub famous for golden shorelines, textile traditions, and historic temples.",
            "places": [
                {"name": "Suryalanka Beach", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Wide, flat sandy shoreline on the Bay of Bengal popular for sunbathing, swimming, and sunrise views."},
                {"name": "Chirala Handloom & Beach Corridor", "category": "Cultural", "entry_fee": 0, "opening": "09:00", "closing": "20:00", "description": "Historic weaving town famed for artisanal Kuppadam zari sarees and quiet nearby beaches."},
            ]
        },
        {
            "district": "Chittoor", "lat": 13.2172, "lon": 79.1003, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Mango delicacies, Jaggery & Filter Coffee",
            "description": "Gateway to southern Andhra bordered by Tamil Nadu and Karnataka, famed for temples, waterfalls, and mango orchards.",
            "places": [
                {"name": "Kanipakam Sri Varasiddhi Vinayaka Temple", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "Famed 11th-century Chola temple where the self-manifested (Swayambhu) Ganesha idol is said to be continuously growing."},
                {"name": "Kaigal Waterfalls (Dumukurallu)", "category": "Waterfall", "entry_fee": 20, "opening": "08:00", "closing": "17:00", "description": "Perennial 40-foot cascading falls in Kaundinya Wildlife Sanctuary surrounded by lush forests."},
            ]
        },
        {
            "district": "East Godavari", "lat": 17.0005, "lon": 81.8040, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Pootharekulu, Rajahmundry Rose Milk & Godavari Pulasa",
            "description": "Cultural heart of Andhra on the banks of the sacred Godavari River, featuring majestic bridges and pushkar ghats.",
            "places": [
                {"name": "Godavari Pushkar Ghat & Havelock Bridge", "category": "Heritage", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Historic 2.7km decommissioned rail bridge across the Godavari and lively riverfront spiritual ghats."},
                {"name": "Kadiyapulanka Flower & Plant Nurseries", "category": "Nature", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Asia's premier horticultural nursery village with thousands of acres of exotic flowers and ornamental plants."},
            ]
        },
        {
            "district": "Eluru", "lat": 16.7107, "lon": 81.0952, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Chepala Pulusu & Eluru Handloom Halwa",
            "description": "Rich historic city connecting the Krishna and Godavari deltas, adjacent to India's largest freshwater wetland.",
            "places": [
                {"name": "Kolleru Lake & Atapaka Bird Sanctuary", "category": "Wildlife", "entry_fee": 30, "opening": "07:00", "closing": "18:00", "description": "One of India's largest freshwater lakes and Ramsar wetland shelter for spot-billed pelicans and painted storks."},
                {"name": "Guntupalli Buddhist Rock Caves", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "3rd-century BCE rock-cut Buddhist chaitya halls and circular sandstone stupas nestled in picturesque hills."},
            ]
        },
        {
            "district": "Guntur", "lat": 16.3067, "lon": 80.4365, "crime_index": 25.0, "safety_tier": "LOW",
            "food": "Guntur Mirchi Bajji, Gongura Pachadi & Andhra Meals",
            "description": "Commercial and cultural epicenter of coastal Andhra, famed for world-renowned spicy chillies, forts, and temples.",
            "places": [
                {"name": "Kondaveedu Fort", "category": "Fort", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "14th-century Reddy dynasty hill fort with panoramic viewpoints, ancient ramparts, and ghat roads."},
                {"name": "Kotappakonda Sri Trikoteswara Swamy Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Ancient Shiva shrine perched on a three-peaked hill symbolizing Brahma, Vishnu, and Rudra."},
            ]
        },
        {
            "district": "Kakinada", "lat": 16.9891, "lon": 82.2475, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kakinada Kaja, Coastal Prawns & Subbayya Gari Butta Bhojanam",
            "description": "The Fertilizer City and port hub known for sweet Kaja, pristine mangrove sanctuaries, and handloom weaving.",
            "places": [
                {"name": "Coringa Wildlife Sanctuary & Mangrove Boardwalk", "category": "Wildlife", "entry_fee": 50, "opening": "08:30", "closing": "17:00", "description": "Second-largest mangrove forest on India's eastern coast with wooden boardwalks and boat rides."},
                {"name": "Uppada Beach & Handloom Silk Weaving Village", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Tranquil coastline famous for Geographically Indicated (GI) Uppada Jamdani handloom sarees."},
            ]
        },
        {
            "district": "Konaseema", "lat": 16.5787, "lon": 81.9961, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Dindi Coconut Water, Kobbari Annam & River Fish",
            "description": "Known as God's Own Creation in Andhra, a lush delta island surrounded by the Godavari River, palms, and lagoons.",
            "places": [
                {"name": "Dindi Godavari Backwaters & Houseboat Cruises", "category": "Nature", "entry_fee": 100, "opening": "07:00", "closing": "18:00", "description": "Tranquil river channels lined with coconut groves offering traditional wooden houseboat stays."},
                {"name": "Antarvedi Lakshmi Narasimha Temple & Sea Confluence", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Historic shrine situated at the sacred Sangamam where the Vashishta Godavari River merges into the Bay of Bengal."},
            ]
        },
        {
            "district": "Krishna", "lat": 16.1875, "lon": 81.1389, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bandar Laddu, Bandar Halwa & Gongura Rice",
            "description": "Historic seaside district with colonial maritime trading roots, famous sweets, and coastal pilgrimage spots.",
            "places": [
                {"name": "Manginapudi Beach", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Historic beach near Machilipatnam with black natural soil and shallow waters ideal for evening strolls."},
                {"name": "Machilipatnam Kalamkari Handloom Workshops", "category": "Cultural", "entry_fee": 0, "opening": "09:30", "closing": "18:00", "description": "Centuries-old block-printing workshops famous for natural vegetable dyes and Mughal-era motifs."},
            ]
        },
        {
            "district": "Kurnool", "lat": 15.8281, "lon": 78.0373, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Rayalaseema Uggani Bajji, Jowar Roti & Gongura Mutton",
            "description": "The Gateway of Rayalaseema, featuring subterranean limestone caverns, rock gardens, and historic watchtowers.",
            "places": [
                {"name": "Belum Caves", "category": "Nature", "entry_fee": 65, "opening": "10:00", "closing": "17:00", "description": "Second-longest natural limestone cave system in India with illuminated passages and Patalaganga underground stream."},
                {"name": "Konda Reddy Buruju & Oravakallu Rock Garden", "category": "Historical", "entry_fee": 30, "opening": "09:00", "closing": "18:00", "description": "Iconic Vijayanagara watchtower citadel and ancient natural igneous silica rock garden with boating lake."},
            ]
        },
        {
            "district": "Nandyal", "lat": 15.4875, "lon": 78.4811, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Nandyal Pulao & Rayalaseema Sweets",
            "description": "Surrounded by nine sacred Nandi temples, gateway to the sacred Srisailam forest and Ahobilam hills.",
            "places": [
                {"name": "Srisailam Bhramaramba Mallikarjuna Jyotirlinga", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "Ancient temple on the Nallamala Hills, uniquely revered as both one of the 12 Jyotirlingas and 18 Shakti Peethas."},
                {"name": "Ahobilam Nava Narasimha Temples", "category": "Temple", "entry_fee": 0, "opening": "06:30", "closing": "19:00", "description": "Nine sacred temples of Lord Narasimha spread across the deep forested valleys of the Eastern Ghats."},
                {"name": "Mahanandi Temple & Natural Mineral Springs", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "1,500-year-old temple surrounded by lush orchards with crystal-clear perennial spring pools (Kalyani)."},
            ]
        },
        {
            "district": "NTR", "lat": 16.5062, "lon": 80.6480, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Pesarattu Upma, Gongura Pickle & Bandar Halwa",
            "description": "Encompassing the bustling commercial hub of Vijayawada on the Krishna River, dotted with ancient cave temples.",
            "places": [
                {"name": "Kanaka Durga Temple Indrakeeladri", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Sacred hilltop Shakti Peetham overlooking the Krishna River, associated with Arjuna receiving the Pasupatastra."},
                {"name": "Undavalli Rock-Cut Caves", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Monolithic 5th-century sandstone caves featuring a giant sculpted reclining Vishnu (Ananthasayana)."},
                {"name": "Prakasam Barrage & Bhavani Island", "category": "Nature", "entry_fee": 50, "opening": "08:00", "closing": "18:30", "description": "1.2km modern dam and one of India's largest river islands offering water sports and gardens."},
            ]
        },
        {
            "district": "Palnadu", "lat": 16.2349, "lon": 79.5855, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Karempudi Spicy Chutney & Jowar Rotis",
            "description": "Famed for the medieval Battle of Palnadu, Buddhist archaeology, and the massive Nagarjuna Sagar Reservoir.",
            "places": [
                {"name": "Nagarjunakonda Island & ASI Museum", "category": "Historical", "entry_fee": 50, "opening": "09:00", "closing": "17:00", "description": "Island museum in the center of Nagarjuna Sagar Lake housing rescued 3rd-century Ikshvaku Buddhist ruins."},
                {"name": "Ethipothala Waterfalls & Crocodile Sanctuary", "category": "Waterfall", "entry_fee": 30, "opening": "07:00", "closing": "18:00", "description": "70-foot natural cascading waterfall on the Chandravanka River with a breeding lagoon for mugger crocodiles."},
            ]
        },
        {
            "district": "Parvathipuram Manyam", "lat": 18.7797, "lon": 83.4282, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Manyam Millet Rotis & Wild Forest Honey",
            "description": "Pristine tribal hill district in the Eastern Ghats bounded by Odisha, rich in forest biodiversity and waterfalls.",
            "places": [
                {"name": "Nagavali River Ghat & Thotapalli Reservoir", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Picturesque reservoir and river corridor surrounded by lush green forested hills and peaceful picnic groves."},
            ]
        },
        {
            "district": "Prakasam", "lat": 15.5057, "lon": 80.0499, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Ongole Ghee Sweets & Andhra Spicy Veg Thali",
            "description": "Known worldwide for the indigenous Ongole breed of cattle, extensive coastal salt pans, and stone temples.",
            "places": [
                {"name": "Kothapatnam Beach", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Tranquil sandy beach surrounded by casuarina trees on the Bay of Bengal."},
                {"name": "Markapur Chennakesava Swamy Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Glorious Vijayanagara-era temple renowned for intricate stone carvings, musical pillars, and galigopuram."},
            ]
        },
        {
            "district": "Nellore", "lat": 14.4426, "lon": 79.9865, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Nellore Chepala Pulusu & Malgudi Filter Coffee",
            "description": "Major maritime, aquaculture, and space exploration district home to Pulicat Lake and ISRO Sriharikota.",
            "places": [
                {"name": "Pulicat Lake & Nelapattu Bird Sanctuary", "category": "Wildlife", "entry_fee": 30, "opening": "06:30", "closing": "18:00", "description": "India's second-largest brackish lagoon, hosting tens of thousands of pink flamingos every winter."},
                {"name": "Mypadu Beach & Penna Riverfront", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Pristine golden beach lined with lush palm groves and clean recreational bathing zones."},
            ]
        },
        {
            "district": "Sri Sathya Sai", "lat": 14.1683, "lon": 77.8108, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Rayalaseema Thali, Obbattu & Groundnut Chutney",
            "description": "Global spiritual pilgrimage destination home to Puttaparthi and the 16th-century Vijayanagara wonders of Lepakshi.",
            "places": [
                {"name": "Lepakshi Veerabhadra Temple & Hanging Pillar", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Architectural wonder famous for its suspended stone pillar, colossal monolithic Nandi, and Vijayanagara frescoes."},
                {"name": "Prasanthi Nilayam Ashram Puttaparthi", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "Global peace and meditation sanctuary founded by Sri Sathya Sai Baba, attracting seekers from over 100 nations."},
            ]
        },
        {
            "district": "Srikakulam", "lat": 18.2949, "lon": 83.8938, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Srikakulam Khaja, Upma Pesarattu & Sea Crab",
            "description": "Northern coastal district on the Odisha border, celebrated for ancient sun temples and Buddhist archaeology.",
            "places": [
                {"name": "Arasavalli Sri Suryanarayana Swamy Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Ancient 7th-century Kalinga sun temple where sunlight falls directly on the deity's feet during Equinox mornings."},
                {"name": "Srimukhalingam Shiva Temple Complex", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "8th-century Eastern Ganga architectural masterpiece situated on the banks of the Vamsadhara River."},
                {"name": "Kalingapatnam Beach & Colonial Lighthouse", "category": "Beach", "entry_fee": 20, "opening": "08:00", "closing": "18:00", "description": "Historic European port beach featuring a 73-foot British-era maritime lighthouse."},
            ]
        },
        {
            "district": "Vizianagaram", "lat": 18.1133, "lon": 83.4073, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Vizianagaram Pootharekulu & Andhra Vegetarian Meals",
            "description": "City of Victory, cultural and classical music bastion ruled by the Gajapati and Pusapati royal dynasties.",
            "places": [
                {"name": "Vizianagaram Fort & Moti Mahal", "category": "Fort", "entry_fee": 20, "opening": "09:30", "closing": "17:30", "description": "18th-century quadrangular stone fortress with grand Rajasthani-influenced entrance gates and royal council halls."},
                {"name": "Ramatheertham Buddhist & Rama Temple Hill", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Ancient hilltop archaeological site featuring 1,000-year-old rock-cut Buddhist chaityas and a Rama temple."},
            ]
        },
        {
            "district": "West Godavari", "lat": 16.5449, "lon": 81.5212, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bhimavaram Prawn Curry & Cashew Sweets",
            "description": "Lush delta agricultural and aquaculture powerhouse famed for Pancharama Shiva temples and tranquil canals.",
            "places": [
                {"name": "Somarama Temple (Somarama Kshethram)", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "One of the sacred Pancharama temples dedicated to Someswara Swamy, featuring the sacred Chandrakundam pond."},
                {"name": "Mavullamma Temple Bhimavaram", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "21:00", "description": "Beloved historic temple of Gramadevatha Goddess Mavullamma renowned for grand seasonal festivities."},
            ]
        },
        {
            "district": "YSR Kadapa", "lat": 14.4673, "lon": 78.8242, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Rayalaseema Karam Dosa & Ragi Sangati",
            "description": "Home to the spectacular Gandikota Gorge (Grand Canyon of India) and ancient Vijayanagara citadels.",
            "places": [
                {"name": "Gandikota Fort & Pennar River Gorge", "category": "Fort", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "The Grand Canyon of India, an 11th-century fort perched atop a dramatic 300-foot red sandstone gorge."},
                {"name": "Vontimitta Sri Kodandarama Swamy Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "16th-century Vijayanagara monolithic temple marvel admired by French merchant Jean-Baptiste Tavernier in 1652."},
                {"name": "Ameen Peer Dargah (Asthana-e-Magdoom Ilahi)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Historic Sufi shrine dating back to 1683, visited by people of all faiths from across the world."},
            ]
        },
    ],

    # ==================== 2. KARNATAKA (31 Districts) ====================
    "Karnataka": [
        {
            "district": "Bengaluru Urban", "lat": 12.9716, "lon": 77.5946, "crime_index": 26.0, "safety_tier": "LOW",
            "food": "Masala Dosa, Filter Coffee, Bisi Bele Bath & Mysore Pak",
            "description": "Silicon Valley of India and Garden City, home to tech parks, lush public gardens, and royal palaces.",
            "places": [
                {"name": "Lalbagh Botanical Garden & Glass House", "category": "Nature", "entry_fee": 25, "opening": "06:00", "closing": "19:00", "description": "240-acre botanical haven founded by Hyder Ali in 1760, famous for its London Crystal Palace-inspired Glass House."},
                {"name": "Bangalore Palace & Grounds", "category": "Palace", "entry_fee": 250, "opening": "10:00", "closing": "17:30", "description": "Tudor-revival architectural marvel inspired by Windsor Castle, featuring turrets, wood carvings, and royal memorabilia."},
                {"name": "Cubbon Park & Vidhana Soudha", "category": "Heritage", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "300-acre lush lung of Bangalore facing the magnificent Neo-Dravidian granite legislative assembly palace."},
                {"name": "Bannerghatta Biological Park & Safari", "category": "Wildlife", "entry_fee": 100, "opening": "09:30", "closing": "17:00", "description": "Vast wilderness reserve featuring tiger/lion safari, India's first butterfly conservatory, and zoo."},
            ]
        },
        {
            "district": "Bengaluru Rural", "lat": 13.2385, "lon": 77.7119, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Ragi Mudde, Soppina Saaru & Jackfruit Delicacies",
            "description": "Surrounding Bengaluru with heritage silk cocoon markets, scenic granite hillocks, and historic forts.",
            "places": [
                {"name": "Devanahalli Fort (Birthplace of Tipu Sultan)", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "15th-century stone fortress with twelve bastions where the famed Tiger of Mysore Tipu Sultan was born."},
                {"name": "Ghati Subramanya Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "Centuries-old pilgrimage shrine where Lord Subramanya and Lord Lakshmi Narasimha idols emerge from a single stone."},
                {"name": "Shivagange Hill Peak & Monolithic Nandi", "category": "Adventure", "entry_fee": 0, "opening": "06:00", "closing": "17:30", "description": "Sacred 1,368m hillock shaped like a Shiva Linga with rock-cut springs and panoramic trekking trails."},
            ]
        },
        {
            "district": "Mysuru", "lat": 12.2958, "lon": 76.6394, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Mysore Pak, Mylari Dosa & Mysore Filter Kaapi",
            "description": "The Heritage City of Palaces, world-renowned for Dussehra celebrations, sandalwood, and silk.",
            "places": [
                {"name": "Mysore Palace (Amba Vilas)", "category": "Palace", "entry_fee": 100, "opening": "10:00", "closing": "17:30", "description": "Grand Indo-Saracenic royal seat of the Wadiyar dynasty, illuminated by 97,000 golden bulbs on weekends."},
                {"name": "Chamundi Hills & Sri Chamundeshwari Temple", "category": "Temple", "entry_fee": 0, "opening": "07:30", "closing": "21:00", "description": "Historic hilltop shrine atop 1,000-step hill overlooking Mysuru, featuring a colossal 15-foot monolithic Nandi."},
                {"name": "Brindavan Gardens & Musical Fountain", "category": "Nature", "entry_fee": 50, "opening": "06:30", "closing": "21:00", "description": "Terraced botanical gardens across the Krishna Raja Sagara Dam, famous for synchronized evening musical fountain shows."},
            ]
        },
        {
            "district": "Ballari", "lat": 15.1394, "lon": 76.9214, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Ballari Jowar Roti, Mirchi Mandakki & Shenga Chutney",
            "description": "Historic mining and heritage gateway to the UNESCO World Heritage monuments of the Vijayanagara Empire.",
            "places": [
                {"name": "Ballari Fort (Upper & Lower Fort)", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Ancient monolithic rock citadel renovated by French engineer for Hyder Ali, offering sweeping district views."},
            ]
        },
        {
            "district": "Vijayanagara", "lat": 15.3350, "lon": 76.4600, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Kishkindha Mangoes, Jowar Bhakri & Coconut Curry",
            "description": "Created from Ballari, housing the magnificent UNESCO World Heritage city of Hampi along the Tungabhadra.",
            "places": [
                {"name": "Hampi UNESCO World Heritage Complex & Virupaksha Temple", "category": "Historical", "entry_fee": 40, "opening": "06:00", "closing": "18:00", "description": "14th-century capital of the Vijayanagara Empire with stone-carved ruins, giant boulder hills, and active shrine."},
                {"name": "Vittala Temple & Iconic Stone Chariot", "category": "Historical", "entry_fee": 40, "opening": "08:30", "closing": "17:30", "description": "Architectural masterpiece featured on the Indian ₹50 note, renowned for musical pillars and monolithic chariot."},
                {"name": "Lotus Mahal & Elephant Stables", "category": "Palace", "entry_fee": 40, "opening": "08:30", "closing": "17:30", "description": "Indo-Islamic two-storey royal pavilion with arched vaults and domed elephant stable chambers."},
            ]
        },
        {
            "district": "Bagalkot", "lat": 16.1691, "lon": 75.6615, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Jolada Roti Oota & Badami Peda",
            "description": "Cradle of Indian temple architecture on the Malaprabha River, home to the Chalukyan cave temples.",
            "places": [
                {"name": "Badami Cave Temples & Agastya Lake", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Four 6th-century rock-cut cave shrines sculpted into red sandstone cliffs overlooking the sacred Agastya Lake."},
                {"name": "Pattadakal UNESCO World Heritage Temple Complex", "category": "Historical", "entry_fee": 40, "opening": "09:00", "closing": "17:00", "description": "7th-to-8th century royal coronation site exhibiting an exquisite blend of North Indian Rekha-Nagara and Dravidian architectural styles."},
                {"name": "Aihole Cradle of Indian Temple Architecture", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Over 120 stone temples dating from 450 CE featuring the famous apsidal Durga Temple with relief sculptures."},
            ]
        },
        {
            "district": "Belagavi", "lat": 15.8497, "lon": 74.4977, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Belgaum Kunda, Karadant & Kolhapuri Mutton",
            "description": "Second capital of Karnataka located in the Western Ghats foothills, famous for Kunda sweet, forts, and waterfalls.",
            "places": [
                {"name": "Belagavi Fort & Kamal Basti Jain Temple", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:30", "description": "13th-century stone fortress with deep moats, housing the intricately sculpted 72-petal lotus ceiling Kamal Basti."},
                {"name": "Gokak Waterfalls & Historic Suspension Bridge", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "18:00", "description": "Horseshoe-shaped 177-foot plunge on the Ghataprabha River (Niagara of Karnataka) with a 19th-century hanging bridge."},
            ]
        },
        {
            "district": "Chikkamagaluru", "lat": 13.3161, "lon": 75.7720, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Filter Coffee, Akki Roti & Jackfruit Payasa",
            "description": "The Coffee Land of Karnataka, where Baba Budan first cultivated coffee in 1670 amidst misty Western Ghats peaks.",
            "places": [
                {"name": "Mullayanagiri Peak (Highest in Karnataka)", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Highest mountain peak in Karnataka at 1,930m elevation with stunning sunrise views and trekking routes."},
                {"name": "Baba Budangiri & Dattatreya Peetha", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Sacred mountain range venerated by both Sufis and Hindus, offering panoramic coffee valley vistas."},
                {"name": "Kudremukh National Park & Trekking Valley", "category": "Nature", "entry_fee": 100, "opening": "06:00", "closing": "17:00", "description": "UNESCO World Heritage Western Ghats biodiversity hotspot with horse-face shaped mountain peaks and shola forests."},
            ]
        },
        {
            "district": "Kodagu", "lat": 12.4244, "lon": 75.7382, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Pandi Curry (Coorg Pork), Kadambuttu & Coorg Orange Honey",
            "description": "Scotland of India, mist-covered Western Ghats district renowned for warrior heritage, coffee estates, and Kaveri river origin.",
            "places": [
                {"name": "Abbey Waterfalls & Hanging Bridge", "category": "Waterfall", "entry_fee": 25, "opening": "09:00", "closing": "17:00", "description": "70-foot roaring waterfall cascading amidst lush private coffee plantations and spice bushes."},
                {"name": "Namdroling Monastery (Bylakuppe Golden Temple)", "category": "Spiritual", "entry_fee": 0, "opening": "09:00", "closing": "18:00", "description": "Second-largest Tibetan settlement in India featuring giant 40-foot gilded statues of Padmasambhava and Buddha."},
                {"name": "Raja's Seat Madikeri", "category": "Viewpoint", "entry_fee": 20, "opening": "06:00", "closing": "20:00", "description": "Perched terrace garden where Kodagu kings enjoyed sunsets over green rolling valleys with musical fountains."},
                {"name": "Dubare Elephant Camp & River Rafting", "category": "Wildlife", "entry_fee": 50, "opening": "09:00", "closing": "17:00", "description": "Eco-tourism camp on the Kaveri River where visitors observe elephant bathing, feeding, and tranquil river rafting."},
            ]
        },
        {
            "district": "Dakshina Kannada", "lat": 12.9141, "lon": 74.8560, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Mangalorean Fish Curry, Neer Dosa, Ghee Roast & Gadbad Ice Cream",
            "description": "Coastal and educational hub of Tulunadu featuring clean Arabian Sea beaches, historic shrines, and seafood.",
            "places": [
                {"name": "Panambur Beach & Lighthouse", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Clean, well-maintained beach with jet-skiing, camel rides, and international kite festival gatherings."},
                {"name": "Kudroli Gokarnanatheshwara Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Renowned temple built by saint Narayana Guru, world-famous for grand Mangalore Dasara celebrations."},
                {"name": "Kadri Manjunatha Temple & Pandava Caves", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "10th-century Vijayanagara bronze Lokeshwara sculpture temple set against natural spring-fed ponds."},
            ]
        },
        {
            "district": "Uttara Kannada", "lat": 14.7937, "lon": 74.1306, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Karwar Fish Thali, Cashew Curry & Toddy Palm Delicacies",
            "description": "Lush coastal district combining pristine Arabian Sea beaches, Western Ghats jungles, and iconic Shiva shrines.",
            "places": [
                {"name": "Gokarna Om Beach & Mahabaleshwar Temple", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Sacred Atmalinga shrine and picturesque beach naturally contoured like the spiritual Hindu 'Om' symbol."},
                {"name": "Murudeshwar Shiva Statue & Raja Gopura", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "World's second-tallest Shiva statue (123 feet) on Kanduka hill surrounded by the Arabian Sea on three sides."},
                {"name": "Yana Massive Monolithic Rock Formations", "category": "Nature", "entry_fee": 20, "opening": "08:00", "closing": "17:00", "description": "Two towering crystalline karst rock monoliths rising 90 and 120 meters amidst thick Sahyadri rain forests."},
                {"name": "Dandeli River Rafting & Wildlife Sanctuary", "category": "Adventure", "entry_fee": 50, "opening": "08:00", "closing": "17:00", "description": "Premier white-water rafting destination on the Kali River, home to black panthers and hornbills."},
            ]
        },
        {
            "district": "Udupi", "lat": 13.3409, "lon": 74.7421, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Udupi Sambar, Masala Dosa, Goli Baje & Filter Coffee",
            "description": "The spiritual culinary capital of Coastal Karnataka, famous worldwide for Udupi cuisine, temples, and beaches.",
            "places": [
                {"name": "Sri Krishna Matha & Kanakana Kindi", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "13th-century Dvaita temple established by saint Madhvacharya where Lord Krishna is viewed through a silver window."},
                {"name": "Malpe Beach & St. Mary's Basaltic Islands", "category": "Beach", "entry_fee": 400, "opening": "09:00", "closing": "17:30", "description": "National Geological Monument of columnar hexagonal basaltic rock formations formed by prehistoric volcanic activity."},
                {"name": "Kaup Beach & 1901 Victorian Lighthouse", "category": "Beach", "entry_fee": 20, "opening": "06:00", "closing": "19:00", "description": "Scenic rocky beach featuring an active 100-foot British-era lighthouse offering panoramic Arabian Sea sunsets."},
            ]
        },
        {
            "district": "Hassan", "lat": 13.0033, "lon": 76.1004, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Ragi Mudde, Bisi Bele Bath & Akki Roti",
            "description": "Architectural showcase of the Hoysala Empire, home to UNESCO World Heritage stone-carved temples.",
            "places": [
                {"name": "Belur Chennakeshava Temple (UNESCO World Heritage)", "category": "Historical", "entry_fee": 40, "opening": "07:30", "closing": "19:30", "description": "12th-century soapstone star-shaped temple built by King Vishnuvardhana, renowned for 42 bracket dancer sculptures."},
                {"name": "Halebidu Hoysaleswara Temple (UNESCO World Heritage)", "category": "Historical", "entry_fee": 40, "opening": "07:30", "closing": "18:00", "description": "Exquisite twin Hoysala temple with over 20,000 intricate friezes depicting scenes from Mahabharata and Ramayana."},
                {"name": "Shravanabelagola Gommateshwara Statue", "category": "Spiritual", "entry_fee": 0, "opening": "06:30", "closing": "18:30", "description": "World's largest monolithic free-standing stone statue (57 feet tall) sculpted in 981 CE by Ganga dynasty minister Chavundaraya."},
            ]
        },
        {
            "district": "Shivamogga", "lat": 13.9299, "lon": 75.5681, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Thuppa Dosa, Halasina Hannina Kadubu & Kaapi",
            "description": "Gateway to the Western Ghats (Malnad), blessed with roaring waterfalls, thick forests, and wildlife sanctuaries.",
            "places": [
                {"name": "Jog Falls (Gerosoppa Plunge)", "category": "Waterfall", "entry_fee": 30, "opening": "08:00", "closing": "18:00", "description": "Second-highest plunge waterfall in India, where the Sharavathi River drops 253 meters in four cascades: Raja, Roarer, Rocket, and Rani."},
                {"name": "Sakrebyle Elephant Camp", "category": "Wildlife", "entry_fee": 50, "opening": "08:30", "closing": "11:30", "description": "Forest eco-camp on the Tunga River where travelers observe wild Asian elephants taking morning river baths."},
            ]
        },
        {
            "district": "Vijayapura", "lat": 16.8302, "lon": 75.7100, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Jolada Roti Oota & Bijapur Peda",
            "description": "The City of Victory ruled by the Adil Shahi dynasty, famed for Indo-Islamic tombs and whispering galleries.",
            "places": [
                {"name": "Gol Gumbaz (World's Second-Largest Dome)", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Mausoleum of Mohammed Adil Shah featuring a 44-meter unsupported circular dome and an acoustic Whispering Gallery."},
                {"name": "Ibrahim Rauza (Taj Mahal of the Deccan)", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "16th-century palatial mosque and tomb constructed with delicate minarets, stone chains, and Persian inscriptions."},
            ]
        },
        {
            "district": "Bidar", "lat": 17.9104, "lon": 77.5199, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Bidri Mutton Biryani & Handcrafted Bidriware Artisans",
            "description": "Crown of Karnataka, medieval Bahmani and Barid Shahi capital famous for giant fort moats and Bidriware metalwork.",
            "places": [
                {"name": "Bidar Fort & Mahmud Gawan Madrasa", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Massive 15th-century citadel featuring triple-layered moats, Rangeen Mahal with mother-of-pearl mosaics, and Solah Khamba Mosque."},
                {"name": "Guru Nanak Jhira Sahib Gurudwara", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "Historic Sikh pilgrimage shrine where Guru Nanak Dev Ji created a perennial freshwater spring amidst drought."},
            ]
        },
        {
            "district": "Chamarajanagar", "lat": 11.9261, "lon": 76.9437, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Biligiriranga Honey & South Karnataka Meals",
            "description": "Southernmost border district famed for contiguous tiger reserves, sandalwood forests, and scenic ghats.",
            "places": [
                {"name": "Bandipur National Park & Tiger Reserve", "category": "Wildlife", "entry_fee": 300, "opening": "06:00", "closing": "18:00", "description": "Premier Project Tiger sanctuary in the Nilgiri Biosphere Reserve home to elephants, gaurs, and royal Bengal tigers."},
                {"name": "Biligirirangana Hills (BR Hills Wildlife Sanctuary)", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Ecological bridge between the Western and Eastern Ghats, revered for the hilltop Ranganathaswamy Temple."},
            ]
        },
        {
            "district": "Chikkaballapur", "lat": 13.4355, "lon": 77.7275, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Nandi Valley Grapes & South Indian Tiffin",
            "description": "Hilly terrain adjacent to Bengaluru airport, home to the sunrise paradise Nandi Hills and ancient temples.",
            "places": [
                {"name": "Nandi Hills (Nandidurga Sunrise Peak)", "category": "Viewpoint", "entry_fee": 20, "opening": "06:00", "closing": "18:00", "description": "Historic 1,478m hilltop fortress famous for spectacular sea-of-clouds sunrises, Tipu's Drop, and cool breezes."},
                {"name": "Bhoga Nandeeshwara 9th-Century Temple Complex", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "One of Karnataka's oldest Dravidian architectural complexes, showcasing pristine Nolamba, Chola, and Hoysala craftsmanship."},
            ]
        },
        {
            "district": "Chitradurga", "lat": 14.2251, "lon": 76.3980, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Chitradurga Benne Dosa & Jowar Roti",
            "description": "The Stone Fortress City of Karnataka, famed for the impregnable Fort of Seven Rounds and heroic folklore.",
            "places": [
                {"name": "Chitradurga Fort (Kallina Kote - Fort of Seven Rounds)", "category": "Fort", "entry_fee": 25, "opening": "08:30", "closing": "17:30", "description": "Massive medieval rock citadel with seven concentric defensive walls, 38 secret gateways, and 18 ancient temples."},
                {"name": "Chandravalli Caves & Lake Archaeology", "category": "Historical", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "Subterranean prehistoric caves nestled between three hills where coins from Rome and the Satavahanas were uncovered."},
            ]
        },
        {
            "district": "Davanagere", "lat": 14.4644, "lon": 75.9218, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Davanagere Benne Dosa (Butter Dosa) & Mandakki Menasinakayi",
            "description": "Textile and culinary powerhouse of Central Karnataka, renowned across India for crispy wood-fired Butter Dosas.",
            "places": [
                {"name": "Shanti Sagara (Sulekere - 2nd Largest Tank in Asia)", "category": "Lake", "entry_fee": 0, "opening": "07:00", "closing": "18:30", "description": "12th-century historic water reservoir built by princess Shantavva covering over 6,500 acres with hills."},
                {"name": "Bathi Gudda & Glass House", "category": "Viewpoint", "entry_fee": 20, "opening": "09:00", "closing": "18:00", "description": "Picturesque hillock overlooking the city featuring a TV relay tower and landscaped municipal glass pavilion."},
            ]
        },
        {
            "district": "Dharwad", "lat": 15.4589, "lon": 75.0078, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Dharwad Peda (GI Tag) & Girmit",
            "description": "Cultural, educational, and Hindustani classical music twin-city with Hubballi, world-famed for caramelized brown Dharwad Peda.",
            "places": [
                {"name": "Unkal Lake & Swami Vivekananda Statue", "category": "Lake", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Historic 300-year-old freshwater lake featuring a 10-foot bronze statue of Swami Vivekananda and boat rides."},
                {"name": "Chandramouleshwara 11th-Century Chalukya Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Badami Chalukyan black-stone monument with four carved entrances and twin Shiva lingas."},
            ]
        },
        {
            "district": "Gadag", "lat": 15.4298, "lon": 75.6322, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Jolada Roti, Shengada Chutney & Girmit",
            "description": "Cradle of the Western Chalukya architectural style and printing press heritage, dotted with intricately carved temples.",
            "places": [
                {"name": "Lakkundi Stepwells & 11th-Century Temples", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Ancient village housing 50 Chalukyan stone temples and magnificent stepped water wells (Pushkarinis)."},
                {"name": "Trikuteshwara Temple Complex", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "19:30", "description": "Magnificent tripartite sanctum dedicated to Brahma, Shiva, and Surya with ornate Saraswati pillars."},
            ]
        },
        {
            "district": "Haveri", "lat": 14.7963, "lon": 75.3995, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Byadagi Chilli Spicy Delicacies & Jowar Roti",
            "description": "World-famous for vibrant Byadagi red chillies (GI tag) and ancient Hoysala-Chalukya border temples.",
            "places": [
                {"name": "Tarakeshwara Temple Hangal", "category": "Temple", "entry_fee": 0, "opening": "06:30", "closing": "19:00", "description": "12th-century Chalukyan architectural jewel featuring an enormous 21-foot domed stone lotus ceiling."},
                {"name": "Ranebennur Blackbuck Sanctuary", "category": "Wildlife", "entry_fee": 30, "opening": "07:00", "closing": "18:00", "description": "Eucalyptus scrub forest sanctuary safeguarding thousands of endangered Indian blackbucks and great Indian bustards."},
            ]
        },
        {
            "district": "Kalaburagi", "lat": 17.3297, "lon": 76.8343, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Jolada Roti, Malpuri & Tahari",
            "description": "Historical seat of the Bahmani Sultanate and Sufi spiritualism, home to unique subterranean mosques and forts.",
            "places": [
                {"name": "Gulbarga Fort & Jama Masjid", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "14th-century citadel housing a rare Persian-style covered mosque with 68 domed bays and 29-foot bronze cannon."},
                {"name": "Khwaja Bande Nawaz Dargah", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "21:30", "description": "Revered 15th-century Sufi shrine attracting millions during its annual Urs, showcasing Indo-Saracenic calligraphy."},
            ]
        },
        {
            "district": "Kolar", "lat": 13.1367, "lon": 78.1291, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Kolar Milk Sweets & Mysore Masala Dosa",
            "description": "Land of Silk, Milk, and Gold (KGF), featuring volcanic cave springs and crore-linga temples.",
            "places": [
                {"name": "Kotilingeshwara Temple (1 Crore Shiva Lingas)", "category": "Spiritual", "entry_fee": 20, "opening": "06:00", "closing": "21:00", "description": "Famed pilgrimage temple boasting over 10 million installed Shiva lingas and a colossal 108-foot central linga."},
                {"name": "Antara Gange Perennial Spring & Volcanic Caves", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Sacred spring emerging from a stone bull's mouth and volcanic boulders popular for night cave exploration."},
                {"name": "Kolar Gold Fields (KGF) Heritage Town", "category": "Heritage", "entry_fee": 0, "opening": "09:00", "closing": "17:00", "description": "Historic colonial gold mining township established in 1880, featuring British bungalows and shaft ruins."},
            ]
        },
        {
            "district": "Koppal", "lat": 15.3524, "lon": 76.1554, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kinnal Wooden Art Crafts & Jowar Roti",
            "description": "Home to the UNESCO-famed Kishkindha boulder hills, Kinnal toy-makers, and Chalukya Mahadeva temples.",
            "places": [
                {"name": "Anegundi (Mythological Kishkindha Monkey Kingdom)", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Ancient monkey kingdom of Sugriva and Vali on the northern bank of Tungabhadra, with Anjanadri Hanuman Hill."},
                {"name": "Mahadeva Temple Itagi (Emperor of Temples)", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "1112 CE Western Chalukyan architectural marvel inscribed as 'Devalaya Chakravarti' with intricate stone carvings."},
            ]
        },
        {
            "district": "Mandya", "lat": 12.5230, "lon": 76.8967, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Maddur Vada (GI Tag) & Mandya Jaggery",
            "description": "Sugar City of Karnataka on the Bengaluru-Mysuru corridor, blessed by the Kaveri River, waterfalls, and bird sanctuaries.",
            "places": [
                {"name": "Shivanasamudra Falls (Gaganachukki & Bharachukki)", "category": "Waterfall", "entry_fee": 0, "opening": "08:00", "closing": "17:30", "description": "Spectacular segmented twin waterfalls on the Kaveri River, site of Asia's first hydroelectric power station in 1902."},
                {"name": "Ranganathittu Bird Sanctuary", "category": "Wildlife", "entry_fee": 70, "opening": "08:30", "closing": "17:30", "description": "Island bird sanctuary on the Kaveri offering boat safaris alongside nesting pelicans, storks, and mugger crocodiles."},
                {"name": "Srirangapatna Island Fort & Ranganathaswamy Temple", "category": "Historical", "entry_fee": 25, "opening": "07:00", "closing": "18:00", "description": "River island capital of Tipu Sultan featuring the Gumbaz mausoleum, Daria Daulat Summer Palace, and 9th-century temple."},
            ]
        },
        {
            "district": "Raichur", "lat": 16.2076, "lon": 77.3463, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Raichur Rice, Jowar Roti & Shenga Chutney",
            "description": "The fertile Doab between the Krishna and Tungabhadra rivers, contested historically by Vijayanagara and Bahmani rulers.",
            "places": [
                {"name": "Raichur Hill Fort & Aam Talab", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "13th-century Kakatiya-Vijayanagara fortress with monumental Persian inscriptions and stone-cut ramparts."},
            ]
        },
        {
            "district": "Ramanagara", "lat": 12.7209, "lon": 77.2799, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bidadi Thatte Idli & Ramanagara Silk",
            "description": "Silk City of India and Bollywood's famed Ramgarh (where Sholay was filmed), renowned for rock climbing and folk arts.",
            "places": [
                {"name": "Ramadevara Betta (Sholay Gabbar Rocks & Vulture Sanctuary)", "category": "Nature", "entry_fee": 25, "opening": "09:00", "closing": "16:30", "description": "Massive granite hill where the film Sholay was shot, home to India's only dedicated long-billed vulture sanctuary."},
                {"name": "Janapada Loka (Folk Culture Museum of Karnataka)", "category": "Museum", "entry_fee": 50, "opening": "09:00", "closing": "17:30", "description": "Sprawling 15-acre open-air museum preserving 5,000+ folk artifacts, Yakshagana masks, puppets, and village arts."},
            ]
        },
        {
            "district": "Tumakuru", "lat": 13.3392, "lon": 77.1017, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Tumkur Thatte Idli & Tender Coconut",
            "description": "Education and industrial city known as the Kalpataru Nadu (Land of Coconuts), featuring hill shrines and natural springs.",
            "places": [
                {"name": "Devarayanadurga Hills & Yoganarasimha Temple", "category": "Hill Station", "entry_fee": 0, "opening": "07:00", "closing": "18:30", "description": "Rocky hill station at 1,200m elevation surrounded by forests, featuring historic Chola temples and Namada Chilume spring."},
                {"name": "Siddaganga Math Pilgrimage Center", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Renowned philanthropic institution founded by Sri Shivakumara Swamiji providing free food and education to thousands daily."},
            ]
        },
        {
            "district": "Yadgir", "lat": 16.7645, "lon": 77.1352, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Jowar Bhakri, Shenga Holige & Spicy Chutney",
            "description": "Historic Yadav and Bahmani district with sprawling hill fortresses and sleeping Buddha rock formations.",
            "places": [
                {"name": "Yadgir Fort & Sleeping Buddha Hill (Shorapur)", "category": "Fort", "entry_fee": 0, "opening": "08:30", "closing": "17:30", "description": "Hilltop bastion with three layers of fortification walls and natural rocks resembling a reclining Buddha."},
            ]
        },
    ],

    # ==================== 3. KERALA (14 Districts) ====================
    "Kerala": [
        {
            "district": "Alappuzha", "lat": 9.4981, "lon": 76.3388, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Karimeen Pollichathu, Kuttanad Duck Roast & Appam",
            "description": "Venice of the East, world-famous for emerald backwaters, traditional kettuvallam houseboats, and coir crafts.",
            "places": [
                {"name": "Vembanad Lake Backwaters & Houseboat Cruise", "category": "Nature", "entry_fee": 150, "opening": "07:00", "closing": "18:00", "description": "India's longest lake, offering serene houseboat voyages through palm-fringed canals, paddy fields, and lagoons."},
                {"name": "Alappuzha Beach & 1862 Colonial Lighthouse", "category": "Beach", "entry_fee": 20, "opening": "06:00", "closing": "19:00", "description": "Historic beach with a 150-year-old wooden sea pier jutting into the Arabian Sea and a Victorian lighthouse."},
                {"name": "Marari Beach (Mararikulam)", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Pristine coconut-fringed eco-beach known for serene tranquility, traditional fishing hamlets, and luxury resorts."},
            ]
        },
        {
            "district": "Ernakulam", "lat": 9.9816, "lon": 76.2999, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Kochi Seafood, Appam with Stew, Puttu & Kerala Parotta",
            "description": "Commercial capital of Kerala encompassing cosmopolitan Kochi, historic Fort Kochi, and Chinese fishing nets.",
            "places": [
                {"name": "Fort Kochi & Chinese Fishing Nets (Cheena Vala)", "category": "Heritage", "entry_fee": 0, "opening": "06:00", "closing": "19:30", "description": "14th-century cantilevered fishing nets introduced by Chinese traders, framing legendary Arabian Sea sunsets."},
                {"name": "Mattancherry Dutch Palace & Jewish Synagogue", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:00", "description": "1555 Portuguese palace with Hindu mythological murals and the 1568 Paradesi Synagogue with Belgian glass lamps."},
                {"name": "Marine Drive Promenade & Rainbow Bridge", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Vibrant pedestrian waterfront walkway overlooking Kochi Harbor, offering evening boat cruises and city lights."},
            ]
        },
        {
            "district": "Idukki", "lat": 9.8494, "lon": 76.9806, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Munnar Cardamom Tea, Kerala Sadhya & Bamboo Biryani",
            "description": "High-altitude misty paradise in the Western Ghats home to Munnar tea plantations, wildlife, and double-curvature arch dams.",
            "places": [
                {"name": "Munnar Tea Estates & KDHP Tea Museum", "category": "Nature", "entry_fee": 75, "opening": "09:00", "closing": "17:00", "description": "Rolling emerald tea garden hills at 1,600m elevation showcasing orthodox tea processing and plantation history."},
                {"name": "Eravikulam National Park (Home of Nilgiri Tahr)", "category": "Wildlife", "entry_fee": 200, "opening": "07:30", "closing": "16:00", "description": "Sanctuary for the endangered Nilgiri Tahr mountain goat and the blooming grounds of the rare Neelakurinji flower."},
                {"name": "Idukki Arch Dam & Kuravan Kurathi Hills", "category": "Nature", "entry_fee": 40, "opening": "09:00", "closing": "17:00", "description": "Asia's second double-curvature parabolic arch dam built between two colossal granite gorges on the Periyar River."},
            ]
        },
        {
            "district": "Kannur", "lat": 11.8745, "lon": 75.3704, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Thalassery Biryani (Kaima Rice), Kallummakkaya (Mussels) & Banana Chips",
            "description": "Land of Theyyam, Handlooms, and Cirque, famous for fiery ritual dances, sea fortresses, and driving beaches.",
            "places": [
                {"name": "St. Angelo Fort (Kannur Fort)", "category": "Fort", "entry_fee": 25, "opening": "08:00", "closing": "18:00", "description": "1505 coastal Portuguese laterite fortress offering sweeping vistas of Mopla Bay and Dutch battlements."},
                {"name": "Muzhappilangad Drive-In Beach", "category": "Beach", "entry_fee": 50, "opening": "06:00", "closing": "19:00", "description": "Asia's longest drive-in beach, where cars can cruise along 4 kilometers of firm golden sands alongside breaking waves."},
            ]
        },
        {
            "district": "Kasaragod", "lat": 12.5102, "lon": 74.9852, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Kasaragod Rice Roti, Mutton Sukka & Halwa",
            "description": "Northernmost district of Kerala, celebrated as the Land of Seven Languages, coastal forts, and rivers.",
            "places": [
                {"name": "Bekal Fort & Observation Tower", "category": "Fort", "entry_fee": 25, "opening": "08:00", "closing": "18:00", "description": "Largest and best-preserved 1650 CE keyhole-shaped laterite sea fortress in Kerala, surrounded by the Arabian Sea."},
                {"name": "Ananthapura Lake Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "The only lake temple in Kerala, situated in the middle of a natural spring pool, guarded by a revered vegetarian crocodile."},
            ]
        },
        {
            "district": "Kollam", "lat": 8.8932, "lon": 76.6141, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Cashew delicacies, Tapioca Fish Curry & Karimeen",
            "description": "The Cashew Capital of the world, historic trade port on the serene shores of Ashtamudi Lake.",
            "places": [
                {"name": "Ashtamudi Lake & DTPC Backwater Cruise", "category": "Nature", "entry_fee": 100, "opening": "08:00", "closing": "18:00", "description": "Eight-armed gateway lake to the Kerala backwaters, famous for scenic water safaris to Munroe Island."},
                {"name": "Jatayu Earth's Center (World's Largest Bird Sculpture)", "category": "Viewpoint", "entry_fee": 450, "opening": "10:00", "closing": "18:00", "description": "World's largest functional bird sculpture (200ft long) atop a 1,000ft rock with cable car and adventure park."},
            ]
        },
        {
            "district": "Kottayam", "lat": 9.5916, "lon": 76.5222, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Kottayam Fish Stew, Palappam & Meen Vevichathu",
            "description": "Land of Letters, Latex, and Lakes, the first 100% literate city in India set amidst backwaters and rubber hills.",
            "places": [
                {"name": "Kumarakom Bird Sanctuary & Vembanad Lake", "category": "Wildlife", "entry_fee": 50, "opening": "06:30", "closing": "17:00", "description": "14-acre paradise on the banks of Vembanad Lake sheltering Siberian cranes, herons, egrets, and waterfowl."},
                {"name": "Illikkal Kallu Mountain Peak", "category": "Viewpoint", "entry_fee": 30, "opening": "08:00", "closing": "17:30", "description": "4,000-foot Sahyadri peak with half of its rock fallen away, creating an ethereal misty canyon vista."},
            ]
        },
        {
            "district": "Kozhikode", "lat": 11.2588, "lon": 75.7804, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Kozhikode Halwa (Sweet Meat Street), Malabar Dum Biryani & Sulaimani Tea",
            "description": "The City of Spices where Vasco da Gama landed in 1498, world-renowned for culinary warmth and coastal sunsets.",
            "places": [
                {"name": "Kozhikode Beach & Old Pier Ruins", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Lively seaside promenade with two century-old iron piers, marine aquarium, and sunset food stalls."},
                {"name": "Kappad Beach (Historic Vasco da Gama Landing Site)", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Historic rocky beach where Portuguese explorer Vasco da Gama anchored in May 1498, opening the sea route to India."},
            ]
        },
        {
            "district": "Malappuram", "lat": 11.0732, "lon": 76.0740, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Malappuram Pathiri, Neypathiri & Kozhi Curry",
            "description": "Hill capital of southern Malabar, rich in teak forests, Islamic heritage, and the birthplace of Malayalam literature.",
            "places": [
                {"name": "Kottakkal Arya Vaidya Sala Heritage Complex", "category": "Spiritual", "entry_fee": 0, "opening": "08:30", "closing": "17:30", "description": "World-famous Ayurvedic healing center established in 1902 with herbal gardens and cultural Kathakali performances."},
                {"name": "Nedumkayam Rainforest & Conolly's Teak Plot", "category": "Nature", "entry_fee": 50, "opening": "09:00", "closing": "17:00", "description": "World's oldest surviving teak plantation planted in 1840s, featuring giant trees along the Chaliyar River."},
            ]
        },
        {
            "district": "Palakkad", "lat": 10.7867, "lon": 76.6548, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Ramaswamy Idli, Palakkad Matta Rice & Elaneer Payasam",
            "description": "The Granary of Kerala and Gateway to God's Own Country through the 30km natural Palakkad Gap in the Western Ghats.",
            "places": [
                {"name": "Palakkad Fort (Tipu's Granite Fort)", "category": "Fort", "entry_fee": 20, "opening": "08:00", "closing": "18:00", "description": "Impeccably preserved 1766 square granite fortress with a water moat and historic temple, built by Hyder Ali."},
                {"name": "Malampuzha Dam & Rock Garden", "category": "Nature", "entry_fee": 30, "opening": "09:00", "closing": "20:00", "description": "Large irrigation reservoir featuring landscaped flower gardens, passenger ropeway, and Nek Chand rock garden."},
                {"name": "Silent Valley National Park (Untouched Rainforest)", "category": "Wildlife", "entry_fee": 150, "opening": "08:00", "closing": "13:00", "description": "Pristine tropical evergreen rainforest in the Kundali Hills sheltering the endangered lion-tailed macaque."},
            ]
        },
        {
            "district": "Pathanamthitta", "lat": 9.2648, "lon": 76.7870, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Aranmula Vallasadhya (64-dish feast) & Appam",
            "description": "Spiritual headquarters of Kerala, pilgrimage portal to Sabarimala nestled amidst Western Ghats rivers.",
            "places": [
                {"name": "Aranmula Parthasarathy Temple & Metal Mirror Workshops", "category": "Cultural", "entry_fee": 0, "opening": "05:00", "closing": "20:00", "description": "Ancient Krishna shrine famed for the annual boat race and the GI-tagged Aranmula Kannadi handmade bronze mirrors."},
                {"name": "Perunthenaruvi Waterfalls", "category": "Waterfall", "entry_fee": 20, "opening": "08:00", "closing": "17:30", "description": "Spectacular cascade on the Pamba River flowing over wide rocky beds into a deep ravine pool."},
            ]
        },
        {
            "district": "Thiruvananthapuram", "lat": 8.5241, "lon": 76.9366, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Trivandrum Boli with Payasam, Puttu & Seafood Fry",
            "description": "Capital of Kerala built across seven hills, home to the richest temple in the world and pristine crescent beaches.",
            "places": [
                {"name": "Sree Padmanabhaswamy Temple", "category": "Temple", "entry_fee": 0, "opening": "03:30", "closing": "19:30", "description": "Ancient Dravidian temple dedicated to Lord Vishnu in Anantha Shayana posture, renowned for its golden gopuram and royal vaults."},
                {"name": "Kovalam Crescent Beaches & Lighthouse", "category": "Beach", "entry_fee": 20, "opening": "06:00", "closing": "20:00", "description": "World-famous trio of crescent beaches (Lighthouse, Hawah, Samudra) lined with palm groves and seafood bistros."},
                {"name": "Napier Museum & Kanakakkunnu Palace", "category": "Museum", "entry_fee": 20, "opening": "10:00", "closing": "16:45", "description": "19th-century Indo-Saracenic gothic museum with natural air-conditioning, bronze sculptures, and royal gardens."},
            ]
        },
        {
            "district": "Thrissur", "lat": 10.5276, "lon": 76.2144, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Thrissur Vellayappam, Kerala Sadhya & Banana Chips",
            "description": "The Cultural Capital of Kerala, epicenter of classical arts, temple festivals, and the majestic Thrissur Pooram.",
            "places": [
                {"name": "Athirappilly Waterfalls (Niagara of India)", "category": "Waterfall", "entry_fee": 50, "opening": "08:00", "closing": "17:00", "description": "80-foot wide thundering cascade on the Chalakudy River in the Sholayar ranges, featured in iconic Indian movies."},
                {"name": "Vadakkunnathan Shiva Temple (UNESCO Awarded)", "category": "Temple", "entry_fee": 0, "opening": "04:00", "closing": "20:30", "description": "Ancient 1,000-year-old temple complex on Thekkinkadu Maidan with wooden carvings and monumental gopurams."},
            ]
        },
        {
            "district": "Wayanad", "lat": 11.6854, "lon": 76.1320, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Wayanad Bamboo Rice Kheer, Malabar Duck & Pepper Chicken",
            "description": "Pristine Western Ghats plateau at 700–2,100m elevation, featuring prehistoric petroglyphs, lakes, and misty peaks.",
            "places": [
                {"name": "Edakkal Caves (Neolithic Rock Carvings)", "category": "Historical", "entry_fee": 50, "opening": "09:00", "closing": "16:00", "description": "Prehistoric rock shelters with 6,000 BCE pictorial engravings from the Neolithic era, located at 1,200m on Ambukuthi Mala."},
                {"name": "Banasura Sagar Dam (Largest Earth Dam in India)", "category": "Nature", "entry_fee": 40, "opening": "09:00", "closing": "17:30", "description": "Largest earthen dam in India and second-largest in Asia, with scenic island clusters on its reservoir."},
                {"name": "Chembra Peak & Heart-Shaped Lake", "category": "Viewpoint", "entry_fee": 750, "opening": "07:00", "closing": "14:00", "description": "Highest summit in Wayanad (2,100m) renowned for the perennial heart-shaped lake (Hridaya Saras) midway to the peak."},
            ]
        },
    ],

    # ==================== 4. TAMIL NADU (38 Districts) ====================
    "Tamil Nadu": [
        {
            "district": "Chennai", "lat": 13.0827, "lon": 80.2707, "crime_index": 27.0, "safety_tier": "LOW",
            "food": "Filter Coffee, Medu Vada, Madras Sambar & Chettinad Chicken",
            "description": "Gateway to South India, major cultural and automotive capital featuring the world's second-longest urban beach.",
            "places": [
                {"name": "Marina Beach & Promenade", "category": "Beach", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "13-kilometer natural sandy urban beach along the Bay of Bengal with colonial memorials and street-food stalls."},
                {"name": "Kapaleeshwarar Temple Mylapore", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "21:30", "description": "7th-century Dravidian Shiva shrine with a 120-foot multicolored gopuram, tank, and classical music assemblies."},
                {"name": "Fort St. George & Clive House", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:00", "description": "First British fortress in India built in 1644, now housing the Tamil Nadu Secretariat and ASI colonial museum."},
            ]
        },
        {
            "district": "Chengalpattu", "lat": 12.6939, "lon": 79.9757, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Mahabalipuram Fresh Catch Seafood & Filter Kaapi",
            "description": "Home to the UNESCO World Heritage monuments of Mamallapuram and serene coastal heritage resorts.",
            "places": [
                {"name": "Shore Temple & Pancha Rathas (UNESCO World Heritage)", "category": "Historical", "entry_fee": 40, "opening": "06:00", "closing": "18:00", "description": "7th-century Pallava monolithic rock-cut shrines facing the Bay of Bengal and Arjuna's Penance giant relief bas-relief."},
                {"name": "Krishna's Butter Ball & Mamallapuram Beach", "category": "Nature", "entry_fee": 40, "opening": "06:00", "closing": "18:00", "description": "Enormous 250-tonne precariously balanced granite boulder perched on a 45-degree smooth rock slope."},
            ]
        },
        {
            "district": "Madurai", "lat": 9.9252, "lon": 78.1198, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Jigarthanda, Madurai Kari Dosa & Bun Parotta",
            "description": "The Athens of the East, 2,500-year-old living temple city planned in concentric lotuses around Meenakshi Amman.",
            "places": [
                {"name": "Meenakshi Amman Temple Complex", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "22:00", "description": "Historic Dravidian temple complex with 14 towering gopurams, Hall of Thousand Pillars, and Golden Lotus Pond."},
                {"name": "Thirumalai Nayakkar Palace", "category": "Palace", "entry_fee": 20, "opening": "09:00", "closing": "17:00", "description": "1636 CE Indo-Saracenic palace renowned for colossal circular masonry pillars and evening sound & light spectacle."},
            ]
        },
        {
            "district": "Thanjavur", "lat": 10.7870, "lon": 79.1378, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Thanjavur Degree Coffee, Ashoka Halwa & South Indian Meals",
            "description": "The Rice Bowl of Tamil Nadu, imperial Chola capital celebrated for the Great Living Chola Temples and bronze casting.",
            "places": [
                {"name": "Brihadisvara Temple (Big Temple - UNESCO World Heritage)", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "Built by Raja Raja Chola I in 1010 CE, featuring a 216-foot granite vimana capped by an 80-tonne single stone dome."},
                {"name": "Thanjavur Maratha Palace & Saraswathi Mahal Library", "category": "Palace", "entry_fee": 50, "opening": "09:00", "closing": "17:30", "description": "Royal complex housing Asia's oldest manuscript library with over 40,000 rare palm-leaf and paper scrolls."},
            ]
        },
        {
            "district": "Nilgiris", "lat": 11.4102, "lon": 76.6950, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Ooty Homemade Chocolates, Varkey & Nilgiri Black Tea",
            "description": "Queen of Hill Stations, misty Blue Mountains at 2,240m elevation famed for the UNESCO mountain railway.",
            "places": [
                {"name": "Nilgiri Mountain Railway (UNESCO Toy Train)", "category": "Heritage", "entry_fee": 300, "opening": "07:10", "closing": "18:00", "description": "Historic 1908 rack-and-pinion steam railway ascending through 16 tunnels and 250 bridges across misty valleys."},
                {"name": "Government Botanical Garden Ooty", "category": "Nature", "entry_fee": 40, "opening": "07:00", "closing": "18:30", "description": "55-acre terraced garden established in 1848 with a 20-million-year-old fossilized tree trunk and exotic flora."},
                {"name": "Doddabetta Peak (Highest in Nilgiris)", "category": "Viewpoint", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "Highest summit in the Nilgiris (2,637m) offering a telescope house and 360-degree views of Tamil Nadu and Kerala."},
            ]
        },
        {
            "district": "Dindigul", "lat": 10.3673, "lon": 77.9803, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Dindigul Thalappakatti Mutton Biryani (GI Tag)",
            "description": "Famous for the historic Dindigul Rock Fort, GI locks, and the serene Princess of Hill Stations, Kodaikanal.",
            "places": [
                {"name": "Kodaikanal Lake & Coaker's Walk", "category": "Hill Station", "entry_fee": 30, "opening": "06:00", "closing": "19:00", "description": "Star-shaped 60-acre artificial lake at 2,285m elevation with pedal boats, cycling, and scenic pedestrian ridge paths."},
                {"name": "Pillar Rocks & Silver Cascade Falls", "category": "Viewpoint", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "Three vertical granite rock pillars standing 122 meters tall, emerging through thick mountain mist."},
            ]
        },
        {
            "district": "Ramanathapuram", "lat": 9.3639, "lon": 78.8395, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Rameswaram Seafood & Traditional South Indian Tiffin",
            "description": "Sacred island pilgrimage gateway to Rameswaram, Pamban Sea Bridge, and the ghost town of Dhanushkodi.",
            "places": [
                {"name": "Ramanathaswamy Temple Rameswaram", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "One of the 12 Jyotirlingas, famous for having the longest pillared corridor in the world with 1,212 carved pillars."},
                {"name": "Pamban Cantilever Rail Bridge", "category": "Heritage", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "India's first sea bridge opened in 1914, featuring a double-leaf bascule section that opens to let ocean ships pass."},
                {"name": "Dhanushkodi Ghost Town & Ram Setu Point", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "17:30", "description": "Submerged sand spit at the confluence of the Bay of Bengal and Indian Ocean, pointing toward Sri Lanka."},
            ]
        },
        {
            "district": "Kanyakumari", "lat": 8.0883, "lon": 77.5385, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Nanjil Fish Curry, Banana Chips & Appam",
            "description": "The Land's End of mainland India, where the Arabian Sea, Bay of Bengal, and Indian Ocean meet in harmony.",
            "places": [
                {"name": "Vivekananda Rock Memorial & Thiruvalluvar Statue", "category": "Spiritual", "entry_fee": 50, "opening": "08:00", "closing": "16:30", "description": "Sacred rock sanctuary where Swami Vivekananda meditated in 1892, facing the colossal 133-foot stone statue of saint Thiruvalluvar."},
                {"name": "Triveni Sangam Sunset & Sunrise Viewpoint", "category": "Viewpoint", "entry_fee": 0, "opening": "05:30", "closing": "19:00", "description": "Mainland India's southernmost tip, uniquely offering simultaneous sunrise and sunset views over the ocean."},
            ]
        },
        {
            "district": "Kanchipuram", "lat": 12.8342, "lon": 79.7036, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Kanchipuram Idli & South Indian Sweets",
            "description": "City of Thousand Temples and pure mulberry silk, home to magnificent Pallava and Chola architectural masterpieces.",
            "places": [
                {"name": "Ekambareswarar Temple (Earth Element - Prithvi Stalam)", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "One of the Pancha Bhoota Sthalams representing Earth, featuring a 194-foot gopuram and a 3,500-year-old mango tree."},
                {"name": "Kailasanathar 8th-Century Pallava Temple", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Oldest sandstone temple structure in Kanchipuram, renowned for intricate 8th-century circumambulatory shrines."},
            ]
        },
        {
            "district": "Coimbatore", "lat": 11.0168, "lon": 76.9558, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Kongunadu Chicken, Arisi Paruppu Sadam & Filter Coffee",
            "description": "Manchester of South India, premier industrial and wellness hub situated at the foothills of the Western Ghats.",
            "places": [
                {"name": "Adiyogi Shiva 112-Foot Statue (Isha Yoga Center)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Guinness World Record largest bust sculpture of Shiva, dedicated to the originator of yoga and inner engineering."},
                {"name": "Marudhamalai Murugan Hill Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "Scenic 12th-century hilltop shrine of Lord Murugan surrounded by Western Ghats medicinal herbs."},
            ]
        },
        {
            "district": "Tiruchirappalli", "lat": 10.7905, "lon": 78.7047, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Trichy Banana Leaf Thali & Filter Coffee",
            "description": "Historic fortress city on the Kaveri River, famous for the colossal Rockfort Temple and Srirangam temple city.",
            "places": [
                {"name": "Rockfort Ucchi Pillayar Temple", "category": "Historical", "entry_fee": 10, "opening": "06:00", "closing": "20:00", "description": "Ancient 7th-century rock citadel rising 83 meters on an 83-meter single quartz rock older than the Himalayas."},
                {"name": "Sri Ranganathaswamy Temple Srirangam", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "World's largest functioning Hindu temple complex covering 156 acres with 21 grand gopurams including the 236-foot Rajagopuram."},
            ]
        },
        {
            "district": "Tirunelveli", "lat": 8.7139, "lon": 77.7567, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Tirunelveli Halwa (Iruttu Kadai Halwa) & Sodhi",
            "description": "Ancient Pandyan city on the perennial Thamirabarani River, world-famous for melt-in-mouth wheat Halwa.",
            "places": [
                {"name": "Nellaiappar Temple & Musical Stone Pillars", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "21:00", "description": "7th-century architectural marvel dedicated to Shiva, with a musical stone pillar hall that rings distinct musical notes."},
                {"name": "Manimuthar & Courtallam Spa Waterfalls", "category": "Waterfall", "entry_fee": 20, "opening": "06:00", "closing": "18:00", "description": "Known as the Spa of South India, cascading waterfalls infused with natural Western Ghats forest herbal properties."},
            ]
        },
        {
            "district": "Tiruvannamalai", "lat": 12.2253, "lon": 79.0747, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Annamalaiyar Temple Prasadam & Filter Coffee",
            "description": "Spiritual heart of Saivism and Advaita, home to the sacred Arunachala Hill and Sri Ramana Maharshi Ashram.",
            "places": [
                {"name": "Annamalaiyar Temple (Fire Element - Agni Stalam)", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "21:30", "description": "One of the Pancha Bhoota Sthalams representing Fire, spanning 25 acres with four colossal gateway gopurams."},
                {"name": "Sri Ramana Maharshi Ashram & Arunachala Girivalam", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "20:30", "description": "World-renowned meditation sanctuary at the base of Arunachala, where millions undertake the 14km barefoot circumambulation."},
            ]
        },
        {
            "district": "Vellore", "lat": 12.9165, "lon": 79.1325, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Vellore Dum Biryani & Makkan Peda",
            "description": "Historic citadel city featuring 16th-century stone moats and the glittering Sripuram Golden Temple.",
            "places": [
                {"name": "Vellore Fort & Jalakanteswarar Temple", "category": "Fort", "entry_fee": 25, "opening": "08:00", "closing": "18:00", "description": "16th-century Vijayanagara granite fortress surrounded by a massive wet moat, housing ornate monolithic stone carvings."},
                {"name": "Sripuram Golden Temple (Malaikodi)", "category": "Spiritual", "entry_fee": 0, "opening": "07:00", "closing": "20:00", "description": "Spiritual sanctuary covered with over 1,500 kilograms of pure gold foil, set within a star-shaped green pathway."},
            ]
        },
        {
            "district": "Salem", "lat": 11.6643, "lon": 78.1460, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Salem Mangoes (Malgova), Thattu Vadai Set & Filter Coffee",
            "description": "Steel City of Tamil Nadu nestled between hills, gateway to the coffee plantations and lakes of Yercaud.",
            "places": [
                {"name": "Yercaud Hill Station & Emerald Lake", "category": "Hill Station", "entry_fee": 20, "opening": "06:00", "closing": "19:00", "description": "Jewel of the Shevaroy Hills at 1,515m elevation featuring coffee groves, spice plantations, and serene boating."},
            ]
        },
        {
            "district": "Erode", "lat": 11.3410, "lon": 77.7172, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bhavani Kudal Fish Curry & Kongu Cuisine",
            "description": "The Turmeric City and textile hub situated on the Kaveri River, famed for sacred river confluences and dams.",
            "places": [
                {"name": "Bhavanisagar Dam & Park", "category": "Nature", "entry_fee": 20, "opening": "09:00", "closing": "18:00", "description": "One of the world's largest earthen dams built across the Bhavani River, featuring expansive children's gardens."},
            ]
        },
        {
            "district": "Cuddalore", "lat": 11.7480, "lon": 79.7714, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Chidambaram Kozhukattai & Coastal Seafood",
            "description": "Coastal pilgrimage district on the Bay of Bengal, home to the Akasa cosmic dancer temple of Chidambaram.",
            "places": [
                {"name": "Chidambaram Nataraja Temple (Space Element - Akasa Stalam)", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "21:30", "description": "Ancient Shiva temple representing the Space element, where Lord Shiva performs the cosmic Ananda Tandava dance."},
                {"name": "Pichavaram Mangrove Forests & Boating", "category": "Nature", "entry_fee": 100, "opening": "08:00", "closing": "17:00", "description": "Second-largest mangrove forest system in the world with over 4,400 water channels and canoe trails."},
            ]
        },
        {
            "district": "Nagapattinam", "lat": 10.7672, "lon": 79.8449, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Nagapattinam Fish Curry & South Indian Tiffin",
            "description": "Major maritime coastal delta port famed for multi-faith pilgrimages to Velankanni and Nagore.",
            "places": [
                {"name": "Basilica of Our Lady of Good Health Velankanni", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Lourdes of the East, sacred Catholic shrine on the shores of the Bay of Bengal visited by millions annually."},
                {"name": "Nagore Dargah (Shahul Hameed)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "21:30", "description": "500-year-old Sufi pilgrimage shrine featuring five elegant minarets, celebrating communal harmony."},
            ]
        },
        {
            "district": "Tenkasi", "lat": 8.9594, "lon": 77.3161, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Courtallam Herbal Tea & Tirunelveli Halwa",
            "description": "Known as South Kashi, nestled below the Western Ghats beside the thunderous cascades of Courtallam.",
            "places": [
                {"name": "Courtallam Main Waterfalls & Five Falls", "category": "Waterfall", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Natural medicinal waterfalls falling across five streams in the Western Ghats, renowned for soothing herbal baths."},
                {"name": "Kasi Viswanathar Temple Tenkasi", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Built in 1455 by Pandya king Parakkirama Pandian, with a majestic 178-foot Raja Gopuram overlooking the mountains."},
            ]
        },
        {
            "district": "Thiruvallur", "lat": 13.1432, "lon": 79.9083, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Tirutani Prasadam & South Indian Tiffin",
            "description": "Gateway district bordering Chennai, home to ancient hill shrines of Murugan and tranquil bird lakes.",
            "places": [
                {"name": "Tiruttani Murugan Temple (Fifth Arupadai Veedu)", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "One of the six sacred abodes of Lord Murugan, perched atop a 365-step hill symbolizing days of the year."},
                {"name": "Pulicat Lake Bird Sanctuary (North TN Zone)", "category": "Wildlife", "entry_fee": 30, "opening": "06:30", "closing": "18:00", "description": "Expansive brackish lagoon famous for flamingos, pelicans, and traditional fishing boats."},
            ]
        },
        # Remaining Tamil Nadu Districts (Ariyalur, Dharmapuri, Kallakurichi, Karur, Krishnagiri, Mayiladuthurai, Namakkal, Perambalur, Pudukkottai, Ranipet, Sivaganga, Theni, Thoothukudi, Tirupathur, Tiruppur, Tiruvarur, Viluppuram, Virudhunagar)
        {
            "district": "Ariyalur", "lat": 11.1401, "lon": 79.0786, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Gangaikonda Cholapuram Feast & Filter Coffee",
            "description": "Ancient imperial capital of the Cholas under Rajendra Chola I, famous for UNESCO monolithic temples and limestone fossils.",
            "places": [
                {"name": "Gangaikonda Cholapuram Temple (UNESCO World Heritage)", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "Magnificent 11th-century living Chola temple with curved vimana and colossal monolithic Nandi built by Rajendra Chola I."},
            ]
        },
        {
            "district": "Dharmapuri", "lat": 12.1211, "lon": 78.1582, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Ragi Kali & Kaveri Fish Fry",
            "description": "Serene agricultural district on the Kaveri River, famous for the roaring Hogenakkal Falls and coracle boating.",
            "places": [
                {"name": "Hogenakkal Falls (Niagara of India on Kaveri)", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Stunning carbonatite rock waterfalls on the Kaveri offering traditional round basket coracle rides and fresh herbal oil baths."},
            ]
        },
        {
            "district": "Kallakurichi", "lat": 11.7384, "lon": 78.9639, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Kalvarayan Forest Honey & Traditional Meals",
            "description": "Known as the Agricultural Basin of Tamil Nadu, blessed with Kalrayan hill tracts, Megam falls, and tribal culture.",
            "places": [
                {"name": "Kalrayan Hills & Periyar Falls", "category": "Waterfall", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Forested hill tract in the Eastern Ghats with tranquil waterfalls, trekking paths, and pleasant climate."},
            ]
        },
        {
            "district": "Karur", "lat": 10.9601, "lon": 78.0766, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Karur Traditional Meals & Filter Coffee",
            "description": "Textile Capital of Tamil Nadu and historic Sangam-era Chera capital on the banks of the sacred Amaravathi River.",
            "places": [
                {"name": "Pasupatheeswarar Temple Karur", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Ancient 7th-century Chola Shiva temple praised in Tevaram hymns, featuring intricate stone carvings."},
            ]
        },
        {
            "district": "Krishnagiri", "lat": 12.5186, "lon": 78.2137, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Krishnagiri Mangoes & South Indian Meals",
            "description": "Land of Black Granite and Mangoes on the Karnataka-Tamil Nadu border, featuring scenic dams and ancient forts.",
            "places": [
                {"name": "Krishnagiri Dam & Reservoir Park", "category": "Nature", "entry_fee": 20, "opening": "09:00", "closing": "18:00", "description": "Picturesque dam across the Thenpennai River with flower gardens, boat rides, and surrounding granite hills."},
            ]
        },
        {
            "district": "Mayiladuthurai", "lat": 11.1075, "lon": 79.6522, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Kumbakonam Degree Coffee & Kaveri Sadhya",
            "description": "Ancient delta spiritual hub on the Kaveri River, surrounded by the sacred Navagraha celestial temples.",
            "places": [
                {"name": "Vaitheeswaran Koil (Navagraha Mars Temple)", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Sacred shrine dedicated to Lord Shiva as the Divine Healer and the presiding temple for planet Mars (Angaraka)."},
                {"name": "Tharangambadi (Tranquebar Danish Coastal Fort)", "category": "Historical", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "17th-century Danish maritime fortress (Fort Dansborg) on the Coromandel coast with Scandinavian architecture."},
            ]
        },
        {
            "district": "Namakkal", "lat": 11.2189, "lon": 78.1674, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Namakkal Chicken Roast & Egg Delicacies",
            "description": "Egg City of India, dominated by a single colossal monolithic rock fort and the Kolli Hills spice range.",
            "places": [
                {"name": "Kolli Hills & Agaya Gangai Waterfalls", "category": "Waterfall", "entry_fee": 25, "opening": "07:00", "closing": "17:00", "description": "Serene mountain range negotiated through 70 hairpin bends, leading to the thundering 300-foot Agaya Gangai cascade."},
                {"name": "Namakkal Anjaneyar Temple & Rock Fort", "category": "Temple", "entry_fee": 0, "opening": "06:30", "closing": "20:30", "description": "Famous for its 18-foot open-air monolithic Hanuman statue carved out of a single granite rock."},
            ]
        },
        {
            "district": "Perambalur", "lat": 11.2342, "lon": 78.8821, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Perambalur Vegetarian Feast & Filter Kaapi",
            "description": "Archaeological wonderland home to 120-million-year-old dinosaur fossils and medieval hill forts.",
            "places": [
                {"name": "Ranjankudi Fort", "category": "Fort", "entry_fee": 0, "opening": "08:30", "closing": "17:30", "description": "17th-century fortress built by the Nawab of the Carnatic, famous for withstanding the Anglo-French Battle of Valikondah in 1751."},
            ]
        },
        {
            "district": "Pudukkottai", "lat": 10.3833, "lon": 78.8001, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Chettinad Paniyaram, Idiyappam & Mutton Chukka",
            "description": "Ancient princely state celebrated for prehistoric dolmens, Jaina rock-cut frescoes, and Chettinad culture.",
            "places": [
                {"name": "Sittannavasal Cave Temples & 7th-Century Frescoes", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Ancient Jain rock-cut monastery renowned for vibrant vegetable-dye ceiling frescoes and acoustic Arivar Koil chamber."},
            ]
        },
        {
            "district": "Ranipet", "lat": 12.9224, "lon": 79.3323, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Arcot Biryani & Makkan Peda",
            "description": "Industrial and historic district on the Palar River, home to the Carnatic capital of Arcot.",
            "places": [
                {"name": "Arcot Delhi Gate & Historic Battle Ramparts", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Historic gateway built by Robert Clive commemorating the Siege of Arcot in 1751."},
            ]
        },
        {
            "district": "Sivaganga", "lat": 9.8433, "lon": 78.4809, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Authentic Chettinad Pepper Chicken, Seeyam & Vellai Paniyaram",
            "description": "Heart of Chettinad, home to palatial merchant mansions, valiant queen Velu Nachiyar, and culinary heritage.",
            "places": [
                {"name": "Chettinad Heritage Mansions Kanadukathan", "category": "Palace", "entry_fee": 50, "opening": "09:00", "closing": "17:30", "description": "Lavish 19th-century merchant palaces decorated with Burma teak, Italian marble, Belgian crystal, and Athangudi tiles."},
            ]
        },
        {
            "district": "Theni", "lat": 10.0104, "lon": 77.4768, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Suruli Herb Water & Kongu Delicacies",
            "description": "Valley paradise nestled between the Western Ghats and Cardamom Hills, lush with grape vineyards and waterfalls.",
            "places": [
                {"name": "Suruli Waterfalls & Meghamalai Tea Hills", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Two-stage 150-foot therapeutic waterfalls originating in the Megamalai mountains, mentioned in the Silappadikaram."},
            ]
        },
        {
            "district": "Thoothukudi", "lat": 8.7642, "lon": 78.1348, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Tuticorin Macaroon (GI Tag) & Coastal Fish Curry",
            "description": "The Pearl City, historic maritime seaport famous for cashew macaroons, salt pans, and coastal temples.",
            "places": [
                {"name": "Thiruchendur Murugan Sea Shore Temple", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "21:30", "description": "Sacred coastal abode of Lord Murugan (Second Arupadai Veedu) situated directly on the shores of the Gulf of Mannar."},
            ]
        },
        {
            "district": "Tirupathur", "lat": 12.4958, "lon": 78.5678, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Yelagiri Jackfruit & South Indian Meals",
            "description": "Hilly green border district featuring the quiet colonial hill resort of Yelagiri and telescope observatories.",
            "places": [
                {"name": "Yelagiri Hills & Punganoor Artificial Lake", "category": "Hill Station", "entry_fee": 20, "opening": "06:00", "closing": "19:00", "description": "Tranquil cluster of 14 tribal villages at 1,110m elevation with boating lakes, rose gardens, and Jalagamparai falls."},
            ]
        },
        {
            "district": "Tiruppur", "lat": 11.1085, "lon": 77.3411, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Tiruppur Kongu Mutton Pallipalayam & Coconut Rice",
            "description": "Knitwear Capital of India, accounting for 90% of cotton knitwear exports, backed by Kongu heritage temples.",
            "places": [
                {"name": "Thirumoorthy Hills & Amanalingeswarar Temple", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Scenic Western Ghats temple situated near a perennial waterfall, dedicated to the holy Trinity on one linga."},
            ]
        },
        {
            "district": "Tiruvarur", "lat": 10.7725, "lon": 79.6366, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Tiruvarur Chariot Feast & Rice Delicacies",
            "description": "Birthplace of the Trinity of Carnatic Music, renowned for Asia's largest temple chariot and Kamalalayam lake.",
            "places": [
                {"name": "Thyagaraja Swamy Temple & Giant Chariot (Aazhi Ther)", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "21:00", "description": "Ancient 30-acre Chola temple complex featuring the largest temple tank in India (Kamalalayam) and 300-tonne wooden chariot."},
            ]
        },
        {
            "district": "Viluppuram", "lat": 11.9401, "lon": 79.4861, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Gingee Millet Dishes & South Indian Tiffin",
            "description": "Centuries-old fortress capital home to Gingee Fort, dubbed the 'Troy of the East' by Chhatrapati Shivaji.",
            "places": [
                {"name": "Gingee Fort (Troy of the East)", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Impregnable citadel spanning three massive rocky hills (Rajagiri, Krishnagiri, Chandrayandurg) with a seven-storey Kalyan Mahal."},
            ]
        },
        {
            "district": "Virudhunagar", "lat": 9.5872, "lon": 77.9514, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Virudhunagar Ennai Parotta & Seeval",
            "description": "Industrial trading and spice center of southern Tamil Nadu, celebrated for crispy oil-fried layered Parottas.",
            "places": [
                {"name": "Srivilliputhur Andal Temple (Emblem of Tamil Nadu)", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Sacred 8th-century birthplace of poetess-saint Andal, whose 193-foot 11-tier gopuram forms the official seal of Tamil Nadu."},
            ]
        },
    ],

    # ==================== 5. TELANGANA (33 Districts) ====================
    "Telangana": [
        {
            "district": "Hyderabad", "lat": 17.3850, "lon": 78.4867, "crime_index": 28.0, "safety_tier": "LOW",
            "food": "Hyderabadi Dum Biryani, Haleem, Double Ka Meetha & Irani Chai",
            "description": "The City of Pearls, 400-year-old Nizami capital blending Qutb Shahi stone architecture with modern cyber hubs.",
            "places": [
                {"name": "Charminar & Laad Bazaar", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Iconic 1591 CE four-minaret monument built by Muhammad Quli Qutb Shah, surrounded by traditional lacquer bangle bazaars."},
                {"name": "Golconda Fort & Sound and Light Show", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Acoustic wonder citadel famed for Koh-i-Noor diamond vaults, secret subterranean passages, and panoramic ramparts."},
                {"name": "Hussain Sagar Lake & Monolithic Buddha", "category": "Lake", "entry_fee": 0, "opening": "08:00", "closing": "22:00", "description": "Heart-shaped historic lake featuring the world's tallest monolithic granite Buddha statue (18 meters, 450 tonnes)."},
                {"name": "Ramoji Film City", "category": "Heritage", "entry_fee": 1350, "opening": "09:00", "closing": "17:30", "description": "Guinness World Record largest film studio complex in the world covering 2,000 acres of cinematic sets and thematic rides."},
            ]
        },
        {
            "district": "Warangal", "lat": 17.9689, "lon": 79.5941, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Warangal Chapala Pulusu & Jowar Rotis",
            "description": "Ancient capital of the Kakatiya Dynasty, world-famed for monolithic stone gateways and star-shaped shrines.",
            "places": [
                {"name": "Warangal Fort & Kakatiya Kala Thoranam (Gateway of Glory)", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "18:00", "description": "13th-century granite fort ruins featuring four majestic ornamental archways that form the official emblem of Telangana."},
                {"name": "Bhadrakali Temple & Lake Promenade", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "21:00", "description": "7th-century Chalukyan lakeside shrine dedicated to Goddess Bhadrakali seated with weapons in eight hands."},
            ]
        },
        {
            "district": "Hanamkonda", "lat": 18.0135, "lon": 79.5445, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Telangana Pachi Pulusu & Sarva Pindi",
            "description": "Cultural twin city of Warangal, home to the architectural wonder Thousand Pillar Temple.",
            "places": [
                {"name": "Thousand Pillar Temple (Rudreswara Swamy)", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "1163 CE Kakatiyan masterpiece built by King Rudra Deva, with star-shaped platforms, perforated stone screens, and black basalt Nandi."},
            ]
        },
        {
            "district": "Mulugu", "lat": 18.1916, "lon": 79.9392, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Tribal Bamboo Chicken & Forest Honey",
            "description": "Forested tribal biodiversity district, home to the UNESCO World Heritage Ramappa Temple and Medaram Jathara.",
            "places": [
                {"name": "Ramappa Temple (UNESCO World Heritage Site)", "category": "Historical", "entry_fee": 40, "opening": "06:00", "closing": "18:00", "description": "1213 CE Kakatiya temple built with floating lightweight bricks, carved bracket figures of dancers, and earthquake-proof sandbox technology."},
                {"name": "Laknavaram Lake & Hanging Suspension Bridge", "category": "Nature", "entry_fee": 50, "opening": "08:00", "closing": "17:30", "description": "10,000-acre medieval reservoir with 13 lush islands connected by pedestrian hanging rope suspension bridges."},
            ]
        },
        {
            "district": "Adilabad", "lat": 19.6641, "lon": 78.5320, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Jowar Roti with Spicy Country Chicken",
            "description": "Forested northern border district of Telangana rich in teak forests, waterfalls, and prehistoric rock art.",
            "places": [
                {"name": "Kuntala Waterfalls (Highest in Telangana)", "category": "Waterfall", "entry_fee": 30, "opening": "08:00", "closing": "17:00", "description": "150-foot thundering natural waterfall on the Kadam River cascading through deep Sahyadri forest canyons."},
                {"name": "Pochera Waterfalls", "category": "Waterfall", "entry_fee": 20, "opening": "08:00", "closing": "17:00", "description": "Wide, amphitheater-like plunge waterfall sliding over ancient basalt rock beds into a deep natural forest gorge."},
            ]
        },
        {
            "district": "Nizamabad", "lat": 18.6725, "lon": 78.0941, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Nizamabad Jowar Gatka & Mutton Curry",
            "description": "Historical agricultural powerhouse along the Godavari River, known for Nizam-era hill forts and water reservoirs.",
            "places": [
                {"name": "Nizamabad Quilla (Raghunatha Hill Fort)", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "10th-century Rashtrakuta hill fortress renovated by the Asaf Jahi rulers, offering a panoramic city view and ancient temple."},
                {"name": "Alisagar Deer Park & Lake", "category": "Nature", "entry_fee": 20, "opening": "09:00", "closing": "18:00", "description": "1928 Nizam royal garden and deer sanctuary with deer herds, treehouses, and island boating."},
            ]
        },
        {
            "district": "Karimnagar", "lat": 18.4386, "lon": 79.1288, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Karimnagar Silver Filigree Crafts & Telangana Thali",
            "description": "Granite and silver filigree center on the Manair River, home to medieval hill bastions and deer parks.",
            "places": [
                {"name": "Elgandal Fort", "category": "Fort", "entry_fee": 0, "opening": "08:30", "closing": "17:30", "description": "Historic hill fort occupied successively by Kakatiya, Bahmani, Qutb Shahi, and Mughal rulers, featuring minarets and deep moats."},
                {"name": "Lower Manair Dam & Deer Park", "category": "Nature", "entry_fee": 20, "opening": "09:00", "closing": "18:30", "description": "Major reservoir with landscaped gardens, speed boating, and sunset views over the Manair valley."},
            ]
        },
        {
            "district": "Khammam", "lat": 17.2473, "lon": 80.1514, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Khammam Mirchi Bajji & Godavari Pulao",
            "description": "Cultural crossroads connecting Telangana to Andhra, dominated by a 1,000-year-old monolithic granite hill fort.",
            "places": [
                {"name": "Khammam Fort (Stambhadri Hill Citadel)", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Built in 950 CE by the Kakatiyas, a massive granite fortress with 60 bastions that blends Hindu and Muslim architecture."},
            ]
        },
        {
            "district": "Bhadradri Kothagudem", "lat": 17.6689, "lon": 80.8920, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Bhadrachalam Prasadam & Bamboo Chicken",
            "description": "Sacred Dandakaranya forest pilgrimage on the banks of the Godavari River, home to Sri Rama's abode.",
            "places": [
                {"name": "Bhadrachalam Sri Sita Ramachandra Swamy Temple", "category": "Temple", "entry_fee": 0, "opening": "04:30", "closing": "21:00", "description": "Renowned 17th-century Vaishnavite temple built by saint-composer Bhakta Ramadasu on the banks of the sacred Godavari."},
                {"name": "Parnasala (Ramayana Exile Hermitage)", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Scenic hermitage 35km from Bhadrachalam where Lord Rama, Sita, and Lakshmana stayed during their exile in Dandakaranya."},
            ]
        },
        {
            "district": "Nalgonda", "lat": 17.0577, "lon": 79.2684, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Nalgonda Jowar Rotis & Natu Kodi Curry",
            "description": "Ancient territory between the Krishna and Musi rivers, famous for the colossal Nagarjuna Sagar Dam and hill forts.",
            "places": [
                {"name": "Nagarjuna Sagar Dam & Hydroelectric Wonder", "category": "Nature", "entry_fee": 20, "opening": "08:00", "closing": "18:00", "description": "World's largest masonry dam across the Krishna River, featuring 26 massive crest gates and lake boat cruises."},
                {"name": "Bhuvanagiri Fort (Bhongir Monolithic Rock)", "category": "Fort", "entry_fee": 25, "opening": "09:00", "closing": "17:30", "description": "Massive 500-foot isolated monolithic granite rock fortress built in the 10th century by Western Chalukya King Tribhuvanamalla."},
            ]
        },
        {
            "district": "Yadadri Bhuvanagiri", "lat": 17.5878, "lon": 78.9482, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Yadagirigutta Prasadam & Telangana Veg Thali",
            "description": "The Spiritual Capital of Telangana, world-renowned for the monumental Dravidian black granite Lakshmi Narasimha temple.",
            "places": [
                {"name": "Yadadri Sri Lakshmi Narasimha Swamy Temple", "category": "Temple", "entry_fee": 0, "opening": "04:00", "closing": "22:00", "description": "Majestic hilltop temple reconstructed with 250,000 tonnes of black Krishna stone (krishnashila), featuring sculpted monolithic pillars."},
                {"name": "Kolanupaka 2,000-Year-Old Jain Temple", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Ancient Jain pilgrimage center featuring a 5-foot emerald jade sculpture of Lord Mahavira and Chalukya carvings."},
            ]
        },
        {
            "district": "Jogulamba Gadwal", "lat": 16.2312, "lon": 77.8016, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Gadwal Zari Saree Crafts & Rayalaseema Pulao",
            "description": "Situated at the sacred confluence of the Krishna and Tungabhadra rivers, home to the 5th Shakti Peetha.",
            "places": [
                {"name": "Alampur Jogulamba Temple (5th Shakti Peetha) & Nava Brahma Temples", "category": "Temple", "entry_fee": 0, "opening": "06:00", "closing": "20:30", "description": "7th-century Badami Chalukyan sandstone temple complex and revered 5th Shakti Peetha at the Sangam."},
                {"name": "Gadwal Fort & Royal Palace", "category": "Fort", "entry_fee": 0, "opening": "09:00", "closing": "18:00", "description": "17th-century mud-and-stone fortress built by Raja Somasekhara Ananda Reddy, housing ancient canons and temples."},
            ]
        },
        {
            "district": "Mahabubnagar", "lat": 16.7488, "lon": 78.0035, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Mahabubnagar Pachi Pulusu, Jowar Roti & Gongura",
            "description": "Known as Palamoor, home to 800-year-old banyan trees, Koilkonda forts, and rich diamond mining history.",
            "places": [
                {"name": "Pillalamarri 800-Year-Old Banyan Tree", "category": "Nature", "entry_fee": 20, "opening": "09:00", "closing": "18:00", "description": "Historic banyan tree spreading across 4 acres, sheltering a mini-zoo, museum, and boating pond."},
                {"name": "Koilkonda Fort & Koilsagar Reservoir", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "17:30", "description": "Qutb Shahi hill fortress reached by climbing deep rocky ravines, overlooking the scenic Koilsagar water reservoir."},
            ]
        },
        {
            "district": "Medak", "lat": 18.0474, "lon": 78.2618, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Medak Jowar Roti & Telangana Country Curries",
            "description": "Historic city featuring Asia's largest cathedral and the 12th-century Kakatiya hill fort.",
            "places": [
                {"name": "Medak Cathedral (Largest in Asia)", "category": "Heritage", "entry_fee": 0, "opening": "07:00", "closing": "18:30", "description": "Magnificent 175-foot Gothic revival cathedral built in 1914, famous for stained glass windows depicting the life of Jesus."},
                {"name": "Medak Fort & 17th-Century Cannon Ramparts", "category": "Fort", "entry_fee": 0, "opening": "08:30", "closing": "17:30", "description": "12th-century Kakatiya stone citadel on a 90-meter hill with three concentric gates and an ancient 3.2-meter bronze cannon."},
            ]
        },
        {
            "district": "Ranga Reddy", "lat": 17.3457, "lon": 78.5522, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Ananthagiri Forest Honey & Telangana Dosa",
            "description": "Surrounds the Hyderabad metropolis with IT corridors, peaceful lakes, and ancient Vishnu temples.",
            "places": [
                {"name": "Statue of Equality (Sri Ramanujacharya 216-Foot Statue)", "category": "Spiritual", "entry_fee": 150, "opening": "11:00", "closing": "20:00", "description": "World's second-tallest metallic sitting statue crafted from panchaloha, commemorating the 11th-century social reformer."},
                {"name": "Chilkur Balaji Temple (Visa Balaji Temple)", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "20:00", "description": "Ancient 500-year-old temple on the banks of Osman Sagar, unique in India for having no VIP queues or hundi donations."},
            ]
        },
        {
            "district": "Medchal-Malkajgiri", "lat": 17.6297, "lon": 78.4814, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "Shamirpet Biryani & Irani Chai",
            "description": "Northern urban corridor of Hyderabad featuring pharmaceutical hubs, deer parks, and scenic lakes.",
            "places": [
                {"name": "Shamirpet Lake & Deer Park", "category": "Nature", "entry_fee": 20, "opening": "09:00", "closing": "18:00", "description": "Picturesque artificial lake surrounded by rocky boulders, teak forests, and a flourishing deer sanctuary."},
            ]
        },
        {
            "district": "Siddipet", "lat": 18.1018, "lon": 78.8520, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Gollabhama Saree Weaving & Telangana Pulao",
            "description": "Rapidly advancing cultural and lakefront city celebrated for GI-tagged Gollabhama sarees and Komuravelli temple.",
            "places": [
                {"name": "Komuravelli Mallanna Temple", "category": "Temple", "entry_fee": 0, "opening": "05:30", "closing": "20:30", "description": "Ancient rock-cave temple of Lord Shiva as Mallikarjuna Swamy atop the Indrakeeladri hillock."},
                {"name": "Komalavancha Eco Park & Ranganayaka Sagar Reservoir", "category": "Nature", "entry_fee": 20, "opening": "08:00", "closing": "19:00", "description": "Modern Kaleshwaram Lift Irrigation project reservoir featuring a panoramic island viewpoint and gardens."},
            ]
        },
        {
            "district": "Vikarabad", "lat": 17.3364, "lon": 77.9048, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Ananthagiri Herbal Tea & Telangana Tiffin",
            "description": "Popular trekking and eco-tourism weekend getaway, source of the sacred Musi River in the Ananthagiri Hills.",
            "places": [
                {"name": "Ananthagiri Hills & Sri Anantha Padmanabha Swamy Temple", "category": "Hill Station", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Dense forest hill range with panoramic trekking trails, ancient cave temples, and medicinal herbal air."},
                {"name": "Kotepally Reservoir & Kayaking", "category": "Adventure", "entry_fee": 100, "opening": "09:00", "closing": "17:30", "description": "Serene water reservoir offering tranquil kayaking, lakeside camping, and sunset views."},
            ]
        },
        # Remaining Telangana Districts (Jagtial, Jangaon, Jayashankar Bhupalpally, Kamareddy, Kumuram Bheem Asifabad, Mahabubabad, Mancherial, Nagarkurnool, Narayanpet, Nirmal, Peddapalli, Rajanna Sircilla, Sangareddy, Suryapet, Wanaparthy)
        {
            "district": "Jagtial", "lat": 18.7946, "lon": 78.9125, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Jagtial Mangoes & Telangana Sweets",
            "description": "Historic territory between the Godavari River and Sahyadri ranges, home to the star-shaped Jagtial Fort.",
            "places": [
                {"name": "Jagtial Star Fort", "category": "Fort", "entry_fee": 0, "opening": "08:30", "closing": "17:30", "description": "17th-century European star-shaped fortress built with lime and mortar by French engineers for the Nizam."},
                {"name": "Dharmapuri Sri Lakshmi Narasimha Swamy Temple", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "20:00", "description": "Ancient temple on the banks of the sacred Godavari, celebrated for Vedic scholarship and river ghats."},
            ]
        },
        {
            "district": "Jangaon", "lat": 17.7231, "lon": 79.1818, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Pembrathi Metal Crafts & Jowar Rotis",
            "description": "Ancient crafts and brassware hub famed for the UNESCO-recognized Pembarthi sheet metal art.",
            "places": [
                {"name": "Pembarthi Brass Metal Crafts Village", "category": "Cultural", "entry_fee": 0, "opening": "09:00", "closing": "18:00", "description": "Centuries-old artisanal village renowned for handcrafted bronze, brass statues, and temple vahanas."},
            ]
        },
        {
            "district": "Jayashankar Bhupalpally", "lat": 18.4312, "lon": 79.8647, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Country Chicken Curry & Rice",
            "description": "Mineral-rich forested district bordered by the Godavari River, home to ancient Kakatiya temple architecture.",
            "places": [
                {"name": "Kaleshwaram Mukteswara Swamy Temple", "category": "Temple", "entry_fee": 0, "opening": "04:30", "closing": "21:00", "description": "Unique Shaivite temple on the Triveni Sangam (Godavari, Pranahita, Saraswati) housing two Shiva lingas on a single pedestal."},
            ]
        },
        {
            "district": "Kamareddy", "lat": 18.3225, "lon": 78.3411, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kamareddy Jowar Roti & Country Chicken",
            "description": "Connecting Hyderabad to Nizamabad, celebrated for Domakonda Fort and historic temples.",
            "places": [
                {"name": "Domakonda Fort (UNESCO Awarded Heritage Structure)", "category": "Fort", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "18th-century royal palace and fortress restored meticulously, winning the UNESCO Asia-Pacific Award for Cultural Heritage Conservation."},
            ]
        },
        {
            "district": "Kumuram Bheem Asifabad", "lat": 19.3582, "lon": 79.2848, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Tribal Millets & Wild Honey",
            "description": "Dense teak-covered tribal district named after Gond martyr Kumuram Bheem, rich in wildlife and waterfalls.",
            "places": [
                {"name": "Mitte Waterfalls (Saptha Gundalu)", "category": "Waterfall", "entry_fee": 20, "opening": "08:00", "closing": "17:00", "description": "Series of seven breathtaking natural waterfalls tumbling through deep virgin deciduous forests."},
            ]
        },
        {
            "district": "Mahabubabad", "lat": 17.5991, "lon": 80.0039, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Kuravi Prasadam & Telangana Thali",
            "description": "Historic Kakatiya district rich in tribal festivals, ancient temples, and granite hill tracks.",
            "places": [
                {"name": "Kuravi Veerabhadra Swamy Temple", "category": "Temple", "entry_fee": 0, "opening": "05:00", "closing": "20:30", "description": "Ancient 9th-century Rashtrakuta temple celebrated for annual Maha Shivaratri tribal jatharas."},
            ]
        },
        {
            "district": "Mancherial", "lat": 18.8679, "lon": 79.4639, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Godavari Fish Fry & Jowar Rotis",
            "description": "Industrial and wildlife district on the Godavari River, home to tiger sanctuaries and ancient dinosaur fossils.",
            "places": [
                {"name": "Kawal Tiger Reserve (Jannaram)", "category": "Wildlife", "entry_fee": 100, "opening": "06:30", "closing": "17:30", "description": "Pristine dry deciduous forest reserve sheltering tigers, leopards, barking deer, and Indian bison."},
            ]
        },
        {
            "district": "Nagarkurnool", "lat": 16.4854, "lon": 78.3323, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Chenchu Forest Honey & Ragi Mudde",
            "description": "Home to the Nallamala tiger forests, Chenchu indigenous tribes, and prehistoric cave dwellings.",
            "places": [
                {"name": "Amrabad Tiger Reserve & Nallamala Viewpoint", "category": "Wildlife", "entry_fee": 150, "opening": "07:00", "closing": "16:30", "description": "Second-largest tiger reserve in India spanning deep Nallamala canyons along the Krishna River."},
            ]
        },
        {
            "district": "Narayanpet", "lat": 16.7369, "lon": 77.4989, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Narayanpet Handloom Zari Sweets & Jowar Roti",
            "description": "Celebrated worldwide for vibrant, GI-tagged Narayanpet handloom silk and cotton sarees.",
            "places": [
                {"name": "Narayanpet Handloom Silk Weaving Centers", "category": "Cultural", "entry_fee": 0, "opening": "09:00", "closing": "18:00", "description": "Centuries-old artisanal weaving centers blending Maharashtrian and Telugu handloom traditions."},
            ]
        },
        {
            "district": "Nirmal", "lat": 19.0964, "lon": 78.3444, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Nirmal Toys & Paintings & Gongura Pulao",
            "description": "400-year-old traditional toy and lacquer craft capital, blessed with the roaring Kadam Dam.",
            "places": [
                {"name": "Nirmal Wooden Toys & Lacquerware Workshops", "category": "Cultural", "entry_fee": 0, "opening": "09:00", "closing": "18:30", "description": "Centuries-old artisanal colony producing world-renowned painted wooden toys from Poniki wood."},
                {"name": "Kadam Dam Reservoir", "category": "Nature", "entry_fee": 20, "opening": "09:00", "closing": "17:30", "description": "Major dam built across the Kadam River amidst forested hills, ideal for birdwatching and picnics."},
            ]
        },
        {
            "district": "Peddapalli", "lat": 18.6163, "lon": 79.3831, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Peddapalli Mutton & Jowar Roti",
            "description": "The Power City of Telangana with Ramagundam thermal plants and ancient Buddhist excavation sites.",
            "places": [
                {"name": "Dhulikatta Buddhist Stupa Ruins", "category": "Historical", "entry_fee": 0, "opening": "09:00", "closing": "17:00", "description": "2nd-century BCE Satavahana Buddhist stupa and fortified ancient town archaeological site."},
            ]
        },
        {
            "district": "Rajanna Sircilla", "lat": 18.3888, "lon": 78.8052, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Vemulawada Prasadam & Rice Delicacies",
            "description": "Textile City of Telangana, celebrated for the holy Vemulawada Raja Rajeshwara Swamy Temple.",
            "places": [
                {"name": "Vemulawada Sri Raja Rajeshwara Swamy Temple (Dakshina Kasi)", "category": "Temple", "entry_fee": 0, "opening": "04:30", "closing": "21:00", "description": "Major medieval pilgrimage shrine dedicated to Shiva, where devotees perform the Kode Mokku (sacred bull-tying) vow."},
            ]
        },
        {
            "district": "Sangareddy", "lat": 17.6190, "lon": 78.0818, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Singur Fish Curry & Irani Chai",
            "description": "Western industrial and historic gateway to Hyderabad, home to the Singur Dam and Manjeera Crocodile Sanctuary.",
            "places": [
                {"name": "Manjeera Wildlife & Crocodile Sanctuary", "category": "Wildlife", "entry_fee": 30, "opening": "09:00", "closing": "17:30", "description": "Riverine wildlife sanctuary on the Manjeera River sheltering mugger crocodiles and migratory birds."},
            ]
        },
        {
            "district": "Suryapet", "lat": 17.1439, "lon": 79.6239, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Suryapet Mirchi Bajji & Jowar Rotis",
            "description": "The Gateway of Telangana on the Hyderabad-Vijayawada highway, rich in Buddhist monuments and Kakatiya temples.",
            "places": [
                {"name": "Phanigiri Buddhist Stupa Site", "category": "Historical", "entry_fee": 0, "opening": "09:00", "closing": "17:30", "description": "1st-century CE hilltop Buddhist monastic site featuring carved toranas, octagonal stupas, and viharas."},
            ]
        },
        {
            "district": "Wanaparthy", "lat": 16.3622, "lon": 78.0622, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Wanaparthy Royal Pulao & Sweets",
            "description": "Ancient Samsthanam princely state with grand palaces, stone temples, and royal stepwells.",
            "places": [
                {"name": "Wanaparthy Palace (Raja Rameshwar Rao Samsthanam)", "category": "Palace", "entry_fee": 0, "opening": "09:00", "closing": "17:30", "description": "19th-century royal palace blending Rajasthani and European architecture, now housing public institutions."},
            ]
        },
    ],
}
