# CS2 Skin Market — Information Management Project

A simple web application that lets you search a database of Counter-Strike 2 skins,
view their image, market value (USD), and rarity tier.

## Tech Stack
| Layer       | Technology              |
|-------------|-------------------------|
| Database    | **SQLite** (single file: `cs2_skins.db`) |
| Backend     | **Python + Flask** (REST API) |
| Frontend    | **HTML + CSS + JavaScript** (Steam-Market inspired UI) |

## Architecture (3-Tier)
```
Browser  ──HTTP──►  Flask Server  ──SQL──►  SQLite Database
(HTML/JS)           (app.py)                (cs2_skins.db)
```

## Database Schema
Table: **skins**

| Column        | Type    | Description                          |
|---------------|---------|--------------------------------------|
| id            | INTEGER | Primary key, auto-increment          |
| name          | TEXT    | Full skin name (e.g. "AK-47 \| Redline") |
| weapon        | TEXT    | Weapon type (AK-47, AWP, Knife…)     |
| rarity        | TEXT    | Rarity tier (Mil-Spec → Contraband)  |
| wear          | TEXT    | Condition (Factory New, Field-Tested…) |
| market_value  | REAL    | Price in USD                         |
| image_url     | TEXT    | URL of the skin's image              |

50 sample rows are pre-loaded.

## How to Run
1. Install Flask:  `pip install flask`
2. Build the database:  `python init_db.py`
3. Start the server:  `python app.py`
4. Open in browser:  `http://127.0.0.1:5000`

## Features
- 🔎 **Search** by skin name or weapon
- 🎯 **Filter** by rarity tier (Mil-Spec, Restricted, Classified, Covert, Contraband)
- 💲 **Sort** by price (low → high or high → low) or name
- 🖼️ **Live preview** of each skin's image and market price
- ⚡ **REST API** (`/api/skins`, `/api/rarities`) returns clean JSON

## Rarity Tiers (CS2 Official Order)
| Tier        | Color     | Example Price |
|-------------|-----------|---------------|
| Consumer    | White     | < $0.50       |
| Industrial  | Light Blue| $0.50–$2      |
| Mil-Spec    | Blue      | $2–$10        |
| Restricted  | Purple    | $5–$50        |
| Classified  | Pink      | $10–$300      |
| Covert      | Red       | $30–$500+     |
| Contraband  | Gold      | $1000+ (rare) |

## Files
```
cs2_skins/
├── app.py             # Flask backend + API routes
├── init_db.py         # Builds the SQLite database
├── cs2_skins.db       # The database file (created by init_db.py)
├── README.md
├── templates/
│   └── index.html     # Main page
└── static/
    ├── style.css      # Steam-market styling
    └── script.js      # Calls the API and renders results
```
