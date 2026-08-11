
import random

def calculate_macros(numeric_data, condition):
    age = numeric_data.get('age', 30)
    bmi = numeric_data.get('bmi', 22)
    calories = 2000
    if bmi > 25: calories = 1800
    if 'Diabetes' in condition: calories -= 100
    
    if 'Diabetes' in condition:
        carb_ratio, protein_ratio, fat_ratio = 0.35, 0.35, 0.30
    else:
        carb_ratio, protein_ratio, fat_ratio = 0.45, 0.25, 0.30
    return {
        'calories': calories,
        'protein_g': round((calories * protein_ratio) / 4),
        'carbs_g': round((calories * carb_ratio) / 4),
        'fat_g': round((calories * fat_ratio) / 9)
    }

def generate_diet(text, state='General'):
    text = text.lower()
    
    # High-Variety Comprehensive Database for 28 States
    state_data = {
        'Andhra Pradesh': {
            'breakfast': ['Pesarattu with Ginger Chutney', 'Idli with Sambar', 'Upma with Podi', 'MLA Pesarattu', 'Dibba Rotti', 'Atukula Upma', 'Poori Masala'],
            'lunch': ['Rice with Pappu', 'Gongura Pachadi', 'Pulihora', 'Tomato Dal', 'Bendakaya Fry', 'Vankaya Kothimeera Karam', 'Curd Rice'],
            'dinner': ['Jonna Rotte with Brinjal Curry', 'Roti with Mixed Veg', 'Semiya Upma', 'Ariselu (limited)', 'Rice with Majjiga Pulusu']
        },
        'Arunachal Pradesh': {
            'breakfast': ['Khura (Pancake)', 'Thukpa', 'Zan', 'Salt Tea with Biscuits', 'Steamed Corn'],
            'lunch': ['Rice', 'Pika Pila', 'Boiled Veg with Bamboo Shoots', 'Lukter', 'Pe Hak', 'Smoked Meat with Herbs'],
            'dinner': ['Apong', 'Bamboo Shoot Stir-fry', 'Steamed Fish', 'Veg Stew with Ginger', 'Boiled Pumpkin']
        },
        'Assam': {
            'breakfast': ['Jolpan', 'Pitha', 'Chira with Curd & Jaggery', 'Luchi with Tarkari', 'Kharoli'],
            'lunch': ['Rice', 'Masor Tenga (Sour Fish)', 'Khar', 'Aloo Pitika', 'Dhekia Xak Fry', 'Baahgajor Lagot Kukura'],
            'dinner': ['Roti', 'Veg Labra', 'Dal Fry', 'Pitika', 'Grilled Eggplant', 'Lentil Soup']
        },
        'Bihar': {
            'breakfast': ['Sattu Paratha', 'Chura Dahi', 'Pua', 'Jhalmuri', 'Ghughni Choila', 'Poori Sabzi'],
            'lunch': ['Litti Chokha', 'Dal-Chawal', 'Kadhi Bari', 'Aloo Bhujia', 'Ol ka Achaar', 'Badi Rice'],
            'dinner': ['Roti', 'Baingan Bharta', 'Sattu Drink', 'Mixed Veg', 'Dal Pitha', 'Parwal Ki Sabji']
        },
        'Chhattisgarh': {
            'breakfast': ['Fara (Rice Dumplings)', 'Muthiya', 'Chila', 'Bafauri', 'Angakar Roti'],
            'lunch': ['Rice', 'Amat', 'Chana Salad', 'Badi Curry', 'Dubki Kadhi', 'Leafy Greens (Chech Bhaji)'],
            'dinner': ['Roti', 'Badi Curry', 'Moong Dal', 'Steamed Rice with Tomato Kutkut']
        },
        'Goa': {
            'breakfast': ['Pao with Bhaji', 'Sannas', 'Polle', 'Kande Pohe', 'Baji Pao'],
            'lunch': ['Fish Curry Rice', 'Veg Xacuti', 'Ambot Tik', 'Goan Dal', 'Caldinho', 'Kokum Solkadhi'],
            'dinner': ['Veg Caldin', 'Poi with Lentils', 'Steamed Rice', 'Khatkhate (Veg Stew)', 'Fried Fish (limited)']
        },
        'Gujarat': {
            'breakfast': ['Dhokla', 'Thepla with Curd', 'Fafda Jalebi', 'Khandvi', 'Muthiya', 'Khakhra', 'Handvo'],
            'lunch': ['Gujarati Thali (Dal, Rice, Shaak, Rotli)', 'Kadhi Khichdi', 'Undhiyu', 'Sev Tameta', 'Ringan No Oro'],
            'dinner': ['Handvo', 'Vagarelo Rotlo', 'Dal Dhokli', 'Khichdi Kadhi', 'Bhakhri with Shaak']
        },
        'Haryana': {
            'breakfast': ['Bajra Khichdi', 'Paneer Paratha', 'Dalia', 'Milk & Nuts', 'Besan Ki Pinni', 'Methi Ladoo'],
            'lunch': ['Kachri ki Sabzi', 'Roti with White Butter', 'Lassi', 'Hara Dhania Chutney', 'Singri ki Sabzi'],
            'dinner': ['Mixed Dal', 'Bajra Roti', 'Alu Gobi', 'Bathua Raita', 'Kadai Paneer']
        },
        'Himachal Pradesh': {
            'breakfast': ['Siddu with Ghee', 'Babru', 'Bhaturu', 'Khoru', 'Sepu Vada'],
            'lunch': ['Madra (Chickpeas in Curd)', 'Dham', 'Rice', 'Chha Gosht', 'Kullu Trout (limited)', 'Tudkiya Bhath'],
            'dinner': ['Thukpa', 'Roti with Guchhi (Mushroom)', 'Aloo Palak', 'Lentils']
        },
        'Jharkhand': {
            'breakfast': ['Dhuska with Alu Chop', 'Arsa', 'Chilka Roti', 'Kurthi Dal', 'Pua'],
            'lunch': ['Rice', 'Marua Roti', 'Dal', 'Rugra (Mushroom) Curry', 'Bamboo Shoot Curry'],
            'dinner': ['Chhilka Roti', 'Veg Stew', 'Rice with Tomato Chutney', 'Lentils']
        },
        'Karnataka': {
            'breakfast': ['Bisi Bele Bath', 'Masala Dosa', 'Akki Rotti', 'Tatite Idli', 'Neer Dosa', 'Rava Idli', 'Chow Chow Bath'],
            'lunch': ['Jolada Roti', 'Ennebadanekayi', 'Ragi Mudde', 'Sambar Rice', 'Vangi Bath', 'Obbattu (limited)'],
            'dinner': ['Ragi Mudde', 'Sambar Rice', 'Chapati with Veg Saagu', 'Lemon Rice', 'Udupi Sambar']
        },
        'Kerala': {
            'breakfast': ['Puttu and Kadala Curry', 'Appam with Stew', 'Idiyappam', 'Pathiri', 'Upma', 'Pazham Pori (limited)'],
            'lunch': ['Kerala Sadya', 'Red Rice', 'Avial', 'Thorans', 'Olan', 'Kalan', 'Erissery'],
            'dinner': ['Kanji (Rice Gruel)', 'Payari (Green Gram)', 'Idiyappam', 'Vegetable Moilee', 'Fish Curry (Meen Veveichathu)']
        },
        'Madhya Pradesh': {
            'breakfast': ['Poha Jalebi', 'Bhutte Ka Kees', 'Dal Bafla', 'Khurma', 'Malpua (limited)'],
            'lunch': ['Dal Bafla', 'Biryani (Veg)', 'Palak Puri', 'Indori Namkeen with Rice', 'Kadhi'],
            'dinner': ['Roti', 'Malwa Kadhi', 'Bhutte Ka Kees', 'Sabudana Khichdi', 'Moong Dal']
        },
        'Maharashtra': {
            'breakfast': ['Kande Pohe', 'Thalipeeth', 'Misal Pav', 'Sabudana Khichdi', 'Upma', 'Batata Vada (limited)', 'Shira'],
            'lunch': ['Jowar Bhakri', 'Pithla', 'Varan Bhaat', 'Leafy Veg (Methi/Palak)', 'Puran Poli', 'Amti', 'Bharli Vangi'],
            'dinner': ['Moong Khichdi', 'Bhakri with Thecha', 'Sprouts Curry (Matki)', 'Masale Bhaat', 'Solkadhi']
        },
        'Manipur': {
            'breakfast': ['Tan (Flatbread)', 'Kanghou (Stir fry)', 'Kabab', 'Rice Porridge'],
            'lunch': ['Eromba', 'Singju (Salad)', 'Morok Metpa', 'Rice', 'Chamthong', 'Fish Curry'],
            'dinner': ['Rice', 'Chamthong', 'Kangshoi', 'Boiled Vegetables']
        },
        'Meghalaya': {
            'breakfast': ['Pukhlein', 'Doh-Neiiong', 'Rice Cakes', 'Sweet Potato'],
            'lunch': ['Jadoh', 'Veg Stew', 'Nakham Bitchi', 'Rice with Sesame Mix'],
            'dinner': ['Roti', 'Bamboo Shoot Stew', 'Smoked Fish Stew', 'Boiled Pumpkin']
        },
        'Mizoram': {
            'breakfast': ['Bai', 'Rice cakes', 'Steamed corn', 'Tea with Jaggery'],
            'lunch': ['Sawhchiar', 'Steamed Veg', 'Rice', 'Koat Pitha'],
            'dinner': ['Rice', 'Mizo Stew', 'Bamboo Shoot Curry', 'Boiled Beans']
        },
        'Nagaland': {
            'breakfast': ['Galho (Rice porridge)', 'Rice', 'Boiled Egg', 'Naga Ginger Tea'],
            'lunch': ['Axone Curry', 'Boiled Veg with Chillies', 'Smoked Meat with Bamboo Shoot', 'Rice'],
            'dinner': ['Smoked Stew', 'Rice', 'Hinkejvu', 'Boiled Cabbage']
        },
        'Odisha': {
            'breakfast': ['Chakuli Pitha', 'Kanika', 'Dahibara Aloo Dum', 'Enduri Pitha', 'Chuda Ghasa'],
            'lunch': ['Dalma', 'Pakhala Bhata', 'Besara', 'Saga Bhaja', 'Santula', 'Rice with Badi'],
            'dinner': ['Roti', 'Santula', 'Dalma', 'Rice with Tomato Khajuri Chutney']
        },
        'Punjab': {
            'breakfast': ['Aloo Paratha with Curd', 'Dalia', 'Paneer Paratha', 'Chole Bhature (small)', 'Stuffed Gobhi Paratha', 'Puri Chole'],
            'lunch': ['Makki di Roti', 'Sarson da Saag', 'Rajma Chawal', 'Amritsari Kulcha', 'Dal Makhani', 'Kadai Paneer'],
            'dinner': ['Dal Tadka', 'Missi Roti', 'Baingan Bharta', 'Mixed Veg', 'Tandoori Roti']
        },
        'Rajasthan': {
            'breakfast': ['Piaz Kachori', 'Bajra Rabri', 'Mirchi Bada', 'Kalmi Vada', 'Bikaneri Bhujia with Roti'],
            'lunch': ['Dal Bati Churma', 'Gatte ki Sabzi', 'Ker Sangri', 'Panchmel Dal', 'Lal Maas (limited)', 'Laapsi'],
            'dinner': ['Ker Sangri', 'Bajra Roti', 'Khichdi', 'Papad ki Sabzi', 'Mangodi Ki Sabzi']
        },
        'Sikkim': {
            'breakfast': ['Sel Roti', 'Momos (Veg)', 'Phagshapa', 'Thenthuk'],
            'lunch': ['Gundruk', 'Rice', 'Sishnu Soup', 'Dal Bhat', 'Dhindo'],
            'dinner': ['Thukpa', 'Phagshapa', 'Kinema Curry', 'Steamed Veg']
        },
        'Tamil Nadu': {
            'breakfast': ['Ven Pongal', 'Idli with Chutney', 'Rava Dosa', 'Uthappam', 'Medhu Vada', 'Kanchipuram Idli'],
            'lunch': ['Sambar Rice', 'Poriyal', 'Kootu', 'Lemon Rice', 'Rasam Rice', 'Curd Rice', 'Bisi Bele Bath (Tamil style)'],
            'dinner': ['Uthappam', 'Adai with Avial', 'Rasam with Rice', 'Idli with Podi', 'Chapati with Kurma']
        },
        'Telangana': {
            'breakfast': ['Sarva Pindi', 'Upma', 'Sakinalu', 'Bobbattu', 'Puri Curry'],
            'lunch': ['Jonna Rotte', 'Pappu Charu', 'Rice with Gongura', 'Hyderabadi Biryani (Veg)', 'Bachali Kura'],
            'dinner': ['Hyderabadi Khichdi', 'Roti', 'Tomato Kut', 'Bagara Khana']
        },
        'Tripura': {
            'breakfast': ['Mui Borok', 'Rice cakes', 'Pitha', 'Boiled Potato'],
            'lunch': ['Chakhwi', 'Fish Stew', 'Rice', 'Gudok', 'Mosdeng'],
            'dinner': ['Rice', 'Veg Berma', 'Bamboo Shoot Stew', 'Boiled Veg']
        },
        'Uttar Pradesh': {
            'breakfast': ['Bedmi Poori', 'Dalia', 'Aloo Kachori', 'Bread Pakora (limited)', 'Jalebi-Dahi (special)'],
            'lunch': ['Tehri (Veg Pulao)', 'Dal-Roti', 'Kadhi Chawal', 'Aloo Puri', 'Paneer Butter Masala', 'Dum Aloo'],
            'dinner': ['Baingan Bharta', 'Roti', 'Arhar Dal', 'Mixed Vegetable', 'Kofta Curry']
        },
        'Uttarakhand': {
            'breakfast': ['Aloo Ke Gutke', 'Jhangora (Millet) Kheer', 'Gulgula', 'Arsa'],
            'lunch': ['Kafuli', 'Phanu', 'Bhat ki Churkani', 'Dubuk', 'Chainsoo', 'Rice'],
            'dinner': ['Chainsoo', 'Mandua (Ragi) Roti', 'Mixed Lentils', 'Sisunak Saag']
        },
        'West Bengal': {
            'breakfast': ['Luchi with Alur Dom', 'Muri with Ghugni', 'Radhaballavi', 'Chira', 'Koraishutir Kochuri'],
            'lunch': ['Rice', 'Machher Jhol (Fish)', 'Shukto', 'Lau Ghonto', 'Moong Dal', 'Begun Bhaja', 'Chholar Dal'],
            'dinner': ['Roti', 'Aloo Posto', 'Chholar Dal', 'Mixed Vegetable', 'Fish Cutlet (limited)']
        }
    }

    default = {'breakfast': ['Oats', 'Eggs', 'Fruits', 'Poha'], 'lunch': ['Roti', 'Dal', 'Salad', 'Rice'], 'dinner': ['Soup', 'Salad', 'Grilled Veg', 'Khichdi']}
    
    staples = state_data.get(state, default)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    plan_output = f"### 7-Day {state} Diet Plan (High Variety Database)\n"
    for day in days:
        plan_output += f"**{day}**:\n"
        plan_output += f"- Breakfast: {random.choice(staples['breakfast'])}\n"
        plan_output += f"- Lunch: {random.choice(staples['lunch'])}\n"
        plan_output += f"- Dinner: {random.choice(staples['dinner'])}\n\n"

    diet = {
        "condition": "Diabetes " if "diabetes" in text else "General Health",
        "allowed_foods": list(set(staples['lunch'] + staples['breakfast'])),
        "restricted_foods": ["Sugar", "Deep fried foods", "Excess Salt"],
        "diet_plan": plan_output,
        "lifestyle_advice": "30 mins walk, adequate hydration."
    }
    return diet
