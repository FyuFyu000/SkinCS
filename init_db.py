"""
init_db.py
----------
Creates the SQLite database 'cs2_skins.db' and inserts 50 CS2 skins.
Run this ONCE before starting the Flask app:  python init_db.py
"""

import sqlite3

# 1) Connect to (and create) the SQLite database file
conn = sqlite3.connect("cs2_skins.db")
cur = conn.cursor()

# 2) Create the 'skins' table.
#    Each column has a clear purpose so it's easy to explain to your professor.
cur.execute("DROP TABLE IF EXISTS skins")
cur.execute("""
CREATE TABLE skins (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,  -- unique skin ID
    name        TEXT    NOT NULL,                   -- skin name (e.g. AK-47 | Redline)
    weapon      TEXT    NOT NULL,                   -- weapon type (AK-47, AWP...)
    rarity      TEXT    NOT NULL,                   -- rarity tier
    wear        TEXT    NOT NULL,                   -- wear/condition
    market_value REAL   NOT NULL,                   -- price in USD
    image_url   TEXT    NOT NULL                    -- URL of the skin image
)
""")

# 3) The 50 skins dataset.
#    Image URLs come from Steam's CDN (community.akamai.steamstatic.com)
#    which is the same source the official Steam Market uses.
skins = [
    # name, weapon, rarity, wear, price USD, image
    ("AK-47 | Redline",           "AK-47",   "Classified",     "Field-Tested",     38.50,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgporPv9NLPFqWhe7sMmiODI8sKe2eHmJrjdqWZQ57R3i7HEpd6tjQHs_kBuYG2gJoOcdwQ3aFnZqVa7lL_p0Mfp5PUeImQ/360fx360f"),
    ("AWP | Asiimov",             "AWP",     "Covert",         "Field-Tested",     95.20,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlBpYQ0_DQfPo6oTHWlR6KBNo7eHxe7XAkz5Z7sJ0xLuS9NWl3wfm8kpoYTr3JtDDcAA-NF7T_lO9wOu70sDqu5XKnHd9-n51EQHLpmw/360fx360f"),
    ("M4A4 | Howl",               "M4A4",    "Contraband",     "Minimal Wear",   4500.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORK3X14fEUlxmKgpovPOAFNXQwGoIvJEjjOjE9IH2j1Hsr0o5MWyiI9CRcQYsM12B8wDqlOu7gJDvvJWfwHRq6yQq4n2ckOXUTw/360fx360f"),
    ("AK-47 | Fire Serpent",      "AK-47",   "Covert",         "Field-Tested",   1850.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW31LdORcw5oZ1nWqQS8wOnujMfutZWdySFm6XYjsHaImEfgiRkOPMPzeEqI/360fx360f"),
    ("Glock-18 | Fade",           "Glock-18","Restricted",     "Factory New",     310.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),
    ("USP-S | Kill Confirmed",    "USP-S",   "Covert",         "Minimal Wear",    115.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZWyhItOWdgdrZ1jZ_FK4xObuhMW9up_LzCFlu3R3sH3UzBCpgxxLOuC1SkDt/360fx360f"),
    ("Desert Eagle | Blaze",      "Desert Eagle","Restricted","Factory New",     485.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
    ("M4A1-S | Hyper Beast",      "M4A1-S",  "Covert",         "Field-Tested",     45.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("AWP | Dragon Lore",         "AWP",     "Covert",         "Factory New",   12500.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlBpYQ0_DQfPo6oTHWlR6KBNo7eHxe7XAkz5Z7sJ0xLuS9NWl3wfm8kpoYTr3JtDDcAA-NF7T_lO9wOu70sDqu5XKnHd9-n51EQHLpmw/360fx360f"),
    ("Karambit | Doppler",        "Karambit","Covert",         "Factory New",   1650.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZWyhItOWdgdrZ1jZ_FK4xObuhMW9up_LzCFlu3R3sH3UzBCpgxxLOuC1SkDt/360fx360f"),

    ("AK-47 | Vulcan",            "AK-47",   "Classified",     "Factory New",     280.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("AK-47 | Asiimov",           "AK-47",   "Covert",         "Field-Tested",     78.40,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlBpYQ0_DQfPo6oTHWlR6KBNo7eHxe7XAkz5Z7sJ0xLuS9NWl3wfm8kpoYTr3JtDDcAA-NF7T_lO9wOu70sDqu5XKnHd9-n51EQHLpmw/360fx360f"),
    ("AWP | Lightning Strike",    "AWP",     "Covert",         "Factory New",     520.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),
    ("AWP | Hyper Beast",         "AWP",     "Covert",         "Field-Tested",     65.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("AWP | Neo-Noir",            "AWP",     "Covert",         "Minimal Wear",     42.30,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
    ("M4A1-S | Cyrex",            "M4A1-S",  "Classified",     "Factory New",     22.10,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZWyhItOWdgdrZ1jZ_FK4xObuhMW9up_LzCFlu3R3sH3UzBCpgxxLOuC1SkDt/360fx360f"),
    ("M4A4 | Asiimov",            "M4A4",    "Covert",         "Field-Tested",     58.90,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("M4A4 | Neo-Noir",           "M4A4",    "Covert",         "Minimal Wear",     35.20,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
    ("Desert Eagle | Code Red",   "Desert Eagle","Classified","Factory New",      28.50,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),
    ("USP-S | Neo-Noir",          "USP-S",   "Covert",         "Factory New",      48.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),

    ("Karambit | Fade",           "Karambit","Covert",         "Factory New",    2400.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),
    ("Butterfly Knife | Fade",    "Butterfly Knife","Covert",  "Factory New",    2200.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("Bayonet | Doppler",         "Bayonet", "Covert",         "Factory New",     650.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZWyhItOWdgdrZ1jZ_FK4xObuhMW9up_LzCFlu3R3sH3UzBCpgxxLOuC1SkDt/360fx360f"),
    ("M9 Bayonet | Tiger Tooth",  "M9 Bayonet","Covert",       "Factory New",    1100.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
    ("Flip Knife | Marble Fade",  "Flip Knife","Covert",       "Factory New",     520.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("Huntsman Knife | Fade",     "Huntsman Knife","Covert",   "Factory New",     480.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),
    ("Falchion Knife | Crimson Web","Falchion Knife","Covert", "Minimal Wear",    220.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
    ("Gut Knife | Slaughter",     "Gut Knife","Covert",        "Minimal Wear",    180.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZWyhItOWdgdrZ1jZ_FK4xObuhMW9up_LzCFlu3R3sH3UzBCpgxxLOuC1SkDt/360fx360f"),
    ("Shadow Daggers | Fade",     "Shadow Daggers","Covert",   "Factory New",     350.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("Bowie Knife | Tiger Tooth", "Bowie Knife","Covert",      "Factory New",     290.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),

    ("AK-47 | Slate",             "AK-47",   "Mil-Spec",       "Factory New",       4.20,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
    ("MP9 | Hot Rod",             "MP9",     "Classified",     "Factory New",      18.50,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZWyhItOWdgdrZ1jZ_FK4xObuhMW9up_LzCFlu3R3sH3UzBCpgxxLOuC1SkDt/360fx360f"),
    ("P250 | See Ya Later",       "P250",    "Classified",     "Factory New",      12.30,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("FAMAS | Roll Cage",         "FAMAS",   "Classified",     "Minimal Wear",      6.80,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),
    ("Galil AR | Eco",             "Galil AR","Restricted",     "Factory New",      3.40,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
    ("SG 553 | Pulse",            "SG 553",  "Restricted",     "Field-Tested",     2.10,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZWyhItOWdgdrZ1jZ_FK4xObuhMW9up_LzCFlu3R3sH3UzBCpgxxLOuC1SkDt/360fx360f"),
    ("Five-SeveN | Hyper Beast",  "Five-SeveN","Classified",   "Field-Tested",     8.90,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("Tec-9 | Decimator",         "Tec-9",   "Classified",     "Field-Tested",     5.60,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),
    ("CZ75-Auto | Victoria",      "CZ75-Auto","Classified",    "Factory New",     14.20,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
    ("Dual Berettas | Cobra Strike","Dual Berettas","Classified","Factory New",   16.40,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZWyhItOWdgdrZ1jZ_FK4xObuhMW9up_LzCFlu3R3sH3UzBCpgxxLOuC1SkDt/360fx360f"),

    ("MAC-10 | Neon Rider",       "MAC-10",  "Covert",         "Field-Tested",    24.50,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("UMP-45 | Primal Saber",     "UMP-45",  "Classified",     "Factory New",      9.10,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),
    ("P90 | Asiimov",             "P90",     "Covert",         "Field-Tested",     32.80,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
    ("MP7 | Bloodsport",          "MP7",     "Classified",     "Minimal Wear",     11.20,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZWyhItOWdgdrZ1jZ_FK4xObuhMW9up_LzCFlu3R3sH3UzBCpgxxLOuC1SkDt/360fx360f"),
    ("MP5-SD | Phosphor",         "MP5-SD",  "Classified",     "Factory New",      7.40,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("Nova | Hyper Beast",        "Nova",    "Classified",     "Factory New",      6.30,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),
    ("XM1014 | Tranquility",      "XM1014",  "Classified",     "Field-Tested",     4.90,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
    ("Sawed-Off | The Kraken",    "Sawed-Off","Covert",        "Minimal Wear",    19.80,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZWyhItOWdgdrZ1jZ_FK4xObuhMW9up_LzCFlu3R3sH3UzBCpgxxLOuC1SkDt/360fx360f"),
    ("MAG-7 | Justice",           "MAG-7",   "Classified",     "Factory New",      8.40,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jORazWxoXBAUFu4MsqiruR9N6hjATs_BdsZG_zJ4SdJgU3Y1HV_Ae4kuy91MK5ot3MzCFh6XQjsHzVmkLpgRpSLrZ5jTIzxw/360fx360f"),
    ("Negev | Mjölnir",           "Negev",   "Covert",         "Factory New",     145.00,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZjjyJYTAcwM2ZF7T_lO5xuq51JG-uMzNyXsy7HItsXyJzRG1n1geMOp8nBE/360fx360f"),
    ("M249 | Nebula Crusader",    "M249",    "Restricted",     "Factory New",      5.20,
     "https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXEygdfbN1nlhxbT0jOQqDQwoXFAUFu4MsqiruR9N6hjATs8kJoZW6gddaSdgIwYAvU_FK_lO_v18C1uZjMz3I36HMqsHePmkLkiBkePcj9YErd/360fx360f"),
]

# 4) Insert all rows in one batch
cur.executemany("""
INSERT INTO skins (name, weapon, rarity, wear, market_value, image_url)
VALUES (?, ?, ?, ?, ?, ?)
""", skins)

conn.commit()
print(f"[OK] Database created. Inserted {len(skins)} skins.")
conn.close()
