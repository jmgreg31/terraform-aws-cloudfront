# Module Example
This is an example of the AWS Cloudfront Distribution with the module in use. The `main.tf` exhibits the module definition.  Pay special attention to the `source` variable, as it is calling a specific reference tag of the module.  It is highly encouraged to follow the same pattern to avoid any breaking changes as updates to the module are released.  Please note the syntax of the variable definitions in the `terraform.tfvars` file for adding and removing multiple items. 

## Terraform Backend
It may be important to store the state of the terraform configuration remotely.  This will ensure that your resources can be referenced from multiple locations.  If you too feel this is important **PLEASE** be sure to update the [Terraform-Backend](https://github.com/jmgreg31/terraform-aws-cloudfront/blob/master/example/main.tf#L119-L126) section in your configuration where:

* `bucket`  = Your S3 bucket
* `key`     = The folder location within your s3 bucket
* `region`  = AWS Region
* `encrypt` = true

Otherwise, this section can be removed.  Due to terraform limitations, these can not be variables within the configuration.  However, terraform does offer a way to pass these variables in at runtime.

Example:
```
terraform init \
-backend-config="bucket=my-bucket" \
-backend-config="key=cloudfront/terraform.tfstate" \
-backend-config="region=us-east-1" \
-backend-config="encrypt=true"
```