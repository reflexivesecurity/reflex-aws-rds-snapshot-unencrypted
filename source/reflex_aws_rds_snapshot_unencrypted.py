""" Module for RDSSnapshotUnencrypted """

import json
import os

import boto3
from reflex_core import AWSRule, subscription_confirmation


class RDSSnapshotUnencrypted(AWSRule):
    """ Rule to detect when RDS snapshot is created unencrypted. """


    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        self.snapshot_id = event["detail"]["requestParameters"]["dBSnapshotIdentifier"]
        self.database_id = event["detail"]["requestParameters"]["dBInstanceIdentifier"]
        self.is_encrypted = event["detail"]["responseElements"]["encrypted"]

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        return self.is_encrypted

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        return f"The snapshot {self.snapshot_id} of RDS instance {self.database_id} was unencrypted."


def lambda_handler(event, _):
    """ Handles the incoming event """
    print(event)
    if subscription_confirmation.is_subscription_confirmation(event):
        subscription_confirmation.confirm_subscription(event)
        return
    rule = RDSSnapshotUnencrypted(json.loads(event["Records"][0]["body"]))
    rule.run_compliance_rule()
