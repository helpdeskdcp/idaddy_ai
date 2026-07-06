from datetime import datetime


class HistoryValidator:

    REQUIRED_COLUMNS = 6

    def validate(self, rows):

        valid = []

        for row in rows:

            if len(row) < self.REQUIRED_COLUMNS:
                continue

            try:
                datetime.fromisoformat(row[0])

                float(row[1])
                float(row[2])
                float(row[3])
                float(row[4])
                int(row[5])

                valid.append(row)

            except Exception:
                continue

        return valid


validator = HistoryValidator()
