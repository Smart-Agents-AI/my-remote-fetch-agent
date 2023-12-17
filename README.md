# Fetch.ai Agent: Send, Receive, and Deploy to Cloud

This repository contains code and instructions for setting up and deploying a Fetch.ai agent, combining the power of AI with blockchain technology.

## Overview

uAgents is a library developed by Fetch.ai that allows for creating autonomous AI agents in Python. With simple and expressive decorators, you can have an agent that performs various tasks on a schedule or takes action on various events.
For a detailed guide, check out my article on Medium: [Fetch.ai agent - Send, Receive, and Deploy](https://link.medium.com/3x2ULAiqBFb)

## Setting Up

### Heroku Deployment

1. **Create a Heroku app**: Name it `my-remote-fetch-agent`.
2. **Set Environment Variables**: Configure `AGENT_ENDPOINT` in the Heroku 'Config Vars'.

### Code and Files

- `Procfile` and `Dockerfile` are essential for Heroku to build and run the application.
- `agent.py` contains the agent instance setup and business logic.

## Deployment

Deploy the agent using Heroku CLI and container registry:

```bash
heroku login
heroku container:login
docker build -t my-remote-fetch-agent .
heroku container:push web -a=my-remote-fetch-agent
heroku container:release web -a=my-remote-fetch-agent
# Optional: heroku ps:scale web=1 --app my-remote-fetch-agent
