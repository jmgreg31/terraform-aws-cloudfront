[![Latest Release](https://img.shields.io/badge/release-v3.0.0-blue.svg)](https://github.com/jmgreg31/terraform-aws-cloudfront/releases/tag/v3.0.0)

# Terraform Cloudfront Module

This is a module to build a cloudfront distribution.  It has been modularized to accept multiple origins, behaviors, and custom error responses.  Please reference the [Example](https://github.com/jmgreg31/terraform-aws-cloudfront/tree/master/example) folder for an example of this module in action

## Notes

* This Module only supports Terraform Version 12
* While `dynamic_custom_origin_config` and `dynamic_s3_origin_config` are considered not
  required, you must supply atleast one origin config.

## Release

See [CHANGELOG](CHANGELOG.md) for release notes

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-----:|:-----:|
| alias | Aliases, or CNAMES, for the distribution | list | `[]` | no |
| comment | Any comment about the CloudFront Distribution | string | `""` | no |
| default\_root\_object | The object that you want CloudFront to return (for example, index.html) when an end user requests the root URL | string | `""` | no |
| dynamic\_custom\_error\_response | Custom error response to be used in dynamic block | any | `[]` | yes |
| dynamic\_custom\_origin\_config | Configuration for the custom origin config to be used in dynamic block | any | `[]` | no |
| dynamic\_default\_cache\_behavior | Default Cache Behviors to be used in dynamic block | any | n/a | yes |
| dynamic\_ordered\_cache\_behavior | Ordered Cache Behaviors to be used in dynamic block | any | `[]` | no |
| dynamic\_origin\_group | Origin Group to be used in dynamic block | any | n/a | yes |
| dynamic\_logging\_config | This is the logging configuration for the Cloudfront Distribution.  It is not required.     If you choose to use this configuration, be sure you have the correct IAM and Bucket ACL     rules.  Your tfvars file should follow this syntax:<br><br>    logging_config = [{     bucket = "<your-bucket>"     include_cookies = <true or false>     prefix = "<your-bucket-prefix>"     }] | any | `[]` | no |
| dynamic\_s3\_origin\_config | Configuration for the s3 origin config to be used in dynamic block | list(map(string)) | `[]` | no |
| enable | Whether the distribution is enabled to accept end user requests for content | bool | `true` | no |
| enable\_ipv6 | Whether the IPv6 is enabled for the distribution | bool | `true` | no |
| http\_version | The maximum HTTP version to support on the distribution. Allowed values are http1.1 and http2 | string | `"http2"` | no |
| minimum\_protocol\_version | The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections.      One of SSLv3, TLSv1, TLSv1_2016, TLSv1.1_2016 or TLSv1.2_2018. Default: TLSv1.      NOTE: If you are using a custom certificate (specified with acm_certificate_arn or iam_certificate_id),      and have specified sni-only in ssl_support_method, TLSv1 or later must be specified.      If you have specified vip in ssl_support_method, only SSLv3 or TLSv1 can be specified.      If you have specified cloudfront_default_certificate, TLSv1 must be specified. | string | n/a | yes |
| price | The price class of the CloudFront Distribution.  Valid types are PriceClass_All, PriceClass_100, PriceClass_200 | string | `"PriceClass_100"` | no |
| region | Target AWS region | string | `"us-east-1"` | no |
| restriction\_location | The ISO 3166-1-alpha-2 codes for which you want CloudFront either to distribute your content (whitelist) or not distribute your content (blacklist) | list | `[]` | no |
| restriction\_type | The restriction type of your CloudFront distribution geolocation restriction. Options include none, whitelist, blacklist | string | `"none"` | no |
| retain\_on\_delete | Disables the distribution instead of deleting it when destroying the resource through Terraform. If this is set, the distribution needs to be deleted manually afterwards. | bool | `false` | no |
| ssl\_certificate | Specifies IAM certificate id for CloudFront distribution | string | n/a | yes |
| ssl\_support\_method | Specifies how you want CloudFront to serve HTTPS requests. One of vip or sni-only. | string | n/a | yes |
| tag\_name | The tagged name | string | n/a | no |
| wait\_for\_deployment | If enabled, the resource will wait for the distribution status to change from InProgress to Deployed. Setting this tofalse will skip the process. | bool | `true` | no |
| webacl | The WAF Web ACL | string | `""` | no |

## Outputs

| Name | Description |
|------|-------------|
| name | The domain name of the CloudFront distribution |
