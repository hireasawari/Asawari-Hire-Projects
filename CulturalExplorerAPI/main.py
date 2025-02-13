from fastapi import FastAPI, HTTPException

app = FastAPI()

# Sample data
cultural_sites = [
    {"id": 1, "name": "Taj Mahal", "location": "India", "description": {"en": "A symbol of love.", "fr": "Un symbole d'amour."}},
    {"id": 2, "name": "Eiffel Tower", "location": "France", "description": {"en": "A global icon of France.", "fr": "Un icône mondial de la France."}},
    {"id": 3, "name": "Great Wall of China", "location": "China", "description": {"en": "An ancient defensive architecture.", "zh": "一座古老的防御建筑。"}}
]

festivals = [
    {"id": 1, "name": "Diwali", "country": "India", "month": "October"},
    {"id": 2, "name": "Oktoberfest", "country": "Germany", "month": "September"},
    {"id": 3, "name": "Chinese New Year", "country": "China", "month": "February"}
]

@app.get("/")
def home():
    return {"message": "Welcome to the Cultural Explorer API."}

@app.get("/sites")
def get_sites():
    return {"Cultural Sites": cultural_sites}

@app.get("/festivals")
def get_festivals():
    return {"Cultural Festivals": festivals}

@app.get("/sites/{site_country}")
def country_sites(site_country: str):
    sites = [site for site in cultural_sites if site["location"].lower() == site_country.lower()]
    if not sites:
        raise HTTPException(status_code=404, detail="No cultural sites found in this country.")
    return {"Cultural Sites": sites}

@app.get("/festivals/{country_name}")
def country_festivals(country_name: str):
    fest_list = [festival for festival in festivals if festival["country"].lower() == country_name.lower()]
    if not fest_list:
        raise HTTPException(status_code=404, detail="No festivals found in this country.")
    return {"Festivals": fest_list}

@app.post("/festivals")
def add_festival(name: str, country: str, month: str):
    new_festival = {"id": len(festivals) + 1, "name": name, "country": country, "month": month}
    festivals.append(new_festival)
    return {"message": "Festival added successfully!", "festival": new_festival}

@app.get("/sites/{site_country}/{lang}")
def site_description(site_country: str, lang: str):
    sites = [site for site in cultural_sites if site["location"].lower() == site_country.lower()]
    if not sites:
        raise HTTPException(status_code=404, detail="No cultural sites found in this country.")
    descriptions = [
        {"name": site["name"], "description": site["description"].get(lang, "Language not available")}
        for site in sites
    ]
    return {"Cultural Sites Descriptions": descriptions}

@app.delete("/sites/{site_id}")
def delete_site(site_id: int):
    global cultural_sites
    cultural_sites = [site for site in cultural_sites if site["id"] != site_id]
    return {"message": "Site deleted successfully!"}

@app.delete("/festivals/{festival_id}")
def delete_festival(festival_id: int):
    global festivals
    festivals = [festival for festival in festivals if festival["id"] != festival_id]
    return {"message": "Festival deleted successfully!"}
