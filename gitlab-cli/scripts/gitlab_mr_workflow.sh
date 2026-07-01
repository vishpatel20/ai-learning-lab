#!/bin/bash

# GitLab Merge Request Workflow Demo
# Purpose: Common merge request commands using glab

echo "Checking GitLab authentication..."
glab auth status

echo "Listing open merge requests..."
glab mr list

echo "Common MR commands:"
echo "glab mr create"
echo "glab mr view <mr-id>"
echo "glab mr checkout <mr-id>"
echo "glab mr merge <mr-id>"