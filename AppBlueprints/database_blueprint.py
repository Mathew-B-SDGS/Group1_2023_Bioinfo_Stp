from __future__ import annotations
from flask import Blueprint, redirect, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, select, Column, ForeignKey, Integer, String, Float, Boolean, JSON, Select, inspect
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from typing import Optional, List
from datetime import datetime

blueprint_db = Blueprint('database', __name__, url_prefix='/database')


class Base(DeclarativeBase):
    '''base class for all tables'''
    pass


db = SQLAlchemy(model_class=Base)


class Sample(db.Model):
    """
    table holds Batch details, for all samples processed in a run
    Used to demonstrate Database functionality. 
    """
    __tablename__ = "sample"
    sample_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    sample_name: Mapped[str] = mapped_column(String(30), nullable=False)
    sample_type: Mapped[str] = mapped_column(String(30), nullable=True)

    def __repr__(self):
        return f"sample_id: {self.sample_id}, sample_name: {self.sample_name}"


class Patient(db.Model):
    """table holds Patient details, for all samples processed in a run"""
    __tablename__ = "patient"

    patient_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, unique=True)
    patient_name: Mapped[str] = mapped_column(String(30), nullable=False)

    # relationships
    which_testcase: Mapped[List['TestCase']] = relationship(
        'TestCase', back_populates='which_patient')

    def __repr__(self):
        return f"patient_id: {self.patient_id}, patient_name: {self.patient_name}"


class TestType(db.Model):
    "table holds TestType details, Includign Rnumber and version"
    __tablename__ = "testtype"
    testtype_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    testtype_name: Mapped[str] = mapped_column(String(30), nullable=False)
    testtype_version: Mapped[str] = mapped_column(String(30), nullable=True)
    testtype_rnumber: Mapped[str] = mapped_column(String(30), nullable=True)
    # TODO think about how to store a list of genes, mabye a Json column?
    list_of_genes: Mapped[dict[list]] = mapped_column(
        type_=JSON, nullable=True)
    # relationships
    which_testcase: Mapped[List['TestCase']] = relationship(
        'TestCase', back_populates='which_testtype')

    def __repr__(self):
        return f"testtype_id: {self.testtype_id}, testtype_name: {self.testtype_name}"


class TestCase(db.Model):
    """table holds TestCase details, Linking Patient and Test type"""
    __tablename__ = "testcase"

    testcase_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    date_of_test: Mapped[str] = mapped_column(String(30), nullable=False)
    user: Mapped[str] = mapped_column(String(30), nullable=True)
    # foreign keys
    fk_sample_id: Mapped[int] = mapped_column(
        (ForeignKey('patient.patient_id')), nullable=False)
    fk_testtype_id: Mapped[int] = mapped_column(
        (ForeignKey('testtype.testtype_id')), nullable=False)

    # relationships
    which_patient: Mapped[Patient] = relationship(
        'Patient', back_populates='which_testcase')
    which_testtype: Mapped[TestType] = relationship(
        'TestType', back_populates='which_testcase')

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
        db.select(Patient).order_by(Patient.patient_id)).scalars()
    return render_template("sample_list_all.html", sample=samples_list_db)


@blueprint_db.route("/samples/<int:sample_id>")
def sample_list_specific(sample_id):
    """list Specfic samples in the database, including all details linke to that sample"""
    stmnt2 = select(Patient, TestType, TestCase)\
        .join(Patient.which_testcase)\
        .join(TestCase.which_testtype)\
        .where(Patient.patient_id == sample_id)

    results = db.session.execute(stmnt2).all()
    list_test_details1 = []
    list_test_details2 = []
    list_test_details3 = []
    for result in results:
        print(result.__getattr__)
        print(result.__getattribute__)
        list_test_details1.extend(["Disease Name = " + result.TestType.testtype_name, "Panel Version = " + result.TestType.testtype_version,
                                  "R Number =" + result.TestType.testtype_rnumber, "Gene List = " + str(result.TestType.list_of_genes)])
        list_test_details2.extend(
            ["Database ID:" + str(result.Patient.patient_id), "Patient Name:" + result.Patient.patient_name])
        list_test_details3.extend(
            ["Test ID"+str(result.TestCase.testcase_id), "Date of Test:"+str(result.TestCase.date_of_test), "Scientist:"+str(result.TestCase.user)])

    # could be scalar or scalars or .all()

    return f"""<h1>Detailed List</h1><br>
        <h3>Laboratory details</h3>{list_test_details3}<hr><br>
        <h3>Patient details</h3>{list_test_details2}<hr><br>
        <h3>Panel details</h3>{list_test_details1}<hr><br>
        <br><a href="/database/samples">Back</a>
        <a href="/">Home</a>
        """


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


@blueprint_db.route("/panel", methods=["GET", "POST"])
def panels_choice():
    """
    Choose between creating a new patient or selecting an existing one
    """
    if request.method == "POST":
        patient_add = Patient(
            patient_name=request.form["patient_name"].strip(),)
        db.session.add(patient_add)
        db.session.commit()
        some_patients = db.session.query(Patient.patient_name).all()
        return render_template("panels_choice.html", patients_list=some_patients)
    else:
        # all_patients = db.session.execute(db.select(Patient).all)
        some_patients = db.session.query(Patient.patient_name).all()
        return render_template("panels_choice.html", patients_list=some_patients)


@blueprint_db.route("/panel/create", methods=["GET", "POST"])
def update_patient_panel():
    """
    add panel to patient details within database
    """
    r_number = session['r']
    if request.method == "POST":

        object_add = TestCase(
            date_of_test=datetime.today().date(),
            user=request.form["user"].strip(),
            which_patient=Patient.query.filter_by(
                patient_name=request.form["patient_selected"]).first(),
            which_testtype=TestType(
                testtype_name=session['panel_name'],
                testtype_version=session['panel_version'],
                testtype_rnumber=r_number,
                list_of_genes=session['gene_list']
            )

        )
        db.session.add(object_add)
        db.session.commit()

        return f"""Updated database for; {request.form['patient_selected']} with panel {r_number}
        <br>
        {session['panel_name']}
         <br>
        {session['panel_version'] }
        <hr>
        <p> detailed info: </p>
        {session['gene_list']} 
        <br><a href="/">Home</a>
        <br><a href="/database/panel">View Database</a>
     """
