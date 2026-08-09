A Cloudflare-style WAF evaluates its rules top to bottom. The first rule that matches and is terminal decides the request. Work out what actually reaches the origin.

Evaluation semantics
BLOCK, CHALLENGE and SKIP are terminal — evaluation stops.
LOG is not terminal — evaluation continues to the next rule.
If no terminal rule matches, the request is allowed.
A request reaches the origin only if the outcome is SKIP or allowed. CHALLENGE does not reach the origin.
eq/ne are exact, contains/starts_with are substring and prefix, in {…} is exact membership, lt/gt are strict.
Parentheses show precedence explicitly; not binds to the expression that follows it.
Rules (in order)
 1. LOG       ip.geoip.country in {"US" "BR"}
 2. BLOCK     cf.bot_management.score lt 30
 3. BLOCK     (http.request.uri.path starts_with "/admin" and not ip.src in {"203.0.113.13" "198.51.100.25"})
 4. BLOCK     http.user_agent contains "curl"
 5. BLOCK     (http.request.method eq "POST" and not http.request.headers["origin"][0] eq "https://app-326.example")
 6. LOG       cf.threat_score gt 49
 7. BLOCK     http.user_agent contains "python-httpx"
 8. CHALLENGE (http.request.uri.path starts_with "/api" and cf.bot_management.score lt 40)
 9. SKIP      http.request.uri.path starts_with "/assets/"
10. CHALLENGE (http.request.uri.path eq "/login" and cf.threat_score gt 25)
11. LOG       http.request.method eq "GET"
12. BLOCK     (http.request.uri.path contains "/.git" or http.request.uri.path contains "/.env")
13. LOG       ip.geoip.country in {"IN" "SG"}
14. BLOCK     (http.request.uri.path starts_with "/admin" and not ip.src in {"203.0.113.13" "198.51.100.25"})
15. SKIP      cf.bot_management.verified_bot eq true
16. BLOCK     http.user_agent contains "curl"
17. BLOCK     (http.request.method eq "POST" and not http.request.headers["origin"][0] eq "https://app-326.example")
18. LOG       cf.threat_score gt 57
19. BLOCK     http.user_agent contains "python-httpx"
20. SKIP      http.request.uri.path starts_with "/assets/"
21. CHALLENGE (http.request.uri.path eq "/login" and cf.threat_score gt 22)
22. LOG       http.request.method eq "GET"
23. BLOCK     (http.request.uri.path contains "/.git" or http.request.uri.path contains "/.env")
24. LOG       ip.geoip.country in {"DE" "IN"}
25. BLOCK     (http.request.uri.path starts_with "/admin" and not ip.src in {"203.0.113.13" "198.51.100.25"})
26. BLOCK     http.user_agent contains "curl"
27. BLOCK     (http.request.method eq "POST" and not http.request.headers["origin"][0] eq "https://app-326.example")
28. LOG       cf.threat_score gt 57
29. BLOCK     http.user_agent contains "python-httpx"
30. SKIP      http.request.uri.path starts_with "/assets/"
31. CHALLENGE (http.request.uri.path eq "/login" and cf.threat_score gt 29)
32. LOG       http.request.method eq "GET"
33. BLOCK     (http.request.uri.path contains "/.git" or http.request.uri.path contains "/.env")
Requests (60)

[
 {
  "id": "req-01",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 38,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "203.0.113.13",
  "country": "DE",
  "threatScore": 19
 },
 {
  "id": "req-02",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 10,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "102.29.243.16",
  "country": "SG",
  "threatScore": 42
 },
 {
  "id": "req-03",
  "method": "POST",
  "path": "/api/v2/search",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 13,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "45.98.149.235",
  "country": "US",
  "threatScore": 28
 },
 {
  "id": "req-04",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 65,
  "verifiedBot": true,
  "origin": "https://app-326.example",
  "ip": "203.0.113.13",
  "country": "SG",
  "threatScore": 44
 },
 {
  "id": "req-05",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 99,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "140.52.226.71",
  "country": "BR",
  "threatScore": 13
 },
 {
  "id": "req-06",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "UptimeMonitor/1.2",
  "botScore": 91,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "116.161.163.61",
  "country": "SG",
  "threatScore": 34
 },
 {
  "id": "req-07",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "curl/8.6.0",
  "botScore": 5,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "30.183.101.91",
  "country": "US",
  "threatScore": 28
 },
 {
  "id": "req-08",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "UptimeMonitor/1.2",
  "botScore": 75,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "198.1.16.126",
  "country": "DE",
  "threatScore": 10
 },
 {
  "id": "req-09",
  "method": "POST",
  "path": "/login",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 5,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "116.216.255.153",
  "country": "US",
  "threatScore": 9
 },
 {
  "id": "req-10",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 7,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "49.113.73.47",
  "country": "US",
  "threatScore": 39
 },
 {
  "id": "req-11",
  "method": "GET",
  "path": "/blog/post",
  "ua": "UptimeMonitor/1.2",
  "botScore": 81,
  "verifiedBot": false,
  "origin": "",
  "ip": "148.44.164.219",
  "country": "US",
  "threatScore": 33
 },
 {
  "id": "req-12",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 17,
  "verifiedBot": false,
  "origin": "",
  "ip": "102.193.188.115",
  "country": "US",
  "threatScore": 53
 },
 {
  "id": "req-13",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "curl/8.6.0",
  "botScore": 96,
  "verifiedBot": true,
  "origin": "https://evil-14.example",
  "ip": "177.124.149.195",
  "country": "IN",
  "threatScore": 28
 },
 {
  "id": "req-14",
  "method": "GET",
  "path": "/login",
  "ua": "curl/8.6.0",
  "botScore": 12,
  "verifiedBot": true,
  "origin": "https://app-326.example",
  "ip": "124.182.145.124",
  "country": "DE",
  "threatScore": 44
 },
 {
  "id": "req-15",
  "method": "GET",
  "path": "/",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 99,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "126.54.224.199",
  "country": "IN",
  "threatScore": 3
 },
 {
  "id": "req-16",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 82,
  "verifiedBot": false,
  "origin": "",
  "ip": "84.213.236.249",
  "country": "IN",
  "threatScore": 11
 },
 {
  "id": "req-17",
  "method": "GET",
  "path": "/login",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 16,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "11.33.55.149",
  "country": "BR",
  "threatScore": 41
 },
 {
  "id": "req-18",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "UptimeMonitor/1.2",
  "botScore": 54,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "203.0.113.13",
  "country": "IN",
  "threatScore": 54
 },
 {
  "id": "req-19",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 67,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "14.240.82.9",
  "country": "IN",
  "threatScore": 19
 },
 {
  "id": "req-20",
  "method": "GET",
  "path": "/",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 45,
  "verifiedBot": false,
  "origin": "",
  "ip": "126.87.75.120",
  "country": "BR",
  "threatScore": 23
 },
 {
  "id": "req-21",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "python-httpx/0.28.1",
  "botScore": 8,
  "verifiedBot": false,
  "origin": "",
  "ip": "80.41.177.59",
  "country": "DE",
  "threatScore": 8
 },
 {
  "id": "req-22",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 71,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "92.155.118.172",
  "country": "SG",
  "threatScore": 47
 },
 {
  "id": "req-23",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "UptimeMonitor/1.2",
  "botScore": 36,
  "verifiedBot": true,
  "origin": "https://app-326.example",
  "ip": "104.44.59.176",
  "country": "SG",
  "threatScore": 6
 },
 {
  "id": "req-24",
  "method": "GET",
  "path": "/login",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 27,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "17.226.180.86",
  "country": "BR",
  "threatScore": 35
 },
 {
  "id": "req-25",
  "method": "GET",
  "path": "/",
  "ua": "python-httpx/0.28.1",
  "botScore": 34,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "12.225.66.231",
  "country": "DE",
  "threatScore": 42
 },
 {
  "id": "req-26",
  "method": "GET",
  "path": "/blog/post",
  "ua": "curl/8.6.0",
  "botScore": 37,
  "verifiedBot": false,
  "origin": "https://evil-95.example",
  "ip": "198.51.100.25",
  "country": "SG",
  "threatScore": 12
 },
 {
  "id": "req-27",
  "method": "GET",
  "path": "/blog/post",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 16,
  "verifiedBot": false,
  "origin": "https://evil-57.example",
  "ip": "37.98.55.113",
  "country": "DE",
  "threatScore": 16
 },
 {
  "id": "req-28",
  "method": "GET",
  "path": "/",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 91,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "107.115.151.157",
  "country": "IN",
  "threatScore": 25
 },
 {
  "id": "req-29",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "python-httpx/0.28.1",
  "botScore": 47,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "203.0.113.13",
  "country": "DE",
  "threatScore": 16
 },
 {
  "id": "req-30",
  "method": "POST",
  "path": "/login",
  "ua": "curl/8.6.0",
  "botScore": 8,
  "verifiedBot": true,
  "origin": "https://app-326.example",
  "ip": "154.36.114.119",
  "country": "SG",
  "threatScore": 7
 },
 {
  "id": "req-31",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 21,
  "verifiedBot": true,
  "origin": "",
  "ip": "72.143.45.93",
  "country": "IN",
  "threatScore": 55
 },
 {
  "id": "req-32",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "UptimeMonitor/1.2",
  "botScore": 86,
  "verifiedBot": false,
  "origin": "https://evil-57.example",
  "ip": "45.136.169.115",
  "country": "SG",
  "threatScore": 0
 },
 {
  "id": "req-33",
  "method": "GET",
  "path": "/blog/post",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 15,
  "verifiedBot": true,
  "origin": "",
  "ip": "66.249.72.157",
  "country": "US",
  "threatScore": 1
 },
 {
  "id": "req-34",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "UptimeMonitor/1.2",
  "botScore": 40,
  "verifiedBot": false,
  "origin": "",
  "ip": "22.12.141.132",
  "country": "IN",
  "threatScore": 14
 },
 {
  "id": "req-35",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "UptimeMonitor/1.2",
  "botScore": 19,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "203.0.113.13",
  "country": "IN",
  "threatScore": 4
 },
 {
  "id": "req-36",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "python-httpx/0.28.1",
  "botScore": 24,
  "verifiedBot": false,
  "origin": "",
  "ip": "196.122.249.42",
  "country": "BR",
  "threatScore": 23
 },
 {
  "id": "req-37",
  "method": "GET",
  "path": "/",
  "ua": "UptimeMonitor/1.2",
  "botScore": 11,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "17.75.158.134",
  "country": "BR",
  "threatScore": 13
 },
 {
  "id": "req-38",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "curl/8.6.0",
  "botScore": 47,
  "verifiedBot": false,
  "origin": "",
  "ip": "203.0.113.13",
  "country": "BR",
  "threatScore": 25
 },
 {
  "id": "req-39",
  "method": "GET",
  "path": "/",
  "ua": "python-httpx/0.28.1",
  "botScore": 18,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "203.0.113.13",
  "country": "IN",
  "threatScore": 53
 },
 {
  "id": "req-40",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "python-httpx/0.28.1",
  "botScore": 83,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "170.54.125.57",
  "country": "IN",
  "threatScore": 21
 },
 {
  "id": "req-41",
  "method": "GET",
  "path": "/login",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 78,
  "verifiedBot": false,
  "origin": "https://evil-70.example",
  "ip": "203.0.113.13",
  "country": "DE",
  "threatScore": 52
 },
 {
  "id": "req-42",
  "method": "GET",
  "path": "/login",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 41,
  "verifiedBot": false,
  "origin": "https://evil-43.example",
  "ip": "203.0.113.13",
  "country": "US",
  "threatScore": 33
 },
 {
  "id": "req-43",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "python-httpx/0.28.1",
  "botScore": 54,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "203.0.113.13",
  "country": "US",
  "threatScore": 45
 },
 {
  "id": "req-44",
  "method": "GET",
  "path": "/blog/post",
  "ua": "python-httpx/0.28.1",
  "botScore": 67,
  "verifiedBot": false,
  "origin": "",
  "ip": "163.168.215.16",
  "country": "BR",
  "threatScore": 18
 },
 {
  "id": "req-45",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "UptimeMonitor/1.2",
  "botScore": 13,
  "verifiedBot": false,
  "origin": "https://evil-88.example",
  "ip": "133.166.92.199",
  "country": "IN",
  "threatScore": 46
 },
 {
  "id": "req-46",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 35,
  "verifiedBot": false,
  "origin": "https://evil-95.example",
  "ip": "168.189.189.162",
  "country": "SG",
  "threatScore": 46
 },
 {
  "id": "req-47",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "curl/8.6.0",
  "botScore": 84,
  "verifiedBot": true,
  "origin": "",
  "ip": "163.110.144.210",
  "country": "BR",
  "threatScore": 53
 },
 {
  "id": "req-48",
  "method": "GET",
  "path": "/",
  "ua": "python-httpx/0.28.1",
  "botScore": 51,
  "verifiedBot": false,
  "origin": "https://evil-52.example",
  "ip": "106.216.91.177",
  "country": "BR",
  "threatScore": 29
 },
 {
  "id": "req-49",
  "method": "POST",
  "path": "/",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 1,
  "verifiedBot": false,
  "origin": "",
  "ip": "36.215.53.190",
  "country": "DE",
  "threatScore": 13
 },
 {
  "id": "req-50",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 66,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "28.131.67.4",
  "country": "US",
  "threatScore": 25
 },
 {
  "id": "req-51",
  "method": "GET",
  "path": "/login",
  "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/17.4",
  "botScore": 80,
  "verifiedBot": false,
  "origin": "https://evil-60.example",
  "ip": "187.252.224.196",
  "country": "IN",
  "threatScore": 16
 },
 {
  "id": "req-52",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "curl/8.6.0",
  "botScore": 51,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "18.10.25.58",
  "country": "IN",
  "threatScore": 24
 },
 {
  "id": "req-53",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "curl/8.6.0",
  "botScore": 21,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "203.0.113.13",
  "country": "BR",
  "threatScore": 51
 },
 {
  "id": "req-54",
  "method": "POST",
  "path": "/assets/logo.svg",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 85,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "198.51.100.25",
  "country": "IN",
  "threatScore": 26
 },
 {
  "id": "req-55",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "Googlebot/2.1 (+http://www.google.com/bot.html)",
  "botScore": 31,
  "verifiedBot": false,
  "origin": "https://evil-30.example",
  "ip": "123.110.176.164",
  "country": "US",
  "threatScore": 35
 },
 {
  "id": "req-56",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "curl/8.6.0",
  "botScore": 40,
  "verifiedBot": true,
  "origin": "",
  "ip": "76.46.35.239",
  "country": "BR",
  "threatScore": 43
 },
 {
  "id": "req-57",
  "method": "GET",
  "path": "/assets/logo.svg",
  "ua": "UptimeMonitor/1.2",
  "botScore": 90,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "198.51.100.25",
  "country": "SG",
  "threatScore": 18
 },
 {
  "id": "req-58",
  "method": "GET",
  "path": "/api/v2/items",
  "ua": "UptimeMonitor/1.2",
  "botScore": 19,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "181.78.213.187",
  "country": "IN",
  "threatScore": 12
 },
 {
  "id": "req-59",
  "method": "GET",
  "path": "/api/v2/search",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0",
  "botScore": 31,
  "verifiedBot": false,
  "origin": "https://app-326.example",
  "ip": "203.0.113.13",
  "country": "US",
  "threatScore": 58
 },
 {
  "id": "req-60",
  "method": "GET",
  "path": "/admin/settings",
  "ua": "UptimeMonitor/1.2",
  "botScore": 68,
  "verifiedBot": true,
  "origin": "https://app-326.example",
  "ip": "39.143.213.11",
  "country": "SG",
  "threatScore": 46
 }
]
      
Answer all three parts
How many of the 60 requests reach the origin under the rules exactly as listed?
Swap rule 8 and rule 15 (they exchange positions; every other rule keeps its relative order). Exactly one request changes between reaching the origin and not. Give its id.
Rule 2 blocks low-scoring clients without exempting verified bots such as search-engine crawlers. In the original order, rewrite that rule as (<original expression> and not cf.bot_management.verified_bot), leave every other rule unchanged, and report how many requests then reach the origin.
Answer as count|request-id|count — for example 17|req-42|19