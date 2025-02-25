import toml
from pathlib import Path

def load_ruff_config(config_path):
    """Load the Ruff configuration and extract 'exclude' and 'include' patterns."""
    config = toml.load(config_path)
    tool_config = config.get("tool", {}).get("ruff", {})
    
    exclude_patterns = tool_config.get("exclude", [])
    include_patterns = tool_config.get("include", [])
    
    return exclude_patterns, include_patterns

# Example usage:
config_file = Path("src/pyproject.toml")
if config_file.exists():
    exclude, include = load_ruff_config(config_file)
    print("Exclude:", exclude)
    print("Include:", include)
else:
    print("Ruff config file not found!")
