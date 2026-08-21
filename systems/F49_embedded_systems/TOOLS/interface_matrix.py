def interface_matrix(interfaces: list[dict]) -> dict:
    return {i.get("name", f"interface_{n}"): i for n, i in enumerate(interfaces)}
