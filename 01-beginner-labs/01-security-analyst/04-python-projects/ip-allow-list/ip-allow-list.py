allowed_ips = ["10.0.0.1", "10.0.0.2"]
ip = "10.0.0.5"

if ip in allowed_ips:
    print("Access allowed")
else:
    print("Access denied")

