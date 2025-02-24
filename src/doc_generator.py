import requests
from bs4 import BeautifulSoup
import json
import os
import re

# Base URL of the patterns
base_pattern_url = "https://docs.astral.sh/ruff/rules/"  # Adjust if needed

# Mapping rule acronyms to severity levels
severity_mapping = {
    # Error
    "S": "Error",
    "B": "Error",
    "BLE": "Error",
    "DTZ": "Error",
    "T10": "Error",
    "EM": "Error",
    "RSE": "Error",
    "RET": "Error",
    "TC": "Error",
    "ARG": "Error",
    "PTH": "Error",
    "E": "Error",
    "F": "Error",
    "PLE": "Error",
    "RUF": "Error",
    "TRY": "Error",
    # Warning
    "YTT": "Warning",
    "ANN": "Warning",
    "ASYNC": "Warning",
    "FBT": "Warning",
    "A": "Warning",
    "COM": "Warning",
    "C4": "Warning",
    "CPY": "Warning",
    "DJ": "Warning",
    "EXE": "Warning",
    "FIX": "Warning",
    "FA": "Warning",
    "INT": "Warning",
    "ISC": "Warning",
    "ICN": "Warning",
    "LOG": "Warning",
    "G": "Warning",
    "INP": "Warning",
    "PIE": "Warning",
    "T20": "Warning",
    "PYI": "Warning",
    "PT": "Warning",
    "Q": "Warning",
    "SLF": "Warning",
    "SIM": "Warning",
    "SLOT": "Warning",
    "TID": "Warning",
    "TD": "Warning",
    "I": "Warning",
    "C90": "Warning",
    "NPY": "Warning",
    "PD": "Warning",
    "N": "Warning",
    "PERF": "Warning",
    "W": "Warning",
    "DOC": "Warning",
    "D": "Warning",
    "PLC": "Warning",
    "PLR": "Warning",
    "PLW": "Warning",
    "UP": "Warning",
    "FURB": "Warning",
    # Info
    "AIR": "Info",
    "ERA": "Info",
    "FAST": "Info",
}

category_mapping = {
    "AIR": "Compatibility",
    "ERA": "UnusedCode",
    "FAST": "BestPractice",
    "YTT": "Compatibility",
    "ANN": "Documentation",
    "ASYNC": "BestPractice",
    "S": "Security",
    "BLE": "ErrorProne",
    "FBT": "CodeStyle",
    "B": "BestPractice",
    "A": "ErrorProne",
    "COM": "CodeStyle",
    "C4": "Performance",
    "CPY": "Documentation",
    "DTZ": "BestPractice",
    "T10": "UnusedCode",
    "DJ": "BestPractice",
    "EM": "CodeStyle",
    "EXE": "Compatibility",
    "FIX": "Documentation",
    "FA": "Compatibility",
    "INT": "BestPractice",
    "ISC": "CodeStyle",
    "ICN": "CodeStyle",
    "LOG": "BestPractice",
    "G": "CodeStyle",
    "INP": "Compatibility",
    "PIE": "BestPractice",
    "T20": "UnusedCode",
    "PYI": "CodeStyle",
    "PT": "BestPractice",
    "Q": "CodeStyle",
    "RSE": "ErrorProne",
    "RET": "BestPractice",
    "SLF": "ErrorProne",
    "SIM": "Complexity",
    "SLOT": "Performance",
    "TID": "BestPractice",
    "TD": "Documentation",
    "TC": "Compatibility",
    "ARG": "UnusedCode",
    "PTH": "BestPractice",
    "FLY": "CodeStyle",
    "I": "CodeStyle",
    "C90": "Complexity",
    "NPY": "BestPractice",
    "PD": "BestPractice",
    "N": "CodeStyle",
    "PERF": "Performance",
    "E": "ErrorProne",
    "W": "CodeStyle",
    "DOC": "Documentation",
    "D": "Documentation",
    "F": "ErrorProne",
    "PGH": "Security",
    "PLC": "CodeStyle",
    "PLE": "ErrorProne",
    "PLR": "Complexity",
    "PLW": "CodeStyle",
    "UP": "Compatibility",
    "FURB": "BestPractice",
    "RUF": "BestPractice",
    "TRY": "BestPractice",
}

enabled_rules = [
        "S101_assert",
        "S102_exec-builtin",
        "S103_bad-file-permissions",
        "S104_hardcoded-bind-all-interfaces",
        "S105_hardcoded-password-string",
        "S106_hardcoded-password-func-arg",
        "S107_hardcoded-password-default",
        "S108_hardcoded-temp-file",
        "S110_try-except-pass",
        "S112_try-except-continue",
        "S113_request-without-timeout",
        "S201_flask-debug-true",
        "S202_tarfile-unsafe-members",
        "S301_suspicious-pickle-usage",
        "S302_suspicious-marshal-usage",
        "S303_suspicious-insecure-hash-usage",
        "S304_suspicious-insecure-cipher-usage",
        "S305_suspicious-insecure-cipher-mode-usage",
        "S306_suspicious-mktemp-usage",
        "S307_suspicious-eval-usage",
        "S308_suspicious-mark-safe-usage",
        "S310_suspicious-url-open-usage",
        "S311_suspicious-non-cryptographic-random-usage",
        "S312_suspicious-telnet-usage",
        "S313_suspicious-xmlc-element-tree-usage",
        "S314_suspicious-xml-element-tree-usage",
        "S315_suspicious-xml-expat-reader-usage",
        "S316_suspicious-xml-expat-builder-usage",
        "S317_suspicious-xml-sax-usage",
        "S318_suspicious-xml-mini-dom-usage",
        "S319_suspicious-xml-pull-dom-usage",
        "S320_suspicious-xmle-tree-usage",
        "S321_suspicious-ftp-lib-usage",
        "S323_suspicious-unverified-context-usage",
        "S324_hashlib-insecure-hash-function",
        "S401_suspicious-telnetlib-import",
        "S402_suspicious-ftplib-import",
        "S403_suspicious-pickle-import",
        "S404_suspicious-subprocess-import",
        "S405_suspicious-xml-etree-import",
        "S406_suspicious-xml-sax-import",
        "S407_suspicious-xml-expat-import",
        "S408_suspicious-xml-minidom-import",
        "S409_suspicious-xml-pulldom-import",
        "S411_suspicious-xmlrpc-import",
        "S412_suspicious-httpoxy-import",
        "S413_suspicious-pycrypto-import",
        "S415_suspicious-pyghmi-import",
        "S501_request-with-no-cert-validation",
        "S502_ssl-insecure-version",
        "S503_ssl-with-bad-defaults",
        "S504_ssl-with-no-version",
        "S505_weak-cryptographic-key",
        "S506_unsafe-yaml-load",
        "S507_ssh-no-host-key-verification",
        "S508_snmp-insecure-version",
        "S509_snmp-weak-cryptography",
        "S601_paramiko-call",
        "S602_subprocess-popen-with-shell-equals-true",
        "S603_subprocess-without-shell-equals-true",
        "S604_call-with-shell-equals-true",
        "S605_start-process-with-a-shell",
        "S606_start-process-with-no-shell",
        "S607_start-process-with-partial-path",
        "S608_hardcoded-sql-expression",
        "S609_unix-command-wildcard-injection",
        "S610_django-extra",
        "S611_django-raw-sql",
        "S612_logging-config-insecure-listen",
        "S701_jinja2-autoescape-false",
        "S702_mako-templates",
        "B002_unary-prefix-increment-decrement",
        "B003_assignment-to-os-environ",
        "B004_unreliable-callable-check",
        "B005_strip-with-multi-characters",
        "B006_mutable-argument-default",
        "B007_unused-loop-control-variable",
        "B008_function-call-in-default-argument",
        "B009_get-attr-with-constant",
        "B010_set-attr-with-constant",
        "B011_assert-false",
        "B012_jump-statement-in-finally",
        "B013_redundant-tuple-in-exception-handler",
        "B014_duplicate-handler-exception",
        "B015_useless-comparison",
        "B016_raise-literal",
        "B017_assert-raises-exception",
        "B018_useless-expression",
        "B019_cached-instance-method",
        "B020_loop-variable-overrides-iterator",
        "B021_f-string-docstring",
        "B022_useless-contextlib-suppress",
        "B023_function-uses-loop-variable",
        "B024_abstract-base-class-without-abstract-method",
        "B025_duplicate-try-block-exception",
        "B026_star-arg-unpacking-after-keyword-arg",
        "B027_empty-method-without-abstract-decorator",
        "B028_no-explicit-stacklevel",
        "B029_except-with-empty-tuple",
        "B030_except-with-non-exception-classes",
        "B031_reuse-of-groupby-generator",
        "B032_unintentional-type-annotation",
        "B033_duplicate-value",
        "B034_re-sub-positional-args",
        "B035_static-key-dict-comprehension",
        "B039_mutable-contextvar-default",
        "B901_return-in-generator",
        "B903_class-as-data-structure",
        "B904_raise-without-from-inside-except",
        "B905_zip-without-explicit-strict",
        "B909_loop-iterator-mutation",
        "B911_batched-without-explicit-strict",
        "FA100_future-rewritable-type-annotation",
        "FA102_future-required-type-annotation",
        "C901_complex-structure",
        "E101_mixed-spaces-and-tabs",
        "E111_indentation-with-invalid-multiple",
        "E112_no-indented-block",
        "E113_unexpected-indentation",
        "E114_indentation-with-invalid-multiple-comment",
        "E115_no-indented-block-comment",
        "E116_unexpected-indentation-comment",
        "E117_over-indented",
        "E201_whitespace-after-open-bracket",
        "E202_whitespace-before-close-bracket",
        "E203_whitespace-before-punctuation",
        "E204_whitespace-after-decorator",
        "E211_whitespace-before-parameters",
        "E221_multiple-spaces-before-operator",
        "E222_multiple-spaces-after-operator",
        "E223_tab-before-operator",
        "E224_tab-after-operator",
        "E225_missing-whitespace-around-operator",
        "E226_missing-whitespace-around-arithmetic-operator",
        "E227_missing-whitespace-around-bitwise-or-shift-operator",
        "E228_missing-whitespace-around-modulo-operator",
        "E231_missing-whitespace",
        "E241_multiple-spaces-after-comma",
        "E242_tab-after-comma",
        "E251_unexpected-spaces-around-keyword-parameter-equals",
        "E252_missing-whitespace-around-parameter-equals",
        "E261_too-few-spaces-before-inline-comment",
        "E262_no-space-after-inline-comment",
        "E265_no-space-after-block-comment",
        "E266_multiple-leading-hashes-for-block-comment",
        "E271_multiple-spaces-after-keyword",
        "E272_multiple-spaces-before-keyword",
        "E273_tab-after-keyword",
        "E274_tab-before-keyword",
        "E275_missing-whitespace-after-keyword",
        "E301_blank-line-between-methods",
        "E302_blank-lines-top-level",
        "E303_too-many-blank-lines",
        "E304_blank-line-after-decorator",
        "E305_blank-lines-after-function-or-class",
        "E306_blank-lines-before-nested-definition",
        "E401_multiple-imports-on-one-line",
        "E402_module-import-not-at-top-of-file",
        "E501_line-too-long",
        "E502_redundant-backslash",
        "E701_multiple-statements-on-one-line-colon",
        "E702_multiple-statements-on-one-line-semicolon",
        "E703_useless-semicolon",
        "E711_none-comparison",
        "E712_true-false-comparison",
        "E713_not-in-test",
        "E714_not-is-test",
        "E721_type-comparison",
        "E722_bare-except",
        "E731_lambda-assignment",
        "E741_ambiguous-variable-name",
        "E742_ambiguous-class-name",
        "E743_ambiguous-function-name",
        "E902_io-error",
        "W191_tab-indentation",
        "W291_trailing-whitespace",
        "W292_missing-newline-at-end-of-file",
        "W293_blank-line-with-whitespace",
        "W391_too-many-newlines-at-end-of-file",
        "W505_doc-line-too-long",
        "W605_invalid-escape-sequence"
        ]

def get_category(rule_id):
    """Extracts the prefix (letters) from the rule ID and maps it to a category."""
    match = re.match(r"([A-Z]+)", rule_id)  # Extracts leading uppercase letters
    acronym = match.group(1) if match else "UNKNOWN"
    return category_mapping.get(
        acronym, "BestPractice"
    )  # Default to BestPractice if not found


def get_severity(rule_id):
    """Extracts the prefix (letters) from the rule ID and maps it to severity."""
    match = re.match(r"([A-Z]+)", rule_id)  # Extracts leading uppercase letters
    acronym = match.group(1) if match else "UNKNOWN"
    return severity_mapping.get(acronym, "Info")  # Default to Info if not found


def fetch_pattern_description(pattern_name, rule_id):
    """Fetches the description for a given pattern from the documentation."""
    try:
        pattern_url = f"{base_pattern_url}{pattern_name}/"
        response = requests.get(pattern_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            content = soup.find("main")
            if content:
                full_description = content.get_text(strip=False)
                relevant_lines = extract_relevant_lines(
                    full_description, pattern_name, rule_id
                )
                return "\n".join(relevant_lines)
            else:
                print(f"No content found for {pattern_name}")
                return f"# {pattern_name}\n\nDescription not available."
        else:
            print(
                f"Failed to fetch {pattern_name} page. Status code: {response.status_code}"
            )
            return f"# {pattern_name}\n\nFailed to fetch description."
    except Exception as e:
        print(f"Error fetching description for {pattern_name}: {e}")
        return f"# {pattern_name}\n\nError fetching description."


def extract_relevant_lines(full_description, pattern_name, rule_id):
    """Extracts relevant parts of the description."""
    start_marker = f"{pattern_name} ({rule_id})"
    end_markers = {"References", "Options", "Back to top"}
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
            elif line in {"What it does", "Why is this bad?", "Example", "Examples"}:
                relevant_lines.append(f"## {line}")
            elif previous_line in {"Example", "Examples", "Use instead:"}:
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


def save_to_markdown(pattern_name, content):
    """Saves the pattern description to a Markdown file."""
    output_dir = os.path.join(os.getcwd(), "docs", "descriptions")
    os.makedirs(output_dir, exist_ok=True)

    md_file_path = os.path.join(output_dir, f"{pattern_name}.md")
    with open(md_file_path, "w", encoding="utf-8") as md_file:
        md_file.write(content)

    print(f"Description for {pattern_name} written to {md_file_path}")


def main():
    """Main function to fetch patterns and generate files."""
    response = requests.get(base_pattern_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all("tr")

        patterns_data = []
        active_patterns = set()
        output_dir = os.path.join(os.getcwd(), "docs", "descriptions")
        os.makedirs(output_dir, exist_ok=True)

        for tr in rows:
            td_elements = tr.find_all("td")
            if len(td_elements) > 1:
                rule_id = td_elements[0].text.strip()
                pattern_link = td_elements[1].find("a")

                # Skip removed rules
                if tr.find("span", attrs={"title": "This rule has been removed"}):
                    print(f"Skipping removed rule: {rule_id}")
                    continue

                pattern_name = pattern_link.text.strip()
                pattern_id = f"{rule_id}_{pattern_name}"

                # Get severity based on rule acronym
                severity = get_severity(rule_id)
                category = get_category(rule_id)

                patterns_data.append(
                    {
                        "patternId": pattern_id,
                        "category": category,
                        "level": severity,
                        "enabled": True if pattern_id in enabled_rules else False,
                    }
                )

                active_patterns.add(f"{pattern_id}.md")

                # Fetch and save description
                description = fetch_pattern_description(pattern_name, rule_id)
                save_to_markdown(pattern_id, description)

        # Remove outdated files
        for filename in os.listdir(output_dir):
            if filename.endswith(".md") and filename not in active_patterns:
                file_path = os.path.join(output_dir, filename)
                print(f"Removing outdated file: {filename}")
                os.remove(file_path)

        # Save patterns.json
        output_data = {"name": "Codacy-Ruff", "patterns": patterns_data}

        output_file_path = os.path.join(os.getcwd(), "docs", "patterns.json")
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

        with open(output_file_path, "w") as json_file:
            json.dump(output_data, json_file, indent=4)

        print(f"Data successfully written to {output_file_path}")
    else:
        print(f"Failed to fetch page. Status code: {response.status_code}")


main()
