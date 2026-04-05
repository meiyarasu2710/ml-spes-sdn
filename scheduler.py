def select_node():

    nodes = {
        "Node1": {"energy":80, "security":9, "load":40},
        "Node2": {"energy":60, "security":8, "load":30},
        "Node3": {"energy":90, "security":7, "load":20}
    }

    best_node = None
    best_score = -1

    for node in nodes:

        energy = nodes[node]["energy"]
        security = nodes[node]["security"]
        load = nodes[node]["load"]

        score = energy + security - load

        if score > best_score:
            best_score = score
            best_node = node

    return best_node