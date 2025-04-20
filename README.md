# Difference Generator

[![hexlet-check](https://github.com/Asankhey/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Asankhey/python-project-50/actions/workflows/hexlet-check.yml)
[![CI](https://github.com/Asankhey/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/Asankhey/python-project-50/actions/workflows/ci.yml)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=Asankhey_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Asankhey_python-project-50)
[![Test Coverage](https://api.codeclimate.com/v1/badges/daed4b2aed51284a46a6/test_coverage)](https://codeclimate.com/github/Asankhey/python-project-50/test_coverage)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=Asankhey_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Asankhey_python-project-50)

## Description

This CLI tool compares two configuration files and shows the difference.  
Supports JSON and YAML formats and outputs results in `stylish`, `plain`, or `json` formats.

## Usage

```bash
gendiff file1.json file2.yaml
gendiff --format plain file1.yaml file2.yaml
gendiff --format json file1.json file2.json

## Demo

[![asciicast](https://asciinema.org/a/YLoy8kE0Vz5TZ5HYvi9uDLtIo.svg)](https://asciinema.org/a/YLoy8kE0Vz5TZ5HYvi9uDLtIo)