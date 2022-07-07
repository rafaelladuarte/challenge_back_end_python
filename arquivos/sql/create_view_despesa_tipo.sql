-- View: public.despesa_tipo

-- DROP VIEW public.despesa_tipo;

CREATE OR REPLACE VIEW public.despesa_tipo
 AS
 SELECT a.tipo_nm,
    round(sum(b.des_vl)::double precision) AS despesa_total,
    EXTRACT(month FROM b.des_dt) AS des_tipo_dt
   FROM tipo a
     JOIN despesa b ON b.des_tipo_id = a.tipo_id
  GROUP BY (EXTRACT(month FROM b.des_dt)), a.tipo_nm;