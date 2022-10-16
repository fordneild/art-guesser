# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Constituent(Base):
    __tablename__ = "constituents"

    constituentid = Column(Integer, primary_key=True)
    ulanid = Column(String(32))
    preferreddisplayname = Column(String(256))
    forwarddisplayname = Column(String(256))
    lastname = Column(String(256))
    displaydate = Column(String(256))
    artistofngaobject = Column(Integer)
    beginyear = Column(Integer)
    endyear = Column(Integer)
    visualbrowsertimespan = Column(String(32))
    nationality = Column(String(128))
    visualbrowsernationality = Column(String(128))
    constituenttype = Column(String(30))


class Object(Base):
    __tablename__ = "objects"

    objectid = Column(Integer, primary_key=True)
    accessioned = Column(Integer)
    accessionnum = Column(String(32))
    locationid = Column(Integer)
    title = Column(String(2048))
    displaydate = Column(String(256))
    beginyear = Column(Integer)
    endyear = Column(Integer)
    visualbrowsertimespan = Column(String(32))
    medium = Column(String(2048))
    dimensions = Column(String(2048))
    inscription = Column(String)
    markings = Column(String)
    attributioninverted = Column(String(1024))
    attribution = Column(String(1024))
    provenancetext = Column(String)
    creditline = Column(String(2048))
    classification = Column(String(64))
    subclassification = Column(String(64))
    visualbrowserclassification = Column(String(32))
    parentid = Column(Integer)
    isvirtual = Column(Integer)
    departmentabbr = Column(String(32))
    portfolio = Column(String(2048))
    series = Column(String(850))
    volume = Column(String(850))
    watermarks = Column(String(512))
    lastdetectedmodification = Column(DateTime(True))
    customprintegerurl = Column(String(512))

    terms = relationship("ObjectsTerm")


class PublishedImage(Base):
    __tablename__ = "published_images"

    uuid = Column(UUID, primary_key=True)
    iiifurl = Column(String(512))
    iiifthumburl = Column(String(512))
    viewtype = Column(String(32))
    sequence = Column(String(32))
    width = Column(Integer)
    height = Column(Integer)
    maxpixels = Column(Integer)
    created = Column(DateTime(True))
    modified = Column(DateTime(True))
    depictstmsobjectid = Column(Integer)
    assistivetext = Column(Text)


class ObjectsConstituent(Base):
    __tablename__ = "objects_constituents"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('objects_constituents_id_seq'::regclass)"),
    )
    objectid = Column(ForeignKey("objects.objectid", ondelete="CASCADE"))
    constituentid = Column(ForeignKey("constituents.constituentid", ondelete="CASCADE"))
    displayorder = Column(Integer)
    roletype = Column(String(64))
    role = Column(String(64))
    prefix = Column(String(64))
    suffix = Column(String(64))
    displaydate = Column(String(128))
    beginyear = Column(Integer)
    endyear = Column(Integer)
    country = Column(String(64))
    zipcode = Column(String(16))

    constituent = relationship("Constituent")
    object = relationship("Object")


class ObjectsTerm(Base):
    __tablename__ = "objects_terms"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('objects_terms_id_seq'::regclass)"),
    )
    termid = Column(Integer)
    objectid = Column(ForeignKey("objects.objectid", ondelete="CASCADE"))
    termtype = Column(String(64))
    term = Column(String(256))
    visualbrowsertheme = Column(String(32))
    visualbrowserstyle = Column(String(64))
