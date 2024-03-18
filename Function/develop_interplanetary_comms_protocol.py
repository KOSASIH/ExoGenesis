import os

from opestom_functions import custom_functions


def develop_interplanetary_comms_protocol(protocol_designs, communication_partners):
    """
    This function develops communication protocols for interplanetary communication.

    Parameters:
    protocol_designs (list): List of communication protocol designs to be developed.
    communication_partners (list): List of communication partners for the developed protocols.

    Returns:
    dict: A dictionary containing the developed communication protocols and their communication partners.
    """

    developed_protocols = {}

    for design in protocol_designs:
        for partner in communication_partners:
            protocol = design(partner)

            if partner in developed_protocols:
                developed_protocols[partner].append(protocol)
            else:
                developed_protocols[partner] = [protocol]

    return developed_protocols
