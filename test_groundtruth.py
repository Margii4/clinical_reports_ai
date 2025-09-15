import json
import sys
from rapidfuzz import fuzz

def load_json(filename):
    with open(filename, encoding='utf-8-sig') as f:
        return json.load(f)

def field_names_equal(a, b):
    return fuzz.token_sort_ratio(a.lower(), b.lower()) > 90

def object_equal(obj1, obj2):
    keys = ["field name", "field value", "field unit of measure", "reference_range_low", "reference_range_high"]
    return all(
        str(obj1.get(k, "")).strip().lower() == str(obj2.get(k, "")).strip().lower()
        if k != "field name" else field_names_equal(obj1.get("field name", ""), obj2.get("field name", ""))
        for k in keys
    )

def evaluate(pred, gt):
    matches = 0
    for gt_obj in gt:
        if any(object_equal(gt_obj, p_obj) for p_obj in pred):
            matches += 1
    return matches / len(gt)

if __name__ == "__main__":
    pred = load_json(sys.argv[1])
    gt_dict = load_json(sys.argv[2])
    gt = gt_dict["groundTruth"]
    acc = evaluate(pred, gt)
    print(f"Accuracy: {acc*100:.1f}%")

