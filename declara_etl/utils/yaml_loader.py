import yaml

class DuplicateKeyError(Exception):
    pass

def no_duplicates_constructor(loader, node, exc=DuplicateKeyError):
    """
    Raises an exception if duplicate keys are found.
    """
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in mapping:
            raise exc(f"Duplicate key '{key}' found.")
        mapping[key] = loader.construct_object(value_node)
    return mapping

yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, no_duplicates_constructor, Loader=yaml.SafeLoader)
