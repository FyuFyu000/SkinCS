"""
app.py
------
Main Flask application for the CS2 Skin Market.
- Serves the homepage
- Provides a /search API endpoint that queries the SQLite database
"""

from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = "cs2_skins.db"


def query_db(sql, args=()):
    """Helper function: open DB, run query, return list of dicts."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # so we can access columns by name
    cur = conn.cursor()
    cur.execute(sql, args)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


# -------- ROUTES --------

@app.route("/")
def home():
    """Render the main page (templates/index.html)."""
    return render_template("index.html")


@app.route("/api/skins")
def api_skins():
    """
    Returns skin data from the database as JSON.
    Supports: ?q=search_term  &rarity=Covert  &sort=price_asc|price_desc|name
    """
    q       = request.args.get("q", "").strip()
    rarity  = request.args.get("rarity", "All")
    sort    = request.args.get("sort", "name")

    # Build SQL dynamically — using parameterized queries to prevent SQL injection
    sql  = "SELECT * FROM skins WHERE 1=1"
    args = []

    if q:
        sql += " AND (name LIKE ? OR weapon LIKE ?)"
        args.extend([f"%{q}%", f"%{q}%"])

    if rarity and rarity != "All":
        sql += " AND rarity = ?"
        args.append(rarity)

    if sort == "price_asc":
        sql += " ORDER BY market_value ASC"
    elif sort == "price_desc":
        sql += " ORDER BY market_value DESC"
    else:
        sql += " ORDER BY name ASC"

    rows = query_db(sql, args)
    return jsonify(rows)


@app.route("/api/rarities")
def api_rarities():
    """Returns the distinct rarity tiers — used to populate the filter dropdown."""
    rows = query_db("SELECT DISTINCT rarity FROM skins ORDER BY rarity")
    return jsonify([r["rarity"] for r in rows])


if __name__ == "__main__":
    # Start the development server on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
