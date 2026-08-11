
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
