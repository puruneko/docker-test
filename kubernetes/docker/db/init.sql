CREATE SEQUENCE seq_person_id
    INCREMENT BY 1
    START WITH 1
    NO CYCLE
;
CREATE TABLE "person" (
	id INTEGER NOT NULL DEFAULT nextval('seq_person_id'), 
	name VARCHAR
);

INSERT INTO "person" (id,name) VALUES (nextval('seq_person_id'),'undefined');