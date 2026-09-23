import json
import sys


def collect_values(node, result):
    if isinstance(node, dict):
        if "id" in node and "value" in node:
            result[node["id"]] = node["value"]
        for child in node.values():
            collect_values(child, result)
    elif isinstance(node, list):
        for child in node:
            collect_values(child, result)


def fill_report(node, values):
    if isinstance(node, dict):
        if "id" in node and "value" in node and node["id"] in values:
            node["value"] = values[node["id"]]
        for child in node.values():
            fill_report(child, values)
    elif isinstance(node, list):
        for child in node:
            fill_report(child, values)


def main():
    values_path, tests_path, report_path = sys.argv[1:4]
    with open(values_path, encoding="utf-8") as f:
        values_data = json.load(f)
    with open(tests_path, encoding="utf-8") as f:
        report = json.load(f)

    values = {}
    collect_values(values_data, values)
    fill_report(report, values)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()