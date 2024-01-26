import pytest
from app import create_app
from appblueprints.database_blueprint import db, TestType, TestCase, Patient 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

"""
conftest.py is the standard file name for a flasking testing app
"""


@pytest.fixture()
def app():
    """Set up app for testing, import app from app.py"""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": 'sqlite:///:memory:'
    })

    with app.app_context():
        db.create_all()
    yield app


@pytest.fixture()
def client(app):
    """Return app for testing"""
    return app.test_client()

@pytest.fixture()
def session(app):
    """Create a session for the test database."""
    with app.app_context():
        Session = sessionmaker(bind=db.engine)
        session = Session()
        yield session
        session.close()


def test_home_page(client):
    """Test that the home page title appears when you load the app"""
    response = client.get("/")
    assert b"<h1>Welcome to PanelSearcher v1.0!</h1>" in response.data


def test_panel_search(client):
    """Check you get the correct panel related to the R test code"""
    response = client.post("/search", data={
        "r": "R167"
    })
    assert response.status_code == 200
    assert (b"<h2>Panel name: Autosomal recessive primary hypertrophic"
            b" osteoarthropathy</h2>" in response.data)

def test_testtype_model(session):
    """Test the TestType model."""
    # Create a TestType
    test_type = TestType(testtype_name='Test Type', testtype_version='v1', testtype_rnumber='R123', list_of_genes=None)
    session.add(test_type)
    session.commit()

    # Retrieve the TestType from the database
    retrieved_test_type = session.query(TestType).filter_by(testtype_name='Test Type').first()

    # Assert TestType properties
    assert retrieved_test_type is not None
    assert retrieved_test_type.testtype_name == 'Test Type'
    assert retrieved_test_type.testtype_version == 'v1'
    assert retrieved_test_type.testtype_rnumber == 'R123'
    #assert retrieved_test_type.list_of_genes == {'gene1', 'gene2'}

def test_patient_model(session):
    """Test the Patient model."""
    random_patient_name = 'Test Patient' + str(random.randint(1, 1000))
    # Create a Patient
    patient = Patient(patient_name=random_patient_name)
    session.add(patient)
    session.commit()

    # Retrieve the Patient from the database
    retrieved_patient = session.query(Patient).filter_by(patient_name=random_patient_name).first()

    # Assert Patient properties
    assert retrieved_patient is not None
    assert retrieved_patient.patient_name == random_patient_name

def test_testcase_model(session):
    """Test the TestCase model."""
    # Create a TestCase
    random_patient_name = 'Test Patient' + str(random.randint(1, 1000))
    random_test_type_name = 'Test Type R' + str(random.randint(1, 100))
    patient = Patient(patient_name=random_patient_name)
    session.add(patient)
    session.commit()

    test_type = TestType(testtype_name=random_test_type_name, testtype_version='v1', testtype_rnumber='R123', list_of_genes=None)
    session.add(test_type)
    session.commit()

    random_user = 'Test User' + str(random.randint(1, 1000))

    test_case = TestCase(date_of_test='2024-01-26', user=random_user, which_patient=patient, which_testtype=test_type)
    session.add(test_case)
    session.commit()

    # Retrieve the TestCase from the database
    retrieved_test_case = session.query(TestCase).filter_by(user=random_user).first()

    # Assert TestCase properties
    assert retrieved_test_case is not None
    assert retrieved_test_case.date_of_test == '2024-01-26'
    assert retrieved_test_case.user == random_user
    assert retrieved_test_case.which_patient == patient
    assert retrieved_test_case.which_testtype == test_type
