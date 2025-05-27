from datetime import datetime, timedelta
from models import DoseLog
from database import session


def generate_dose_logs(medication):
    start = datetime.combine(medication.start_date, datetime.min.time())
    end = datetime.combine(medication.end_date, datetime.min.time()) if medication.end_date else start + timedelta(
        days=7)

    current = start
    while current <= end:
        dose = DoseLog(
            medication_id=medication.id,
            scheduled_datetime=current,
            status="pending",
            actual_datetime=None
        )
        session.add(dose)
        current += timedelta(hours=medication.frequency_hours)

    session.commit()
