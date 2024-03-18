import networkx as nx


def facilitate_cross_planetary_transactions(infrastructure_graph, transaction_fees):
    """
    Facilitate cross-planetary transactions between different celestial bodies within the space-based infrastructure.

    Parameters:
    infrastructure_graph (networkx.Graph): A directed graph representing the space-based infrastructure, where nodes represent
    components and edges represent communication links.
    transaction_fees (dict): A dictionary mapping each pair of celestial bodies to their transaction fee.

    Returns:
    tuple: A tuple containing the optimized transaction fee allocation for each communication link in the infrastructure.
    """

    # Create a bipartite graph for matching transaction fees with communication links
    bipartite_graph = nx.Graph()
    bipartite_graph.add_nodes_from(infrastructure_graph.edges, bipartite=0)
    bipartite_graph.add_nodes_from(transaction_fees.items(), bipartite=1)

    # Add edges between communication links and transaction fees based on their compatibility
    for link in infrastructure_graph.edges:
        for (body1, body2), fee in transaction_fees.items():
            if is_compatible(link, (body1, body2)):
                bipartite_graph.add_edge(link, (body1, body2))

    # Solve the assignment problem to find the optimal transaction fee allocation for each communication link
    row_ind, col_ind = linear_sum_assignment(
        nx.adjacency_matrix(bipartite_graph).toarray(), maximize=True
    )

    # Return the optimized transaction fee allocation for each communication link in the infrastructure
    return {
        infrastructure_graph.edges[i]: transaction_fees[j]
        for i, j in zip(row_ind, col_ind)
        if j != -1
    }
