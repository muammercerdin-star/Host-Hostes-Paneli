-- trips: seferler
CREATE TABLE IF NOT EXISTS trips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    route TEXT,
    departure_time TEXT,
    arrival_time TEXT,
    plate TEXT,
    driver_name TEXT,
    notes TEXT,
    created_at TEXT
);

-- cashflows: kasa hareketleri
CREATE TABLE IF NOT EXISTS cashflows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id INTEGER,
    type TEXT,
    category TEXT,
    description TEXT,
    quantity REAL,
    unit_price REAL,
    total REAL,
    created_at TEXT
);

-- products: ikram ürünleri
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    unit TEXT DEFAULT "adet",
    cost_price REAL,
    sale_price REAL,
    stock_threshold REAL DEFAULT 0,
    is_active INTEGER DEFAULT 1
);

-- inventory_moves: stok hareketleri
CREATE TABLE IF NOT EXISTS inventory_moves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    trip_id INTEGER,
    move_type TEXT,
    quantity REAL,
    unit_cost REAL,
    unit_price REAL,
    created_at TEXT
);

-- notes: hızlı notlar
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id INTEGER,
    category TEXT,
    text TEXT,
    created_at TEXT
);
