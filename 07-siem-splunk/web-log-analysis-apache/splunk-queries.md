# Splunk Queries — Apache Log Analysis

## Status Code Overview
Shows how many times each status code appears.

```spl
index=main
| rex " (?<status>\d{3}) "
| stats count by status

## Failed Login Attempts
Filters for login requests that returned a 401.

index=main "/login"
| rex "^(?<ip>\S+)"
| rex " (?<status>\d{3}) "
| search status=401

## Failed Attempts by IP
Counts how many failed login attempts each IP made.

index=main "/login"
| rex "^(?<ip>\S+)"
| rex " (?<status>\d{3}) "
| search status=401
| stats count by ip
| sort - count

## Service Errors (503)
Finds all service unavailable errors.

index=main
| rex " (?<status>\d{3}) "
| search status=503

## 503 Errors by Page
Shows which pages had the most 503 errors.

index=main
| rex " (?<status>\d{3}) "
| rex "\"(?:GET|POST) (?<uri>\S+)"
| search status=503
| stats count by uri
| sort - count

## Top IP Addresses
Shows which IPs made the most requests.

index=main
| rex "^(?<ip>\S+)"
| stats count by ip
| sort - count

## Combined Errors
Shows IPs that had either 401 or 503 errors.

index=main
| rex "^(?<ip>\S+)"
| rex " (?<status>\d{3}) "
| search status=401 OR status=503
| stats count by ip, status
