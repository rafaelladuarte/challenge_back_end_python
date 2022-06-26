-- View: public.saldo

-- DROP VIEW public.saldo;

CREATE OR REPLACE VIEW public.saldo
 AS
 SELECT sum(a.des_vl) AS despesa_total,
    sum(b.rec_vl) AS receita_total,
    sum(b.rec_vl) - sum(a.des_vl) AS saldo,
    EXTRACT(month FROM a.des_dt) AS saldo_month
   FROM despesa a,
    receita b
  GROUP BY (EXTRACT(month FROM a.des_dt));

