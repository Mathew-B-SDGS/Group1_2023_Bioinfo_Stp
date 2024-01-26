from __future__ import annotations
from flask import Blueprint, redirect, render_template
from flask import request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, ForeignKey
from sqlalchemy import Integer, String, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column, relationship
from typing import List
from datetime import datetime

"""
THIS IS THE DATABASE BLUEPRINT

This blueprint is used to create the database and add to the database.
all directories are relative to the app directory with /database/ added to
the urltables are Written using sqlalchemy ORM and the database
is a sqlite database

Database is stored in Instance folder as project.db
and is created when the app is run for the first time
"""


blueprint_db = Blueprint('database', __name__, url_prefix='/database')


class Base(DeclarativeBase):
    '''base class for all tables'''
    pass


# this is the database object
db = SQLAlchemy(model_class=Base)


class Sample(db.Model):
    """
    table holds Sample details, for all samples processed in a run
    sample type is optional and can be null
    """
    __tablename__ = "sample"
    sample_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True,
        unique=True, nullable=False)
    sample_name: Mapped[str] = mapped_column(String(30), nullable=False)
    sample_type: Mapped[str] = mapped_column(String(30), nullable=True)

    def __repr__(self):
        return f"sample_id: {self.sample_id}, sample_name: {self.sample_name}"


class Patient(db.Model):
    """
    table holds Patient details,
    this is a one to many relationship with the TestCase table
    enabling a patient to have multiple test cases
    Can be created in the database or added to the database from the panel page
    """
    __tablename__ = "patient"

    patient_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, unique=True)
    patient_name: Mapped[str] = mapped_column(String(30), nullable=False)

    # relationships
    which_testcase: Mapped[List['TestCase']] = relationship(
        'TestCase', back_populates='which_patient')

    def __repr__(self):
        return (f"patient_id: {self.patient_id}, "
                f"patient_name: {self.patient_name}")


class TestType(db.Model):
    """
    table holds TestType details, Includign Rnumber and version'
    this table also stores a Json of the list of genes in the panel
    which can be accessed by the panel page
    relationship with TestCase table is one to many
    """
    __tablename__ = "testtype"
    testtype_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True,
        unique=True, nullable=False)
    testtype_name: Mapped[str] = mapped_column(String(30), nullable=False)
    testtype_version: Mapped[str] = mapped_column(String(30), nullable=True)
    testtype_rnumber: Mapped[str] = mapped_column(String(30), nullable=True)
    list_of_genes: Mapped[dict[list]] = mapped_column(
        type_=JSON, nullable=True)
    # relationships
    which_testcase: Mapped[List['TestCase']] = relationship(
        'TestCase', back_populates='which_testtype')

    def __repr__(self):
        return (f"testtype_id: {self.testtype_id}, "
                f"testtype_name: {self.testtype_name}")


class TestCase(db.Model):
    """
    table holds TestCase details, Linking Patient and Test type
    this table also stores the date of the test and the scientist who
    ran the test
    """
    __tablename__ = "testcase"

    testcase_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, unique=True,
        nullable=False)
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
        return (f"testcase_id: {self.testcase_id},"
                f" date_of_test: {self.date_of_test}")


def create_tables(context, db):
    """create all tables"""
    with context:
        db.create_all()


"""
all app routes are to be found below this comment
including
- the home page
- the all samples page
- the individual sample page
- the create sample page
- the panel page
- the create panel page
"""


@blueprint_db.route('/')
def hello():
    """Landing page for the database blueprint" """
    return """
    <style>
    * {
      font-family: sans-serif;
    }
    </style>
    <h1>Patient-Panel Database</h1><br>
    <p>Click below to go to the database</p><br>
    <a href="/database/patients">DATABASE</a><br>
    """


@blueprint_db.route("/patients")
def patient_list():
    """
    list all patients in the database in a table format

    input: none
    output: html page with all patients in the database
    """
    # forms a query object of all patients in the database
    # renders the template passing the query object
    patient_list_db = db.session.execute(
        db.select(Patient).order_by(Patient.patient_id)).scalars()
    return render_template("patient_list_all.html", patients=patient_list_db)


@blueprint_db.route("/patients/<int:sample_id>")
def sample_list_specific(sample_id):
    """
    list Specfic samples in the database, including all details
    linked to that sample
    this is a dynamic route, the sample_id is passed in the url and
    used to query the database

    input: sample_id (int)
    output: dynamic F string with all details of the specific sample
    """
    # query the database for all details and join the tables
    stmnt_all = select(Patient, TestType, TestCase)\
        .join(Patient.which_testcase)\
        .join(TestCase.which_testtype)\
        .where(Patient.patient_id == sample_id)
    # execute the query and store the results
    results = db.session.execute(stmnt_all).all()
    # 3 lists are created to store the details of the 3 tables
    list_test_details1 = []
    list_test_details2 = []
    list_test_details3 = []
    # loop through the results and append the details to the lists
    # (has to loop as the results are a list of tuples)
    for result in results:
        print(result.__getattr__)
        print(result.__getattribute__)
        list_test_details1.extend(["Disease Name = "
                                  + result.TestType.testtype_name,
                                  "Panel Version = " +
                                   result.TestType.testtype_version,
                                   "R Number =" +
                                   result.TestType.testtype_rnumber,
                                   "Gene List = "
                                   + str(result.TestType.list_of_genes)])
        list_test_details2.extend(
            ["Database ID:" + str(result.Patient.patient_id),
             "Patient Name:" + result.Patient.patient_name])
        list_test_details3.extend(
            ["Test ID"+str(result.TestCase.testcase_id),
             "Date of Test:"+str(result.TestCase.date_of_test),
             "Scientist:"+str(result.TestCase.user)])

    # could be scalar or scalars or .all()

    return f"""
    <h1>Patient-Panel entries</h1><br>
    <h3>Laboratory details</h3>{list_test_details3}<hr><br>
    <h3>Patient details</h3>{list_test_details2}<hr><br>
    <h3>Panel details</h3>{list_test_details1}<hr><br>
    <br><a href="/database/patients">Back</a>
    <a href="/">Home</a>
    """


@blueprint_db.route("/patients/create", methods=["GET", "POST"])
def sample_create():
    """
    create a new sample in the database
    Url is dependent on the method, if the method is post then the sample
    is added to the database
    else the form is rendered to the user to fill in

    input: html form with sample details
    output: html page with a form to create a new sample
    """
    # http method is post and the form has been submitted
    if request.method == "POST":
        # access form and strip removes any white space from the input
        sample = Sample(
            sample_name=request.form["sample_name"].strip(),
            sample_type=request.form["sample_type"].strip()
        )
        # add and commit the new sample to the database
        db.session.add(sample)
        db.session.commit()
        return redirect(url_for("database.sample_list"))
    return render_template("sample_create.html")


@blueprint_db.route("/panel", methods=["GET", "POST"])
def panels_choice():
    """
    Choose between creating a new patient or selecting an existing one
    depending on http method the form is rendered or the patient is added
    to the database

    input: html form with patient details
    output: html page with a form to create a new patient or a list
    of existing patients
    """
    # http method is post and the form has been submitted
    if request.method == "POST":
        # instantiate a new patient object for the database
        patient_add = Patient(
            patient_name=request.form["patient_name"].strip(),)
        db.session.add(patient_add)
        db.session.commit()
        # query the database for all patients
        some_patients = db.session.query(
            Patient.patient_name).all()
        return render_template("panels_choice.html",
                               patients_list=some_patients)
    else:  # http method is get and the form has not been submitted
        some_patients = db.session.query(Patient.patient_name).all()
        return render_template("panels_choice.html",
                               patients_list=some_patients)


@blueprint_db.route("/panel/create", methods=["GET", "POST"])
def update_patient_panel():
    """
    Link details of R-panel to patient within database
    this is a dynamic route, the patient_id is passed in
    the url and used to query the database

    input: session token with panel details  and patient_id (int) selected
    from the panel page
    output: dynamic F string with all details of the specific sample
    and session token
    """
    r_number = session['r']
    if request.method == "POST":

        object_add = TestCase(
            date_of_test=datetime.today().date(),
            which_patient=Patient.query.filter_by(
                patient_name=request.form["patient_selected"]).first(),
            which_testtype=TestType(
                # details are stored in the session token
                testtype_name=session['panel_name'],
                testtype_version=session['panel_version'],
                testtype_rnumber=r_number,
                list_of_genes=session['gene_list']
            )
        )
        db.session.add(object_add)
        db.session.commit()

        return f"""Updated database for;
          {request.form['patient_selected']} with panel {r_number}
        <br>
        {session['panel_name']}
         <br>
        {session['panel_version'] }
        <hr>
        <p> detailed info: </p>
        {session['gene_list']}
       <br><a href="/">Home</a>
        <br><a href="/database/">View Database</a>
     """
