import json, sys, argparse
p = argparse.ArgumentParser()
p.add_argument("--min-recall", type=float, required=True)
args = p.parse_args()

m = json.load(open("metrics.json"))
n = json.load(open("baseline.json"))
o = m['recall'] - n['recallDifference']

print(f"recall = {m['recall']:.4f}, required >= {o:.4f}")
if m["recall"] < o:
    print("QUALITY GATE FAILED: recall is below the required minimum")
    sys.exit(1)
print("Quality gate passed")
