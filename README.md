# AWS EC2 Server Monitoring & Auto-Recovery

This project implements automated monitoring and recovery of AWS EC2 instances using Python, Boto3, Docker, and IAM. A Dockerized monitoring agent runs on a dedicated EC2 instance and continuously checks the state of configured EC2 servers. If an instance enters the `stopped` state, the agent automatically sends a start request through the AWS EC2 API to recover it.

### Technologies

AWS EC2 | IAM | Python | Boto3 | Docker | Linux

### Docker

```bash
docker build -t ec2-monitor .
docker run -d --name ec2-monitor ec2-monitor
```

### Workflow

```text
Monitoring EC2 → Python/Boto3 → Check EC2 State
                              ↓
                         STOPPED?
                              ↓
                     Start EC2 Instance
```

The project uses IAM roles for secure AWS access and automatically restores stopped EC2 instances without manual intervention.
