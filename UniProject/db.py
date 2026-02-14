import sqlite3


def inicializar_db():
    """Inicializa la base de datos con todas las tablas necesarias."""
    conn = sqlite3.connect("cultivos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT CHECK(role IN ('admin', 'usuario')),
            email TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hectareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER,
            tipo_de_cultivo TEXT,
            siembra TEXT,
            primera_cosecha TEXT,
            cosecha_rutinaria TEXT,
            tipo_suelo TEXT,
            temperatura REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tipo_suelo (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE,
            descripcion TEXT,
            imagen TEXT
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM tipo_suelo")
    if cursor.fetchone()[0] == 0:
        default_suelos = [
            ("Arenoso", "Suelos con alta cantidad de arena.", "arenoso.jpg"),
            ("Limoso", "Suelos con alta proporción de limo.", "limoso.jpg"),
            ("Franco", "Suelos equilibrados.", "franco.jpg"),
            ("Arcilloso", "Suelos con alta cantidad de arcilla.", "arcilloso.jpg")
        ]
        cursor.executemany("INSERT INTO tipo_suelo (nombre, descripcion, imagen) VALUES (?, ?, ?)", default_suelos)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tipo_hortaliza (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE,
            descripcion TEXT,
            imagen TEXT
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM tipo_hortaliza")
    if cursor.fetchone()[0] == 0:
        default_hortalizas = [
            ("Bulbos", "Vegetales de forma redonda que crecen bajo tierra.", "bulbos.jpg"),
            ("Tallos comestibles", "Vegetales con tallos comestibles.", "tallos.jpg"),
            ("Raíces comestibles", "Vegetales con raíces comestibles.", "raices.jpg"),
            ("Frutos", "Vegetales de tipo fruto.", "frutos.jpg"),
            ("Hojas", "Vegetales donde se consumen las hojas.", "hojas.jpg"),
            ("Flores", "Vegetales en los que se consumen las flores.", "flores.jpg"),
            ("Tubérculos", "Vegetales con tubérculos comestibles.", "tuberculos.jpg")
        ]
        cursor.executemany("INSERT INTO tipo_hortaliza (nombre, descripcion, imagen) VALUES (?, ?, ?)", default_hortalizas)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clima (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE,
            grados_temperatura REAL,
            descripcion TEXT,
            imagen TEXT
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM clima")
    if cursor.fetchone()[0] == 0:
        default_climas = [
            ("Tropical", 30, "Clima cálido y húmedo.", "tropical.jpg"),
            ("Seco", 25, "Clima árido con poca humedad.", "seco.jpg"),
            ("Templado", 20, "Clima moderado.", "templado.jpg"),
            ("Continental", 15, "Clima con estaciones bien marcadas.", "continental.jpg"),
            ("Polar", 0, "Clima muy frío.", "polar.jpg")
        ]
        cursor.executemany("INSERT INTO clima (nombre, grados_temperatura, descripcion, imagen) VALUES (?, ?, ?, ?)", default_climas)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gestion_cultivo (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            id_persona INTEGER,
            id_tipo_hortaliza INTEGER,
            id_tipo_suelo INTEGER,
            id_clima INTEGER,
            video TEXT,
            observaciones TEXT,
            FOREIGN KEY(id_persona) REFERENCES usuarios(id),
            FOREIGN KEY(id_tipo_hortaliza) REFERENCES tipo_hortaliza(codigo),
            FOREIGN KEY(id_tipo_suelo) REFERENCES tipo_suelo(codigo),
            FOREIGN KEY(id_clima) REFERENCES clima(codigo)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tipo_cultivo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE,
            meses_primera INTEGER,
            meses_rutinaria INTEGER
        )
    """)
    cursor.execute("INSERT OR IGNORE INTO usuarios (username, password, role, email) VALUES ('admin', 'admin123', 'admin', NULL)")
    conn.commit()
    conn.close()


def obtener_personas():
    conn = sqlite3.connect("cultivos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM usuarios")
    personas = cursor.fetchall()
    conn.close()
    return personas


def obtener_tipo_hortaliza():
    conn = sqlite3.connect("cultivos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, nombre FROM tipo_hortaliza")
    datos = cursor.fetchall()
    conn.close()
    return datos


def obtener_tipo_suelo():
    conn = sqlite3.connect("cultivos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, nombre FROM tipo_suelo")
    datos = cursor.fetchall()
    conn.close()
    return datos


def obtener_climas():
    conn = sqlite3.connect("cultivos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo, nombre FROM clima")
    datos = cursor.fetchall()
    conn.close()
    return datos
