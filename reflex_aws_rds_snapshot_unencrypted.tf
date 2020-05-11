module "reflex_aws_rds_snapshot_unencrypted" {
  source           = "git::https://github.com/cloudmitigator/reflex-engine.git//modules/cwe_lambda?ref=v0.6.0"
  rule_name        = "RDSSnapshotUnencrypted"
  rule_description = "Rule to detect when snapshots are created unencrypted."

  event_pattern = <<PATTERN
{
  "source": [
    "aws.rds"
  ],
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "rds.amazonaws.com"
    ],
    "eventName": [
      "CreateDBSnapshot"
    ]
  }
}
PATTERN

  function_name   = "RDSSnapshotUnencrypted"
  source_code_dir = "${path.module}/source"
  handler         = "reflex_aws_rds_snapshot_unencrypted.lambda_handler"
  lambda_runtime  = "python3.7"
  environment_variable_map = {
    SNS_TOPIC = var.sns_topic_arn,
    
  }


  queue_name    = "RDSSnapshotUnencrypted"
  delay_seconds = 0

  target_id = "RDSSnapshotUnencrypted"

  sns_topic_arn  = var.sns_topic_arn
  sqs_kms_key_id = var.reflex_kms_key_id
}
