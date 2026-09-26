

import logging
import os
import time

import boto3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

region = os.getenv("AWS_REGION", "ap-south-1")

instance_ids = [
    instance_id.strip()
    for instance_id in os.getenv("INSTANCE_IDS", "").split(",")
    if instance_id.strip()
]

ec2 = boto3.client("ec2", region_name=region)

while True:
    try:
        response = ec2.describe_instances(
            InstanceIds=instance_ids
        )

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                state = instance["State"]["Name"]

                name = next(
                    (
                        tag["Value"]
                        for tag in instance.get("Tags", [])
                        if tag["Key"] == "Name"
                    ),
                    instance_id,
                )

                logging.info(
                    "%s (%s): %s",
                    name,
                    instance_id,
                    state,
                )

                if state == "stopped":
                    ec2.start_instances(
                        InstanceIds=[instance_id]
                    )

                    logging.warning(
                        "Start requested for %s (%s)",
                        name,
                        instance_id,
                    )

    except Exception:
        logging.exception(
            "Check failed; retrying"
        )

    time.sleep(10)


