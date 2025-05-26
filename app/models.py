from sqlalchemy import Column, Integer, String, Date, ForeignKey, Time, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

    medications = relationship("Medication", back_populates="user")

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100), nullable=False)
    dosage = Column(String(100), nullable=False)
    frequency_hours = Column(Integer, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)

    user = relationship("User", back_populates="medications")
    times = relationship("MedicationTime", back_populates="medication")
    doses = relationship("DoseLog", back_populates="medication")

class MedicationTime(Base):
    __tablename__ = "medication_times"

    id = Column(Integer, primary_key=True)
    medication_id = Column(Integer, ForeignKey("medications.id"))
    time = Column(Time, nullable=False)

    medication = relationship("Medication", back_populates="times")

class DoseLog(Base):
    __tablename__ = "dose_logs"

    id = Column(Integer, primary_key=True)
    medication_id = Column(Integer, ForeignKey("medications.id"))
    scheduled_datetime = Column(DateTime, nullable=False)
    status = Column(String(20), nullable=False)  # "taken", "missed", "pending"
    actual_datetime = Column(DateTime, nullable=True)

    medication = relationship("Medication", back_populates="doses")
