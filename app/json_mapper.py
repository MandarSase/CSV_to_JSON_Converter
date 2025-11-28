def build_nested_json(flat):
    output = {}

    for key, value in flat.items():
        parts = key.split(".")
        current = output
        
        for p in parts[:-1]:
            if p not in current:
                current[p] = {}
            current = current[p]
        
        current[parts[-1]] = value
    
    return output
