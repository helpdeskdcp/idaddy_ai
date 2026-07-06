from backend.database.database import db

SCHEMA_VERSION = "1.1"


def create_tables():

    tables = [

    """
    CREATE TABLE IF NOT EXISTS schema_version (
        version TEXT PRIMARY KEY,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS daily_candles (
        symbol TEXT NOT NULL,
        trade_date TEXT NOT NULL,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume REAL,
        PRIMARY KEY(symbol, trade_date)
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS weekly_candles (
        symbol TEXT NOT NULL,
        week TEXT NOT NULL,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume REAL,
        PRIMARY KEY(symbol, week)
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS monthly_candles (
        symbol TEXT NOT NULL,
        month TEXT NOT NULL,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume REAL,
        PRIMARY KEY(symbol, month)
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS yearly_candles (
        symbol TEXT NOT NULL,
        year TEXT NOT NULL,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume REAL,
        PRIMARY KEY(symbol, year)
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS live_ticks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT,
        token TEXT,
        ltp REAL,
        tick_time TEXT
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS oi_history (
        symbol TEXT,
        strike REAL,
        option_type TEXT,
        oi INTEGER,
        timestamp TEXT
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS oi_change_history (
        symbol TEXT,
        strike REAL,
        option_type TEXT,
        oi_change INTEGER,
        timestamp TEXT
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS iv_history (
        symbol TEXT,
        strike REAL,
        option_type TEXT,
        iv REAL,
        timestamp TEXT
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS option_chain_history (
        symbol TEXT,
        strike REAL,
        option_type TEXT,
        ltp REAL,
        bid REAL,
        ask REAL,
        volume INTEGER,
        oi INTEGER,
        iv REAL,
        timestamp TEXT
    )
    """
    ]

    for sql in tables:
        db.execute(sql)

    db.execute(
        "INSERT OR IGNORE INTO schema_version(version) VALUES (?)",
        (SCHEMA_VERSION,)
    )

    print(f"✓ Database Schema {SCHEMA_VERSION} Ready")


if __name__ == "__main__":
    create_tables()
