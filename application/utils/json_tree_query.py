"""
This module converts JSON tree queries to SQL query
"""
from typing import Any, Dict, List, Tuple

SUBSTITUTIONS = {"NOT": "not like", "IS": "=", "AND": "and", "CONTAINS": "like", "NOT IS": "!=" }

def expand_dict(a_dict: Dict, negated: bool) -> Dict:
    for key, value in a_dict.items():
        operation = SUBSTITUTIONS[f'NOT {key}'] if negated else SUBSTITUTIONS[f'{key}']
        return operation, value

    return "", {}

def convert_query(query): # sourcery no-metrics
    ORM_QUERY= ['select * from log where ']

    items: List[Tuple[str, Any]] = list(query.items())
    items_count = len(items)
    if items_count == 0:
        return {}

    (key, values), *_ = items
    if key in ("NOT"):
        (k, v), *_ = values.items()
        if isinstance(v, list):
            for i in range(len(v)):
                (x,y), *_ = v[i].items()
                if isinstance(y, list):
                    z = len(y)
                    for i in range(len(y)):
                        if type(y[i]) == dict:
                            a,b = expand_dict(y[i], negated=True)
                            if isinstance(b, dict):
                                for key, value in b.items():
                                    ORM_QUERY.append(f"{key} {a} '{value}'")
                                    if z > 1:
                                        ORM_QUERY.append(f' {SUBSTITUTIONS[x]} ')
                elif x == "CONTAINS":
                    (a,b), *_ = y.items()
                    ORM_QUERY.append(f"{a} NOT LIKE '{b}%%'")
        elif isinstance(values, dict):
            (x,y) = expand_dict(values, negated=True)
            (key, value), *_= y.items()
            ORM_QUERY.append(f"{key} {x} '{value}'")
    else:
        a,b = expand_dict(query, negated=False)
        for k,v in b.items():
            if key in ("CONTAINS"):
                ORM_QUERY.append(f"{k} {a} '{v}%%'")
            else:
                ORM_QUERY.append(f"{k} {a} '{v}'")

    return "".join(ORM_QUERY)