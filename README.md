# Codacy Ruff

Co-authored by @valeriupredoi

This is the docker engine we use at Codacy to have [Ruff](https://docs.astral.sh/ruff/) support.
You can also create a docker to integrate the tool and language of your choice!
See the [codacy-engine-scala-seed](https://github.com/codacy/codacy-engine-scala-seed) repository for more information.

## Python compatibility
Ruff is compatible with Python 3.13

## Usage

You can create the docker by doing:

  ```bash
  docker build --no-cache -t codacy-ruff:latest .
  ```

The docker is ran with the following command:

  ```bash
  docker run -it -v $srcDir:/src codacy-ruff:latest
  ```

## Generate Docs

 1. Update the version in `requirements.txt`

 2. Run the DocGenerator to update all the patterns/descriptions and the patterns.xml (from all-patterns test)

    ```bash
    python<version> src/doc_generator.py
    ```

## Test

We use the [codacy-plugins-test](https://github.com/codacy/codacy-plugins-test) to test our external tools integration.
You can follow the instructions there to make sure your tool is working as expected.

## What is Codacy?

[Codacy](https://www.codacy.com/) is an Automated Code Review Tool that monitors your technical debt, helps you improve your code quality, teaches best practices to your developers, and helps you save time in Code Reviews.

### Among Codacy’s features:

 - Identify new Static Analysis issues
 - Commit and Pull Request Analysis with GitHub, BitBucket/Stash, GitLab (and also direct git repositories)
 - Auto-comments on Commits and Pull Requests
 - Integrations with Slack, HipChat, Jira, YouTrack
 - Track issues in Code Style, Security, Error Proneness, Performance, Unused Code and other categories

Codacy also helps keep track of Code Coverage, Code Duplication, and Code Complexity.

Codacy supports PHP, Python, Ruby, Java, JavaScript, and Scala, among others.

### Free for Open Source

Codacy is free for Open Source projects.