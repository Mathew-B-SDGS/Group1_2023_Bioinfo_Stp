from __future__ import annotations
from flask import Blueprint, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, select, Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from typing import Optional, List

blueprint_db = Blueprint('database', __name__, url_prefix='/database')


class Base(DeclarativeBase):
    '''base class for all tables'''
    pass


db = SQLAlchemy(model_class=Base)


class Sample(db.Model):
    """table holds Batch details, for all samples processed in a run"""
    __tablename__ = "sample"
    sample_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    sample_name: Mapped[str] = mapped_column(String(30), nullable=False)
    sample_type: Mapped[str] = mapped_column(String(30), nullable=True)
    # relationships
    patient_relationship: Mapped[Patient] = relationship(
        back_populates='patient_samples')

    def __repr__(self):
        return f"sample_id: {self.sample_id}, sample_name: {self.sample_name}"


class Patient(db.Model):
    """table holds Patient details, for all samples processed in a run"""
    __tablename__ = "patient"

    patient_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    patient_name: Mapped[str] = mapped_column(String(30), nullable=False)
    patient_type: Mapped[str] = mapped_column(String(30), nullable=True)

    # relationships
    patient_samples: Mapped[List['Sample']] = relationship(
        'Sample', back_populates='patient_relationship')
    run_testcases: Mapped[List['TestCase']] = relationship(
        'TestCase', back_populates='patient')

    def __repr__(self):
        return f"patient_id: {self.patient_id}, patient_name: {self.patient_name}"


class TestType(db.Model):
    "table holds TestType details, Includign Rnumber and version"
    __tablename__ = "testtype"
    testtype_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    testtype_name: Mapped[str] = mapped_column(String(30), nullable=False)
    testtype_version: Mapped[str] = mapped_column(String(30), nullable=True)

    def __repr__(self):
        return f"testtype_id: {self.testtype_id}, testtype_name: {self.testtype_name}"


class TestCase(db.Model):
    """table holds TestCase details, Linking Patient and Test type"""
    __tablename__ = "testcase"

    testcase_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    date_of_test: Mapped[str] = mapped_column(String(30), nullable=False)
    # foreign keys
    Patient_id: Mapped[int] = mapped_column(
        (ForeignKey('patient.patient_id')), nullable=False)
    TestType_id: Mapped[int] = mapped_column(
        (ForeignKey('testtype.testtype_id')), nullable=False)

    # relationships
    patient: Mapped = relationship('Patient', back_populates='testcase')

    def __repr__(self):
        return f"testcase_id: {self.testcase_id}, date_of_test: {self.date_of_test}"


def create_tables(context, db):
    """create all tables"""
    with context:
        db.create_all()

# another way to create the tables
# Base.metadata.create_all(blueprint_db.engine)


@blueprint_db.route('/')
def hello():
    """Landing page for the database blueprint" """
    return """
    <h1>Database</h1><br>
    <p>this module is for accessing the Database</p><br>
    <p>click below to go to view or add samples</p><br>
    <a href="/database/samples">View All</a><br>
    <a href="/database/samples/create">Add Sample</a><br>
    """


@blueprint_db.route("/samples")
def sample_list():
    """list all samples in the database"""
    samples_list_db = db.session.execute(
        db.select(Sample).order_by(Sample.sample_id)).scalars()
    return render_template("sample_list_all.html", sample=samples_list_db)


@blueprint_db.route("/samples/create", methods=["GET", "POST"])
def sample_create():
    """create a new sample in the database"""
    if request.method == "POST":

        # create a new sample object and add it to the database
        sample = Sample(
            sample_name=request.form["sample_name"].strip(),
            sample_type=request.form["sample_type"].strip()
        )
        db.session.add(sample)
        db.session.commit()
        return redirect(url_for("database.sample_list"))
    return render_template("sample_create.html")
