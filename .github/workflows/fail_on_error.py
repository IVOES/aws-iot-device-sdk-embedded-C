#!/usr/bin/env python3

import json
import sys

# Return whether SARIF file contains error-level results
def codeql_sarif_contain_error(filename):
    with open(filename, 'r') as f:
        s = json.load(f)

    for run in s.get('runs', []):
        rules_metadata = run['tool']['driver']['rules']
        for res in run.get('results', []):
            rule_index = res['ruleIndex']
            rule_level = rules_metadata[rule_index]['defaultConfiguration']['level']
            if rule_level == 'error':
                return True
    return False

if __name__ == "__main__":
    if codeql_sarif_contain_error(sys.argv[1]):
        sys.exit(1)
