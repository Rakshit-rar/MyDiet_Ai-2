
def calculate_macros(numeric_data, condition):
    age = numeric_data.get('age', 30)
    bmi = numeric_data.get('bmi', 22)
    
    # Baseline calories (Sedentary estimate)
    calories = 2000
    if bmi > 25:
        calories = 1800  # Slight deficit for higher BMI
    if 'Diabetes' in condition:
        calories -= 100

    # Macro splits (Protein: 4cal/g, Carbs: 4cal/g, Fat: 9cal/g)
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

def generate_diet(text, region='General'):
    text = text.lower()
    
    # Regional Staples Database
    regional_staples = {
        'North India': {
            'staples': ['Whole wheat roti', 'Paneer', 'Dal Makhani (low oil)', 'Curd'],
            'breakfast': ['Stuffed Paratha (dry)', 'Poha', 'Dalia']
        },
        'South India': {
            'staples': ['Red Rice', 'Sambar', 'Rasam', 'Buttermilk'],
            'breakfast': ['Idli', 'Dosa', 'Upma']
        },
        'East India': {
            'staples': ['Boiled Rice', 'Machher Jhol (Light fish stew)', 'Posto', 'Leafy Greens'],
            'breakfast': ['Luchi-Alur Dom (in moderation)', 'Muri']
        },
        'West India': {
            'staples': ['Jowar/Bajra Bhakri', 'Thepla', 'Pithla', 'Sprouted Moong'],
            'breakfast': ['Thalipeeth', 'Dhokla', 'Khakhra']
        },
        'General': {
            'staples': ['Vegetables', 'Whole Grains', 'Pulses'],
            'breakfast': ['Oats', 'Eggs', 'Fruits']
        }
    }

    diet = {
        "condition": "",
        "allowed_foods": regional_staples.get(region, regional_staples['General'])['staples'],
        "restricted_foods": [],
        "diet_plan": f"Recommended regional breakfast: {regional_staples.get(region, regional_staples['General'])['breakfast'][0]}. ",
        "lifestyle_advice": ""
    }

    if "diabetes" in text:
        diet["condition"] += "Diabetes "
        diet["restricted_foods"].extend(["sugar", "refined flour", "excess potatoes"])
        diet["diet_plan"] += "Focus on fiber-rich grains like Bajra or Red Rice. "

    if "cholesterol" in text:
        diet["condition"] += "Cholesterol "
        diet["restricted_foods"].append("saturated fats")

    if diet["diet_plan"] == "":
        diet["diet_plan"] = "Follow a balanced regional meal plan."

    return diet
