-- View: public.receita_tipo

-- DROP VIEW public.receita_tipo;

CREATE OR REPLACE VIEW public.receita_tipo
 AS
 SELECT a.tipo_nm,
    round(sum(b.rec_vl)::double precision) AS receita_total,
    EXTRACT(month FROM b.rec_dt) AS rec_tipo_dt
   FROM tipo a
     JOIN receita b ON b.rec_tipo_id = a.tipo_id
  GROUP BY (EXTRACT(month FROM b.rec_dt)), a.tipo_nm;