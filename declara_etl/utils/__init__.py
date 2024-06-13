from declara_etl.utils.yaml_loader import yaml
from declara_etl.utils.import_operators import import_operators

def find_all_operators(d, key="operator"):
    results = []

    def search_dict(d):
        if isinstance(d, dict):
            for k, v in d.items():
                if k == key:
                    results.append(v)
                elif isinstance(v, dict):
                    search_dict(v)
                elif isinstance(v, list):
                    for item in v:
                        search_dict(item)
    
    search_dict(d)
    return list(set(results))