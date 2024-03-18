import configparser

def parse_configuration_file(file_path):
    config = configparser.ConfigParser()

    # Read the configuration file
    with open(file_path, 'r') as file:
        config.read_file(file)

    # Extract project settings and parameters
    project_settings = {}
    for section in config.sections():
        project_settings[section] = {}
        for option in config.options(section):
            value = config.get(section, option)

            # Try to convert the value to a boolean if it's a known boolean pair
            if option in config.BOOLEAN_STATES:
                value = config.BOOLEAN_STATES[option]

            project_settings[section][option] = value

    return project_settings
