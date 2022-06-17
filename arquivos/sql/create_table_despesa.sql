-- DROP TABLE IF EXISTS public.despesa;

CREATE TABLE IF NOT EXISTS public.despesa
(
    des_id integer NOT NULL DEFAULT nextval('despesa_des_id_seq'::regclass),
    des_nm character varying(50) COLLATE pg_catalog."default",
    des_ds character varying(150) COLLATE pg_catalog."default",
    des_vl real,
    des_dt timestamp with time zone,
    des_cat_id integer,
    des_tipo_id integer,
    CONSTRAINT pk_des_id PRIMARY KEY (des_id),
    CONSTRAINT fk_des_cat_id FOREIGN KEY (des_cat_id)
        REFERENCES public.categoria (cat_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_des_tipo_id FOREIGN KEY (des_tipo_id)
        REFERENCES public.tipo (tipo_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;
