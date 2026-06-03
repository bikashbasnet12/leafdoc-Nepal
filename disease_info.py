KHETI = "https://store.kheti.farm/index.php?route=product/search&search="

def kheti(search_term, label):
    return {
        "label": label,
        "url": KHETI + search_term.replace(" ", "+"),
        "platform": "Kheti.farm Nepal"
    }

DISEASE_INFO = {

    # ===== APPLE =====
    "APPLE_HEALTHY": {
        "plant": {"en": "Apple", "ne": "स्याउ (Apple)"},
        "disease": {"en": "Healthy Leaf", "ne": "स्वस्थ पात (Healthy Leaf)"},
        "severity": {"en": "None", "ne": "छैन (None)"},
        "treatment": {
            "en": "No treatment required. Maintain regular pruning and monitoring.",
            "ne": "कुनै उपचार आवश्यक छैन। नियमित काँटछाँट र रेखदेख जारी राख्नुहोस्।"
        },
        "fertilizer": {
            "en": "Apply balanced organic compost (NPK Fertilizer) annually to maintain soil health.",
            "ne": "माटोको स्वास्थ्य राम्रो राख्न वार्षिक रूपमा सन्तुलित प्राङ्गारिक मल प्रयोग गर्नुहोस्।"
        },
        "buy_links": [
            kheti("NPK fertilizer", "NPK Fertilizer"),
            kheti("organic fertilizer", "Organic Fertilizer"),
        ]
    },

    "APPLE_ROT": {
        "plant": {"en": "Apple", "ne": "स्याउ (Apple)"},
        "disease": {"en": "Black Rot / Scab", "ne": "कालो सड्ने रोग / स्क्याब (Black Rot)"},
        "severity": {"en": "High", "ne": "उच्च (High)"},
        "treatment": {
            "en": "Apply copper oxychloride fungicide. Remove and destroy infected crop debris from orchard floors.",
            "ne": "कपर अक्सिक्लोराइड ढुसीनाशक प्रयोग गर्नुहोस्। बगैंचाको भुइँबाट संक्रमित बालीका अवशेषहरू हटाउनुहोस् र नष्ट गर्नुहोस्।"
        },
        "fertilizer": {
            "en": "Avoid excess nitrogen. Apply potassium fertilizer to improve plant immunity.",
            "ne": "अत्यधिक नाइट्रोजनको प्रयोग नगर्नुहोस्। बिरुवाको रोग प्रतिरोधात्मक क्षमता बढाउन पोटासियम मल प्रयोग गर्नुहोस्।"
        },
        "buy_links": [
            kheti("copper fungicide", "Copper Fungicide"),
            kheti("potassium fertilizer", "Potassium Fertilizer"),
        ]
    },

    # ===== BANANA =====
    "BANANA_HEALTHY": {
        "plant": {"en": "Banana", "ne": "केरा (Banana)"},
        "disease": {"en": "Healthy Leaf", "ne": "स्वस्थ पात (Healthy Leaf)"},
        "severity": {"en": "None", "ne": "छैन (None)"},
        "treatment": {
            "en": "No treatment required. Ensure adequate spacing between plants.",
            "ne": "कुनै उपचार आवश्यक छैन। बिरुवाहरू बीच पर्याप्त दूरी सुनिश्चित गर्नुहोस्।"
        },
        "fertilizer": {
            "en": "Maintain regular watering and apply nitrogen-rich (NPK) manure during vegetative growth.",
            "ne": "नियमित सिँचाइ गर्नुहोस् र वनस्पति वृद्धिको समयमा नाइट्रोजनयुक्त मल प्रयोग गर्नुहोस्।"
        },
        "buy_links": [
            kheti("NPK fertilizer", "NPK Fertilizer"),
            kheti("organic fertilizer", "Organic Fertilizer"),
        ]
    },

    "BANANA_PANAMA": {
        "plant": {"en": "Banana", "ne": "केरा (Banana)"},
        "disease": {"en": "Panama Wilt (Fusarium oxysporum)", "ne": "पानामा ओइलाउने रोग (Panama Wilt)"},
        "severity": {"en": "Very High", "ne": "अति उच्च (Very High)"},
        "treatment": {
            "en": "No chemical cure. Remove and destroy infected plants. Use resistant varieties.",
            "ne": "कुनै रासायनिक उपचार छैन। संक्रमित बिरुवाहरू हटाउनुहोस् र नष्ट गर्नुहोस्। प्रतिरोधी जातहरू प्रयोग गर्नुहोस्।"
        },
        "fertilizer": {
            "en": "Maintain regular watering and apply nitrogen-rich manure during vegetative growth.",
            "ne": "नियमित सिँचाइ गर्नुहोस् र वनस्पति वृद्धिको समयमा नाइट्रोजनयुक्त मल प्रयोग गर्नुहोस्।"
        },
        "buy_links": [
            kheti("carbendazim fungicide", "Carbendazim Fungicide"),
            kheti("agricultural lime", "Agricultural Lime"),
        ]
    },

    "BANANA_SIGATOKA": {
        "plant": {"en": "Banana", "ne": "केरा (Banana)"},
        "disease": {"en": "Sigatoka Leaf Spot", "ne": "सिगाटोका पातको दाग (Sigatoka)"},
        "severity": {"en": "Medium", "ne": "मध्यम (Medium)"},
        "treatment": {
            "en": "Apply Mancozeb or Chlorothalonil fungicide. Remove and burn heavily infected leaves.",
            "ne": "म्यान्कोजेब वा क्लोरोथालोनिल ढुसीनाशक प्रयोग गर्नुहोस्। धेरै संक्रमित पातहरू हटाउनुहोस् र जलाउनुहोस्।"
        },
        "fertilizer": {
            "en": "Apply potassium-rich fertilizer. Avoid overhead sprinkler irrigation to minimize moisture build-up.",
            "ne": "पोटासियमयुक्त मल प्रयोग गर्नुहोस्। चिसोपन कम गर्न टाउको माथिबाट गरिने सिँचाइ नगर्नुहोस्।"
        },
        "buy_links": [
            kheti("mancozeb fungicide", "Mancozeb Fungicide"),
            kheti("potassium fertilizer", "Potassium Fertilizer"),
        ]
    },

    # ===== CORN =====
    "CORN_HEALTHY": {
        "plant": {"en": "Corn (Maize)", "ne": "मकै (Corn)"},
        "disease": {"en": "Healthy Leaf", "ne": "स्वस्थ पात (Healthy Leaf)"},
        "severity": {"en": "None", "ne": "छैन (None)"},
        "treatment": {
            "en": "No treatment required. Ensure clear weeding around stalks.",
            "ne": "कुनै उपचार आवश्यक छैन। बोटबिरुवाको वरिपरि सफा गोडमेल सुनिश्चित गर्नुहोस्।"
        },
        "fertilizer": {
            "en": "Apply Urea at knee-high stage and during silking time.",
            "ne": "घुँडासम्म उचाइ भएको अवस्थामा र जुँगा आउने समयमा युरिया मल प्रयोग गर्नुहोस्।"
        },
        "buy_links": [
            kheti("urea fertilizer", "Urea Fertilizer"),
        ]
    },

    "CORN_LEAF_BLIGHT": {
        "plant": {"en": "Corn (Maize)", "ne": "मकै (Corn)"},
        "disease": {"en": "Northern Leaf Blight", "ne": "उत्तरी पातको ब्लाइट (Northern Blight)"},
        "severity": {"en": "Medium", "ne": "मध्यम (Medium)"},
        "treatment": {
            "en": "Spray Azoxystrobin or Pyraclostrobin if lesions expand rapidly. Practice crop rotation.",
            "ne": "यदि दागहरू द्रुत रूपमा फैलिएमा एजोक्सिस्ट्रोबिन वा पाइराक्लोस्ट्रोबिन छर्नुहोस्। बाली चक्र अपनाउनुहोस्।"
        },
        "fertilizer": {
            "en": "Balance NPK application. Ensure adequate Zinc micronutrient supplementation.",
            "ne": "एनपीके (NPK) को सन्तुलित प्रयोग गर्नुहोस्। पर्याप्त जस्ता (Zinc) सुक्ष्मपोषक तत्वको आपूर्ति सुनिश्चित गर्नुहोस्।"
        },
        "buy_links": [
            kheti("azoxystrobin fungicide", "Azoxystrobin Fungicide"),
            kheti("zinc micronutrient", "Zinc Micronutrient"),
        ]
    },

    "CORN_LEAF_GRAY_SPOT": {
        "plant": {"en": "Corn (Maize)", "ne": "मकै (Corn)"},
        "disease": {"en": "Gray Leaf Spot", "ne": "खैरो पातको दाग (Gray Leaf Spot)"},
        "severity": {"en": "Medium", "ne": "मध्यम (Medium)"},
        "treatment": {
            "en": "Apply Strobilurin-based fungicide. Improve air circulation.",
            "ne": "स्ट्रोबिलुरिनमा आधारित ढुसीनाशक विषादी प्रयोग गर्नुहोस्। हावाको आवतजावत सुधार्नुहोस्।"
        },
        "fertilizer": {
            "en": "Apply nitrogen fertilizer in split doses.",
            "ne": "नाइट्रोजनयुक्त मल मात्रा मिलाएर विभिन्न चरणमा प्रयोग गर्नुहोस्।"
        },
        "buy_links": [
            kheti("strobilurin fungicide", "Strobilurin Fungicide"),
            kheti("urea fertilizer", "Urea Fertilizer"),
        ]
    },

    "CORN_LEAF_RUST": {
        "plant": {"en": "Corn (Maize)", "ne": "मकै (Corn)"},
        "disease": {"en": "Common Rust", "ne": "सामान्य रस्ट/सिन्दुरे रोग (Common Rust)"},
        "severity": {"en": "Medium", "ne": "मध्यम (Medium)"},
        "treatment": {
            "en": "Apply Mancozeb fungicide. Remove infected leaves.",
            "ne": "म्यान्कोजेब ढुसीनाशक विषादी प्रयोग गर्नुहोस्। संक्रमित पातहरू हटाउनुहोस्।"
        },
        "fertilizer": {
            "en": "Maintain balanced NPK. Avoid excess nitrogen.",
            "ne": "सन्तुलित एनपीके (NPK) को मात्रा कायम राख्नुहोस्। अत्यधिक नाइट्रोजनको प्रयोग नगर्नुहोस्।"
        },
        "buy_links": [
            kheti("mancozeb fungicide", "Mancozeb Fungicide"),
            kheti("NPK fertilizer", "Balanced NPK Fertilizer"),
        ]
    },

    # ===== POTATO =====
    "POTATO_HEALTHY": {
        "plant": {"en": "Potato", "ne": "आलु (Potato)"},
        "disease": {"en": "Healthy", "ne": "स्वस्थ (Healthy)"},
        "severity": {"en": "None", "ne": "छैन (None)"},
        "treatment": {
            "en": "No treatment needed.",
            "ne": "कुनै उपचार आवश्यक छैन।"
        },
        "fertilizer": {
            "en": "Apply NPK 10-20-20 at planting stage.",
            "ne": "रोप्ने चरणमा एनपीके १०-२०-२० (NPK 10-20-20) मल प्रयोग गर्नुहोस्।"
        },
        "buy_links": [
            kheti("NPK fertilizer", "NPK Fertilizer"),
            kheti("DAP fertilizer", "DAP Fertilizer"),
        ]
    },

    "POTATO_EARLY_BLIGHT": {
        "plant": {"en": "Potato", "ne": "आलु (Potato)"},
        "disease": {"en": "Early Blight (Alternaria solani)", "ne": "प्रारम्भिक ब्लाइट/डढुवा रोग (Early Blight)"},
        "severity": {"en": "Medium", "ne": "मध्यम (Medium)"},
        "treatment": {
            "en": "Apply Mancozeb or Chlorothalonil fungicide every 7–10 days.",
            "ne": "प्रत्येक ७-१० दिनमा म्यान्कोजेब वा क्लोरोथालोनिल ढुसीनाशक विषादी प्रयोग गर्नुहोस्।"
        },
        "fertilizer": {
            "en": "Boost potassium and calcium. Avoid excess nitrogen.",
            "ne": "पोटासियम र क्याल्सियमको मात्रा बढाउनुहोस्। अत्यधिक नाइट्रोजनको प्रयोग नगर्नुहोस्।"
        },
        "buy_links": [
            kheti("mancozeb fungicide", "Mancozeb Fungicide"),
            kheti("potassium fertilizer", "Potassium Fertilizer"),
        ]
    },

    "POTATO_LATE_BLIGHT": {
        "plant": {"en": "Potato", "ne": "आलु (Potato)"},
        "disease": {"en": "Late Blight (Phytophthora infestans)", "ne": "पछौटे डढुवा रोग (Late Blight)"},
        "severity": {"en": "Very High", "ne": "अति उच्च (Very High)"},
        "treatment": {
            "en": "Apply Metalaxyl + Mancozeb fungicide immediately. Destroy infected plants.",
            "ne": "तुरुन्तै मेटालाक्सिल + म्यान्कोजेब ढुसीनाशक विषादी प्रयोग गर्नुहोस्। संक्रमित बिरुवाहरू नष्ट गर्नुहोस्।"
        },
        "fertilizer": {
            "en": "Use phosphorus-rich fertilizer. Avoid waterlogging.",
            "ne": "फस्फोरसयुक्त मलको प्रयोग गर्नुहोस्। खेतमा पानी जम्न नदिनुहोस्।"
        },
        "buy_links": [
            kheti("metalaxyl mancozeb", "Metalaxyl + Mancozeb Fungicide"),
            kheti("phosphorus fertilizer", "Phosphorus Fertilizer"),
        ]
    },

    # ===== RICE =====
    "RICE_HEALTHY": {
        "plant": {"en": "Rice (Paddy)", "ne": "धान (Rice)"},
        "disease": {"en": "Healthy", "ne": "स्वस्थ (Healthy)"},
        "severity": {"en": "None", "ne": "छैन (None)"},
        "treatment": {
            "en": "No treatment needed.",
            "ne": "कुनै उपचार आवश्यक छैन।"
        },
        "fertilizer": {
            "en": "Apply urea at tillering stage. Use DAP at transplanting.",
            "ne": "गाँज आउने चरणमा युरिया प्रयोग गर्नुहोस्। रोप्ने समयमा डीएपी (DAP) मल प्रयोग गर्नुहोस्।"
        },
        "buy_links": [
            kheti("urea fertilizer", "Urea Fertilizer"),
            kheti("DAP fertilizer", "DAP Fertilizer"),
        ]
    },

    "RICE_LEAF_BLAST": {
        "plant": {"en": "Rice (Paddy)", "ne": "धान (Rice)"},
        "disease": {"en": "Rice Blast (Pyricularia oryzae)", "ne": "मरिचे/मरुवा रोग (Rice Blast)"},
        "severity": {"en": "High", "ne": "उच्च (High)"},
        "treatment": {
            "en": "Apply Tricyclazole or Isoprothiolane fungicide. Avoid excess nitrogen.",
            "ne": "ट्राइसाइक्लाजोल वा आइसोप्रोथियोलेन ढुसीनाशक विषादी प्रयोग गर्नुहोस्। अत्यधिक नाइट्रोजनको प्रयोग नगर्नुहोस्।"
        },
        "fertilizer": {
            "en": "Reduce nitrogen. Apply silica fertilizer to strengthen leaves.",
            "ne": "नाइट्रोजनको मात्रा घटाउनुहोस्। पातहरूलाई बलियो बनाउन सिलिका (Silica) मल प्रयोग गर्नुहोस्।"
        },
        "buy_links": [
            kheti("tricyclazole fungicide", "Tricyclazole Fungicide"),
            kheti("silica fertilizer", "Silica Fertilizer"),
        ]
    },

    "RICE_LEAF_BLIGHT": {
        "plant": {"en": "Rice (Paddy)", "ne": "धान (Rice)"},
        "disease": {"en": "Bacterial Leaf Blight", "ne": "जीवाणुजन्य पात डढुवा रोग (Bacterial Blight)"},
        "severity": {"en": "High", "ne": "उच्च (High)"},
        "treatment": {
            "en": "Apply copper oxychloride. Remove infected crop debris after harvest.",
            "ne": "कपर अक्सिक्लोराइड प्रयोग गर्नुहोस्। कटानीपछि संक्रमित बालीका अवशेषहरू हटाउनुहोस्।"
        },
        "fertilizer": {
            "en": "Avoid excess nitrogen. Apply potassium fertilizer.",
            "ne": "अत्यधिक नाइट्रोजनको प्रयोग नगर्नुहोस्। पोटासियम मल प्रयोग गर्नुहोस्।"
        },
        "buy_links": [
            kheti("copper oxychloride", "Copper Oxychloride Fungicide"),
            kheti("potassium fertilizer", "Potassium Fertilizer"),
        ]
    },

    "RICE_LEAF_BROWN_SPOT": {
        "plant": {"en": "Rice (Paddy)", "ne": "धान (Rice)"},
        "disease": {"en": "Brown Spot (Cochliobolus miyabeanus)", "ne": "खैरो दाग रोग (Brown Spot)"},
        "severity": {"en": "Medium", "ne": "मध्यम (Medium)"},
        "treatment": {
            "en": "Apply Mancozeb or Iprodione fungicide. Use certified disease-free seeds.",
            "ne": "म्यान्कोजेब वा इप्रोडिओन ढुसीनाशक विषादी प्रयोग गर्नुहोस्। प्रमाणित रोगमुक्त बिउ विजन प्रयोग गर्नुहोस्।"
        },
        "fertilizer": {
            "en": "Apply potassium and phosphorus. Improve soil fertility with compost.",
            "ne": "पोटासियम र फस्फोरस मल प्रयोग गर्नुहोस्। कम्पोस्ट मलद्वारा माटोको उर्वराशक्ति सुधार्नुहोस्।"
        },
        "buy_links": [
            kheti("mancozeb fungicide", "Mancozeb Fungicide"),
            kheti("potassium phosphorus fertilizer", "Potassium + Phosphorus Fertilizer"),
        ]
    },
}

SEVERITY_COLOR = {
    "None":      "#22c55e",
    "Low":       "#84cc16",
    "Medium":    "#f59e0b",
    "High":      "#ef4444",
    "Very High": "#7f1d1d",
}

def get_info(class_name: str) -> dict:
    key = class_name.upper()
    if key in DISEASE_INFO:
        info = DISEASE_INFO[key].copy()
        english_severity = info["severity"].get("en", "None")
        info["color"] = SEVERITY_COLOR.get(english_severity, "#6b7280")
        return info

    return {
        "plant": {"en": "Unknown", "ne": "अज्ञात (Unknown)"},
        "disease": {"en": "Not recognized", "ne": "पहिचान हुन नसकेको (Not recognized)"},
        "severity": {"en": "Unknown", "ne": "अज्ञात (Unknown)"},
        "treatment": {
            "en": "Could not identify the leaf. Please upload a clearer photo.",
            "ne": "पात पहिचान गर्न सकिएन। कृपया स्पष्ट फोटो अपलोड गर्नुहोस्।"
        },
        "fertilizer": {
            "en": "No recommendation available.",
            "ne": "कुनै सिफारिस उपलब्ध छैन।"
        },
        "color": "#6b7280",
        "buy_links": []
    }