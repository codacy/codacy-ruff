import os
import sys
import json
import jsonpickle
import subprocess
import glob
import signal
from contextlib import contextmanager
import traceback
from pathlib import Path
import toml
import fnmatch


@contextmanager
def timeout(time):
    # Register a function to raise a TimeoutError on the signal.
    signal.signal(signal.SIGALRM, lambda: sys.exit(2))
    # Schedule the signal to be sent after ``time``.
    signal.alarm(time)
    yield


DEFAULT_TIMEOUT = 15 * 60


def getTimeout(timeoutString):
    if not timeoutString.isdigit():
        return DEFAULT_TIMEOUT
    return int(timeoutString)


class Result:
    # result need be formatted as JSON
    # expected = '{"filename": "file.py",
    #              "message": "message",
    #              "patternId": "id", "line": 80}'
    def __init__(self, filename, message, patternId, line):
        self.filename = filename
        self.message = message
        self.patternId = patternId
        self.line = line

    def __str__(self):
        return f"Result({self.filename},{self.message},{self.patternId},{self.line})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, o):
        return (
            self.filename == o.filename,
            self.message == o.message,
            self.patternId == o.patternId,
            self.line == o.line,
        )


def toJson(obj):
    return jsonpickle.encode(obj, unpicklable=False)


def readJsonFile(path):
    with open(path, "r", encoding="utf-8") as file:
        res = json.loads(file.read())
    return res


def run_ruff(options, files, cwd=None, configFile=None):
    if configFile is not None:
        cmd = ["ruff", "check", "--output-format=json", "--no-cache", "--config", configFile]
        cmd = cmd + files
    else:
        cmd = ["ruff", "check", "--output-format=json", "--no-cache",]
        cmd = cmd + options + files

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=cwd)
    stdout = process.communicate()[0]
    result = stdout.decode("utf-8")

    return result


def chunks(lst, n):
    return [lst[i : i + n] for i in range(0, len(lst), n)]


def run_ruff_parsed(configFile, options, files, cwd):
    results = []
    res = run_ruff(options, files, cwd, configFile)
    ruff_dicts = json.loads(res)
    # a ruff_dict contains standardized keys:
    # {  'cell': None,
    #    'code': 'F401',
    #    'end_location': {'column': 17, 'row': 3},
    #    'filename': '/home/valeriu/codacy-ruff/src/codacy_ruff.py',
    #    'fix': {'applicability': 'safe', 'edits': [{'content': '',
    #            'end_location': {'column': 1, 'row': 4},
    #            'location': {'column': 1, 'row': 3}}],
    #            'message': 'Remove unused import: `itertools`'},
    #    'location': {'column': 8, 'row': 3},
    #    'message': '`itertools` imported but unused',
    #    'noqa_row': 3,
    #    'url': 'https://docs.astral.sh/ruff/rules/unused-import'
    # }
    for res in ruff_dicts:
        if res["code"] != "failure" and res["code"] != "import-error":
            filename = res["filename"]
            message = f"{res['message']} ({res['code']})"
            patternId = f"{res['code']}_{res['url'].split('/')[-1] if res.get('url') else ''}"
            line = res["end_location"]["row"]
            results.append(Result(filename, message, patternId, line))
    
    return results


def walkDirectory(directory):
    def generate():
        for filename in glob.iglob(os.path.join(directory, "**/*.py"), recursive=True):
            res = os.path.relpath(filename, directory)
            yield res

    return list(generate())


def readConfiguration(configFile, srcDir):
    def allFiles():
        return walkDirectory(srcDir)

    try:
        configuration = readJsonFile(configFile)
        files = configuration.get("files") or allFiles()
        tools = [t for t in configuration["tools"] if t["name"] == "ruff"]
        if tools and "patterns" in tools[0]:
            ruff = tools[0]
            tools = set([p["patternId"] for p in ruff.get("patterns") or []])
            options = []
        else:
            options = []

    except Exception:
        files = allFiles()
        options = []
    return (options, [f for f in files])


def find_ruff_configFile(srcDir):
    config_files = {"pyproject.toml", "ruff.toml", ".ruff.toml"}
    root_files = list(Path(srcDir).iterdir())  # List only root directory files

    for file in root_files:
        if file.name in config_files and file.is_file():
            return str(file)

    return None  # Return None if no config file is found

def get_patterns_from_configFile(config_path):
    """Load the Ruff configuration and extract 'exclude' and 'include' patterns."""
    config = toml.load(config_path)
    tool_config = config.get("tool", {}).get("ruff", {})
    
    exclude_patterns = tool_config.get("exclude", [])
    include_patterns = tool_config.get("include", [])
    
    return exclude_patterns, include_patterns

def filter_files(files, include_patterns, exclude_patterns):
    """Filter files based on include and exclude glob patterns."""
    
    if exclude_patterns:
        files = [f for f in files if not any(fnmatch.fnmatch(f, pat) for pat in exclude_patterns)]
    if include_patterns:
        files = [f for f in files if any(fnmatch.fnmatch(f, pat) for pat in include_patterns)]
    return files

def run_tool(configFile, srcDir):
    (options, files) = readConfiguration(configFile, srcDir)
    res = []
    filesWithPath = [os.path.join(f) for f in files]
    toolConfigFile = find_ruff_configFile(srcDir)
    
    # When we run Ruff Check command with files, all exclude/include patterns from the
    # Configuration file is not considered, so we need to filter them somehow
    (exclude, include) = get_patterns_from_configFile(toolConfigFile) if toolConfigFile else ([], [])

    # Apply filtering
    filesWithPath = filter_files(filesWithPath, include, exclude)

    for chunk in chunks(filesWithPath, 10):
        res.extend(run_ruff_parsed(toolConfigFile, options, chunk, srcDir))

    for result in res:
        
        if result.filename.startswith(srcDir):
            result.filename = os.path.relpath(result.filename, srcDir)
    
    return res


def results_to_json(results):
    return os.linesep.join([toJson(res) for res in results])


if __name__ == "__main__":
    with timeout(getTimeout(os.environ.get("TIMEOUT_SECONDS") or "")):
        try:
            results = run_tool("/.codacyrc", "/src")     
            results = results_to_json(results)
            print(results)
        except Exception:
            traceback.print_exc()
            sys.exit(1)
