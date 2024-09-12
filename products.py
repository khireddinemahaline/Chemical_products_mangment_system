#!/usr/bin/python3
import requests

products  = [
    {
        "name": "Sodium Chloride",
        "ref": "SC-001",
        "quentity": 100,
        "description": "Common table salt used in various chemical applications."
    },
    {
        "name": "Sulfuric Acid",
        "ref": "SA-002",
        "quentity": 50,
        "description": "Strong acid used in batteries and industrial processes."
    },
    {
        "name": "Hydrochloric Acid",
        "ref": "HA-003",
        "quentity": 75,
        "description": "Powerful acid used in cleaning and chemical synthesis."
    },
    {
        "name": "Sodium Hydroxide",
        "ref": "SH-004",
        "quentity": 60,
        "description": "Caustic soda used in soap making and water treatment."
    },
    {
        "name": "Acetic Acid",
        "ref": "AA-005",
        "quentity": 80,
        "description": "Vinegar acid used in food preservation and chemical synthesis."
    },
    {
        "name": "Ethanol",
        "ref": "ET-006",
        "quentity": 90,
        "description": "Alcohol used as a solvent and in the production of beverages."
    },
    {
        "name": "Ammonium Nitrate",
        "ref": "AN-007",
        "quentity": 40,
        "description": "Fertilizer and explosive compound."
    },
    {
        "name": "Potassium Permanganate",
        "ref": "PP-008",
        "quentity": 30,
        "description": "Oxidizing agent used in water treatment and disinfection."
    },
    {
        "name": "Calcium Carbonate",
        "ref": "CC-009",
        "quentity": 100,
        "description": "Compound used in cement and as a dietary supplement."
    },
    {
        "name": "Magnesium Sulfate",
        "ref": "MS-010",
        "quentity": 55,
        "description": "Epsom salts used in agriculture and medicine."
    },
    {
        "name": "Boric Acid",
        "ref": "BA-011",
        "quentity": 70,
        "description": "Used as an antiseptic and in pest control."
    },
    {
        "name": "Copper Sulfate",
        "ref": "CS-012",
        "quentity": 85,
        "description": "Used in agriculture, chemistry, and as a fungicide."
    },
    {
        "name": "Zinc Oxide",
        "ref": "ZO-013",
        "quentity": 40,
        "description": "Used in ointments, cosmetics, and as a pigment."
    },
    {
        "name": "Sodium Bicarbonate",
        "ref": "SB-014",
        "quentity": 95,
        "description": "Baking soda used in cooking and as a cleaning agent."
    },
    {
        "name": "Hydrogen Peroxide",
        "ref": "HP-015",
        "quentity": 60,
        "description": "Bleaching agent and disinfectant."
    },
    {
        "name": "Nitric Acid",
        "ref": "NA-016",
        "quentity": 50,
        "description": "Strong acid used in fertilizers and explosives."
    },
    {
        "name": "Formic Acid",
        "ref": "FA-017",
        "quentity": 75,
        "description": "Used in leather production and as a preservative."
    },
    {
        "name": "Sodium Thiosulfate",
        "ref": "ST-018",
        "quentity": 65,
        "description": "Used in photography and as a dechlorinating agent."
    },
    {
        "name": "Potassium Iodide",
        "ref": "PI-019",
        "quentity": 80,
        "description": "Used in medical applications and as a nutritional supplement."
    },
    {
        "name": "Calcium Chloride",
        "ref": "CCL-020",
        "quentity": 90,
        "description": "Used for de-icing roads and as a drying agent."
    }
]

url = 'http://127.0.0.1:5002/api/v1/products'
for product in products:
    request = requests.post(url, json=product)

