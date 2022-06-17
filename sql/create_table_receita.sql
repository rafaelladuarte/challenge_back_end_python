-- DROP TABLE IF EXISTS public.receita;

CREATE TABLE IF NOT EXISTS public.receita
(
    rec_id integer NOT NULL DEFAULT nextval('receita_rec_id_seq'::regclass),
    rec_nm character varying(50) COLLATE pg_catalog."default",
    rec_ds character varying(150) COLLATE pg_catalog."default",
    rec_vl real,
    rec_dt timestamp with time zone,
    rec_cat_id integer,
    rec_tipo_id integer,
    CONSTRAINT pk_rec_id PRIMARY KEY (rec_id),
    CONSTRAINT fk_rec_cat_id FOREIGN KEY (rec_cat_id)
        REFERENCES public.categoria (cat_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_rec_tipo_id FOREIGN KEY (rec_tipo_id)
        REFERENCES public.tipo (tipo_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;