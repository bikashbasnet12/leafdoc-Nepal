# Buy links:
# - store.kheti.farm = verified Nepal agro store (Kathmandu & Pokhara delivery)
# - Daraz link only included if product confirmed available

KHETI = "https://store.kheti.farm/index.php?route=product/search&search="

# Only one Daraz link confirmed working for fungicides
DARAZ_FUNGICIDE = "https://www.daraz.com.np/catalog/?q=fungicide"

def kheti(search_term, label):
    return {
        "label": label,
        "url": KHETI + search_term.replace(" ", "+"),
        "platform": "Kheti.farm Nepal"
    }

DISEASE_INFO = {

    # ===== APPLE =====
    "APPLE_HEALTHY": {
        "plant": "Apple",
        "disease": "Healthy",
        "severity": "None",
        "treatment": "No treatment needed. Keep monitoring regularly.",
        "fertilizer": "Apply balanced NPK fertilizer (10-10-10) once a month.",
        "buy_links": [
            kheti("NPK fertilizer", "NPK Fertilizer"),
            kheti("organic fertilizer", "Organic Fertilizer"),
        ]
    },

    "APPLE_ROT": {
        "plant": "Apple",
        "disease": "Apple Rot (Black Rot)",
        "severity": "High",
        "treatment": "Remove infected fruits and leaves. Apply copper-based fungicide.",
        "fertilizer": "Reduce nitrogen. Apply potassium-rich fertilizer.",
        "buy_links": [
            kheti("copper fungicide", "Copper Fungicide"),
            kheti("potassium fertilizer", "Potassium Fertilizer"),
        ]
    },

    # ===== BANANA =====
    "BANANA_HEALTHY": {
        "plant": "Banana",
        "disease": "Healthy",
        "severity": "None",
        "treatment": "No treatment needed.",
        "fertilizer": "Apply NPK 8-10-10 every 2 months.",
        "buy_links": [
            kheti("NPK fertilizer", "NPK Fertilizer"),
            kheti("organic fertilizer", "Organic Fertilizer"),
        ]
    },

    "BANANA_PANAMA": {
        "plant": "Banana",
        "disease": "Panama Disease (Fusarium Wilt)",
        "severity": "Very High",
        "treatment": "No chemical cure. Remove and destroy affected plants. Use disease-resistant varieties.",
        "fertilizer": "Use organic compost to improve soil health.",
        "buy_links": [
            kheti("organic compost", "Organic Compost"),
            kheti("bio fertilizer", "Bio Fertilizer"),
        ]
    },

    "BANANA_SIGATOKA": {
        "plant": "Banana",
        "disease": "Sigatoka Leaf Spot",
        "severity": "Medium",
        "treatment": "Apply Mancozeb or Chlorothalonil fungicide. Remove infected leaves.",
        "fertilizer": "Apply potassium-rich fertilizer. Avoid overhead irrigation.",
        "buy_links": [
            kheti("mancozeb fungicide", "Mancozeb Fungicide"),
            kheti("potassium fertilizer", "Potassium Fertilizer"),
        ]
    },

    # ===== CORN =====
    "CORN_HEALTHY": {
        "plant": "Corn (Maize)",
        "disease": "Healthy",
        "severity": "None",
        "treatment": "No treatment needed.",
        "fertilizer": "Apply urea fertilizer at 3–4 week intervals.",
        "buy_links": [
            kheti("urea fertilizer", "Urea Fertilizer"),
            kheti("nitrogen fertilizer", "Nitrogen Fertilizer"),
        ]
    },

    "CORN_LEAF_BLIGHT": {
        "plant": "Corn (Maize)",
        "disease": "Northern Corn Leaf Blight",
        "severity": "High",
        "treatment": "Apply Propiconazole or Azoxystrobin fungicide. Remove infected leaves.",
        "fertilizer": "Apply balanced NPK with extra potassium.",
        "buy_links": [
            kheti("propiconazole fungicide", "Propiconazole Fungicide"),
            kheti("NPK fertilizer", "NPK + Potassium Fertilizer"),
        ]
    },

    "CORN_LEAF_GRAY_SPOT": {
        "plant": "Corn (Maize)",
        "disease": "Gray Leaf Spot",
        "severity": "Medium",
        "treatment": "Apply Strobilurin-based fungicide. Improve air circulation.",
        "fertilizer": "Apply nitrogen fertilizer in split doses.",
        "buy_links": [
            kheti("strobilurin fungicide", "Strobilurin Fungicide"),
            kheti("urea fertilizer", "Urea Fertilizer"),
        ]
    },

    "CORN_LEAF_RUST": {
        "plant": "Corn (Maize)",
        "disease": "Common Rust",
        "severity": "Medium",
        "treatment": "Apply Mancozeb fungicide. Remove infected leaves.",
        "fertilizer": "Maintain balanced NPK. Avoid excess nitrogen.",
        "buy_links": [
            kheti("mancozeb fungicide", "Mancozeb Fungicide"),
            kheti("NPK fertilizer", "Balanced NPK Fertilizer"),
        ]
    },

    # ===== POTATO =====
    "POTATO_HEALTHY": {
        "plant": "Potato",
        "disease": "Healthy",
        "severity": "None",
        "treatment": "No treatment needed.",
        "fertilizer": "Apply NPK 10-20-20 at planting stage.",
        "buy_links": [
            kheti("NPK fertilizer", "NPK Fertilizer"),
            kheti("DAP fertilizer", "DAP Fertilizer"),
        ]
    },

    "POTATO_EARLY_BLIGHT": {
        "plant": "Potato",
        "disease": "Early Blight (Alternaria solani)",
        "severity": "Medium",
        "treatment": "Apply Mancozeb or Chlorothalonil fungicide every 7–10 days.",
        "fertilizer": "Boost potassium and calcium. Avoid excess nitrogen.",
        "buy_links": [
            kheti("mancozeb fungicide", "Mancozeb Fungicide"),
            kheti("potassium fertilizer", "Potassium Fertilizer"),
        ]
    },

    "POTATO_LATE_BLIGHT": {
        "plant": "Potato",
        "disease": "Late Blight (Phytophthora infestans)",
        "severity": "Very High",
        "treatment": "Apply Metalaxyl + Mancozeb fungicide immediately. Destroy infected plants.",
        "fertilizer": "Use phosphorus-rich fertilizer. Avoid waterlogging.",
        "buy_links": [
            kheti("metalaxyl mancozeb", "Metalaxyl + Mancozeb Fungicide"),
            kheti("phosphorus fertilizer", "Phosphorus Fertilizer"),
        ]
    },

    # ===== RICE =====
    "RICE_HEALTHY": {
        "plant": "Rice (Paddy)",
        "disease": "Healthy",
        "severity": "None",
        "treatment": "No treatment needed.",
        "fertilizer": "Apply urea at tillering stage. Use DAP at transplanting.",
        "buy_links": [
            kheti("urea fertilizer", "Urea Fertilizer"),
            kheti("DAP fertilizer", "DAP Fertilizer"),
        ]
    },

    "RICE_LEAF_BLAST": {
        "plant": "Rice (Paddy)",
        "disease": "Rice Blast (Pyricularia oryzae)",
        "severity": "High",
        "treatment": "Apply Tricyclazole or Isoprothiolane fungicide. Avoid excess nitrogen.",
        "fertilizer": "Reduce nitrogen. Apply silica fertilizer to strengthen leaves.",
        "buy_links": [
            kheti("tricyclazole fungicide", "Tricyclazole Fungicide"),
            kheti("silica fertilizer", "Silica Fertilizer"),
        ]
    },

    "RICE_LEAF_BLIGHT": {
        "plant": "Rice (Paddy)",
        "disease": "Bacterial Leaf Blight",
        "severity": "High",
        "treatment": "Apply copper oxychloride. Remove infected crop debris after harvest.",
        "fertilizer": "Avoid excess nitrogen. Apply potassium fertilizer.",
        "buy_links": [
            kheti("copper oxychloride", "Copper Oxychloride Fungicide"),
            kheti("potassium fertilizer", "Potassium Fertilizer"),
        ]
    },

    "RICE_LEAF_BROWN_SPOT": {
        "plant": "Rice (Paddy)",
        "disease": "Brown Spot (Cochliobolus miyabeanus)",
        "severity": "Medium",
        "treatment": "Apply Mancozeb or Iprodione fungicide. Use certified disease-free seeds.",
        "fertilizer": "Apply potassium and phosphorus. Improve soil fertility with compost.",
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
        info["color"] = SEVERITY_COLOR.get(info["severity"], "#6b7280")
        return info
    return {
        "plant": "Unknown",
        "disease": "Not recognized",
        "severity": "Unknown",
        "treatment": "Could not identify the leaf. Please upload a clearer image.",
        "fertilizer": "N/A",
        "color": "#6b7280",
        "buy_links": []
    }