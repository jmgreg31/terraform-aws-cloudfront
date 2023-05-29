<!-- markdownlint-disable MD041 -->
## UNRELEASED (May 2023)

* Refactor GitHub Actions and script structure
* Enhancements to GitHub Actions Workflow

## v4.3.8 (May 2023)

* Simplify Contribution Workflow
* Fix GitHub Actions

## v4.3.7 (May 2023)

* Update `version.tf` to support aws provider >= 3.41

## v4.3.6 (February 2023)

* Update `default_cache_behavior` and `dynamic_ordered_cache_behavior` with ability to accept `response_headers_policy_id`(UUID) parameter.
  
* Move from Travis CI to GitHub Actions

## v4.3.5 (June 2021)

* Update to add Cloudfront Function support.  PLEASE NOTE: Logging must be enabled for the function to be attached.

## v4.3.4 (May 2021)

* Update `origin_path` variables to default to `""` as opposed to `null`.  This will solve issue #36

## v4.3.3 (April 2021)

* Add enhancement to support `cache_policy_id` and `origin_request_policy_id`.  When in use, forwarded values cannot be used.  You are now able to set `use_forwarded_values` in the cache behavior blocks.

* General Code clean-up

## v4.3.2 (October 2020)

* fix `dynamic_s3_origin_config` variable, to match the configuration of `dynamic_custom_origin_config`. This fixes a bug where `custom_headers` couldn't be set.

## v4.3.1 (September 2020)

* refactored the `dynamic_custom_error_response` variable, specifying all the fields is not needed anymore

## v4.3.0 (August 2020)

* Updated the module to support AWS Provider 3.0.0, this is now minimum version required
* `active_trusted_signers` variable has been renamed to `trusted_signers` to accomodate the change in the provider
* Supports now `TLSv1.2_2019` for SSL in Cloudfront, under the `minimum_protocol_version` variable

## v4.2.1 (March 2020)

* fixed a bug that was previously allowing to apply a security policy when no certificate is specified
* default root object now set as null

## v4.2.0 (February 2020)

* Added ability to disable the creation of the resource with variable `create_cf`, defaults to `true`
* Adding possibility to add additional tags
* Inside `ordered_cache_behavior` & `default_cache_behavior` made these variables optional: `compress`, `headers`, `min_ttl`, `max_ttl`, `default_ttl`, also made `lambda_function_association` optional, now possible not to specify it at all
* Inside `lambda_function_association`, made the variable `include_body` optional
* Inside `logging_config`, the variables `include_cookies` & `prefix` are now optional
* `origin_group` is now optional
* `logging_config` & `default_cache_behavior` are not iterating anymore (as there can be only max one of these configs)
* remove `provider.tf` as this should be defined per implementation.  Also removed `region` variable as this was only used for the provider.
* certificates - `cloudfront_default_certificate` & `ssl_support_method` are not required anymore, they default to `true` & `sni-only` if a certificate acm or iam is specified, configuration will auto modify them

## v4.1.1 (February 2020)

* Adding in the ability to Test
* Adding ability to bump version
* Files created: `CONTRIBUTING.md` `VERSION` `bump.py` `.travis.yml`

## v4.1.0 (February 2020)

* Add all CloudFront outputs
* Made `s3_origin_config` dynamic and `origin_access_identity` optional

## v4.0.0 (February 2020)

* Update the `viewer_certificate` block to include `acme_certificate_arn` and `cloudfront_default_certificate`
* Update the name of `ssl_certificate` to `iam_certificate_id` to align with the resource
* Made `iam_certificate_id` optional

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
