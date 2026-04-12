# Findings Report — Apache Log Analysis

## 1. Failed Login Attempts
I searched for requests to `/login` that returned a 401 status. These usually mean the user was not authorized, which could be a failed login attempt.

There were multiple results, which could suggest repeated login failures.

---

## 2. Service Errors
I found many 503 status codes in the logs. A 503 usually means the service is unavailable.

These errors showed up across different pages like `/search`, `/cart`, and `/orderstatus`, so it might not just be one page having issues.

---

## 3. Traffic Patterns
I looked at which IP addresses were making the most requests.

Some IPs had a much higher count than others, which could be normal traffic or something to look into more.

---

## 4. Working with Raw Data
The log data was not automatically split into fields, so I used `rex` to extract things like:
- IP address
- status code
- URI

This made it easier to search and analyze.

---

## 5. What I Learned
- How to search logs in Splunk
- How to extract fields from raw data
- How to identify errors like 401 and 503
- How to break down traffic by IP and endpoint

---

## Conclusion
This lab helped me understand how to analyze web logs and find possible issues like failed logins and service outages using Splunk.
