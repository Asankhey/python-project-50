# Difference Generator

[![hexlet-check](https://github.com/Asankhey/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Asankhey/python-project-50/actions/workflows/hexlet-check.yml)
[![CI](https://github.com/Asankhey/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/Asankhey/python-project-50/actions/workflows/ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/daed4b2aed51284a46a6/maintainability)](https://codeclimate.com/github/Asankhey/python-project-50)
[![Test Coverage](https://api.codeclimate.com/v1/badges/daed4b2aed51284a46a6/test_coverage)](https://codeclimate.com/github/Asankhey/python-project-50/test_coverage)

## Description

This CLI tool compares two configuration files and shows the difference.  
Supports JSON and YAML formats and outputs results in `stylish`, `plain`, or `json` formats.

## Usage

```bash
gendiff file1.json file2.yaml
gendiff --format plain file1.yaml file2.yaml
gendiff --format json file1.json file2.json
