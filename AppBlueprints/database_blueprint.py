from flask import Blueprint, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

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
