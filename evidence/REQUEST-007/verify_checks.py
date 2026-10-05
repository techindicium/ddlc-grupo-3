# Exploratory verify checks for REQUEST-007. Run from the root of a scratch clone of
# portwell-analytics after project/run.py:  .venv/bin/python verify_checks.py <evidence-dir>
import csv, sys, duckdb, yaml
E = sys.argv[1]
c = duckdb.connect('warehouse.duckdb', read_only=True)
man = yaml.safe_load(open('data/ops-extract/extract-manifest.yaml'))
out = []
def q(title, sql):
    out.append(f"## {title}\n-- {sql.strip()}\n{c.sql(sql)}\n")
out.append(f"# exploratory: verify checks for REQUEST-007, period 2026-08-01..2026-08-31\n")
out.append(f"## check 1 coverage\nmanifest taken_at: {man['taken_at']}\nmanifest notes: {man['notes'].strip()}\n")
q("check 1 coverage: latest ticket in extract", "select max(opened_at) as latest_opened_at, count(*) filter (where opened_at >= DATE '2026-08-01') as august_tickets from staging.tickets")
q("check 1 coverage: what staging.extract_metadata claims", "select * from staging.extract_metadata")
q("check 3 definition match: columns the v3 numerator and exclusion need", "select table_name, column_name from information_schema.columns where table_schema='ops' and column_name in ('human_edit_material','reopened_at','closed_at')")
q("check 3 definition match: is_self_served equals was_sent on every row (v2 rule)", "select count(*) as rows, count(*) filter (where is_self_served <> was_sent) as rows_where_v2_rule_not_used from staging.suggestions")
q("check 4 applicability: non-pilot accounts in August", "select s.account_id, s.self_service_rate from marts.self_service s join staging.accounts a using(account_id) where not a.is_pilot and s.month = DATE '2026-08-01' order by 1")
q("check 5 denominator: tickets counted vs tickets closed, August", "select sum(s.closed_tickets) as mart_denominator, (select count(*) from staging.tickets where month = DATE '2026-08-01' and status='closed') as closed_august, (select count(*) from staging.tickets where month = DATE '2026-08-01' and status<>'closed') as not_closed_august from marts.self_service s where s.month = DATE '2026-08-01'")
q("check 6 continuity: July and August per pilot account (v2 mart)", "select account_id, month, self_service_rate from marts.self_service s join staging.accounts a using(account_id) where a.is_pilot and month >= DATE '2026-07-01' order by 1,2")
open(f"{E}/verify-checks-output.txt","w").write("\n".join(out))
rows = c.sql("select s.account_id, a.is_pilot, s.self_service_rate from marts.self_service s join staging.accounts a using(account_id) where s.month = DATE '2026-08-01' order by 1").fetchall()
with open(f"{E}/figure-draft.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["account_id","period","metric","version_requested","version_implemented_by_mart","value","extract_taken_at","status"])
    for acc, pilot, v in rows:
        w.writerow([acc,"2026-08","self_service_rate","not stated","2 (mart logic; definitions file says 3 is current)", v if pilot else "not applicable", man['taken_at'], "EXPLORATORY DRAFT, NOT FOR PUBLICATION"])
