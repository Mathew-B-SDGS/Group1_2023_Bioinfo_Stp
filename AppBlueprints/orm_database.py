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

    patient_key: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, unique=True, nullable=False)
    patient_identifier: Mapped[str] = mapped_column(String(30), unique=True)
    # foreign key to the NationalTestDirectory table that links patient to applied Test
    clinical_indication_id: Mapped[str] = mapped_column(
        ForeignKey("natinal_test_directory.test_key"))

    def __repr__(self):
        return f"patient_id: {self.patient_key}, patient_name: {self.patient_name}"


class User(Base):
    '''table holds Batch details, for all samples processed in a run'''
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(30), nullable=False)

    def __repr__(self):
        return f"user_id: {self.user_id}, username: {self.username}"


class NatinalTestDirectory(Base):
    __tablename__ = "natinal_test_directory"

    test_key: Mapped[str] = mapped_column(
        primary_key=True, autoincrement=True, unique=True, nullable=False)
    clinical_indication_id: Mapped[str] = mapped_column(String(30))
    test_id: Mapped[str] = mapped_column(String(30))
    clinical_indication: Mapped[str] = mapped_column(String)
    target_genes: Mapped[str] = mapped_column(String)
    test_method: Mapped[str] = mapped_column(String)
    commissioning_category: Mapped[str] = mapped_column(String)
    specialist_test_group: Mapped[str] = mapped_column(String)
    changes_since_april_2023_publication: Mapped[str] = mapped_column(String)


Base.metadata.create_all(engine)
