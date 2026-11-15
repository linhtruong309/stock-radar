# Stock Radar

A real-time stock tracker built with Django. It streams live US stock trades, tracks a portfolio's
profit and loss, and flags unusual price moves the moment they happen.

> Work in progress. Market data comes from the free [Finnhub](https://finnhub.io) API.

## Stack

| Part | Tools |
|---|---|
| Web and REST API | Django, Django REST Framework |
| Real-time updates | Django Channels (WebSocket), Redis |
| Database | PostgreSQL |
| Local services | Docker Compose |
| Tests | pytest, pytest-django |

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

cp .env.example .env        # then fill in the values
docker compose up -d        # starts PostgreSQL and Redis
```

## Roadmap

- [ ] Project setup: Django, PostgreSQL and Redis in Docker
- [ ] Watchlist and portfolio models with a REST API
- [ ] Live trade stream from Finnhub stored in PostgreSQL
- [ ] Live prices pushed to the browser over WebSocket
- [ ] Unusual-move radar and price alerts
- [ ] Replay a past trading session
- [ ] Web page, deployment and CI
