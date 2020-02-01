## v3.0.0 (February 2020)
* Update to Terraform version 12 syntax
* Add `custom_header` to both `dynamic_custom_origin_config` and `dynamic_s3_origin_config`
* Update the way origin group members are assigned.  Fixes [Issue #1](https://github.com/jmgreg31/terraform-aws-cloudfront/issues/1)
* Remove the dependancy to always have `origin_path` defined
* Add `lambda_function_assocation` to all cache behaviors.  Fixes [Issue #3](https://github.com/jmgreg31/terraform-aws-cloudfront/issues/3)

## v2.0.0 (June 2019)
* Update to `dynamic_custom_origin_config` variable to include `origin_path`
* Breaking change as you will now need to include this in your variable block
* Fixes [Issue #5](https://github.com/jmgreg31/terraform-aws-cloudfront/issues/5)

## v1.0.0 (June 2019)
* Initial Release
* Supports Terraform Version 12 only