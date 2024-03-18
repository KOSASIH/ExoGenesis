import numpy as np


def analyze_extraterrestrial_resource_composition(resource_data):
    """
    Analyzes the composition of extraterrestrial resources to determine their suitability for various applications and inform mining strategies.

    Parameters:
    resource_data (dict): A dictionary containing the composition data of extraterrestrial resources.

    Returns:
    dict: A dictionary containing the analysis results for each resource.
    """

    analysis_results = {}

    for resource_name, resource_composition in resource_data.items():
        analysis_result = {}

        # Calculate the percentage of each element in the resource composition
        element_percentages = {}
        total_elements = sum(resource_composition.values())
        for element, count in resource_composition.items():
            element_percentages[element] = (count / total_elements) * 100

        analysis_result["element_percentages"] = element_percentages

        # Determine the suitability of the resource for various applications
        applications = ["mining", "construction", "power generation", "communication"]
        suitability_scores = {}
        for application in applications:
            suitability_score = 0

            # Calculate the suitability score based on the percentage of each required element in the resource composition
            required_elements = {
                "mining": ["iron", "nickel", "copper", "silicon"],
                "construction": ["iron", "silicon", "carbon"],
                "power generation": ["uranium", "thorium"],
                "communication": ["silicon", "gold"],
            }

            for required_element in required_elements[application]:
                if required_element in resource_composition:
                    suitability_score += element_percentages[required_element]
                else:
                    # Penalize if the required element is not present in the resource composition
                    suitability_score -= 100

            suitability_scores[application] = suitability_score

        analysis_result["suitability_scores"] = suitability_scores

        analysis_results[resource_name] = analysis_result

    return analysis_results
