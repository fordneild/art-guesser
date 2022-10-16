CREATE TABLE
    objects (
        objectid integer PRIMARY key,
        accessioned integer,
        accessionnum character varying(32),
        locationid integer,
        title character varying(2048),
        displaydate character varying(256),
        beginyear integer,
        endyear integer,
        visualbrowsertimespan character varying(32),
        medium character varying(2048),
        dimensions character varying(2048),
        inscription character varying,
        markings character varying,
        attributioninverted character varying(1024),
        attribution character varying(1024),
        provenancetext character varying,
        creditline character varying(2048),
        classification character varying(64),
        subclassification character varying(64),
        visualbrowserclassification character varying(32),
        parentid integer,
        isvirtual integer,
        departmentabbr character varying(32),
        portfolio character varying(2048),
        series character varying(850),
        volume character varying(850),
        watermarks character varying(512),
        lastdetectedmodification timestamp
        with
            time zone,
            customprintegerurl character varying(512)
    );

COPY objects FROM '/app/data/objects.csv' WITH (FORMAT csv, header);

CREATE TABLE
    objects_terms(
        id SERIAL PRIMARY key,
        termid integer,
        objectid integer,
        termtype character varying(64),
        term character varying(256),
        visualbrowsertheme character varying(32),
        visualbrowserstyle character varying(64),
        CONSTRAINT objectid FOREIGN KEY(objectid) REFERENCES objects(objectid) ON DELETE CASCADE
    );

COPY
    objects_terms(
        termid,
        objectid,
        termtype,
        term,
        visualbrowsertheme,
        visualbrowserstyle
    )
FROM
    '/app/data/objects_terms.csv'
WITH (FORMAT csv, header);

CREATE TABLE
    constituents(
        constituentid integer PRIMARY key,
        ulanid character varying(32),
        preferreddisplayname character varying(256),
        forwarddisplayname character varying(256),
        lastname character varying(256),
        displaydate character varying(256),
        artistofngaobject integer,
        beginyear integer,
        endyear integer,
        visualbrowsertimespan character varying(32),
        nationality character varying(128),
        visualbrowsernationality character varying(128),
        constituenttype character varying(30)
    );

COPY constituents
FROM
    '/app/data/constituents.csv'
WITH (FORMAT csv, header);

CREATE TABLE
    objects_constituents(
        id SERIAL PRIMARY key,
        objectid integer,
        constituentid integer,
        displayorder integer,
        roletype character varying(64),
        role character varying(64),
        prefix character varying(64),
        suffix character varying(64),
        displaydate character varying(128),
        beginyear integer,
        endyear integer,
        country character varying(64),
        zipcode character varying(16),
        CONSTRAINT objectid FOREIGN KEY(objectid) REFERENCES objects(objectid) ON DELETE CASCADE,
        CONSTRAINT constituentid FOREIGN KEY(constituentid) REFERENCES constituents(constituentid) ON DELETE CASCADE
    );

COPY
    objects_constituents(
        objectid,
        constituentid,
        displayorder,
        roletype,
        role,
        prefix,
        suffix,
        displaydate,
        beginyear,
        endyear,
        country,
        zipcode
    )
FROM
    '/app/data/objects_constituents.csv'
WITH (FORMAT csv, header);

Create Table
    published_images(
        uuid UUID PRIMARY key,
        iiifurl character varying(512),
        iiifthumburl character varying(512),
        viewtype character varying(32),
        sequence character varying(32),
        width integer,
        height integer,
        maxpixels integer,
        created timestamp
        with
            time zone,
            modified timestamp
        with
            time zone,
            depictstmsobjectid integer,
            assistivetext text
    );

COPY published_images
FROM
    '/app/data/published_images.csv'
WITH (FORMAT csv, header);