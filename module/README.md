# Module Example
This is an example of the AWS Cloudfront Distribution with the module in use. The `main.tf` exhibits the module definition.  Pay special attention to the `source` variable, as it is calling a specific reference tag of the module.  We would highly encourage you to follow the same pattern to avoid any breaking changes as updates to the module are released.  You will also notice that some fields are commented out, showcasing that some components are not required (As described in the [ReadMe](https://github.com/jmgreg31/terraform_aws_cloudfront/blob/master/README.md) Table).  Please note the syntax of the variable definitions in the `terraform.tfvars` file for adding and removing multiple items. 

## Terraform Backend
It is important to store the state of the terraform configuration remotely.  This ensures that your resources can be referenced from multiple locations.  **PLEASE** be sure to update the [Terraform_Backend](https://github.com/jmgreg31/terraform_aws_cloudfront/blob/master/module/main.tf#L163-L171) section in your configuration where:
* `bucket`  = Your S3 bucket
* `key`     = The folder location within your s3 bucket
* `region`  = AWS Region
* `profile` = AWS Profile
* `encrypt` = true

Due to terraform limitations, these can not be variables within the configuration.  However, terraform does offer a way to pass these variables in at runtime.

Example:
```
terraform init \
-backend-config="bucket=spyderco-east" \
-backend-config="key=cloudfront/ASVTEST/terraform.tfstate" \
-backend-config="region=us-east-1" \
-backend-config="profile=GR_GG_COF_AWS_STSdigital_Dev_Developer" \
-backend-config="encrypt=true"
```