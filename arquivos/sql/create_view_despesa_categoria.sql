-- View: public.despesa_categoria

-- DROP VIEW public.despesa_categoria;

CREATE OR REPLACE VIEW public.despesa_categoria
 AS
 SELECT a.cat_nm,
    round(sum(b.des_vl)::double precision) AS des_cat_total,
    EXTRACT(month FROM b.des_dt) AS des_cat_dt
   FROM categoria a
     JOIN despesa b ON b.des_cat_id = a.cat_id
  GROUP BY a.cat_nm, (EXTRACT(month FROM b.des_dt));