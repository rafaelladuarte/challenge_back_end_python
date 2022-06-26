-- DROP TABLE IF EXISTS public.tipo;

CREATE TABLE IF NOT EXISTS public.tipo
(
    tipo_id integer NOT NULL DEFAULT nextval('tipo_tipo_id_seq'::regclass),
    tipo_nm character varying(50) COLLATE pg_catalog."default",
    tipo_ds character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT tipo_pkey PRIMARY KEY (tipo_id)
)

TABLESPACE pg_default;
