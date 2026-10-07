# Builds data/program-items-coded.csv from the coder-1 files (product, profession, norms)
# and adds the norms agreement to data/methods/agreement.json. Run from the repo root:
#   python3 data/methods/merge.py <path-to-coder2-norms.csv>
import csv, json, sys
base = "data"
old = list(csv.DictReader(open(f"{base}/program-presentations.csv")))
c1 = {r["id"]: r for r in csv.DictReader(open(f"{base}/methods/coder1-items.csv"))}
nm = {r["id"]: r for r in csv.DictReader(open(f"{base}/methods/coder1-norms.csv"))}
cols = ["id","session_id","session_title","session_type","title","presenters","product","profession","norms","confidence","rationale","norms_rationale","v1_code"]
with open(f"{base}/program-items-coded.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in old:
        a, n = c1[r["id"]], nm[r["id"]]
        conf = "low" if "low" in (a["confidence"], n["confidence"]) else "high"
        w.writerow({**{k: r[k] for k in cols[:6]}, "product": a["product"], "profession": a["profession"], "norms": n["norms"],
                    "confidence": conf, "rationale": a["rationale"], "norms_rationale": n["rationale"], "v1_code": r["code"]})
if len(sys.argv) > 1:
    c2 = {r["id"]: r for r in csv.DictReader(open(sys.argv[1]))}
    ids = [i for i in c2 if i in nm]
    a = [int(nm[i]["norms"]) for i in ids]; b = [int(c2[i]["norms"]) for i in ids]
    n = len(ids); po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a)/n, sum(b)/n; pe = pa*pb + (1-pa)*(1-pb)
    ag = json.load(open(f"{base}/methods/agreement.json"))
    ag["norms"] = {"agreement": round(po,3), "kappa": round((po-pe)/(1-pe),3) if pe < 1 else None,
                   "confusion_c1_by_c2": {f"{x}{y}": sum(1 for p,q in zip(a,b) if p==x and q==y) for x in (1,0) for y in (1,0)}}
    json.dump(ag, open(f"{base}/methods/agreement.json","w"), indent=1)
    print("norms agreement", ag["norms"])
rows = list(csv.DictReader(open(f"{base}/program-items-coded.csv")))
cnt = lambda k: sum(r[k] == "1" for r in rows)
print("items", len(rows), "product", cnt("product"), "profession", cnt("profession"), "norms", cnt("norms"),
      "norms&profession", sum(r["norms"] == "1" and r["profession"] == "1" for r in rows))
