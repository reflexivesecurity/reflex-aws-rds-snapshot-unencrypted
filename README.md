# reflex-aws-rds-snapshot-unencrypted
Rule to detect when snapshots are created in an unencrypted state.

## Usage
To use this rule either add it to your `reflex.yaml` configuration file:  
```
rules:
  - reflex-aws-rds-snapshot-unencrypted:
      version: latest
```

or add it directly to your Terraform:  
```
...

module "reflex-aws-rds-snapshot-unencrypted" {
  source           = "github.com/cloudmitigator/reflex-aws-rds-snapshot-unencrypted"
}

...
```

## License
This Reflex rule is made available under the MPL 2.0 license. For more information view the [LICENSE](https://github.com/cloudmitigator/reflex-aws-rds-snapshot-unencrypted/blob/master/LICENSE) 
