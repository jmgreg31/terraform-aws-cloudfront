<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD041 -->
[![Build Status](https://travis-ci.com/jmgreg31/terraform-aws-cloudfront.svg?branch=master)](https://travis-ci.com/jmgreg31/terraform-aws-cloudfront)
[![Latest Release](https://img.shields.io/badge/release-v4.3.8-blue.svg)](https://github.com/jmgreg31/terraform-aws-cloudfront/releases/tag/v4.3.8)

# Terraform Cloudfront Module

This is a module to build a cloudfront distribution.  It has been modularized to accept multiple origins, behaviors, and custom error responses.  Please reference the [Example](https://github.com/jmgreg31/terraform-aws-cloudfront/tree/master/example) folder for an example of this module in action

## Notes

* This Module supports Terraform Version 0.12 and above
* This Module has been tested & verified with 0.13.3
* While `dynamic_custom_origin_config` and `dynamic_s3_origin_config` are considered not
  required, you must supply at least one origin config.
* Cloudfront functions require logging to be enabled

## Release

See [CHANGELOG](CHANGELOG.md) for release notes

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-----:|:-----:|
| acm\_certificate\_arn | "The ARN of the AWS Certificate Manager certificate that you wish to use with this distribution. The ACM certificate must be in US-EAST-1. | string | `null` | no |
| additional_tags | A mapping of additional tags to attach | map(string) | `{}` | no |
| alias | Aliases, or CNAMES, for the distribution | list | `[]` | no |
| comment | Any comment about the CloudFront Distribution | string | `""` | no |
| cloudfront\_default\_certificate | This variable is not required anymore, being auto generated, left here for compability purposes | bool | `true` | no |
| create_cf | Set to false to prevent the module from creating any resources | bool | `true` | no |
| default\_root\_object | The object that you want CloudFront to return (for example, index.html) when an end user requests the root URL | string | `""` | no |
| dynamic\_custom\_error\_response | Custom error response to be used in dynamic block | any | `[]` | no |
| dynamic\_custom\_origin\_config | Configuration for the custom origin config to be used in dynamic block | any | `[]` | no |
| dynamic\_default\_cache\_behavior | Default Cache Behviors to be used in dynamic block | any | n/a | yes |
| dynamic\_ordered\_cache\_behavior | Ordered Cache Behaviors to be used in dynamic block | any | `[]` | no |
| dynamic\_origin\_group | Origin Group to be used in dynamic block | any | `[]` | no |
| dynamic\_logging\_config | This is the logging configuration for the Cloudfront Distribution.  It is not required.     If you choose to use this configuration, be sure you have the correct IAM and Bucket ACL     rules.  Your tfvars file should follow this syntax:<br><br>    logging_config = [{     bucket = "<your-bucket>"     include_cookies = <true or false>     prefix = "<your-bucket-prefix>"     }] | any | `[]` | no |
| dynamic\_s3\_origin\_config | Configuration for the s3 origin config to be used in dynamic block | list(map(string)) | `[]` | no |
| enable | Whether the distribution is enabled to accept end user requests for content | bool | `true` | no |
| enable\_ipv6 | Whether the IPv6 is enabled for the distribution | bool | `true` | no |
| http\_version | The maximum HTTP version to support on the distribution. Allowed values are http1.1 and http2 | string | `"http2"` | no |
| iam\_certificate\_id | Specifies IAM certificate id for CloudFront distribution | string | `null` | no |
| minimum\_protocol\_version | The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.      One of SSLv3, TLSv1, TLSv1_2016, TLSv1.1_2016, TLSv1.2_2018 or TLSv1.2_2019. Default: TLSv1.      NOTE: If you are using a custom certificate (specified with acm_certificate_arn or iam_certificate_id),      and have specified sni-only in ssl_support_method, TLSv1 or later must be specified.      If you have specified vip in ssl_support_method, only SSLv3 or TLSv1 can be specified.      If you have specified cloudfront_default_certificate, TLSv1 must be specified. | string | TLSv1 | no |
| price | The price class of the CloudFront Distribution.  Valid types are PriceClass_All, PriceClass_100, PriceClass_200 | string | `"PriceClass_100"` | no |
| restriction\_location | The ISO 3166-1-alpha-2 codes for which you want CloudFront either to distribute your content (whitelist) or not distribute your content (blacklist) | list | `[]` | no |
| restriction\_type | The restriction type of your CloudFront distribution geolocation restriction. Options include none, whitelist, blacklist | string | `"none"` | no |
| retain\_on\_delete | Disables the distribution instead of deleting it when destroying the resource through Terraform. If this is set, the distribution needs to be deleted manually afterwards. | bool | `false` | no |
| ssl\_support\_method | This variable is not required anymore, being auto generated, left here for compability purposes | string | sni-only | no |
| tag\_name | The tagged name | string | n/a | no |
| wait\_for\_deployment | If enabled, the resource will wait for the distribution status to change from InProgress to Deployed. Setting this tofalse will skip the process. | bool | `true` | no |
| webacl | The WAF Web ACL | string | `""` | no |

## Outputs

| Name | Description |
|------|-------------|
| id | The identifier for the distribution. For example: EDFDVBD632BHDS5. |
| arn | The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID. |
| caller_reference | Internal value used by CloudFront to allow future updates to the distribution configuration. |
| status | The current status of the distribution. Deployed if the distribution's information is fully propagated throughout the Amazon CloudFront system. |
| trusted_signers | The key pair IDs that CloudFront is aware of for each trusted signer, if the distribution is set up to serve private content with signed URLs. |
| domain_name | The domain name corresponding to the distribution. For example: d604721fxaaqy9.cloudfront.net. |
| name | The domain name corresponding to the distribution. For example: d604721fxaaqy9.cloudfront.net. |
| last_modified_time | The date and time the distribution was last modified. |
| in_progress_validation_batches | The number of invalidation batches currently in progress. |
| etag | The current version of the distribution's information. For example: E2QWRUHAPOMQZL. |
| hosted_zone_id | The CloudFront Route 53 zone ID that can be used to route an Alias Resource Record Set to. This attribute is simply an alias for the zone ID Z2FDTNDATAQYW2. |
