from __future__ import annotations
from sqlalchemy import create_engine, Integer, String, ForeignKey, select, Column, Float, Boolean, DateTime, Date, DateTime
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from typing import Optional, List


# TODO change the name of the sever
engine = create_engine('sqlite:///./bed_project_database.db')
session = Session(engine)


class Base(DeclarativeBase):
    '''base class for all tables'''
    pass


class Patient(Base):
    '''table holds Batch details, for all samples processed in a run'''
    __tablename__ = "patient"

    patient_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, unique=True, nullable=False)
    patient_name: Mapped[str] = mapped_column(String(30), unique=True)

    def __repr__(self):
        return f"patient_id: {self.patient_id}, patient_name: {self.patient_name}"


class User(Base):
    '''table holds Batch details, for all samples processed in a run'''
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(30), nullable=False)

    def __repr__(self):
        return f"user_id: {self.user_id}, username: {self.username}"


class ClinicalIndication(Base):
    __tablename__ = "clinical_indication"

    clinical_indication_id: Mapped[str] = mapped_column(primary_key=True)
    test_id: Mapped[str] = mapped_column(primary_key=True)
    clinical_indication: Mapped[str] = mapped_column(String)
    target_genes: Mapped[str] = mapped_column(String)
    test_method: Mapped[str] = mapped_column(String)
    commissioning_category: Mapped[str] = mapped_column(String)
    specialist_test_group: Mapped[str] = mapped_column(String)
    changes_since_april_2023_publication: Mapped[str] = mapped_column(String)


Base.metadata.create_all(engine)
