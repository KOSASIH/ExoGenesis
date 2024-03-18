def mine_resources_from_space(extraterrestrial_bodies, mining_algorithms):
    """
    This function mines resources from extraterrestrial bodies using advanced mining algorithms.

    Parameters:
    extraterrestrial_bodies (list): List of extraterrestrial bodies to mine resources from.
    mining_algorithms (list): List of advanced mining algorithms to use for mining resources.

    Returns:
    dict: A dictionary containing the mined resources and their quantities.
    """

    mined_resources = {}

    for body in extraterrestrial_bodies:
        for algorithm in mining_algorithms:
            resources = algorithm(body)

            for resource, quantity in resources.items():
                if resource in mined_resources:
                    mined_resources[resource] += quantity
                else:
                    mined_resources[resource] = quantity

    return mined_resources
