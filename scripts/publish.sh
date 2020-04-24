#!/bin/bash
# DONT USE THIS UNLESS IT WORKS 100% (PR a fix if it doesn't work)

# Script for Unix-systems to publish the package
# Author: August (https://augu.dev)

# Sets the directory as a variable
$twine_installed=false
$directory=$(pwd -P)
$installed=false

# Check if Python is installed on the system
check_installation() {
  if python --version &> /dev/null; then
    echo 'Python is installed!'
    $installed = true
  else
    echo 'Missing Python! Exiting...'
    $installed = false
    exit 1
  fi
}

# Check if `twine` is installed
check_twine() {
  if python -m "import twine" &> /dev/null; then
    echo 'Twine is installed from PIP!'
    $twine_installed = true
  else
    echo 'Missing `twine` package! Installing from PIP...'
    pip install twine
  fi
}

# Start the process
start_process() {
  # Remove the cache directories
  remove_cache

  # Setup the package files
  python setup.py sdist
  twine upload dist/*

  echo 'Published!'
  exit 0
}

# Removes the azurlane.egg-info and the dist directory
remove_cache() {
  local EGG_CACHE_DIR = "$directory/azurlane.egg-info"
  local DIST_CACHE_DIR = "$directory/dist"

  if [ -d "$EGG_CACHE_DIR" ]; then
    rm -Rf $EGG_CACHE_DIR;
  fi

  if [ -d "$DIST_CACHE_DIR" ]; then
    rm -Rf $DIST_CACHE_DIR;
  fi
}

check_installation
check_twine
start_process