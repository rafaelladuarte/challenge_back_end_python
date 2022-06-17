-- Table: public.categoria

-- DROP TABLE IF EXISTS public.categoria;

CREATE TABLE IF NOT EXISTS public.categoria
(
    cat_id integer NOT NULL DEFAULT nextval('categoria_cat_id_seq'::regclass),
    cat_nm character varying(50) COLLATE pg_catalog."default",
    cat_ds character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT categoria_pkey PRIMARY KEY (cat_id)
)

TABLESPACE pg_default;