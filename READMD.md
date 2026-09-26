# AWS EC2 Server Monitoring & Auto-Recovery

## Overview

Implemented an automated AWS EC2 monitoring and recovery solution using **Python, Boto3, Docker, and IAM**.

A dedicated monitoring server continuously monitors configured EC2 instances through AWS APIs. When an instance enters a stopped state, the monitoring agent automatically initiates the recovery process and brings the instance back to a running state.

## Architecture

```text
Monitoring EC2
      │
      ▼
Python + Boto3
      │
      ▼
AWS EC2 API
   ┌──┴──┐
   ▼     ▼
 EC2-1  EC2-2
   │     │
   └─ Auto-Recovery
```

## Key Features

* Automated EC2 instance monitoring
* Automatic recovery of stopped instances
* Secure AWS access using IAM roles
* Dockerized monitoring agent
* Continuous monitoring without manual intervention

## Technologies

**AWS EC2 | IAM | Python | Boto3 | Docker | Linux**

## Outcome

This project demonstrates automated infrastructure monitoring and recovery, helping reduce manual intervention and improve EC2 operational reliability.

