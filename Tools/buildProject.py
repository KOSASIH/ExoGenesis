import os
import subprocess


def buildProject(build_type):
    """
    Builds the project from source code, generating executable binaries or distribution packages.

    :param build_type: The type of build to perform, either 'debug' or 'release'.
    """

    # Set the build directory based on the build type
    build_dir = "build" if build_type == "debug" else "build_release"

    # Create the build directory if it doesn't exist
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    # Change the current working directory to the build directory
    os.chdir(build_dir)

    # Run the appropriate build command based on the build type
    if build_type == "debug":
        # Run the debug build command

    else:
        raise ValueError("Invalid build type. Please use either 'debug' or 'release'.")
