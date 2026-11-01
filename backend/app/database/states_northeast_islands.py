"""
Northeast India and Island / Coastal UTs Master Districts & Tourist Attractions
Covers:
- Arunachal Pradesh (26)
- Assam (35)
- Manipur (16)
- Meghalaya (12)
- Mizoram (11)
- Nagaland (16)
- Sikkim (6)
- Tripura (8)
- Andaman and Nicobar Islands (3)
- Dadra and Nagar Haveli and Daman and Diu (3)
- Lakshadweep (1)
- Puducherry (4)
Total: 141 Districts
"""

NORTHEAST_ISLANDS_STATES = {
    # ==================== 1. ARUNACHAL PRADESH (26 Districts) ====================
    "Arunachal Pradesh": [
        {
            "district": "Tawang", "lat": 27.5861, "lon": 91.8594, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Thukpa, Zan, Momos, Butter Tea & Gyapa Khazi",
            "description": "High-altitude Himalayan wonderland famed for India's largest Buddhist monastery and snow-capped passes.",
            "places": [
                {"name": "Tawang Monastery (Galden Namgey Lhatse)", "category": "Monastery", "entry_fee": 20, "opening": "07:00", "closing": "19:00", "description": "Founded in 1680–81 by Merak Lama, this is India's largest and the world's second-largest Tibetan Buddhist monastery."},
                {"name": "Sela Pass & Sela Lake (13,700 ft)", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "High-altitude mountain pass connecting Tawang with Guwahati, flanked by the crystal clear sacred Sela Lake."},
                {"name": "Sangetsar Lake (Madhuri Lake)", "category": "Nature", "entry_fee": 0, "opening": "08:00", "closing": "16:00", "description": "Scenic glacial lake surrounded by snow peaks and dead pine tree trunks created by an earthquake in 1950."},
            ]
        },
        {
            "district": "West Kameng", "lat": 27.2644, "lon": 92.4159, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Khura buckwheat pancakes, Momos & Apong rice brew",
            "description": "Scenic Himalayan valleys, apple orchards, and historic Buddhist monasteries at Bomdila and Dirang.",
            "places": [
                {"name": "Bomdila Monastery (Gentse Gaden)", "category": "Monastery", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Magnificent monastery established in 1965 with panoramic views of the Eastern Himalayan peaks."},
                {"name": "Dirang Valley & Hot Water Springs", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Picturesque valley on the banks of Kameng River with medicinal sulphur hot springs and kiwi orchards."},
            ]
        },
        {
            "district": "East Kameng", "lat": 27.3300, "lon": 93.0300, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Bamboo shoot pork, Puta, Lukter & boiled green leafy stews",
            "description": "Lush forested district on the Kameng River famous for white-water rafting and Nyishi tribal culture.",
            "places": [
                {"name": "Pakke Tiger Reserve (Pakhui Wildlife Sanctuary)", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "17:00", "description": "Sanctuary renowned for the conservation of four species of Hornbills in the Himalayan foothills."},
                {"name": "Seppa Riverside & Kameng Rapids", "category": "Adventure", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "District headquarters on the swirling Kameng River offering world-class angling and river rafting expeditions."},
            ]
        },
        {
            "district": "Pakke-Kessang", "lat": 27.1200, "lon": 93.1800, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Boiled rice with fish cooked in bamboo hollows & fermented soybean",
            "description": "Pristine ecological corridor blessed with evergreen rainforests, waterfalls, and wildlife biodiversity.",
            "places": [
                {"name": "Lemking Waterfalls & Evergreen Valley", "category": "Waterfall", "entry_fee": 0, "opening": "07:00", "closing": "17:00", "description": "Spectacular cascade cascading through untamed sub-tropical forests ideal for bird-watching and nature hikes."},
            ]
        },
        {
            "district": "Papum Pare", "lat": 27.1004, "lon": 93.6166, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Chura Sabji, Dung Po steamed rice & Lukter spicy dried meat",
            "description": "Administrative heartland of Arunachal Pradesh featuring historic fort ruins, lakes, and botanical wealth.",
            "places": [
                {"name": "Ita Fort (Fort of Bricks)", "category": "Historical", "entry_fee": 15, "opening": "09:00", "closing": "17:00", "description": "14th–15th century irregular-shaped brick fortress built during the Chutiya kingdom rule in Itanagar."},
                {"name": "Ganga Lake (Gyakar Sinyi)", "category": "Nature", "entry_fee": 20, "opening": "08:00", "closing": "17:00", "description": "Picturesque green lake shrouded by primeval evergreen trees, tall bamboo, and orchid orchids."},
                {"name": "Jawaharlal Nehru State Museum", "category": "Museum", "entry_fee": 20, "opening": "10:00", "closing": "16:30", "description": "Exhibits rich tribal heritage, musical instruments, wood carvings, textiles, and archaeological finds of Arunachal."},
            ]
        },
        {
            "district": "Itanagar Capital Complex", "lat": 27.0844, "lon": 93.6053, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Traditional Nyishi smoked meat, Apong, Puta & Momos",
            "description": "State capital hub featuring modern institutions, Buddhist Gompa, and cultural exhibition centers.",
            "places": [
                {"name": "Theravada Gompa (Buddha Vihar)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Consecrated Buddhist shrine perched on a hilltop offering serene views of Itanagar city below."},
                {"name": "Indira Gandhi Park", "category": "Park", "entry_fee": 10, "opening": "06:00", "closing": "19:00", "description": "Sprawling public park with blooming gardens, children's play area, and morning walking tracks."},
            ]
        },
        {
            "district": "Kurung Kumey", "lat": 27.9100, "lon": 93.3500, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Nyishi smoked pork with bamboo shoot, Pika Pila pickle",
            "description": "Rugged mountainous frontier along the Kurung and Kumey rivers known for deep gorges and traditional suspension bridges.",
            "places": [
                {"name": "Koloriang River Valley & Paro Hanging Bridge", "category": "Adventure", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "Picturesque hanging cane and bamboo suspension bridge spanning the raging Kurung River amidst mist-laden peaks."},
            ]
        },
        {
            "district": "Kra Daadi", "lat": 27.8500, "lon": 93.5500, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Steamed red rice, dried fish chutney, boiled pumpkin leaves",
            "description": "Picturesque highlands centered around Palin and Jamin, inhabited by Nyishi tribes maintaining ancient customs.",
            "places": [
                {"name": "Palin Holy Rosary Catholic Church & Hilltop", "category": "Viewpoint", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Elevated viewpoint overlooking the Palin valley and dramatic Himalayan ridge-lines."},
            ]
        },
        {
            "district": "Lower Subansiri", "lat": 27.5950, "lon": 93.8340, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Apatani fish cooked in bamboo stem, Pikey Pila, Marua millet beer",
            "description": "Famed for Ziro Valley, UNESCO World Heritage tentative site, unique Apatani wet-rice cultivation and music festivals.",
            "places": [
                {"name": "Ziro Valley Pine Groves & Apatani Villages", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Enchanting plateau with lush terraced paddy fields, pine-clad hills, and unique Apatani culture."},
                {"name": "Kardo Shiva Lingam (Siddheshwar Nath)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Massive natural rock formation resembling a 25-foot Shiva Lingam discovered amidst pristine bamboo forests."},
                {"name": "Meghna Cave Temple", "category": "Spiritual", "entry_fee": 0, "opening": "07:00", "closing": "17:00", "description": "Ancient 5000-year-old carved cave temple dedicated to Lord Lakulisha nestled at an elevation of 3000 feet."},
            ]
        },
        {
            "district": "Upper Subansiri", "lat": 27.9900, "lon": 94.2200, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Tagin smoked meat, boiled roots, local corn cakes",
            "description": "Mountainous home of the Tagin and Galo tribes, featuring the crystal Subansiri River and limestone caves.",
            "places": [
                {"name": "Menga Cave Temple", "category": "Spiritual", "entry_fee": 0, "opening": "07:00", "closing": "17:30", "description": "Natural limestone cave dedicated to Lord Shiva near Daporijo, attracting pilgrims during Maha Shivaratri."},
            ]
        },
        {
            "district": "Kamle", "lat": 27.7500, "lon": 94.0200, "crime_index": 11.0, "safety_tier": "LOW",
            "food": "Smoked river fish, bamboo shoot curry & indigenous rice dishes",
            "description": "Carved out along the Kamle River, dotted with peaceful villages like Raga and unspoiled river trails.",
            "places": [
                {"name": "Raga Valley & Kamle River Confluence", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "Breathtaking river gorge surrounded by lush sub-tropical evergreen vegetation and terraced farming."},
            ]
        },
        {
            "district": "West Siang", "lat": 28.1670, "lon": 94.7950, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Galo smoked meat, Lukter, boiled colocasia & millet brew",
            "description": "Cultural center of the Galo tribe at Aalo (Along), surrounded by orange orchards and bamboo bridges.",
            "places": [
                {"name": "Aalo (Along) Darka Village & Hanging Bridge", "category": "Cultural", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Largest village in West Siang showcasing traditional Galo stilt houses and suspension rope bridges over the Siyom River."},
                {"name": "Patum Zoo & Eco Park", "category": "Wildlife", "entry_fee": 20, "opening": "09:00", "closing": "16:30", "description": "Houses regional wildlife including Himalayan black bears, serows, and exotic pheasants."},
            ]
        },
        {
            "district": "Siang", "lat": 28.3200, "lon": 94.9500, "crime_index": 11.0, "safety_tier": "LOW",
            "food": "Adi fish in bamboo pipe, leafy potherbs & Apong",
            "description": "Rugged district centered around Boleng and Pangin, where the mighty Siyom meets the Siang River.",
            "places": [
                {"name": "Pangin Confluence of Siang and Siyom Rivers", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Spectacular natural site where the blue waters of the Siyom River blend into the turquoise Siang River."},
            ]
        },
        {
            "district": "Upper Siang", "lat": 28.6100, "lon": 94.9900, "crime_index": 11.0, "safety_tier": "LOW",
            "food": "Memba and Khamba butter tea, tsampa, dried yak meat",
            "description": "Northern frontier where the Brahmaputra (Siang) enters India from Tibet, surrounded by sacred peaks.",
            "places": [
                {"name": "Mouling National Park", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "16:00", "description": "Bio-diverse biosphere named after Mouling Peak, home to takins, red pandas, and clouded leopards."},
                {"name": "Tuting Sacred Circuit & Tsangpo Gorges", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Spiritual heart of the Memba Buddhists, gateway to sacred pilgrimage trails along the mighty Tsangpo bends."},
            ]
        },
        {
            "district": "East Siang", "lat": 28.0667, "lon": 95.3333, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Adi Smoked Pork, Bamboo Shoot Curry, Puta & Apong",
            "description": "Arunachal's oldest town, Pasighat, perched where the Siang leaves the Himalayas and enters the plains.",
            "places": [
                {"name": "Daying Ering Memorial Wildlife Sanctuary", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "17:00", "description": "Riverine island sanctuary on the Siang River hosting migratory waterfowls and endangered Bengal floricans."},
                {"name": "Bodak Scenic Point & Siang Rapids", "category": "Adventure", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Picturesque bend on the Siang River surrounded by forested crags, popular for angling and white-water kayaking."},
            ]
        },
        {
            "district": "Lower Siang", "lat": 27.8800, "lon": 94.6700, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Steamed pitha, river fish boiled with ginger and chilies",
            "description": "Foothill district home to Malinithan, an ancient Hindu archaeological temple complex.",
            "places": [
                {"name": "Malinithan Archaeological Temple Ruins", "category": "Historical", "entry_fee": 25, "opening": "07:00", "closing": "17:30", "description": "14th-century granite stone temple ruins dedicated to Goddess Durga, featuring exquisite Orissan-style carvings."},
            ]
        },
        {
            "district": "Lepa Rada", "lat": 27.9700, "lon": 94.6500, "crime_index": 11.0, "safety_tier": "LOW",
            "food": "Galo traditional fermented bamboo shoots & smoked fish",
            "description": "Basar eco-tourism hub famous for mysterious underground caves, waterfalls, and cultural festivals.",
            "places": [
                {"name": "Basar Bat Cave (Podi Rbi Cave) & Bumi Falls", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "16:30", "description": "Enchanting limestone cave system inhabited by fruit bats, complemented by the roaring Bumi waterfalls."},
            ]
        },
        {
            "district": "Shi Yomi", "lat": 28.6000, "lon": 94.1300, "crime_index": 10.0, "safety_tier": "LOW",
            "food": "Memba Tsampa, Yak butter tea & handmade cheese",
            "description": "Pristine Mechuka Valley, often called the mini Switzerland of India, situated near the Indo-Tibet border.",
            "places": [
                {"name": "Mechuka (Menchukha) Valley", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Picturesque glacial valley at 6,000 feet surrounded by pine forests, snow-clad peaks, and the Yargyapchu River."},
                {"name": "Samten Yongcha Monastery (400-year-old)", "category": "Monastery", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Ancient Tibetan Buddhist monastery of the Gelugpa sect perched atop a scenic hilltop overlooking Mechuka."},
            ]
        },
        {
            "district": "Dibang Valley", "lat": 28.7800, "lon": 95.8200, "crime_index": 10.0, "safety_tier": "LOW",
            "food": "Idu Mishmi smoked game meat, wild herbal roots, rice wine",
            "description": "India's least populated district, boasting untamed alpine beauty, Anini town, and the Seven Lakes Trek.",
            "places": [
                {"name": "Anini & Seven Lakes Trek Trail", "category": "Adventure", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "High alpine glacial lakes expedition nestled among emerald meadows and rocky ridges of the Mishmi Hills."},
            ]
        },
        {
            "district": "Lower Dibang Valley", "lat": 28.1400, "lon": 95.8300, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Idu Mishmi dried fish broth, tender bamboo shoots & rice beer",
            "description": "Centred around Roing, featuring ancient fort ruins, Mayudia snowy pass, and Mehao wildlife sanctuary.",
            "places": [
                {"name": "Mayudia Pass (Snow Pass)", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "Picturesque mountain pass at 8,711 feet that experiences heavy snowfall during winter, surrounded by oak forests."},
                {"name": "Bhismaknagar Fort Ruins", "category": "Historical", "entry_fee": 15, "opening": "08:00", "closing": "16:30", "description": "8th-century burnt-brick fortress built by Chutiya kings, linked to the legend of Princess Rukmini and Lord Krishna."},
            ]
        },
        {
            "district": "Anjaw", "lat": 28.0200, "lon": 96.5300, "crime_index": 10.0, "safety_tier": "LOW",
            "food": "Mishmi maize dishes, wild cardamom tea & smoked mountain trout",
            "description": "Easternmost district of India, where the first rays of the sun kiss Indian soil at Dong Valley.",
            "places": [
                {"name": "Dong Valley (India's First Sunrise Point)", "category": "Nature", "entry_fee": 0, "opening": "04:00", "closing": "18:00", "description": "Breathtaking peak at the tri-junction of India, China, and Myanmar where dawn breaks earliest in India around 4:30 AM."},
                {"name": "Walong War Memorial (1962 Battle of Walong)", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Hallowed memorial commemorating the valiant Indian soldiers who held off advancing forces during the 1962 war."},
            ]
        },
        {
            "district": "Lohit", "lat": 27.9170, "lon": 96.1670, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Spicy fish curry, bamboo shoot pickle & fragrant Joha rice",
            "description": "Famous for holy Parashuram Kund on the Lohit River, attracting thousands of Hindu pilgrims on Makar Sankranti.",
            "places": [
                {"name": "Parashuram Kund Holy Pilgrimage Shrine", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "19:00", "description": "Sacred water kund on the lower reaches of the Lohit River where Sage Parashuram washed away his sins with a dip."},
                {"name": "Tezu Botanical Garden & Glow Lake", "category": "Nature", "entry_fee": 20, "opening": "08:00", "closing": "17:00", "description": "Picturesque high-altitude lake surrounded by lush subtropical wildlife and alpine meadows."},
            ]
        },
        {
            "district": "Namsai", "lat": 27.6700, "lon": 95.8700, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Tai Khamti Khao Lam (sticky rice in bamboo), Paa Saa fish soup",
            "description": "Land of the Tai Khamti and Singpho people, renowned for majestic Golden Pagoda and Theravada Buddhist culture.",
            "places": [
                {"name": "Golden Pagoda of Namsai (Kongmu Kham)", "category": "Spiritual", "entry_fee": 20, "opening": "06:00", "closing": "19:00", "description": "Breathtaking Burmese-style golden pagoda spread over 20 hectares, a prominent Theravada Buddhist monument."},
                {"name": "Chongkham Khamti Cultural Heritage Village", "category": "Cultural", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Scenic riverside village showcasing Tai Khamti stilt architecture, woven silks, and sacred monasteries."},
            ]
        },
        {
            "district": "Changlang", "lat": 27.1500, "lon": 95.7300, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Singpho bamboo-cooked tea (Phalap), smoked duck & sticky rice",
            "description": "Home to Namdapha National Park, India's third-largest national park, and historic World War II Stilwell Road.",
            "places": [
                {"name": "Namdapha National Park & Tiger Reserve", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "17:00", "description": "Sprawling biodiversity hotspot harboring four wild cat species: Tiger, Leopard, Snow Leopard, and Clouded Leopard."},
                {"name": "Jairampur World War II Military Cemetery", "category": "Historical", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Historic burial ground for Allied soldiers and workers who laid down their lives constructing the Stilwell (Ledo) Road."},
            ]
        },
        {
            "district": "Tirap", "lat": 27.0200, "lon": 95.5000, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Nocte millet bread, smoked pork with local chilies",
            "description": "Centred around Khonsa, showcasing traditional Nocte tribal culture, headman woodcarvings, and scenic ridges.",
            "places": [
                {"name": "Khonsa Museum of Tribal Arts & Hills", "category": "Museum", "entry_fee": 15, "opening": "09:30", "closing": "16:30", "description": "Exhibits intricate woodcarvings, weapons, bead ornaments, and headgear worn during the Chalo Loku festival."},
            ]
        },
        {
            "district": "Longding", "lat": 26.8500, "lon": 95.3000, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Wancho smoked meat, roasted tubers & fermented rice beverage",
            "description": "Homeland of the Wancho tribe, known for master woodcraft, gunsmithing, and vibrant Oriah festival celebrations.",
            "places": [
                {"name": "Wakka & Pongchau Wancho Heritage Villages", "category": "Cultural", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Traditional villages featuring large thatch-roofed chief's longhouses with totem poles carved from single logs."},
            ]
        },
    ],

    # ==================== 2. ASSAM (35 Districts) ====================
    "Assam": [
        {
            "district": "Kamrup Metropolitan", "lat": 26.1445, "lon": 91.7362, "crime_index": 28.0, "safety_tier": "MEDIUM",
            "food": "Assamese Thali, Masor Tenga (sour fish), Khar, Duck Curry & Pitha",
            "description": "Gateway to Northeast India, housing Guwahati, ancient Shakti shrines, and the mighty Brahmaputra riverfront.",
            "places": [
                {"name": "Maa Kamakhya Devalaya (Nilachal Hill)", "category": "Spiritual", "entry_fee": 0, "opening": "05:30", "closing": "20:00", "description": "One of the 51 sacred Shakti Peethas, honoring the mother goddess and host of the famous annual Ambubachi Mela."},
                {"name": "Umananda Island Temple (Peacock Island)", "category": "Spiritual", "entry_fee": 20, "opening": "06:00", "closing": "17:30", "description": "17th-century Shiva temple built by King Gadadhar Singha on the smallest inhabited river island in the world."},
                {"name": "Assam State Museum & Dighalipukhuri", "category": "Museum", "entry_fee": 20, "opening": "10:00", "closing": "17:00", "description": "Premier repository of sculptures, royal Ahom armour, epigraphy, and natural history specimens."},
                {"name": "Brahmaputra River Ropeway & Sunset Cruise", "category": "Viewpoint", "entry_fee": 150, "opening": "08:00", "closing": "20:00", "description": "Longest river ropeway in India connecting Guwahati to North Guwahati with sweeping views of the mighty river."},
            ]
        },
        {
            "district": "Kamrup", "lat": 26.3100, "lon": 91.5600, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Sualkuchi Pitha, Koldil (banana flower) chicken, Jolpan",
            "description": "Historic silk weaving hub at Sualkuchi and spiritual confluence of religions at Hajo.",
            "places": [
                {"name": "Hajo (Hayagriva Madhava Temple & Powa Mecca)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Unique syncretic pilgrimage center sacred to Hindus, Buddhists, and Muslims on the banks of Brahmaputra."},
                {"name": "Sualkuchi Silk Weaving Village (Manchester of Assam)", "category": "Cultural", "entry_fee": 0, "opening": "08:00", "closing": "19:00", "description": "Renowned center for handwoven golden Muga and white Paat silk sarees, mekhela chadors, and craft workshops."},
                {"name": "Madan Kamdev Archaeological Temple Complex", "category": "Historical", "entry_fee": 25, "opening": "08:00", "closing": "17:00", "description": "10th–12th century erotic and classical stone temple ruins built by the Pala dynasty, dubbed the Khajuraho of Assam."},
            ]
        },
        {
            "district": "Golaghat", "lat": 26.5167, "lon": 93.9667, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Local pork with Lai Xaak, Jolpan with curd and jaggery",
            "description": "Heart of Kaziranga National Park Kohora central range, tea gardens, and geothermal hot springs.",
            "places": [
                {"name": "Kaziranga National Park (Kohora Central Range - UNESCO)", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "16:30", "description": "World-famous sanctuary home to two-thirds of the world's Great One-horned Rhinoceroses, wild water buffalos, and tigers."},
                {"name": "Garampani Wildlife Sanctuary & Hot Springs", "category": "Nature", "entry_fee": 30, "opening": "07:00", "closing": "16:30", "description": "One of Assam's oldest sanctuaries containing natural sulfur hot springs surrounded by dense semi-evergreen canopy."},
            ]
        },
        {
            "district": "Nagaon", "lat": 26.3484, "lon": 92.6841, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Masor Tenga, Boror Tenga, Pigeon curry with banana flower",
            "description": "Birthplace of Mahapurush Srimanta Sankardev, filled with historic Satras, wetlands, and Kaziranga's southern ranges.",
            "places": [
                {"name": "Batadrava (Bordowa) Than", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Sacred birthplace of 15th-century saint-reformer Srimanta Sankardev, the epicenter of Neo-Vaishnavite culture and Naamghars."},
                {"name": "Samaguri Beel (Pokhi Tirth)", "category": "Wildlife", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Oxbow lake brimming with thousands of migratory birds during winter months, framed by aquatic lilies."},
            ]
        },
        {
            "district": "Jorhat", "lat": 26.7509, "lon": 94.2037, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Duck curry with Ash Gourd, Hurum with cream, Til Pitha",
            "description": "Cultural capital of Assam, world's oldest tea research station at Tocklai, and gateway to Majuli Island.",
            "places": [
                {"name": "Tocklai Tea Research Institute (Est. 1911)", "category": "Cultural", "entry_fee": 50, "opening": "09:30", "closing": "16:30", "description": "World's oldest and largest experimental tea research station shaping the cultivation of global Assam orthodox tea."},
                {"name": "Nimati Ghat Majuli Ferry Point", "category": "Viewpoint", "entry_fee": 30, "opening": "07:00", "closing": "16:30", "description": "Scenic ferry embarkation point on the Brahmaputra connecting mainland Assam to the river island of Majuli."},
            ]
        },
        {
            "district": "Majuli", "lat": 26.9500, "lon": 94.2167, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Mising Porang Aapin (rice in wild leaf), smoked fish, roasted pork",
            "description": "World's largest river island, seat of Neo-Vaishnavite Satras, vibrant mask-making, and migratory bird wetlands.",
            "places": [
                {"name": "Sri Sri Kamalabari Satra & Auniati Satra", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Major centers of classical Sattriya dance, music, spiritual education, and Ahom royal artifacts."},
                {"name": "Samaguri Satra (Traditional Mask-Making)", "category": "Cultural", "entry_fee": 0, "opening": "08:00", "closing": "17:30", "description": "Famous worldwide for handcrafting intricate mythological bamboo and clay masks used in Bhaona religious theater."},
            ]
        },
        {
            "district": "Sivasagar", "lat": 26.9826, "lon": 94.6425, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Ahom Lukter, Pork with black sesame (Til), sticky bora saul",
            "description": "Historic capital of the 600-year Ahom kingdom, adorned with magnificent palaces, massive tanks, and grand stone temples.",
            "places": [
                {"name": "Rang Ghar (Asia's Oldest Royal Amphitheater)", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:00", "description": "Two-storey 1746 royal sports pavilion where Ahom kings watched bullfights, wrestling, and Bihu performances."},
                {"name": "Talatal Ghar & Kareng Ghar (Ahom Royal Palaces)", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:00", "description": "7-storey palace featuring secret underground tunnels and multi-level barracks constructed by King Rudra Singha."},
                {"name": "Sivasagar Sivadol (Tallest Shiva Temple in India)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "104-foot high 1734 temple tower topped by an 8-foot golden mastaka on the banks of the massive Borpukhuri tank."},
            ]
        },
        {
            "district": "Charaideo", "lat": 26.9300, "lon": 94.9000, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Traditional Tai-Ahom feast, steamed herb chicken, sweet rice cakes",
            "description": "First capital of Chaolung Sukaphaa in 1253, home to the UNESCO World Heritage royal burial mounds (Maidams).",
            "places": [
                {"name": "Charaideo Maidams (UNESCO World Heritage Site)", "category": "Historical", "entry_fee": 25, "opening": "08:00", "closing": "17:00", "description": "Sacred burial tumuli of the Ahom royalty, often hailed as the Pyramids of Assam, demonstrating ancient mortuary practices."},
            ]
        },
        {
            "district": "Dibrugarh", "lat": 27.4728, "lon": 94.9120, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Assam Tea with snacks, Singju, Masor Tenga & Duck Roast",
            "description": "Tea City of India, home to century-old tea gardens and the engineering marvel Bogibeel Bridge over the Brahmaputra.",
            "places": [
                {"name": "Bogibeel Rail-cum-Road Bridge", "category": "Viewpoint", "entry_fee": 0, "opening": "00:00", "closing": "23:59", "description": "India's longest rail-cum-road bridge (4.94 km) spanning the mighty Brahmaputra river connecting Dibrugarh to Dhemaji."},
                {"name": "Jokai Botanical Garden & Rainforest Reserve", "category": "Nature", "entry_fee": 20, "opening": "08:00", "closing": "16:30", "description": "Rich germplasm repository featuring rare orchids, medicinal ferns, and canopy elephant safari trails."},
            ]
        },
        {
            "district": "Tinsukia", "lat": 27.5000, "lon": 95.3667, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Smoked pork with bamboo shoot, steamed fish in banana leaves",
            "description": "Industrial and wilderness hub housing Asia's first oil refinery at Digboi and Dibru-Saikhowa National Park.",
            "places": [
                {"name": "Dibru-Saikhowa National Park & Maguri Beel", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "16:30", "description": "Feral horse sanctuary and wetland paradise famous for boat safaris to spot endangered white-winged wood ducks and river dolphins."},
                {"name": "Digboi Centenary Oil Museum & First Oil Well", "category": "Museum", "entry_fee": 30, "opening": "09:00", "closing": "17:00", "description": "Historic birthplace of the Indian oil industry in 1889, displaying operational machinery and Victorian-era colonial artifacts."},
            ]
        },
        {
            "district": "Dhemaji", "lat": 27.4800, "lon": 94.5800, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Mising Apong, fish roasted in hollow bamboo, sticky rice",
            "description": "Scenic sub-Himalayan plains on the north bank of the Brahmaputra rich in Mising tribal folklore and green pastures.",
            "places": [
                {"name": "Gerukamukh Subansiri Gorge", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "Stunning natural gorge where the Subansiri River emerges from the Arunachal mountains into the Assam valley."},
                {"name": "Maa Manipuri Than Historical Temple", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Revered shrine established by Ahom King Gaurinath Singha, surrounded by ancient sal groves."},
            ]
        },
        {
            "district": "Lakhimpur", "lat": 27.2300, "lon": 94.1000, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Bora rice with duck curry, fried dried fish, bamboo shoots",
            "description": "Verdant agricultural hub nestled between the hills of Arunachal and the Brahmaputra, noted for traditional handicrafts.",
            "places": [
                {"name": "Leteku Pukhuri (Birthplace of Sri Sri Madhavdev)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Sacred birthplace of the great 16th-century saint and literary giant Madhavdev, disciple of Sankardev."},
            ]
        },
        {
            "district": "Sonitpur", "lat": 26.6338, "lon": 92.8000, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Tezpur litchis, Masor Tenga, Duck curry with black pepper",
            "description": "Centred around Tezpur, the City of Eternal Romance, rich in mythologies of Princess Usha and Prince Aniruddha.",
            "places": [
                {"name": "Agnigarh Hill & Viewpoint", "category": "Historical", "entry_fee": 20, "opening": "07:00", "closing": "19:00", "description": "Legendary fortress of fire built by King Banasura, featuring sculpted mythological dioramas and river views."},
                {"name": "Mahabhairab Temple (5000-year-old Shiva Lingam)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "20:00", "description": "Ancient Shiva shrine said to have been consecrated by the legendary mythological King Banasura."},
                {"name": "Nameri National Park & Eco Camp Gateway", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "16:00", "description": "Scenic park at the foot of Eastern Himalayas famed for river rafting on the Jia Bhoroli and Golden Mahseer angling."},
            ]
        },
        {
            "district": "Biswanath", "lat": 26.7300, "lon": 93.1500, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Tea garden snacks, freshwater fish curry, pitha",
            "description": "Known as Gupta Kashi for its cluster of ancient stone temples along the sacred Biswanath Ghat on the Brahmaputra.",
            "places": [
                {"name": "Biswanath Ghat (Gupta Kashi of Assam)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "19:00", "description": "Ancient pilgrimage ghat featuring submerged Shiva temples that emerge during winter low-water months."},
                {"name": "Monabarie Tea Estate (Largest in Asia)", "category": "Nature", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "Asia's largest single tea estate stretching over thousands of rolling acres of emerald tea bushes."},
            ]
        },
        {
            "district": "Darrang", "lat": 26.4500, "lon": 92.0300, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Khar with raw papaya, river fish fry, Jolpan",
            "description": "Cultural epicenter of the Darrangi folk dance (Ojapali and Deodhani) and historic Orang National Park.",
            "places": [
                {"name": "Orang National Park (The Mini Kaziranga)", "category": "Wildlife", "entry_fee": 100, "opening": "06:30", "closing": "16:30", "description": "Reputed rhino habitat on the north bank of Brahmaputra with highest density of royal Bengal tigers and pygmy hogs."},
            ]
        },
        {
            "district": "Udalguri", "lat": 26.7400, "lon": 92.1000, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Bodo Onla curry (rice powder curry with chicken), Zou rice beer",
            "description": "Bodoland Territorial Region hub bordering Bhutan, blessed with picnicking spots, gorges, and wildlife.",
            "places": [
                {"name": "Bhairabkunda Tri-Junction (Assam-Arunachal-Bhutan)", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Picturesque spot where the Jampui and Bhairabi rivers merge to form the Dhansiri River against Bhutanese hills."},
            ]
        },
        {
            "district": "Barpeta", "lat": 26.3200, "lon": 91.0000, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Barpeta Sandesh, Khar, Masor Jhol & fried Chitol fish",
            "description": "Land of the Satras, renowned for traditional bell-metal craft, brassware, and fireworks artistry.",
            "places": [
                {"name": "Barpeta Kirtan Ghar (Barpeta Satra)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "20:00", "description": "Established in 1583 by Madhavdev, one of the greatest Vaishnavite monasteries in Assam with grand architectural portals."},
            ]
        },
        {
            "district": "Baksa", "lat": 26.6800, "lon": 91.3000, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Bodo Napham (fermented fish paste), pork with bamboo shoots",
            "description": "Gateway to the UNESCO World Heritage Manas National Park, sharing pristine alpine borders with Bhutan.",
            "places": [
                {"name": "Manas National Park (UNESCO World Heritage Site)", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "16:30", "description": "Renowned biosphere reserve home to rare golden langurs, hispid hares, pygmy hogs, and majestic elephants."},
                {"name": "Bogamati River Picnic Valley", "category": "Nature", "entry_fee": 20, "opening": "07:00", "closing": "17:00", "description": "Picturesque riverbed along the Bornadi River overlooked by the forested mountains of Bhutan."},
            ]
        },
        {
            "district": "Nalbari", "lat": 26.4400, "lon": 91.4300, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Nalbari curd and flattened rice (Chira Doi), sweet pithas",
            "description": "Land of Sanskrit scholars (Navadwip of Assam), ancient temples, and bell-metal artisan workshops.",
            "places": [
                {"name": "Sri Sri Hari Mandir & Raas Mahotsav Ground", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Spiritual epicenter famous for celebrating the magnificent 11-day Nalbari Raas festival with hundreds of clay idols."},
                {"name": "Billeswar Temple (Centuries-old Shiva Peeth)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Ancient temple revered for over 500 years, surrounded by sacred water tanks and banyan trees."},
            ]
        },
        {
            "district": "Chirang", "lat": 26.5600, "lon": 90.5800, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Bodo smoked chicken with dried jute leaves, spicy chutneys",
            "description": "Part of Bodoland Territorial Region, featuring dense sal forests, waterfalls, and eco-tourism parks.",
            "places": [
                {"name": "Champamati Waterfalls & Koilamoila", "category": "Waterfall", "entry_fee": 0, "opening": "07:00", "closing": "17:00", "description": "Serene cascade on the Champamati River nestled along the Bhutan border foothills."},
            ]
        },
        {
            "district": "Bongaigaon", "lat": 26.4800, "lon": 90.5600, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Fish fry, Assamese Khar, Muga tea snacks",
            "description": "Major commercial hub with historical rock-cut caves at Jogighopa and golden langur sanctuaries.",
            "places": [
                {"name": "Kakoijana Golden Langur Wildlife Sanctuary", "category": "Wildlife", "entry_fee": 30, "opening": "07:00", "closing": "16:30", "description": "Protected reserve famous for conserving the rare and endangered Golden Langur in its natural forest habitat."},
                {"name": "Rock-Cut Caves & Ruins of Jogighopa", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "5 ancient rock-cut monastic caves on the Brahmaputra cliffs dating back to the Salasthambha period."},
            ]
        },
        {
            "district": "Kokrajhar", "lat": 26.4000, "lon": 90.2700, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Ohm bedor (pork curry with herbs), Sobai jhol, Jou",
            "description": "Headquarters of the Bodoland Territorial Council, home to Raimona National Park and rich Bodo culture.",
            "places": [
                {"name": "Raimona National Park", "category": "Wildlife", "entry_fee": 100, "opening": "06:30", "closing": "16:30", "description": "Assam's 6th national park, renowned for sheltering the endemic golden langur, Asian elephants, and wild water buffalos."},
                {"name": "Chakrashila Wildlife Sanctuary", "category": "Wildlife", "entry_fee": 50, "opening": "06:30", "closing": "16:30", "description": "Second protected home of the golden langur in India, encompassing scenic hillocks and two lakes, Dheer and Diplai."},
            ]
        },
        {
            "district": "Dhubri", "lat": 26.0200, "lon": 89.9700, "crime_index": 26.0, "safety_tier": "LOW",
            "food": "Muri-Ghol, Ilish fish curry, Chitol fish muitha",
            "description": "Historic riverine town on the Brahmaputra, famous for Gurdwara Sri Guru Tegh Bahadur Sahib and terracotta craft.",
            "places": [
                {"name": "Gurdwara Sri Guru Tegh Bahadur Sahib (Damdama Sahib)", "category": "Spiritual", "entry_fee": 0, "opening": "04:30", "closing": "21:00", "description": "Historic Sikh pilgrimage shrine established in 1505 by Guru Nanak Dev and blessed in 1666 by Guru Tegh Bahadur."},
                {"name": "Asharikandi Terracotta & Pottery Craft Village", "category": "Cultural", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "India's largest cluster of traditional terracotta artisans known for distinctive mother-and-child mud sculptures."},
            ]
        },
        {
            "district": "South Salmara-Mankachar", "lat": 25.7500, "lon": 89.9200, "crime_index": 23.0, "safety_tier": "LOW",
            "food": "River fish curry, steamed pitha, country chicken curry",
            "description": "Southern bank border outpost across the Brahmaputra, dotted with historical tombs and scenic river islands.",
            "places": [
                {"name": "Mir Jumla Tomb & Historic Ramparts", "category": "Historical", "entry_fee": 0, "opening": "07:00", "closing": "17:30", "description": "Mausoleum of Mughal general Mir Jumla, who commanded the famous 17th-century invasion of Assam."},
            ]
        },
        {
            "district": "Goalpara", "lat": 26.1700, "lon": 90.6200, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Bora rice cakes, mashed eggplant with mustard oil, river fish",
            "description": "Archaeological treasure-trove featuring Sri Surya Pahar, a historic confluence of Hinduism, Buddhism, and Jainism.",
            "places": [
                {"name": "Sri Surya Pahar Archaeological Site", "category": "Historical", "entry_fee": 25, "opening": "08:00", "closing": "17:00", "description": "Significant archaeological complex featuring hundreds of carved rock-cut Shiva lingas, Buddhist stupas, and Jain Tirthankaras."},
                {"name": "Kumri Beel & Urpad Beel Bird Sanctuaries", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Expansive natural wetlands hosting hundreds of thousands of resident and migratory water birds."},
            ]
        },
        {
            "district": "Morigaon", "lat": 26.2500, "lon": 92.3400, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Tiwa traditional pork dish, rice beer, Pitha",
            "description": "Home to Pobitora Wildlife Sanctuary, Mayong black magic village, and the annual Jonbeel Mela barter fair.",
            "places": [
                {"name": "Pobitora Wildlife Sanctuary (Highest Rhino Density)", "category": "Wildlife", "entry_fee": 100, "opening": "06:30", "closing": "16:30", "description": "Small sanctuary with the world's densest population of the One-horned Rhinoceros, perfect for jeep safaris."},
                {"name": "Mayong Village (Black Magic Capital of India)", "category": "Cultural", "entry_fee": 20, "opening": "09:00", "closing": "17:00", "description": "Fabled village renowned for ancient occult traditions, Ayurvedic healing, and the Mayong Central Museum & Research Centre."},
            ]
        },
        {
            "district": "Hojai", "lat": 26.0000, "lon": 92.8600, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Puffed rice snacks, traditional Bengali and Assamese curries",
            "description": "Known as the Agarwood perfume capital of India and home to ancient ruins at Doboka.",
            "places": [
                {"name": "Doboka Archaeological Ruins & Reserve Forest", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "Ancient kingdom sites with carved sandstone pillars and stone tanks dating back to the 8th century."},
            ]
        },
        {
            "district": "Karbi Anglong", "lat": 25.8500, "lon": 93.4300, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Kangmoi, Karbi smoked pork with bamboo shoot, Horlang rice beer",
            "description": "Hill district of rolling hills, pine forests, waterfalls, and the rich ethnic culture of the Karbi people.",
            "places": [
                {"name": "Diphu Recreation Park & Botanical Arboretum", "category": "Park", "entry_fee": 20, "opening": "08:00", "closing": "17:30", "description": "Beautiful hilltop park showcasing indigenous flora, bamboo varieties, and orchids of the Karbi Hills."},
                {"name": "Silbheta & Khanduli Tourist Spot", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "Scenic rocky stream cascade and grassland plateau reminiscent of European downs."},
            ]
        },
        {
            "district": "West Karbi Anglong", "lat": 25.8000, "lon": 92.5000, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Boiled bamboo shoot pork, sticky rice, wild mint salad",
            "description": "Centred around Hamren, featuring pristine valleys, Kopili River rapids, and Amreng eco-tourism sites.",
            "places": [
                {"name": "Kopili River Falls & Amreng Tourist Complex", "category": "Waterfall", "entry_fee": 0, "opening": "07:00", "closing": "17:00", "description": "Spectacular river rapid and eco-park situated amidst rolling green hills and crystal-clear streams."},
            ]
        },
        {
            "district": "Dima Hasao", "lat": 25.1800, "lon": 93.0300, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Dimasa traditional chicken curry (Judima beer pairing), bamboo shoot",
            "description": "Assam's only hill station district, famed for Haflong, Jatinga bird mysteries, and Panimoor waterfalls.",
            "places": [
                {"name": "Haflong Lake & Hill Station Ridge", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Charming hilltop town nestled at 2,200 feet centered around the picturesque Haflong Lake and hanging footbridge."},
                {"name": "Jatinga Bird Mystery Valley", "category": "Nature", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Famous ridge where birds demonstrate an enigmatic attraction phenomenon during foggy monsoon nights."},
                {"name": "Panimoor Waterfalls (Niagara of Dima Hasao)", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:00", "description": "Majestic thundering waterfall where the turquoise Kopili River cascades over multiple jagged limestone steps."},
                {"name": "Maibang Medieval Kachari Kingdom Ruins", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "16th-century stone temple ruins including a monolithic rock-cut temple built by King Harishchandra Narayan."},
            ]
        },
        {
            "district": "Cachar", "lat": 24.8333, "lon": 92.7789, "crime_index": 25.0, "safety_tier": "LOW",
            "food": "Barak Valley Sylheti Thali, Shidol Chutney, Chitol fish curry",
            "description": "Southern Assam's premier commercial hub at Silchar, home to Khaspur Kachari ruins and tea estates.",
            "places": [
                {"name": "Khaspur Medieval Kachari Palace Ruins", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "17:30", "description": "Historic 18th-century capital of the Kachari kings featuring the Sun Gate, Lion Gate, and King's Temple."},
                {"name": "Bhuban Hill Shiva Temple (Bhubaneswar)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "18:00", "description": "Ancient hilltop temple attracting thousands of devotees during Shivaratri, offering views over Bangladesh plains."},
            ]
        },
        {
            "district": "Hailakandi", "lat": 24.6800, "lon": 92.5600, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Pithe, freshwater prawn malai curry, fermented shutki",
            "description": "Lush valley flanked by tea gardens, scenic river meanders, and historic shrines.",
            "places": [
                {"name": "Siddheswar Shiva Temple (Badarpurghat)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Revered temple on the banks of the Barak River famous for its annual Baruni Mela holy congregation."},
            ]
        },
        {
            "district": "Karimganj", "lat": 24.8667, "lon": 92.3500, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Hilsa fish cooked with mustard, Shidol Chutney, sweet sandesh",
            "description": "Border district on the Kushiyara River, home to Son Beel—the largest wetland in Assam.",
            "places": [
                {"name": "Son Beel (Largest Wetland in Assam)", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Vast freshwater lake with seasonal floating islands and colorful fishing boats framed by rolling green hills."},
                {"name": "Malegarh Sepoy Mutiny 1857 War Memorial", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "Historical memorial where Indian mutineers fought a fierce pitched battle against the Sylhet Light Infantry."},
            ]
        },
        {
            "district": "Bajali", "lat": 26.5500, "lon": 91.1800, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Bajali Pitha, mustard fish curry, sweet curds",
            "description": "Cultural district centred around Pathsala, widely celebrated as the mobile theater capital of Assam.",
            "places": [
                {"name": "Pathsala Mobile Theater Cultural Hub", "category": "Cultural", "entry_fee": 0, "opening": "09:00", "closing": "21:00", "description": "Epicenter of the iconic Bhramyaman (Mobile Theatre) industry, featuring historic Natya Mandirs and cultural stages."},
            ]
        },
        {
            "district": "Tamulpur", "lat": 26.6300, "lon": 91.5700, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Bodo Onla chicken, steamed pithas, smoked pork",
            "description": "Picturesque border gateway connecting Assam to the mountain trails of Samdrup Jongkhar in Bhutan.",
            "places": [
                {"name": "Daranga International Mela Border Post", "category": "Cultural", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "Historic trade route where Bhutanese villagers and Indian traders exchange woolens, spices, and tea."},
            ]
        },
    ],

    # ==================== 3. MANIPUR (16 Districts) ====================
    "Manipur": [
        {
            "district": "Imphal West", "lat": 24.8170, "lon": 93.9368, "crime_index": 26.0, "safety_tier": "LOW",
            "food": "Eromba, Kangshoi, Singju, Chak-hao kheer (black rice pudding)",
            "description": "Heart of Manipur, home to Kangla Fort, the ancient royal seat, and the iconic all-women Ima Keithel market.",
            "places": [
                {"name": "Kangla Fort (Ancient Palace of Manipur)", "category": "Historical", "entry_fee": 20, "opening": "07:00", "closing": "17:00", "description": "Revered royal seat of the Ningthouja dynasty, surrounded by moats, sacred ponds, and the twin Kangla Sha dragon statues."},
                {"name": "Ima Keithel (Mother's Market - Asia's Largest All-Women Market)", "category": "Cultural", "entry_fee": 0, "opening": "07:00", "closing": "19:00", "description": "Historic 500-year-old marketplace run exclusively by over 5,000 married women traders selling textiles and food."},
                {"name": "Shree Govindajee Temple", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "20:00", "description": "Golden-domed 1846 Vaishnavite temple renowned for its spiritual aura, classical Raas Leela dances, and daily arati."},
            ]
        },
        {
            "district": "Imphal East", "lat": 24.8000, "lon": 93.9600, "crime_index": 24.0, "safety_tier": "LOW",
            "food": "Chagem Pomba, Ngari chutney, Ooti, Bora",
            "description": "Cultural district showcasing heritage pottery at Andro village, the sacred Nongmaiching hills, and botanical parks.",
            "places": [
                {"name": "Andro Heritage Cultural Village & Doll House", "category": "Cultural", "entry_fee": 30, "opening": "08:00", "closing": "17:00", "description": "Ancient craft village preserving continuous sacred fire since the 1st century AD and distinctive coil pottery."},
                {"name": "Samban-Lei Sekpil (Tallest Topiary Plant)", "category": "Nature", "entry_fee": 15, "opening": "08:00", "closing": "17:30", "description": "Guinness Record-holding shaped topiary hedge reaching over 60 feet height, pruned meticulously over 30 years."},
            ]
        },
        {
            "district": "Bishnupur", "lat": 24.6300, "lon": 93.7600, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Thalgari fish fry, Sareng thongba, Loktak smoked fish",
            "description": "Famed for Loktak Lake, Keibul Lamjao floating national park, and INA Memorial at Moirang.",
            "places": [
                {"name": "Loktak Lake & Keibul Lamjao National Park", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "17:00", "description": "World's only floating national park on heterogeneous masses of floating vegetation (phumdis), sheltering the endangered Sangai deer."},
                {"name": "INA War Memorial & Netaji Subhash Chandra Bose Museum (Moirang)", "category": "Historical", "entry_fee": 20, "opening": "09:00", "closing": "17:00", "description": "Historic site where the Indian National Army hoisted the Indian tricolor on Indian soil for the first time in April 1944."},
                {"name": "Bishnupur 15th-Century Vishnu Temple", "category": "Historical", "entry_fee": 0, "opening": "07:00", "closing": "17:30", "description": "1467 single-cell brick temple displaying Burmese conical design influence built during King Kyamba's reign."},
            ]
        },
        {
            "district": "Thoubal", "lat": 24.6400, "lon": 93.9900, "crime_index": 21.0, "safety_tier": "LOW",
            "food": "Kangshoi vegetable stew, Morok Metpa, fried fish",
            "description": "Agricultural valley dotted with wetlands like Waithou Lake and the historic Khongjom War Memorial.",
            "places": [
                {"name": "Khongjom War Memorial (Anglo-Manipur War 1891)", "category": "Historical", "entry_fee": 20, "opening": "08:00", "closing": "18:00", "description": "Towering monument commemorating Major General Paona Brajabasi and Manipuri soldiers who fought valiantly against British forces."},
                {"name": "Waithou Lake Scenic Eco-Spot", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Scenic lake renowned for pineapples, smoked fresh fish, and soothing roadside viewpoints."},
            ]
        },
        {
            "district": "Kakching", "lat": 24.4900, "lon": 93.9800, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Chak-hao kheer, bamboo shoot curry, fermented soybeans",
            "description": "Granary of Manipur, awarded India's cleanest town in the Northeast zone, featuring beautiful hill parks.",
            "places": [
                {"name": "Kakching Garden (Uyok Ching)", "category": "Park", "entry_fee": 20, "opening": "08:00", "closing": "18:00", "description": "Immaculate terraced garden on a hilltop featuring fountains, statues of Lord Shiva, and sweeping views of the valley."},
            ]
        },
        {
            "district": "Churachandpur", "lat": 24.3300, "lon": 93.6800, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Zomi and Kuki smoked beef/pork dishes, boiled mustard greens",
            "description": "Largest hill district of Manipur, home to rich tribal communities, Khuga Dam, and scenic trekking trails.",
            "places": [
                {"name": "Khuga Dam & Reservoir", "category": "Nature", "entry_fee": 10, "opening": "07:00", "closing": "18:00", "description": "Multi-purpose earthen dam surrounded by blue waters and pine-clad hills, ideal for day picnics and boating."},
                {"name": "Tuibuong Tribal Peace Museum", "category": "Museum", "entry_fee": 20, "opening": "09:00", "closing": "16:30", "description": "Displays indigenous costumes, war shields, hunting horns, and ancient tribal artifacts of southwestern Manipur."},
            ]
        },
        {
            "district": "Pherzawl", "lat": 24.2600, "lon": 93.1800, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Boiled bamboo shoots with pork, smoked fish",
            "description": "Remote southwest border district on the Barak River, adorned with untouched virgin forests.",
            "places": [
                {"name": "Barak River Canyon & Taithu Hills", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "Pristine mountain gorges where the nascent Barak River flows through unspoiled sub-tropical forests."},
            ]
        },
        {
            "district": "Senapati", "lat": 25.2600, "lon": 94.0200, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Mao potato dishes, smoked pork with pumpkin seeds",
            "description": "Northern gateway to Manipur, famous for the Mao hill station, Purul village, and Makhel heritage tree.",
            "places": [
                {"name": "Mao Hill Station & Cherry Blossom Slopes", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Picturesque border hill station at 5,800 feet blanketed in wild Himalayan cherry blossoms in late autumn."},
                {"name": "Makhel Sacred Historical Banyan Tree", "category": "Cultural", "entry_fee": 0, "opening": "07:00", "closing": "17:30", "description": "Legendary cradle of migration for several Naga and indigenous tribes, marked by ancient sacred stone monoliths."},
            ]
        },
        {
            "district": "Kangpokpi", "lat": 25.1500, "lon": 93.9700, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Kuki traditional sa-um (fermented fat pork), boiled herbs",
            "description": "Hill district along the National Highway, featuring Koubru mountain peaks and lush ginger terraces.",
            "places": [
                {"name": "Mount Koubru Sacred Peak Trail", "category": "Adventure", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "Revered mountain peak held sacred in Meitei mythology as the dwelling place of Lord Koubru."},
            ]
        },
        {
            "district": "Ukhrul", "lat": 25.1100, "lon": 94.3600, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Tangkhul smoked pork with local Sichuan pepper, sticky rice",
            "description": "Land of the Shirui Lily, the rare terrestrial lily found only on Shirui Kashong Peak, and Longpi black pottery.",
            "places": [
                {"name": "Shirui Kashong Peak (Home of the Shirui Lily)", "category": "Nature", "entry_fee": 30, "opening": "06:00", "closing": "17:00", "description": "8,500-foot peak where the endangered, pinkish-white Shirui Lily blooms exclusively during May–June."},
                {"name": "Longpi (Nungbi) Black Stone Pottery Village", "category": "Cultural", "entry_fee": 0, "opening": "08:00", "closing": "17:30", "description": "Famed village crafting royal black earthenware pots made without a potter's wheel from serpentine stone and brown clay."},
                {"name": "Khangkhui Mangsor Limestone Caves", "category": "Adventure", "entry_fee": 20, "opening": "08:00", "closing": "16:30", "description": "Prehistoric limestone cave system that served as an air-raid shelter for villagers during World War II."},
            ]
        },
        {
            "district": "Kamjong", "lat": 24.8700, "lon": 94.5200, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Smoked river fish with hot king chili chutney, boiled greens",
            "description": "Tranquil border hills along the Indo-Myanmar frontier, blessed with mist-draped pine ridges and orchids.",
            "places": [
                {"name": "Azoa Jenephi & Chassad Hill Vistas", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:30", "description": "Breathtaking ridge walk offering panoramic vistas stretching into the Chindwin valley of Myanmar."},
            ]
        },
        {
            "district": "Tamenglong", "lat": 24.9800, "lon": 93.4900, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Tamenglong oranges, Rongmei smoked pork, bamboo shoots",
            "description": "Orange Bowl of Manipur, famed for Zeilad Lake, Barak waterfalls, and roosting Amur falcons.",
            "places": [
                {"name": "Barak River Seven Waterfalls & Tharon Cave", "category": "Waterfall", "entry_fee": 0, "opening": "07:00", "closing": "16:30", "description": "Series of seven majestic cascades crashing down rock cliffs alongside 655m long prehistoric cave passages."},
                {"name": "Zeilad Wildlife Sanctuary & Holy Lake", "category": "Nature", "entry_fee": 20, "opening": "07:00", "closing": "16:30", "description": "Highland lake famous for migratory waterfowls, giant tortoises, and lush semi-evergreen sub-Himalayan forest."},
            ]
        },
        {
            "district": "Noney", "lat": 24.8200, "lon": 93.6300, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Inpui and Rongmei tribal stews, bamboo shoot pickles",
            "description": "Home to the world's tallest railway pier bridge over the Ijai River, an engineering wonder amidst deep hills.",
            "places": [
                {"name": "Noney Railway Bridge (World's Tallest Railway Pier)", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Record-setting railway bridge with a pier height of 141 meters towering over the Ijai river valley."},
            ]
        },
        {
            "district": "Chandel", "lat": 24.3200, "lon": 94.0000, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Anal tribal smoked meats, bamboo shoots, wild herbal broths",
            "description": "Border district rich in ethnic diversity, home to the Yangoupokpi-Lokchao Wildlife Sanctuary.",
            "places": [
                {"name": "Yangoupokpi-Lokchao Wildlife Sanctuary", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "16:30", "description": "Important Indo-Burma biodiversity corridor sheltering Malayan sun bears, leopards, and hoolock gibbons."},
            ]
        },
        {
            "district": "Tengnoupal", "lat": 24.3800, "lon": 94.1500, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Myanmar noodles, Burmese street snacks, fried tofu",
            "description": "Home to the international border town of Moreh, the vibrant trade conduit between India and Myanmar.",
            "places": [
                {"name": "Moreh Border Market & Indo-Myanmar Friendship Gate", "category": "Cultural", "entry_fee": 0, "opening": "07:00", "closing": "17:00", "description": "Bustling international border trading gate and market selling exotic Burmese goods, teakwood, and textiles."},
            ]
        },
        {
            "district": "Jiribam", "lat": 24.8000, "lon": 93.1200, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Fresh Jiri river fish curry, Ilish, bamboo shoot chicken",
            "description": "Western gateway connecting Manipur to Assam's Barak Valley, surrounded by the scenic Jiri River.",
            "places": [
                {"name": "Jiri River Waterfront & Tea Estates", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Pleasant riverfront where the Jiri and Barak rivers meet, framed by undulating tea plantations."},
            ]
        },
    ],

    # ==================== 4. MEGHALAYA (12 Districts) ====================
    "Meghalaya": [
        {
            "district": "East Khasi Hills", "lat": 25.5788, "lon": 91.8933, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Jadoh (rice with meat), Dohneiiong (pork with black sesame), Tungrymbai & Pumaloi",
            "description": "Abode of Clouds, housing Shillong (Scotland of the East) and wettest place on Earth Cherrapunji (Sohra).",
            "places": [
                {"name": "Double Decker Living Root Bridge (Nongriat)", "category": "Nature", "entry_fee": 50, "opening": "06:00", "closing": "17:00", "description": "Centuries-old bio-engineering marvel crafted by Khasi tribes from the aerial roots of Ficus elastica trees."},
                {"name": "Nohkalikai Falls (Tallest Plunge Waterfall in India)", "category": "Waterfall", "entry_fee": 30, "opening": "07:00", "closing": "17:30", "description": "Dramatic 340m plunge waterfall tumbling into a vibrant turquoise-blue pool on the edge of the Sohra plateau."},
                {"name": "Laitlum Canyons (End of the World)", "category": "Viewpoint", "entry_fee": 20, "opening": "06:00", "closing": "17:30", "description": "Perched on the edge of towering cliffs with panoramic bird's-eye views of deep gorges, winding rivers, and cloud ribbons."},
                {"name": "Elephant Falls & Shillong Peak", "category": "Waterfall", "entry_fee": 50, "opening": "08:00", "closing": "17:00", "description": "Three-tiered waterfall cascading through dense fern glades alongside the highest point in Meghalaya (6,449 ft)."},
            ]
        },
        {
            "district": "West Khasi Hills", "lat": 25.5200, "lon": 91.2700, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Khasi roasted pork, steamed rice bread (Pukhlein), wild honey",
            "description": "Centred around Nongstoin, home to Nongkhnum River Island, the second-largest river island in Asia.",
            "places": [
                {"name": "Nongkhnum River Island & Beach", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:30", "description": "Vast 20-sq km river island formed by Kynshi and Phanliang rivers, featuring sand beaches and Langshiang Falls."},
                {"name": "Weinia & Langshiang Waterfalls", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:00", "description": "Spectacular cascading waterfalls roaring over sheer basalt rock cliffs into deep forested valleys."},
            ]
        },
        {
            "district": "South West Khasi Hills", "lat": 25.3600, "lon": 91.4500, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Khasi pork blood sausage, boiled tapioca, Jastem yellow rice",
            "description": "Known for Mawkyrwat, natural sulphur hot springs at Jakrem, and pristine mountain rivers.",
            "places": [
                {"name": "Jakrem Sulphur Hot Springs & Health Resort", "category": "Nature", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Thermal springs renowned for curative medicinal properties against skin ailments and joint pain."},
            ]
        },
        {
            "district": "Eastern West Khasi Hills", "lat": 25.5600, "lon": 91.6300, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Jadoh, roasted fish, Khasi mint and fermented soybean chutney",
            "description": "Centred around Mairang, famous for Kyllang Rock—a giant red granite dome rising high above pine forests.",
            "places": [
                {"name": "Kyllang Rock (Giant Monolithic Granite Dome)", "category": "Nature", "entry_fee": 20, "opening": "07:00", "closing": "17:00", "description": "Massive single granite rock dome soaring 1,000 feet above the surrounding pine landscape, easily climbable from northern face."},
                {"name": "U Tirot Sing Memorial (Mairang)", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "Memorial honoring the courageous Khasi hero U Tirot Sing Syiem who led the resistance against British forces in 1829."},
            ]
        },
        {
            "district": "Ri-Bhoi", "lat": 25.9000, "lon": 91.8800, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Bhoi smoked fish, pineapples, wild mushroom stir fry",
            "description": "Northern gateway to Meghalaya, home to the scenic Umiam Lake (Barapani) and pine-fringed hill roads.",
            "places": [
                {"name": "Umiam Lake (Barapani Reservoir)", "category": "Nature", "entry_fee": 30, "opening": "06:00", "closing": "18:00", "description": "Enchanting 220-sq km freshwater lake surrounded by sylvan hills, offering water sports, kayaking, and yachting."},
                {"name": "Lum Nehru Park & Orchidarium", "category": "Park", "entry_fee": 20, "opening": "08:30", "closing": "17:30", "description": "Landscaped park adjoining Umiam Lake with exotic orchids, lawns, musical fountain, and walking promenades."},
            ]
        },
        {
            "district": "West Jaintia Hills", "lat": 25.4500, "lon": 92.2000, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Jaintia Jadoh with chicken, Dohsnam, Lakadong Turmeric tea",
            "description": "Home to Jowai, the fairytale turquoise waters of Krang Suri Falls, and ancient Nartiang monoliths.",
            "places": [
                {"name": "Krang Suri Waterfalls", "category": "Waterfall", "entry_fee": 50, "opening": "07:00", "closing": "17:00", "description": "Fairytale curtain waterfall cascading into a luminous crystal turquoise swimming pool, framed by stone steps."},
                {"name": "Nartiang Monoliths (Tallest Monoliths in the World)", "category": "Historical", "entry_fee": 0, "opening": "07:00", "closing": "18:00", "description": "Largest cluster of megaliths and upright menhirs (Moo Shynrang) erected between 1500 and 1835 AD."},
                {"name": "Thadlaskein Lake & Nartiang Durga Temple", "category": "Spiritual", "entry_fee": 20, "opening": "06:00", "closing": "18:00", "description": "Historic 500-year-old Shakti temple where ancient human sacrifices were replaced with goat offerings."},
            ]
        },
        {
            "district": "East Jaintia Hills", "lat": 25.3200, "lon": 92.4200, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Smoked pork with local ginger, rice with dry fish paste",
            "description": "Limestone karst paradise featuring Krem Liat Prah—the longest natural cave system in South Asia.",
            "places": [
                {"name": "Krem Liat Prah Cave (Longest Cave in South Asia)", "category": "Adventure", "entry_fee": 100, "opening": "08:00", "closing": "16:00", "description": "Spectacular karst cave system mapped over 34 kilometers with enormous passages known as the Aircraft Hangar."},
                {"name": "Lubha (Kopili) River Suspension Bridge", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Historic British-era iron bridge spanning the emerald green Lubha river against dense tropical crags."},
            ]
        },
        {
            "district": "East Garo Hills", "lat": 25.6000, "lon": 90.5800, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Garo Wak Grika (pork curry with bamboo shoots), Minil steamed rice",
            "description": "Centred around Williamnagar, home to the Simsang River, Ta'sek Lake, and vibrant Wangala harvest dance.",
            "places": [
                {"name": "Ta'sek Lake & Simsang River Valley", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:30", "description": "Natural lake formed during the Great Assam Earthquake of 1897, wrapped in lush sub-tropical forest."},
            ]
        },
        {
            "district": "West Garo Hills", "lat": 25.5140, "lon": 90.2030, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Do'o Kappa (chicken cooked with soda/potash), Nakham Bitchi",
            "description": "Centred around Tura, home to Tura Peak, Pelga Falls, and Nokrek Biosphere Reserve.",
            "places": [
                {"name": "Nokrek National Park (UNESCO Biosphere Reserve)", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "16:30", "description": "Core home of the rare citrus indica (mother of all citrus fruits), red pandas, Asian elephants, and stump-tailed macaques."},
                {"name": "Pelga Falls & Traditional Bamboo Hanging Bridge", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Scenic falls on the Ganol River famous for angling and the adjacent traditional Garo bamboo footpath."},
                {"name": "Tura Peak Summit Viewpoint", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "17:30", "description": "Panoramic summit at 2,860 ft offering sweeping views of Tura town and the vast plains of Bangladesh."},
            ]
        },
        {
            "district": "South Garo Hills", "lat": 25.2000, "lon": 90.6300, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Wak Kappa (pork with karchi alkali), steamed yam",
            "description": "Home to Balpakram National Park (Grand Canyon of Meghalaya) and the limestone wonders of Siju Cave.",
            "places": [
                {"name": "Balpakram National Park (Land of Perpetual Winds)", "category": "Wildlife", "entry_fee": 100, "opening": "06:00", "closing": "16:30", "description": "High plateau canyon revered by Garos as the resting place of departed souls, home to barking deer and clouded leopards."},
                {"name": "Siju Cave (Dobakkol - Cave of Bats)", "category": "Adventure", "entry_fee": 50, "opening": "08:00", "closing": "16:30", "description": "Third longest cave system in the Indian subcontinent with majestic limestone stalactites and underground river chambers."},
            ]
        },
        {
            "district": "North Garo Hills", "lat": 25.9000, "lon": 90.5800, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Garo chicken soup with nakham dry fish, boiled greens",
            "description": "Centred around Resubelpara, known for geothermal hot springs, orange groves, and peaceful rubber plantations.",
            "places": [
                {"name": "Resubelpara Hot Springs & Lake", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "17:30", "description": "Natural thermal sulphur springs set amidst scenic hills, known for soothing natural bath pools."},
            ]
        },
        {
            "district": "South West Garo Hills", "lat": 25.5000, "lon": 89.9200, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Fish fry, Nakham dry fish chutney, steamed rice",
            "description": "Centred around Ampati, featuring scenic wetlands at Kata Beel and historical ties to the Mughal period.",
            "places": [
                {"name": "Kata Beel & Eco-Park Ampati", "category": "Park", "entry_fee": 15, "opening": "08:00", "closing": "17:30", "description": "Expansive natural wetland park popular for boating, nature walks, and community fishing festivals."},
            ]
        },
    ],

    # ==================== 5. MIZORAM (11 Districts) ====================
    "Mizoram": [
        {
            "district": "Aizawl", "lat": 23.7271, "lon": 92.7176, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Bai (boiled vegetable & pork stew), Vawksa Rep (smoked pork), Sawhchiar & Koat Pitha",
            "description": "Capital of Mizoram perched on sharp mountain ridges, celebrated for Solomon's Temple and vibrant choir culture.",
            "places": [
                {"name": "Solomon's Temple (Kidron Valley)", "category": "Spiritual", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Spectacular white marble Christian church accommodating over 3,000 worshippers, built by Kohhran Thianghlim."},
                {"name": "Durtlang Hills Viewpoint", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Towering cliffside ridge offering 360-degree panoramic views of Aizawl city glowing against mountain horizons."},
                {"name": "Mizoram State Museum (Babu Tlang)", "category": "Museum", "entry_fee": 20, "opening": "09:30", "closing": "16:30", "description": "Showcases traditional Mizo tribal costumes, weapons, musical instruments, and anthropological dioramas."},
                {"name": "KV Paradise (Taj Mahal of Mizoram)", "category": "Historical", "entry_fee": 25, "opening": "09:00", "closing": "17:00", "description": "Grand two-storey white memorial church built by a grieving husband in memory of his beloved wife Vankhuma."},
            ]
        },
        {
            "district": "Lunglei", "lat": 22.8800, "lon": 92.7300, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Sawhchiar rice porridge, smoked meat, boiled pumpkin leaves",
            "description": "Second largest city of Mizoram named after the Bridge of Rock, blessed with panoramic hills.",
            "places": [
                {"name": "Lunglei Stone Bridge Natural Rock Formation", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Historic natural bridge-like rock structure found along the Nghasih river tributary from which the town gets its name."},
                {"name": "Khawnglung Wildlife Sanctuary", "category": "Wildlife", "entry_fee": 30, "opening": "07:00", "closing": "16:30", "description": "Dense mountain forest harboring barking deer, serows, hoolock gibbons, and leopards."},
            ]
        },
        {
            "district": "Champhai", "lat": 23.4700, "lon": 93.3300, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Local passion fruit, wild grape wine, Mizo boiled pork",
            "description": "Rice Bowl of Mizoram bordering Myanmar, famed for lush green paddy valley and heart-shaped Rih Dil lake.",
            "places": [
                {"name": "Rih Dil Border Lake (Heart-Shaped Lake)", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:30", "description": "Fabled heart-shaped natural lake revered in Mizo folklore as the passage of souls to the other world."},
                {"name": "Murlen National Park & Lianchhiari Lunglen Tlang", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "16:30", "description": "Sub-tropical forest so dense that only 1% of sunlight penetrates the canopy; habitat of Mrs. Hume's pheasant."},
            ]
        },
        {
            "district": "Kolasib", "lat": 24.2200, "lon": 92.6800, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Bai stew, steamed fish, bamboo shoots, sticky rice",
            "description": "Northern gateway to Mizoram along the Tlawng River, blessed with fishing spots and fruit orchards.",
            "places": [
                {"name": "Tlawng River Waterfront & Bairabi Rapids", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Longest river in Mizoram flowing through dense bamboo valleys, popular for angling and camping."},
            ]
        },
        {
            "district": "Serchhip", "lat": 23.3100, "lon": 92.8500, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Vawksa Rep, Thenzawl pineapple wine, boiled squash",
            "description": "Highest literacy district in India, home to Vantawng Falls—the highest waterfall in Mizoram, and Thenzawl handloom.",
            "places": [
                {"name": "Vantawng Khawhthla (Highest Waterfall in Mizoram)", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Dramatic 750-foot two-tiered waterfall roaring out of dense bamboo and evergreen forests near Thenzawl."},
                {"name": "Thenzawl Golf Resort & Handloom Village", "category": "Cultural", "entry_fee": 50, "opening": "08:00", "closing": "18:00", "description": "World-class 18-hole golf course nestled in highlands alongside indigenous Mizo handloom weaving ateliers."},
                {"name": "Tuirihiau Falls (Walk-Behind Waterfall)", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:00", "description": "Enchanting cascade with a natural rock cave cavern behind it, allowing visitors to walk directly behind the curtain of water."},
            ]
        },
        {
            "district": "Lawngtlai", "lat": 22.5300, "lon": 92.8900, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Lai ethnic chicken stew, boiled colocasia, fermented bamboo shoots",
            "description": "Autonomous district of the Lai people, gateway to the Phawngpui Blue Mountain and Chhimtuipui River.",
            "places": [
                {"name": "Phawngpui National Park (Blue Mountain - Highest Peak)", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "16:30", "description": "Highest peak in Mizoram (7,100 ft) renowned for spectacular cliffs, rare orchids, and rhododendron meadows."},
            ]
        },
        {
            "district": "Saiha (Siaha)", "lat": 22.4800, "lon": 92.9800, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Mara traditional smoked fish, boiled wild greens, millet beer",
            "description": "Autonomous district of the Mara people, celebrated for Palak Dil—the largest natural lake in Mizoram.",
            "places": [
                {"name": "Palak Dil (Pala Tipo - Largest Natural Lake in Mizoram)", "category": "Nature", "entry_fee": 20, "opening": "06:00", "closing": "17:30", "description": "Oval-shaped oval lake spanning 30 hectares, surrounded by pristine virgin rainforests and aquatic birdlife."},
            ]
        },
        {
            "district": "Mamit", "lat": 23.9300, "lon": 92.4900, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Reiek orange preserves, smoked meat, boiled pumpkin",
            "description": "Home to Dampa Tiger Reserve, India's westernmost rainforest sanctuary, and Reiek Tlang tourist peaks.",
            "places": [
                {"name": "Dampa Tiger Reserve (Largest Sanctuary in Mizoram)", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "16:30", "description": "Vast wilderness spanning 500 sq km protecting royal Bengal tigers, clouded leopards, and great Indian hornbills."},
                {"name": "Reiek Heritage Village & Peak", "category": "Cultural", "entry_fee": 30, "opening": "07:00", "closing": "18:00", "description": "Recreated traditional Mizo chieftain village perched on high cliffs with spectacular vistas of the Bangladesh plains."},
            ]
        },
        {
            "district": "Hnahthial", "lat": 22.9600, "lon": 92.9300, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Mizo bamboo rice, boiled seasonal forest vegetables",
            "description": "Southern district on the Tuipui River known for bamboo artisan communities and cave formations.",
            "places": [
                {"name": "Tuipui River Valley & Cherhlun Caves", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "17:00", "description": "Pristine mountain river flanked by deep lime caves and picturesque Mizo traditional settlements."},
            ]
        },
        {
            "district": "Khawzawl", "lat": 23.5300, "lon": 93.1800, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Mizo pork curry, steamed mustard greens, corn cakes",
            "description": "Agricultural ridge district famous for Kawnzar eco-park, orange plantations, and Chalfilh hill views.",
            "places": [
                {"name": "Chalfilh Tourist Mountain Ridge", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "17:30", "description": "High ridge trail at over 6,000 feet providing striking 360-degree vistas across northeastern Mizoram."},
            ]
        },
        {
            "district": "Saitual", "lat": 23.9700, "lon": 92.9700, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Freshwater fish fry from Tamdil, Bai, Sawhchiar",
            "description": "Centred around Tamdil Lake, a serene emerald reservoir surrounded by evergreen tropical forests.",
            "places": [
                {"name": "Tamdil (Mustard) Lake Resort", "category": "Nature", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Tranquil natural lake framed by weeping willows and tropical forests, popular for paddle boating and fish culture."},
            ]
        },
    ],

    # ==================== 6. NAGALAND (16 Districts) ====================
    "Nagaland": [
        {
            "district": "Kohima", "lat": 25.6751, "lon": 94.1086, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Smoked Pork with Axone (fermented soy), Galho rice stew, Naga King Chili (Bhut Jolokia) Chutney",
            "description": "State capital perched on green ridges, home to the World War II War Cemetery, Dzukou Valley, and Hornbill Festival.",
            "places": [
                {"name": "Kohima War Cemetery (WWII Battle of Kohima)", "category": "Historical", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "Solemn Commonwealth war cemetery honoring soldiers of the 1944 Battle of Kohima, engraved with the famous Kohima Epitaph."},
                {"name": "Kisama Heritage Village (Hornbill Festival Venue)", "category": "Cultural", "entry_fee": 50, "opening": "08:00", "closing": "18:00", "description": "Showcases authentic traditional morungs (dormitories) of all 16 major Naga tribes, stage for the world-renowned Hornbill Festival."},
                {"name": "Dzukou Valley (Valley of Flowers of the Northeast)", "category": "Nature", "entry_fee": 100, "opening": "06:00", "closing": "17:00", "description": "High-altitude rolling emerald valley at 8,000 ft blooming with endemic Dzukou lilies and carved by frozen mountain rivulets."},
                {"name": "Kohima State Museum & Cathedral Church", "category": "Museum", "entry_fee": 20, "opening": "09:30", "closing": "16:30", "description": "Displays priceless dioramas, authentic clan regalia, Naga spears, carved gateposts, and head-hunting trophies."},
            ]
        },
        {
            "district": "Dimapur", "lat": 25.9090, "lon": 93.7267, "crime_index": 28.0, "safety_tier": "MEDIUM",
            "food": "Naga Pork with bamboo shoots, Raja Mircha chutney, Steamed fish in banana leaf",
            "description": "Commercial capital and main rail-air gateway of Nagaland, home to medieval Kachari monolith ruins.",
            "places": [
                {"name": "Kachari Ruins & Mushroom Monoliths", "category": "Historical", "entry_fee": 25, "opening": "08:00", "closing": "17:00", "description": "10th-century carved monolithic mushroom-shaped sandstone pillars built during the Dimasa Kachari kingdom."},
                {"name": "Nagaland Zoological Park & Green Park", "category": "Wildlife", "entry_fee": 30, "opening": "09:00", "closing": "16:30", "description": "Sprawling wildlife conservation facility housing Blyth's tragopans, Great Indian hornbills, and leopards."},
            ]
        },
        {
            "district": "Mokokchung", "lat": 26.3250, "lon": 94.5300, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Ao Anishi (fermented taro leaves) with smoked pork, bamboo shoot fish",
            "description": "Cultural heart of the Ao Nagas, famous for historic villages like Ungma, Longkhum, and Mopungchuket.",
            "places": [
                {"name": "Ungma & Mopungchuket Cultural Heritage Villages", "category": "Cultural", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Oldest Ao villages showcasing ancient ceremonial log drums, monumental wood sculptures, and tribal museums."},
                {"name": "Longkhum Eagle's Nest Ridge", "category": "Viewpoint", "entry_fee": 0, "opening": "06:00", "closing": "17:30", "description": "Scenic hilltop village at 6,000 feet offering breathtaking vistas of snow-dusted Himalayan peaks and rhododendron trails."},
            ]
        },
        {
            "district": "Mon", "lat": 26.7500, "lon": 95.0500, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Konyak smoked beef, boiled yam, hot king chili paste",
            "description": "Land of the Konyaks—the legendary tattooed headhunter warriors, home to Longwa village straddling the Myanmar border.",
            "places": [
                {"name": "Longwa Village & Angh's (King's) Palace (Indo-Myanmar Border)", "category": "Cultural", "entry_fee": 0, "opening": "07:00", "closing": "17:30", "description": "Unique international border village where the chief's bedroom lies in India and kitchen in Myanmar; home to tattooed elders."},
                {"name": "Shangnyu Village & 8-Foot Carved Wooden Memorial", "category": "Cultural", "entry_fee": 0, "opening": "08:00", "closing": "17:00", "description": "Houses an ancient 8-foot tall and 12-foot wide solid wood structure carved with human and animal figures from antiquity."},
            ]
        },
        {
            "district": "Wokha", "lat": 26.1000, "lon": 94.2700, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Lotha smoked meat, bamboo shoot chicken, sticky rice",
            "description": "Homeland of the Lotha Nagas, famous for Mount Tiyi and the Doyang Reservoir where millions of Amur falcons roost.",
            "places": [
                {"name": "Doyang Reservoir (Amur Falcon Capital of the World)", "category": "Wildlife", "entry_fee": 20, "opening": "06:00", "closing": "17:30", "description": "Global stopover site where over a million migrating Amur falcons roost in late autumn during their epic migration to Africa."},
                {"name": "Mount Tiyi Peak & Totsu Cliff", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "Sacred summit at 6,550 feet blanketed in wild yellow and purple orchids, revered as the Orchard of Souls."},
            ]
        },
        {
            "district": "Tuensang", "lat": 26.2800, "lon": 94.8300, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Chang smoked pork with axone, millet cakes, boiled beans",
            "description": "Eastern highland district home to the Chang, Khiamniungan, and Sangtam tribes, rich in traditional living traditions.",
            "places": [
                {"name": "Livingston Ridge & Tsadang Village", "category": "Cultural", "entry_fee": 0, "opening": "07:00", "closing": "17:30", "description": "Pristine mountain village preserving centuries-old warrior Morungs, stone monoliths, and hand-woven shawls."},
            ]
        },
        {
            "district": "Phek", "lat": 25.6800, "lon": 94.4800, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Chakhesang dried meat with ginger, wild herbs, terraced rice",
            "description": "Home to the Chakhesang and Pochury tribes, featuring Pfutsero—the coldest town in Nagaland, and heart-shaped Shilloi Lake.",
            "places": [
                {"name": "Pfutsero Town & Glory Peak (Coldest Town in Nagaland)", "category": "Viewpoint", "entry_fee": 20, "opening": "06:00", "closing": "17:30", "description": "Highest altitude town in Nagaland (7,000 ft) offering views of Mount Saramati and terraced apple orchards."},
                {"name": "Shilloi Lake (Luphe - Footprint Lake)", "category": "Nature", "entry_fee": 20, "opening": "06:00", "closing": "17:30", "description": "Enchanting foot-shaped natural lake surrounded by pine forests, revered in Pochury folklore as the abode of holy spirits."},
            ]
        },
        {
            "district": "Zunheboto", "lat": 26.0000, "lon": 94.5200, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Sumi Axone with smoked pork, roasted grasshoppers, Anishi",
            "description": "Homeland of the fierce martial Sumi Nagas, featuring the largest Baptist church in Asia at Zunheboto.",
            "places": [
                {"name": "Zunheboto Sumi Baptist Church (Largest Church in Asia)", "category": "Spiritual", "entry_fee": 0, "opening": "07:00", "closing": "18:30", "description": "Monumental blue-roofed church standing 166 feet high that can seat over 8,500 people simultaneously."},
                {"name": "Satoi Range Wildlife Corridor", "category": "Wildlife", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "High ridge forest shelter for rare Blyth's tragopans and blooming wild rhododendrons."},
            ]
        },
        {
            "district": "Kiphire", "lat": 25.8700, "lon": 94.7800, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Sangtam and Yimkhiung smoked meat, boiled corn bread",
            "description": "Home to Mount Saramati, the highest peak in Nagaland, bordering Myanmar, and limestone caves at Mimi.",
            "places": [
                {"name": "Mount Saramati Summit (12,600 ft - Nagaland's Highest Peak)", "category": "Adventure", "entry_fee": 0, "opening": "05:00", "closing": "17:00", "description": "Majestic snow-clad peak on the Myanmar border forming a natural barrier between India and Burma."},
                {"name": "Mimi & Salomi Limestone Caves", "category": "Adventure", "entry_fee": 0, "opening": "08:00", "closing": "16:00", "description": "Intricate subterranean cave passages inhabited by colonies of bats, tucked away in the eastern hills."},
            ]
        },
        {
            "district": "Longleng", "lat": 26.4700, "lon": 94.8200, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Phom traditional pork stew with king chili, smoked taro",
            "description": "Homeland of the Phom Nagas, celebrated for skilled bamboo weaving, pottery, and the Monyu festival.",
            "places": [
                {"name": "Shendang Village & Dikhu River Cliffs", "category": "Cultural", "entry_fee": 0, "opening": "07:00", "closing": "17:30", "description": "Ancient village perching on rocky cliffs above the Dikhu River, preserving authentic Phom woodcraft traditions."},
            ]
        },
        {
            "district": "Peren", "lat": 25.5200, "lon": 93.7300, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Zeliang bamboo tube pork, roasted pumpkin seeds, wild honey",
            "description": "Green valley of the Zeliangrong people, home to Ntangki National Park and Mount Pauna.",
            "places": [
                {"name": "Ntangki National Park (Intanki)", "category": "Wildlife", "entry_fee": 50, "opening": "06:30", "closing": "16:30", "description": "Sprawling 200-sq km national park preserving hoolock gibbons, golden langurs, hornbills, and wild elephants."},
                {"name": "Benreu Tourist Village & Mount Pauna (3rd Highest Peak)", "category": "Cultural", "entry_fee": 20, "opening": "07:00", "closing": "17:30", "description": "Centuries-old village at 6,400 ft built on vertical cliffs with traditional wooden morungs and herbal wellness trails."},
            ]
        },
        {
            "district": "Noklak", "lat": 26.2000, "lon": 95.0000, "crime_index": 11.0, "safety_tier": "LOW",
            "food": "Khiamniungan smoked pork, boiled millet, wild roots",
            "description": "Known as the Frontier District, home to the Khiamniungan tribe, brass craft, and border trade routes.",
            "places": [
                {"name": "Pangsha Indo-Myanmar Border Village & Pass", "category": "Cultural", "entry_fee": 0, "opening": "07:00", "closing": "17:00", "description": "Historic trans-border village along the Patkai Range known for peaceful trade exchanges with Myanmar tribes."},
            ]
        },
        {
            "district": "Chumoukedima", "lat": 25.8200, "lon": 93.7500, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Naga fusion cuisine, smoked pork burgers, iced passion fruit juice",
            "description": "Fast-growing district featuring Chumoukedima waterfall, eco-adventure resorts, and the Bamboo Resource Centre.",
            "places": [
                {"name": "Chumoukedima Waterfalls & Triple Falls", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:00", "description": "Three scenic parallel cascades dropping into a natural rock pool amidst thick bamboo hills."},
                {"name": "Nagaland Bamboo Resource Centre", "category": "Cultural", "entry_fee": 20, "opening": "09:00", "closing": "17:00", "description": "Modern center showcasing bamboo architectural structures, fine furniture, musical instruments, and charcoal crafts."},
            ]
        },
        {
            "district": "Niuland", "lat": 25.9500, "lon": 93.8800, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Local river fish, smoked chicken with chili, sticky rice",
            "description": "Agricultural plains district rich in orange and rubber plantations, bird habitats, and river trails.",
            "places": [
                {"name": "Insha River Picnic Banks & Forest Trails", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "17:30", "description": "Tranquil riverfront with shaded canopies popular for weekend camping and community angling."},
            ]
        },
        {
            "district": "Tseminyu", "lat": 25.9200, "lon": 94.2100, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Rengma smoked meat with bitter eggplant, Galho rice",
            "description": "Historical homeland of the Rengma Nagas, celebrated for Ngada festival and community biodiversity reserves.",
            "places": [
                {"name": "Sendenyu Community Biodiversity Reserve", "category": "Wildlife", "entry_fee": 30, "opening": "07:00", "closing": "16:30", "description": "Pioneering village-managed sanctuary conserving barking deer, serow, and rich avian biodiversity."},
            ]
        },
        {
            "district": "Shamator", "lat": 26.0500, "lon": 94.9000, "crime_index": 11.0, "safety_tier": "LOW",
            "food": "Yimkhiung and Tikhir traditional boiled pork, roasted yam",
            "description": "Known as the Brotherhood town, uniting Yimkhiung and Tikhir cultures at the foot of Mount Saramati.",
            "places": [
                {"name": "Chessore Village & Brotherhood Vistas", "category": "Cultural", "entry_fee": 0, "opening": "07:00", "closing": "17:00", "description": "Scenic mountain settlements preserving ancient wood-carving arts and vibrant Medümneo festival rituals."},
            ]
        },
    ],

    # ==================== 7. SIKKIM (6 Districts) ====================
    "Sikkim": [
        {
            "district": "East Sikkim (Gangtok)", "lat": 27.3389, "lon": 88.6065, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Momos, Thukpa, Gundruk & Sinki soup, Phagshapa (pork with radish), Chhurpi soup",
            "description": "Administrative and tourist capital featuring MG Marg, Rumtek Monastery, and sacred Tsomgo Lake on the Nathula highway.",
            "places": [
                {"name": "Tsomgo (Changu) Lake & Baba Mandir (12,310 ft)", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "15:00", "description": "Glacial alpine lake sacred to both Buddhists and Hindus, surrounded by steep mountains and yak rides."},
                {"name": "Nathula Pass (Indo-China Border - 14,140 ft)", "category": "Historical", "entry_fee": 200, "opening": "08:00", "closing": "14:00", "description": "Historic mountain pass on the Old Silk Route connecting India to Tibet, flanked by Indian Army bunkers."},
                {"name": "Rumtek Monastery (Dharmachakra Centre)", "category": "Monastery", "entry_fee": 20, "opening": "06:00", "closing": "18:00", "description": "Seat of His Holiness the Gyalwang Karmapa (Kagyupa lineage), holding golden stupas, rare thangkas, and Buddhist scriptures."},
                {"name": "MG Marg Boulevard & Ban Jhakri Waterfalls", "category": "Park", "entry_fee": 50, "opening": "08:00", "closing": "21:00", "description": "Litter-free, pedestrian-only cobblestone promenade with vibrant cafes, coupled with shamanic ethnic waterfall park."},
            ]
        },
        {
            "district": "West Sikkim (Geyzing)", "lat": 27.2800, "lon": 88.2500, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Kinema curry (fermented soybean), Sel Roti with potato curry, Tongba (millet beer)",
            "description": "Historical heartland of Sikkim at Pelling, home to Pemayangtse Monastery, Rabdentse royal ruins, and Skywalk.",
            "places": [
                {"name": "Pemayangtse Monastery (1705 CE)", "category": "Monastery", "entry_fee": 20, "opening": "07:00", "closing": "17:00", "description": "One of Sikkim's oldest and premier Nyingma monasteries, housing the famous wooden sculpture of Zandog Palri."},
                {"name": "Rabdentse Ruins & Pelling Glass Skywalk", "category": "Historical", "entry_fee": 50, "opening": "08:00", "closing": "17:30", "description": "Ancient ruins of Sikkim's 2nd royal capital alongside India's first glass skywalk overlooking the giant Chenrezig statue."},
                {"name": "Khecheopalri Lake (Wish-Fulfilling Sacred Lake)", "category": "Spiritual", "entry_fee": 20, "opening": "06:00", "closing": "18:00", "description": "Sacred footprint lake revered by Buddhists and Hindus where birds reportedly do not allow a single leaf to float on water."},
                {"name": "Kanchenjunga Falls", "category": "Waterfall", "entry_fee": 20, "opening": "07:00", "closing": "17:00", "description": "Perennial multi-stream waterfall roaring down rocky gorges on the highway to Yuksom."},
            ]
        },
        {
            "district": "North Sikkim (Mangan)", "lat": 27.5000, "lon": 88.5300, "crime_index": 10.0, "safety_tier": "LOW",
            "food": "Lachung vegetable stew, Yak cheese, Thukpa, butter tea",
            "description": "Glacial alpine wonderland featuring Yumthang Valley of Flowers, Zero Point, and holy Gurudongmar Lake at 17,800 ft.",
            "places": [
                {"name": "Gurudongmar Lake (17,800 ft - Sacred High-Altitude Lake)", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "12:00", "description": "One of the highest lakes in the world, blessed by Guru Padmasambhava; a portion remains unfrozen even during harsh sub-zero winters."},
                {"name": "Yumthang Valley of Flowers & Shingba Rhododendron Sanctuary", "category": "Nature", "entry_fee": 50, "opening": "06:00", "closing": "16:00", "description": "Paradise valley at 11,800 feet blooming with over 24 species of rhododendrons, hot springs, and grazing yaks."},
                {"name": "Zero Point (Yumesamdong - 15,300 ft)", "category": "Nature", "entry_fee": 0, "opening": "07:00", "closing": "13:00", "description": "Edge of civilization where three rivers meet surrounded by snow blankets, right before the international frontier."},
            ]
        },
        {
            "district": "South Sikkim (Namchi)", "lat": 27.1667, "lon": 88.3500, "crime_index": 13.0, "safety_tier": "LOW",
            "food": "Temi orthodox tea, Sel Roti, Gundruk jhol, Chhurpi ningro",
            "description": "Spiritual and scenic center featuring Char Dham (Siddhesvara Dhaam), giant Guru Padmasambhava statue, and Temi Tea Garden.",
            "places": [
                {"name": "Siddhesvara Dhaam (Char Dham Namchi)", "category": "Spiritual", "entry_fee": 50, "opening": "06:30", "closing": "20:30", "description": "Grand spiritual complex recreating the 12 Jyotirlingas and the 4 holy Dhams (Badrinath, Jagannath, Dwarka, Rameswaram) with an 87-ft Shiva statue."},
                {"name": "Samdruptse Hill & 138-Foot Guru Padmasambhava Statue", "category": "Spiritual", "entry_fee": 30, "opening": "07:00", "closing": "18:00", "description": "Hill of the wish-fulfilling jewel crowned by a 138-foot shimmering gilded statue of Sikkim's patron saint Guru Rinpoche."},
                {"name": "Temi Tea Garden (Sikkim's Only Tea Estate)", "category": "Nature", "entry_fee": 20, "opening": "07:00", "closing": "18:00", "description": "Sprawling over 440 acres of picturesque slopes, producing internationally renowned organic orthodox tea."},
                {"name": "Tarey Bhir Ridge Viewpoint", "category": "Viewpoint", "entry_fee": 30, "opening": "07:00", "closing": "17:30", "description": "10,000-foot ridge pathway offering breathtaking edge-of-the-cliff views into the deep Teesta and Rangit river valleys."},
            ]
        },
        {
            "district": "Pakyong", "lat": 27.2300, "lon": 88.5800, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Organic ginger snacks, Momos, nettle soup (Sisnu)",
            "description": "Home to Sikkim's greenfield Pakyong Airport, historical Kartok Monastery, and Saramsa Garden.",
            "places": [
                {"name": "Saramsa Garden & Orchidarium (Ipecac Garden)", "category": "Park", "entry_fee": 20, "opening": "08:00", "closing": "17:30", "description": "Established in 1922 by the Chogyal royal family, showcasing hundreds of exotic orchids and medicinal plants."},
                {"name": "Rolep River Valley Eco-Trail", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "17:00", "description": "Unspoiled village with gushing mountain streams, wooden bridges, and Sokeythang water cascades."},
            ]
        },
        {
            "district": "Soreng", "lat": 27.1700, "lon": 88.2000, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Sel Roti, Kinema, Tongba, organic mountain vegetables",
            "description": "Gateway to the Barsey Rhododendron Sanctuary, Rinchenpong, and Kaluk, blessed with Mount Kanchenjunga panoramas.",
            "places": [
                {"name": "Barsey Rhododendron Sanctuary", "category": "Nature", "entry_fee": 50, "opening": "06:00", "closing": "16:30", "description": "High-altitude sanctuary stretching over 104 sq km that transforms into a fiery crimson carpet of blooms during spring."},
                {"name": "Rinchenpong Heritage Monastery & Poison Pokhari", "category": "Monastery", "entry_fee": 0, "opening": "07:00", "closing": "17:30", "description": "1730 monastery housing rare Ati Buddha statues, near the historic pond where British troops were thwarted with poisonous herbs."},
            ]
        },
    ],

    # ==================== 8. TRIPURA (8 Districts) ====================
    "Tripura": [
        {
            "district": "West Tripura", "lat": 23.8315, "lon": 91.2868, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Mui Borok (fermented Berma fish), Chakhwi, Mosdeng Serma & Bangui rice",
            "description": "Capital district of Agartala featuring the royal Ujjayanta Palace, Heritage Park, and Akhaura border post.",
            "places": [
                {"name": "Ujjayanta Palace & Tripura State Museum", "category": "Historical", "entry_fee": 20, "opening": "10:00", "closing": "17:00", "description": "Magnificent neoclassical white palace built in 1901 by Maharaja Radha Kishore Manikya, set in Mughal gardens."},
                {"name": "Heritage Park Agartala", "category": "Park", "entry_fee": 20, "opening": "09:00", "closing": "19:00", "description": "Landscaped cultural park featuring mini-replicas of Tripura's iconic monuments like Unakoti, Neermahal, and Ujjayanta."},
                {"name": "Akhaura Integrated Check Post (Indo-Bangladesh Border)", "category": "Cultural", "entry_fee": 0, "opening": "16:00", "closing": "18:00", "description": "Border ceremony venue with joint beating retreat and flag-lowering parade by BSF and Border Guards Bangladesh."},
            ]
        },
        {
            "district": "Sepahijala", "lat": 23.6300, "lon": 91.3100, "crime_index": 19.0, "safety_tier": "LOW",
            "food": "Freshwater fish curry, Berma chutney, bamboo shoot pork",
            "description": "Home to Neermahal—the floating water palace on Rudrasagar Lake, and Clouded Leopard National Park.",
            "places": [
                {"name": "Neermahal Water Palace (Rudrasagar Lake)", "category": "Historical", "entry_fee": 50, "opening": "09:00", "closing": "17:00", "description": "Fabulous 1930 red-and-white royal summer palace built in the center of the lake, blending Hindu and Mughal styles."},
                {"name": "Sepahijala Wildlife Sanctuary & Clouded Leopard Park", "category": "Wildlife", "entry_fee": 30, "opening": "08:30", "closing": "16:30", "description": "Bio-reserve dedicated to breeding clouded leopards, capped langurs, and sheltering over 150 species of birds."},
            ]
        },
        {
            "district": "Gomati", "lat": 23.5300, "lon": 91.4800, "crime_index": 20.0, "safety_tier": "LOW",
            "food": "Peda from Matabari, Gomati freshwater fish, Chakhwi",
            "description": "Spiritual center at Udaipur (City of Lakes), renowned for the 500-year-old Tripura Sundari Temple (Matabari).",
            "places": [
                {"name": "Tripura Sundari Temple (Matabari - 51 Shakti Peethas)", "category": "Spiritual", "entry_fee": 0, "opening": "05:00", "closing": "21:00", "description": "Consecrated in 1501 CE by Maharaja Dhanya Manikya, one of the 51 sacred Shakti Peethas where Sati's right foot fell."},
                {"name": "Bhubaneswari Temple & Kalyan Sagar", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "17th-century brick temple immortalized in Rabindranath Tagore's famous works Rajarshi and Bisarjan."},
                {"name": "Tepania Eco-Park", "category": "Park", "entry_fee": 20, "opening": "08:00", "closing": "17:30", "description": "Lush eco-tourism reserve housing a tree-house trail, cactus garden, and natural orchidarium."},
            ]
        },
        {
            "district": "South Tripura", "lat": 23.2300, "lon": 91.4500, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Traditional tribal pork stew, roasted fish with spicy chili, Pitha",
            "description": "Centred around Belonia, featuring the historic Buddhist rock-cut ruins of Pilak and Rajbari National Park.",
            "places": [
                {"name": "Pilak Archaeological Buddhist-Hindu Site", "category": "Historical", "entry_fee": 25, "opening": "08:00", "closing": "17:00", "description": "8th–12th century archaeological site revealing colossal stone images of Avalokiteshvara, terracotta seals, and stupas."},
                {"name": "Trishna Wildlife Sanctuary & Rajbari National Park", "category": "Wildlife", "entry_fee": 40, "opening": "07:00", "closing": "16:30", "description": "Premier sanctuary conserving Indian bison (Gaur), golden langurs, pheasant colonies, and virgin sal reserves."},
            ]
        },
        {
            "district": "Khowai", "lat": 24.0600, "lon": 91.6000, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Bamboo shoot chicken, Berma chutney, seasonal sweet pitha",
            "description": "Green district of rubber and tea plantations, featuring Baramura Eco Park and historical shrines.",
            "places": [
                {"name": "Baramura Eco Park & Hathai Kotor Ridge", "category": "Park", "entry_fee": 20, "opening": "08:00", "closing": "17:30", "description": "Scenic eco-park set across the Baramura hills with suspension rope bridges, aviaries, and tree-top walkways."},
            ]
        },
        {
            "district": "Dhalai", "lat": 23.9000, "lon": 91.8500, "crime_index": 17.0, "safety_tier": "LOW",
            "food": "Freshwater fish fry from Dumbur lake, Mosdeng, steamed tubers",
            "description": "Largest district of Tripura, home to the breathtaking Dumbur Lake with its 48 emerald islets and Narikel Kunja.",
            "places": [
                {"name": "Dumbur Lake & Narikel Kunja (Coconut Island)", "category": "Nature", "entry_fee": 30, "opening": "07:00", "closing": "17:30", "description": "Massive waterbody shaped like Lord Shiva's dambur spanning 41 sq km, with speedboat rides to coconut-fringed islands."},
                {"name": "Longtharai Shiva Temple (Dhalai Hills)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Deeply revered hilltop shrine of Lord Shiva in the indigenous Debbarma dialect, surrounded by dense forests."},
            ]
        },
        {
            "district": "Unakoti", "lat": 24.3300, "lon": 92.0200, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Berma spicy fish soup, fermented bamboo shoots, fresh pineapples",
            "description": "Home to Unakoti—the ancient Shaivite rock-carved marvel often described as the Angkor Wat of the North East.",
            "places": [
                {"name": "Unakoti Rock-Cut Relief Carvings (One Less than a Crore)", "category": "Historical", "entry_fee": 25, "opening": "06:00", "closing": "18:00", "description": "7th–9th century colossal bas-relief rock carvings of Lord Shiva (Unakotiswara Kal Bhairava, 30 ft) and Ganesh on a lush hill face."},
            ]
        },
        {
            "district": "North Tripura", "lat": 24.3800, "lon": 92.1700, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Jampui orange blossom tea, Mizo and Reang boiled stews",
            "description": "Home to the Jampui Hills (Land of Eternal Spring), famous for orange orchards and panoramic vistas into Mizoram.",
            "places": [
                {"name": "Jampui Hills & Vanghmun Village (Land of Eternal Spring)", "category": "Nature", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Highest hill range in Tripura (3,000 ft) renowned for orange festivals, misty valleys, and views into Chittagong Hill Tracts."},
                {"name": "Bhavatarini Temple (Kumarghat)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Revered Kali shrine surrounded by manicured flower gardens and spiritual prayer pavilions."},
            ]
        },
    ],

    # ==================== 9. ANDAMAN AND NICOBAR ISLANDS (3 Districts) ====================
    "Andaman and Nicobar Islands": [
        {
            "district": "South Andaman", "lat": 11.6234, "lon": 92.7265, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Andaman Fish Curry, Lobster Thermidor, Coconut Prawn Curry, Chilli Crab",
            "description": "Gateway to the Andaman archipelago at Port Blair, historic Cellular Jail, and world-famous Radhanagar Beach on Havelock.",
            "places": [
                {"name": "Cellular Jail National Memorial (Kala Pani)", "category": "Historical", "entry_fee": 30, "opening": "09:00", "closing": "17:00", "description": "Historic colonial prison where Indian freedom fighters were exiled, famous for its 7-winged panopticon design and light & sound show."},
                {"name": "Radhanagar Beach (Beach No. 7, Havelock Island / Swaraj Dweep)", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Consistently voted one of the best beaches in Asia, boasting powder-white sands, turquoise surf, and majestic Mahua tree canopies."},
                {"name": "Ross Island (Netaji Subhash Chandra Bose Dweep)", "category": "Historical", "entry_fee": 50, "opening": "08:30", "closing": "16:30", "description": "Former British administrative headquarters now enveloped in giant ficus tree roots, with deer roaming among ruined colonial ballrooms."},
                {"name": "Neil Island (Shaheed Dweep) Natural Bridge & Bharatpur Beach", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Living rock formation carved by ocean tides alongside vibrant coral reefs offering glass-bottom boat excursions."},
                {"name": "Chidiya Tapu Sunset Point & Biological Park", "category": "Viewpoint", "entry_fee": 20, "opening": "06:00", "closing": "18:00", "description": "Southernmost tip of South Andaman renowned for majestic crimson sunsets over the sea and exotic endemic forest birds."},
            ]
        },
        {
            "district": "North and Middle Andaman", "lat": 12.9100, "lon": 92.9000, "crime_index": 12.0, "safety_tier": "LOW",
            "food": "Fresh seafood fry, steamed fish in coconut milk, tropical fruits",
            "description": "Rugged eco-paradise featuring Baratang limestone caves, mud volcanoes, twin Ross & Smith Islands, and Saddle Peak.",
            "places": [
                {"name": "Baratang Island Limestone Caves & Mud Volcano", "category": "Nature", "entry_fee": 100, "opening": "07:00", "closing": "15:00", "description": "Boat cruise through dense mangrove creeks leading to spectacular million-year-old stalactite and stalagmite limestone caverns."},
                {"name": "Ross and Smith Twin Islands (Diglipur)", "category": "Beach", "entry_fee": 50, "opening": "06:00", "closing": "15:00", "description": "Two paradise islands joined naturally by a 50-meter-wide sandbar that submerges during high tide and surfaces during low tide."},
                {"name": "Saddle Peak National Park (Highest Peak in Andamans - 732m)", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "14:00", "description": "Highest mountain peak in the archipelago surrounded by lush sub-tropical rain forests and pristine streams."},
            ]
        },
        {
            "district": "Nicobar", "lat": 7.0000, "lon": 93.8000, "crime_index": 10.0, "safety_tier": "LOW",
            "food": "Nicobarese seafood boiled with pandanus, coconut water",
            "description": "Southern island group home to Great Nicobar Biosphere Reserve and Indira Point—the southernmost geographic tip of India.",
            "places": [
                {"name": "Indira Point & Lighthouse (Southernmost Tip of India)", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Southernmost geographic point of the Republic of India at 6°45'10″ N latitude, featuring a towering red-and-white lighthouse."},
                {"name": "Great Nicobar Biosphere Reserve & Campbell Bay", "category": "Wildlife", "entry_fee": 50, "opening": "06:00", "closing": "16:00", "description": "UNESCO World Biosphere reserve home to the indigenous Shompen and Nicobarese tribes, saltwater crocodiles, and robber crabs."},
            ]
        },
    ],

    # ==================== 10. DADRA AND NAGAR HAVELI AND DAMAN AND DIU (3 Districts) ====================
    "Dadra and Nagar Haveli and Daman and Diu": [
        {
            "district": "Daman", "lat": 20.3974, "lon": 72.8328, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Portuguese Chicken Poha, Fish Koliwada, Jet (Sweet toddy), Prawn Curry Rice",
            "description": "Coastal enclave on the Arabian Sea renowned for massive 16th-century Portuguese fortresses, beaches, and tax-free hospitality.",
            "places": [
                {"name": "Moti Daman Fort & Lighthouse", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "19:00", "description": "Massive 1559 Portuguese stronghold enclosed by ten bastions and ramparts on the mouth of the Daman Ganga River."},
                {"name": "Church of Bom Jesus (1603 CE)", "category": "Spiritual", "entry_fee": 0, "opening": "07:00", "closing": "18:30", "description": "Exquisite Portuguese church famous for its intricate gilded wooden altar carved by local artisans and Portuguese friars."},
                {"name": "Jampore Beach & Water Sports", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Tranquil blackish-sand beach with shallow waters ideal for swimming, parasailing, buggy rides, and sunset snacks."},
                {"name": "Nani Daman Fort (Fort of St. Jerome)", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:30", "description": "Picturesque fortress facing Moti Daman across the river, housing the Church of Our Lady of the Sea and historic cemetery."},
            ]
        },
        {
            "district": "Diu", "lat": 20.7144, "lon": 70.9874, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Diu Lobster, Cozido (Portuguese meat stew), Crab masala, Cashew feni",
            "description": "Picturesque island off Gujarat's Saurashtra coast, famous for Diu Fort, Naida Caves, Nagoa beach, and colonial charm.",
            "places": [
                {"name": "Diu Fort (Fortaleza de São Tomé - 1535 CE)", "category": "Fort", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Formidable sea fortress surrounded by the sea on three sides, studded with bronze cannons and an active lighthouse."},
                {"name": "Naida Caves (Sunlit Geological Rock Caverns)", "category": "Nature", "entry_fee": 0, "opening": "08:00", "closing": "17:30", "description": "Intricate network of ancient open-roofed stone quarries and caves with natural light beams cutting through jagged arches."},
                {"name": "Nagoa Beach (Horseshoe Beach with Hoka Trees)", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "22:00", "description": "Crescent-shaped horseshoe beach famous for calm waters, water scooters, and rare African Hoka branching palm trees."},
                {"name": "INS Khukri Memorial & Sunset Point", "category": "Historical", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "Memorial honoring Captain Mahendra Nath Mulla and sailors of the INS Khukri who perished during the 1971 Indo-Pak war."},
            ]
        },
        {
            "district": "Dadra and Nagar Haveli", "lat": 20.2763, "lon": 73.0083, "crime_index": 15.0, "safety_tier": "LOW",
            "food": "Ubadiyu (earthen pot winter vegetable roast), Khaman, Gamthi chicken",
            "description": "Centred around Silvassa, wrapped in dense teak forests, tribal folklore, Madhuban Dam, and lion safaris.",
            "places": [
                {"name": "Vanganga Lake Garden (Dadra Garden)", "category": "Park", "entry_fee": 20, "opening": "08:30", "closing": "20:30", "description": "Japanese-style landscaped lake garden featuring wooden bridges, paddle boats, and musical illuminated fountains."},
                {"name": "Lion Safari Wildlife Park (Vasona)", "category": "Wildlife", "entry_fee": 50, "opening": "09:00", "closing": "17:00", "description": "Fenced sanctuary allowing visitors to view Asiatic lions in an open jungle setting from caged safari buses."},
                {"name": "Dudhni Water Sports Complex (Madhuban Dam)", "category": "Adventure", "entry_fee": 30, "opening": "08:30", "closing": "17:30", "description": "Vast reservoir on the Damanganga River offering jet-skis, speedboats, houseboats, and tribal Warli craft markets."},
                {"name": "Silvassa Tribal Cultural Museum", "category": "Museum", "entry_fee": 10, "opening": "09:30", "closing": "17:30", "description": "Curates authentic masks, hunting gear, Warli wall paintings, and musical instruments of Dhodia and Varli tribes."},
            ]
        },
    ],

    # ==================== 11. LAKSHADWEEP (1 District) ====================
    "Lakshadweep": [
        {
            "district": "Lakshadweep", "lat": 10.5667, "lon": 72.6417, "crime_index": 8.0, "safety_tier": "LOW",
            "food": "Tuna Fish Curry, Mus Kavaab, Rayereha (red fish curry), Coconut Rice, Kadalakka",
            "description": "India's smallest Union Territory, an archipelago of 36 breathtaking coral atolls, turquoise lagoons, and virgin white beaches.",
            "places": [
                {"name": "Agatti Island Lagoon & Scuba Diving Reefs", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Pristine lagoon with coral reefs offering world-class scuba diving, snorkeling with sea turtles, and kayaking."},
                {"name": "Bangaram Island (Uninhabited Jewel of the Arabian Sea)", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Teardrop-shaped uninhabited coral atoll surrounded by phosphorescent bioluminescent waters at night and coral reefs."},
                {"name": "Kavaratti Island & Marine Aquarium", "category": "Spiritual", "entry_fee": 25, "opening": "08:30", "closing": "18:00", "description": "Capital island housing the famous 17th-century Ujra Mosque with carved driftwood ceilings and a vibrant marine museum."},
                {"name": "Minicoy Island British Lighthouse (1885)", "category": "Historical", "entry_fee": 20, "opening": "09:00", "closing": "17:00", "description": "Historic 300-foot white masonry lighthouse built by the British, offering sweeping vistas of the entire atoll and Maldivian-style villages."},
                {"name": "Kalpeni Island Coral Debris Bank", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "18:00", "description": "Famous for its massive storm bank of coral boulders along the shoreline and scenic islets of Tilakkam and Pitti."},
            ]
        },
    ],

    # ==================== 12. PUDUCHERRY (4 Districts) ====================
    "Puducherry": [
        {
            "district": "Puducherry", "lat": 11.9416, "lon": 79.8083, "crime_index": 22.0, "safety_tier": "LOW",
            "food": "Creole Curry, Baguette & Croissants, French Ratatouille, Prawn Masala, Filter Coffee",
            "description": "French Riviera of the East, famed for White Town colonial quarters, Promenade Beach, Sri Aurobindo Ashram, and Auroville.",
            "places": [
                {"name": "Promenade Beach & French Quarter (White Town)", "category": "Beach", "entry_fee": 0, "opening": "00:00", "closing": "23:59", "description": "1.5km pedestrian seaside boulevard lined with yellow-and-white Franco-Tamil mansions, Gandhi statue, and cafes."},
                {"name": "Sri Aurobindo Ashram (Samadhi Shrine)", "category": "Spiritual", "entry_fee": 0, "opening": "08:00", "closing": "18:00", "description": "Spiritual center founded in 1926 by Sri Aurobindo and The Mother, housing their marble samadhi surrounded by blooms."},
                {"name": "Auroville & The Matrimandir (City of Dawn)", "category": "Spiritual", "entry_fee": 0, "opening": "09:00", "closing": "16:30", "description": "Universal township founded by The Mother; features the iconic golden geodesic dome with an optical glass globe meditation chamber."},
                {"name": "Paradise Beach (Chunnambar Boat House)", "category": "Beach", "entry_fee": 30, "opening": "09:00", "closing": "17:30", "description": "Pristine isolated sand spit reachable via backwater boat cruise along the Chunnambar River."},
                {"name": "Basilica of the Sacred Heart of Jesus", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "18:30", "description": "Stunning 1907 Gothic Revival Catholic basilica adorned with stained-glass panels depicting the life of Jesus Christ."},
            ]
        },
        {
            "district": "Karaikal", "lat": 10.9254, "lon": 79.8380, "crime_index": 18.0, "safety_tier": "LOW",
            "food": "Karaikal Ammaiyar Halwa, Crab Curry, Meen Kulambu, Idiyappam",
            "description": "Coastal pilgrimage district on the Coromandel Coast, famous for Karaikal Ammaiyar Temple and French beachfront.",
            "places": [
                {"name": "Karaikal Sandy Beach & Arasalar Riverfront", "category": "Beach", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Expansive coastal beach promenade on the Bay of Bengal popular for sunset strolls and boating on the Arasalar river."},
                {"name": "Karaikal Ammaiyar Temple (Mango Festival Peeth)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "20:00", "description": "Dedicated to one of the 63 Nayanmars, celebrated for the annual Mangani (Mango) festival where sweet mangoes are cast from rooftops."},
                {"name": "Tirunallar Saneeswaran Temple", "category": "Spiritual", "entry_fee": 0, "opening": "05:30", "closing": "21:00", "description": "Renowned worldwide as the only temple where Lord Saturn (Shani Bhagavan) lost his malefic power to blessing Lord Nala."},
            ]
        },
        {
            "district": "Mahe", "lat": 11.7000, "lon": 75.5300, "crime_index": 14.0, "safety_tier": "LOW",
            "food": "Malabar Biryani, French-influenced seafood, Kallummakkaya (mussels) fry",
            "description": "Small enclave on the Arabian Sea surrounded entirely by Kerala, known for French colonial memories and St. Teresa's Shrine.",
            "places": [
                {"name": "Mahe Riverside Walkway & Tagore Park", "category": "Park", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Landscaped river promenade where the Mahe River meets the sea, featuring French streetlamps and statue of Marianne."},
                {"name": "St. Teresa's Church of Mahe (Est. 1736)", "category": "Spiritual", "entry_fee": 0, "opening": "06:00", "closing": "19:00", "description": "One of the oldest Catholic churches in Malabar, celebrated for the annual feast of Saint Teresa attracting all communities."},
            ]
        },
        {
            "district": "Yanam", "lat": 16.7300, "lon": 82.2100, "crime_index": 16.0, "safety_tier": "LOW",
            "food": "Godavari Royyala Vepudu (prawn fry), Chepala Pulusu, Pootharekulu",
            "description": "Enclave on the Godavari River surrounded by Andhra Pradesh, noted for its replica Eiffel Tower and riverside obelisk.",
            "places": [
                {"name": "Yanam Godavari Riverfront & Eiffel Tower Replica (Aanam Tower)", "category": "Viewpoint", "entry_fee": 20, "opening": "08:00", "closing": "21:00", "description": "100-meter-tall steel observation tower resembling Paris's Eiffel Tower offering circular views over the lush Godavari delta."},
                {"name": "Rajiv Gandhi Beach Promenade & Shiva Idol", "category": "Park", "entry_fee": 0, "opening": "06:00", "closing": "21:00", "description": "Scenic water promenade with life-sized statues, elephant sculptures, and seating areas along the Gautami Godavari."},
            ]
        },
    ]
}

