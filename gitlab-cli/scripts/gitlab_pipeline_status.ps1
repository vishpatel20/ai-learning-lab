# GitLab Pipeline Status Script
# Purpose: Check recent GitLab pipelines using glab

Write-Host "Checking GitLab authentication..."
glab auth status

Write-Host "Listing recent pipelines..."
glab pipeline list

Write-Host "Viewing pipeline details..."
glab ci viewss