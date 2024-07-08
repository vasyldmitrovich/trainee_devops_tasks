import os
from jinja2 import Template

# Get current build number from environment
build_number = os.getenv('GITHUB_RUN_NUMBER', 'N/A')

# Path to the template file
template_path = './01_git/task2_jinja_template/template.j2'

# Read template content from file
with open(template_path, 'r') as file:
    template_str = file.read()

# Create a Jinja2 Template object
template = Template(template_str)

# Render the template with build number
rendered_content = template.render(build_number=build_number)

# File to update
file_path = 'README.md'

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Find existing template block in README.md
start_marker = '### My Actions'
end_marker = '-End-'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
    # Replace existing template block
    new_content = content[:start_idx] + rendered_content + content[end_idx+len(end_marker):]
else:
    # Append new template block to end of file
    new_content = content + "\n" + rendered_content

# Write updated content back to file
with open(file_path, 'w') as file:
    file.write(new_content)

print("Template rendered and updated in README.md")
