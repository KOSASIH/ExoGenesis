import ExoGenesis.project.AstroMesh as AstroMesh

# Create an exo-world network with 5 exo-worlds
network = AstroMesh.create_network(5)

# Generate the initial energy distribution across the exo-worlds
initial_energy_distribution = AstroMesh.generate_initial_energy_distribution(network)

# Simulate the energy distribution over 100 time steps
energy_distribution_over_time = AstroMesh.simulate_energy_distribution(
    network, initial_energy_distribution, 100
)

# Model the communication network between the exo-worlds
communication_network = AstroMesh.create_communication_network(network)

# Calculate the energy transmission between exo-worlds over 100 time steps
energy_transmission_over_time = AstroMesh.calculate_energy_transmission(
    communication_network, energy_distribution_over_time
)
