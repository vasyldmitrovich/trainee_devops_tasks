import os
from jinja2 import Template

# Get current build number from environment
build_number = os.getenv('GITHUB_RUN_NUMBER', 'N/A')
print(f"Current build number: {build_number}")

# Path to the template file
template_path = '01_git/task2_jinja/template.j2'
print(f"Template path: {template_path}")

# Read template content from file
with open(template_path, 'r') as file:
    template_str = file.read()
    print(f"Read template content:\n{template_str}")

# Create a Jinja2 Template object
template = Template(template_str)
print("Jinja2 Template object created.")

# Render the template with build number
rendered_content = template.render(build_number=build_number)
print(f"Rendered content:\n{rendered_content}")

# File to update
file_path = 'README.md'
print(f"File path to update: {file_path}")

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()
    print(f"Read file content:\n{content}")

# Find existing template block in README.md
start_marker = '### My Actions'
end_marker = '-End-'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
    # Replace existing template block
    new_content = content[:start_idx] + rendered_content + content[end_idx+len(end_marker):]
    print("Replacing existing template block.")
else:
    # Append new template block to end of file
    new_content = content + "\n" + rendered_content
    print("Appending new template block.")

# Write updated content back to file
with open(file_path, 'w') as file:
    file.write(new_content)
    print(f"Updated file {file_path} with:\n{new_content}")

print("Template rendered and updated in README.md")
