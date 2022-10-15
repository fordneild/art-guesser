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
        termid integer,
        objectid integer,
        termtype character varying(64),
        term character varying(256),
        visualbrowsertheme character varying(32),
        visualbrowserstyle character varying(64),
        CONSTRAINT objectid FOREIGN KEY(objectid) REFERENCES objects(objectid) ON DELETE CASCADE
    );

COPY objects_terms
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

COPY objects_constituents
FROM
    '/app/data/objects_constituents.csv'
WITH (FORMAT csv, header);

CREATE TABLE
    media_items(
        mediaid bigint PRIMARY key,
        mediatype character varying(32),
        title character varying(2048),
        description text,
        duration integer,
        language character varying(12),
        thumbnailurl character varying(1024),
        playurl character varying(1024),
        downloadurl character varying(1024),
        keywords character varying(2048),
        tags character varying(2048),
        imageurl character varying(1024),
        presentationdate timestamp
        with
            time zone,
            releasedate timestamp
        with
            time zone,
            lastmodified timestamp
        with time zone
    );

COPY media_items
FROM
    '/app/data/media_items.csv'
WITH (FORMAT csv, header);

CREATE TABLE
    media_relationships(
        mediaid bigint,
        relatedid bigint,
        relatedentity character varying(32),
        CONSTRAINT mediaid FOREIGN KEY(mediaid) REFERENCES media_items(mediaid) ON DELETE CASCADE
    );

COPY media_relationships
FROM
    '/app/data/media_relationships.csv'
WITH (FORMAT csv, header);