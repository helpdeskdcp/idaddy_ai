from backend.database.database import db


class HistoryUpdater:

    def save_daily(
        self,
        symbol,
        rows,
    ):

        count = 0

        for r in rows:

            db.execute(
                """
                INSERT OR REPLACE INTO daily_candles
                (
                    symbol,
                    trade_date,
                    open,
                    high,
                    low,
                    close,
                    volume
                )
                VALUES
                (
                    ?,?,?,?,?,?,?
                )
                """,
                (
                    symbol,
                    r[0],
                    r[1],
                    r[2],
                    r[3],
                    r[4],
                    r[5],
                ),
            )

            count += 1

        return count


history_updater = HistoryUpdater()
