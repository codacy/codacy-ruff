import requests
from bs4 import BeautifulSoup
import json
import os
from importlib.metadata import version

# Base URL of the patterns (replace with the actual base URL for pattern details)
base_pattern_url = 'https://docs.astral.sh/ruff/rules/'  # Adjust if needed

def fetch_pattern_description(pattern_name,rule_id):
    try:
        # Construct the URL for the specific pattern
        pattern_url = f"{base_pattern_url}{pattern_name}/"
        response = requests.get(pattern_url)
        
        if response.status_code == 200:
            # Parse the content of the pattern's page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the relevant content (adjust as needed based on the page structure)
            content = soup.find('main')  # Assuming <main> contains the relevant details
            if content:
                full_description = content.get_text(strip=False)  # Extract the full content
                relevant_lines = extract_relevant_lines(full_description,pattern_name,rule_id)  # Process the content
                return "\n".join(relevant_lines)  # Join lines back for the output
            else:
                print(f"No content found for {pattern_name}")
                return f"# {pattern_name}\n\nDescription not available."
        else:
            print(f"Failed to fetch {pattern_name} page. Status code: {response.status_code}")
            return f"# {pattern_name}\n\nFailed to fetch description."
    except Exception as e:
        print(f"Error fetching description for {pattern_name}: {e}")
        return f"# {pattern_name}\n\nError fetching description."

def extract_relevant_lines(full_description,pattern_name,rule_id):
    start_marker = f"{pattern_name} ({rule_id})" 
    end_markers = {"References", "Options","Back to top"}  
    relevant_lines = []
    capture = False
    previous_line = ""
    for line in full_description.splitlines():
        stripped_line = line.strip()
        if start_marker in stripped_line:
            capture = True
        if stripped_line in end_markers:
            break
        if capture:
                if line == start_marker:
                    relevant_lines.append(f"# {line}")
                    continue
                elif line == "What it does" or line == "Why is this bad?" or line == "Example" or line == "Examples":
                    relevant_lines.append(f"## {line}")
                elif previous_line == "Example" or previous_line == "Examples" or previous_line == "Use instead:":
                    relevant_lines.append(f"```\n{line}")
                elif line == "Use instead:":
                    relevant_lines.append(f"```\n## {line}")
                elif line == "":
                    continue
                else:
                    relevant_lines.append(line)
        previous_line = stripped_line
    relevant_lines.append("```")
    return relevant_lines

# Function to save the pattern description to a Markdown file
def save_to_markdown(pattern_name, content):
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, 'docs', 'descriptions')
    os.makedirs(output_dir, exist_ok=True)  # Create the folder if it doesn't exist
    
    # Define the markdown file path
    md_file_path = os.path.join(output_dir, f"{pattern_name}.md")
    
    # Write content to the markdown file
    with open(md_file_path, 'w',encoding='utf-8') as md_file:
        md_file.write(content)
    
    print(f"Description for {pattern_name} written to {md_file_path}")

def get_package_version(requirements_file, package_name):
    with open(requirements_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line.startswith(package_name):
            # Look for a version in the format "package_name==version"
            parts = line.split("==")
            if len(parts) == 2:
                return parts[1]  # Return the version part
            else:
                return None  # No version found
    return None  # Package not found

def main():
    response = requests.get(base_pattern_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find_all('tr')

        patterns_data = []
        active_patterns = set()  # Store active patterns to track outdated files
        output_dir = os.path.join(os.getcwd(), 'docs', 'descriptions')
        os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

        for tr in rows:
            td_elements = tr.find_all('td')
            if len(td_elements) > 1:
                rule_id = td_elements[0].text.strip()
                pattern_link = td_elements[1].find('a')
                
                # Check if the rule is marked as removed
                removed_marker = tr.find('span', attrs={"title": "This rule has been removed"})
                if removed_marker:
                    print(f"Skipping removed rule: {rule_id}")
                    continue  # Skip removed rules

                pattern_name = pattern_link.text.strip()
                pattern_id = f"{rule_id}_{pattern_name}"

                patterns_data.append({
                    "patternId": pattern_id,
                    "category": "ErrorProne",
                    "level": "Info",
                    "enabled": False
                })

                # Store active pattern filenames
                active_patterns.add(f"{pattern_id}.md")

                # Fetch and save the description for each pattern
                description = fetch_pattern_description(pattern_name, rule_id)
                save_to_markdown(pattern_id, description)

        # Remove old Markdown files that are no longer relevant
        for filename in os.listdir(output_dir):
            if filename.endswith(".md") and filename not in active_patterns:
                file_path = os.path.join(output_dir, filename)
                print(f"Removing outdated file: {filename}")
                os.remove(file_path)

        # Save patterns.json
        requirements_file = "requirements.txt"
        package_name = "ruff"
        version = get_package_version(requirements_file, package_name)
        output_data = {
            "name": "Codacy-Ruff",
            "version": version,
            "patterns": patterns_data
        }

        current_dir = os.getcwd()
        output_file_path = os.path.join(current_dir, 'docs', 'patterns.json')
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        with open(output_file_path, 'w') as json_file:
            json.dump(output_data, json_file, indent=4)

        print(f"Data successfully written to {output_file_path}")
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")


main()