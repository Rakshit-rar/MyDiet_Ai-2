def generate_diet(text):
    text = text.lower()

    diet = {
        "condition": "",
        "allowed_foods": ["vegetables", "whole grains", "fruits"],
        "restricted_foods": [],
        "diet_plan": "",
        "lifestyle_advice": ""
    }

    if "diabetes" in text:
        diet["condition"] += "Diabetes "
        diet["restricted_foods"].append("sugar")
        diet["diet_plan"] += "Follow diabetic diet. "
        diet["lifestyle_advice"] += "Walk daily. "

    if "cholesterol" in text:
        diet["condition"] += "Cholesterol "
        diet["restricted_foods"].append("oily food")

    if "blood pressure" in text or "hypertension" in text:
        diet["condition"] += "Hypertension "
        diet["restricted_foods"].append("salt")

    if diet["diet_plan"] == "":
        diet["diet_plan"] = "Maintain a balanced and healthy diet."

    return diet


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
