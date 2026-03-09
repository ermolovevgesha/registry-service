# Overview
A REST API emulating a registry for exchanging documents with external system A. Documents are signed with an electronic digital signature (emulation) and stored in a blockchain-like structure (in-memory storage).

# Technology Stack and Features
- FastAPI
- SQLAlchemy
-  Docker Compose
- SQLite
- Pydantic
- Alembic

# Installation
Clone this repository to your local machine:
```bash
git clone https://github.com/ermolovevgesha/registry-service

```

Run the following in the terminal from the project root folder:
```bash
docker compose up -d
```

# API Endpoints
## Checking service availability
```
GET /api/health
```

Checks if the API is working:
```bash
curl -X 'GET' \
  'http://localhost:8000/api/health' \
  -H 'accept: application/json'
```

## Receiving incoming messages
```
POST /api/messages/outgoing
```
Returns a list of transactions with messages addressed to System A for the specified
period:
```bash
curl -X 'POST' \
  'http://localhost:8000/api/messages/outgoing' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Data": "eyJTdGFydERhdGUiOiAiMjAyNC0wMS0wMVQwMDowMDowMFoiLCAiRW5kRGF0ZSI6ICIyMDI2LTEyLTMxVDIzOjU5OjU5WiIsICJMaW1pdCI6IDEwLCAiT2Zmc2V0IjogMH0=",
  "Sign": "MTlGOEI3QTJDOEE3NDAzNUJERTBBRjRCMTY1MjIzNDREREIyM0E1ODVBRTdEMjFEQjQ4N0ZBNTdGNkEyRjM3Ng==",
  "SignerCert": "string"
}'

```

## Sending messages to the registry
```
POST /api/messages/incoming
```

Sends new messages from System A to System B:
```bash
curl -X 'POST' \
  'http://localhost:8000/api/messages/incoming' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Data": "eyJUcmFuc2FjdGlvbnMiOiBbewogICAgIlRyYW5zYWN0aW9uVHlwZSI6IDksCiAgICAiRGF0YSI6ICJld29nSUNKRVlYUmhJam9nSW1WM2IyZEpRMHBQV1ZjeGJFbHFiMmRKZEVObE1FbzNVVzVwUVc0d1NpOVJkblJETnpCWlVGSm9PVU4zTUZsTVVYUmtRemN3V1hkdVNXbDNTMGxEUVdsUmJVWjFZVEJrTVZsWVNtaGlibEpzV2xWb2FHTXlaMmxQYVVGcFRsVlJNbEpxYUVaTmEwVjRVWHBPUTA5VldUQlNSR1JHVDBWRmVWRjZWa05OVlZGNlVtcGFSazlGUlRWUmVrcEZUa1ZaTWxGVWFFTk5WVTE2VWxSV1IwNHdSVFZTUkVwRFRrVk5NbEpVYUVkTlJVVjRTV2wzUzBsRFFXbFZNbXh1WW1sSk5rbERTbXBOYlhoMVdXMHhSMDFIVWxsVGJYaFpUV3haTUZkV1kzaGtNa3BJVmxRd2FVeEJiMmRKUTBwVVlWZGtkVnBZU2tSYVdFb3dTV3B2WjBsc1ZYaGlSbEpYVWxaYVQxZEVRa1pRVTBsTFpsRnZQU0lzQ2lBZ0lsTmxibVJsY2tKeVlXNWphQ0k2SUNKVFdWTlVSVTFmUVNJc0NpQWdJbEpsWTJWcGRtVnlRbkpoYm1Ob0lqb2dJbE5aVTFSRlRWOUNJaXdLSUNBaVNXNW1iMDFsYzNOaFoyVlVlWEJsSWpvZ01qQXlMQW9nSUNKTlpYTnpZV2RsVkdsdFpTSTZJQ0l5TURJMExUQTFMVEl3VkRFd09qQTFPakF3V2lJc0NpQWdJa05vWVdsdVIzVnBaQ0k2SUNJMU5UQmxPRFF3TUMxbE1qbGlMVFF4WkRRdFlUY3hOaTAwTkRZMk5UVTBOREF3TURBaUxBb2dJQ0pRY21WMmFXOTFjMVJ5WVc1ellXTjBhVzl1U0dGemFDSTZJQ0k0TnpBMU9FSkZOREJCUXpkQ1JEUTRSalZCTTBNMVF6VTNPRU00TVVZNE5VSXdOREUxUWpVM056YzVPVGs1UVVZNU5UTkZPVE5DTVVFd1F6VTNRalJCSWl3S0lDQWlUV1YwWVdSaGRHRWlPaUFpMEtMUXRkR0IwWUxRdnRDeTBMN1F0U0RSZ2RDKzBMN1FzZEdKMExYUXZkQzQwTFVpQ24wPSIsCiAgICAiSGFzaCI6ICIxQkE5QzlCRENGM0ZEMDU2NDlEQTZENUJGN0ZCQTUzMERDN0IwOTFEOTQzNTZBQTkzNzRCMzE5NENBRjQ2MEEyIiwKICAgICJTaWduIjogIiIsCiAgICAiU2lnbmVyQ2VydCI6ICJVMVpUVEVWTlgwRWlMQyIsCiAgICAiVHJhbnNhY3Rpb25UaW1lIjogIjIwMjQtMDUtMjBUMTE6MzA6MDBaIgogIH1dLAoiQ291bnQiIDogMQp9=",
  "Sign": "MEQzNDdFNzVCMDg1Nzc2RDNCODM5NjRFMUIxRjY5OEFEMDExOUJCQ0IwNzYwRTg0MEUwMDFBMzgwMDQ1NUU5Nw==",
  "SignerCert": "string"
}'
```

# Structure
```text
.
├── pyproject.toml              # tooling and environment config (uv)
├── main.py                     # app entry point
├── ...                         
└─ src/                          
   ├── __init__.py              
   ├── api/v1/                   
   │       ├── __init__.py      
   │       ├── deps.py          # dependencies
   │       ├── routes.py        # API endpoints
   │       ├── schemas.py       # Pydantic models
   │       └── services.py      # Business logic   
   ├── core/
   │   ├── __init__.py
   │   ├── config.py            # configuration file
   │   └── utils.py             # encoding/decoding functions
   ├── db/
   │   ├── __init__.py
   │   ├── alembic/...          # migration directory
   │   ├── database.py          # DB connection
   │   ├── init_db.py           # DB initialization
   │   ├── models.py            # SQLAlchemy ORM-models
   │   ├── repositories.py      # data access abstraction
   │   └── test_data.py         # generating test data
   └── schemas/...              # Pydantic models

```

