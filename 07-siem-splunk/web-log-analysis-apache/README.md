# Splunk Web Log Investigation: Unauthorized Access and Service Issues

## Overview
In this lab, I used Splunk to look at Apache web logs. The goal was to find failed login attempts, check for any errors, and understand general traffic patterns.

---

## Objectives
- Find failed access attempts (401 errors)
- Look for service issues (503 errors)
- See which IP addresses are most active
- Practice using Splunk search and basic field extraction

---

## Tools Used
- Splunk (Search & Reporting)
- Apache access log file

---

## What I Did
- Uploaded a log file into Splunk
- Used search queries to filter data
- Created fields using `rex` because the data was not parsed automatically
- Looked for patterns in login activity and errors

---

## Key Observations
- Found multiple 401 errors on `/login`, which likely means failed login attempts
- Found a lot of 503 errors across different pages, which could mean the site had issues or was down for a period of time
- Identified some IP addresses making a lot of requests

---

## Screenshots
Screenshots are included in the `/screenshots` folder showing each step of the analysis.

---

## Project Structure
