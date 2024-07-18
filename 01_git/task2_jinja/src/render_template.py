#!/usr/bin/python3

import os
import logging
from jinja2 import Template

# Config logger
logging.basicConfig(filename='render_template.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Get current build number from environment
build_number = os.getenv('GITHUB_RUN_NUMBER', 'N/A')
logger.info(f"Current build number: {build_number}")

# Path to the template file
template_path = '01_git/task2_jinja/src/template.j2'
logger.info(f"Template path: {template_path}")

# Read template content from file
try:
    with open(template_path, 'r') as file:
        template_str = file.read()
        logger.info(f"Read template content:\n{template_str}")
except FileNotFoundError:
    logger.error(f"Template file not found: {template_path}")
    exit(1)

# Create a Jinja2 Template object
template = Template(template_str)
logger.info("Jinja2 Template object created.")

# Render the template with build number
rendered_content = template.render(build_number=build_number)
logger.info(f"Rendered content:\n{rendered_content}")

# File to update
file_path = 'README.md'
logger.info(f"File path to update: {file_path}")

# Read the content of the file
try:
    with open(file_path, 'r') as file:
        content = file.read()
        logger.info(f"Read file content:\n{content}")
except FileNotFoundError:
    logger.error(f"File not found: {file_path}")
    exit(1)

# Find existing template block in README.md
start_marker = '### My Actions'
end_marker = '-End-'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
    # Replace existing template block
    new_content = content[:start_idx] + rendered_content + content[end_idx+len(end_marker):]
    logger.info("Replacing existing template block.")
else:
    # Append new template block to end of file
    new_content = content + "\n" + rendered_content
    logger.info("Appending new template block.")

# Write updated content back to file
with open(file_path, 'w') as file:
    file.write(new_content)
    logger.info(f"Updated file {file_path} with:\n{new_content}")

logger.info("Template rendered and updated in README.md")
