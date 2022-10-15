# coding: utf-8
from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
)
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


class MediaItem(Base):
    __tablename__ = "media_items"

    mediaid = Column(BigInteger, primary_key=True)
    mediatype = Column(String(32))
    title = Column(String(2048))
    description = Column(Text)
    duration = Column(Integer)
    language = Column(String(12))
    thumbnailurl = Column(String(1024))
    playurl = Column(String(1024))
    downloadurl = Column(String(1024))
    keywords = Column(String(2048))
    tags = Column(String(2048))
    imageurl = Column(String(1024))
    presentationdate = Column(DateTime(True))
    releasedate = Column(DateTime(True))
    lastmodified = Column(DateTime(True))


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


t_media_relationships = Table(
    "media_relationships",
    metadata,
    Column("mediaid", ForeignKey("media_items.mediaid", ondelete="CASCADE")),
    Column("relatedid", BigInteger),
    Column("relatedentity", String(32)),
)


t_objects_constituents = Table(
    "objects_constituents",
    metadata,
    Column("objectid", ForeignKey("objects.objectid", ondelete="CASCADE")),
    Column(
        "constituentid", ForeignKey("constituents.constituentid", ondelete="CASCADE")
    ),
    Column("displayorder", Integer),
    Column("roletype", String(64)),
    Column("role", String(64)),
    Column("prefix", String(64)),
    Column("suffix", String(64)),
    Column("displaydate", String(128)),
    Column("beginyear", Integer),
    Column("endyear", Integer),
    Column("country", String(64)),
    Column("zipcode", String(16)),
)


t_objects_terms = Table(
    "objects_terms",
    metadata,
    Column("termid", Integer),
    Column("objectid", ForeignKey("objects.objectid", ondelete="CASCADE")),
    Column("termtype", String(64)),
    Column("term", String(256)),
    Column("visualbrowsertheme", String(32)),
    Column("visualbrowserstyle", String(64)),
)
