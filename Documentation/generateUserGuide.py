import os
import markdown
from jinja2 import Environment, FileSystemLoader

def generateUserGuide(project_name, project_description, user_manual_sections):
    """
    Generates the user guide documentation for the project.

    :param project_name: Name of the project
    :param project_description: Description of the project
    :param user_manual_sections: List of sections for the user manual
    """

    # Create the necessary directories for the user guide
    user_guide_dir = os.path.join(os.getcwd(), 'user_guide')
    if not os.path.exists(user_guide_dir):
        os.makedirs(user_guide_dir)

    # Load the Jinja2 template for the user guide
    env = Environment(loader=FileSystemLoader('templates'))
    user_guide_template = env.get_template('user_guide.md')

    # Generate the user guide content
    user_guide_content = user_guide_template.render(
        project_name=project_name,
        project_description=project_description,
        user_manual_sections=user_manual_sections
    )

    # Save the user guide content as a Markdown file
    with open(os.path.join(user_guide_dir, 'user_guide.md'), 'w') as f:
        f.write(user_guide_content)

    # Convert the Markdown file to HTML
    with open(os.path.join(user_guide_dir, 'user_guide.md'), 'r') as f:
        markdown_content = f.read()

    html_content = markdown.markdown(markdown_content)

    # Save the HTML content as an HTML file
    with open(os.path.join(user_guide_dir, 'user_guide.html'), 'w') as f:
        f.write(html_content)
