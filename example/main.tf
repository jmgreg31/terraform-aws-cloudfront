variable create_cf {
  description = "Set to false to prevent the module from creating any resources"
  type        = bool
  default     = true
}

variable acm_certificate_arn {
  description = "The ARN of the AWS Certificate Manager certificate that you wish to use with this distribution"
  type        = string
  default     = null
}

variable additional_tags {
  description = "A mapping of additional tags to attach"
  type        = map(string)
  default     = {}
}

variable alias {
  description = "Aliases, or CNAMES, for the distribution"
  type        = list
  default     = []
}

variable cloudfront_default_certificate {
  description = "If you want viewers to use HTTPS to request your objects and you're using the cloudfront domain name for your distribution"
  type        = bool
  default     = true
}

variable comment {
  description = "Any comment about the CloudFront Distribution"
  type        = string
  default     = ""
}

variable dynamic_custom_error_response {
  description = "Custom error response to be used in dynamic block"
  type        = any
}

variable dynamic_custom_origin_config {
  description = "Configuration for the custom origin config to be used in dynamic block"
  type        = any
}

variable dynamic_default_cache_behavior {
  description = "Default Cache Behviors to be used in dynamic block"
  type        = any
}

variable dynamic_ordered_cache_behavior {
  description = "Ordered Cache Behaviors to be used in dynamic block"
  type        = any
}

variable dynamic_origin_group {
  description = "Origin Group to be used in dynamic block"
  type        = any
}

variable dynamic_s3_origin_config {
  description = "Configuration for the s3 origin config to be used in dynamic block"
  type        = list(map(string))
}

variable enable {
  description = "Whether the distribution is enabled to accept end user requests for content"
  type        = string
  default     = true
}

variable enable_ipv6 {
  description = "Whether the IPv6 is enabled for the distribution"
  type        = string
  default     = true
}

variable http_version {
  description = "The maximum HTTP version to support on the distribution. Allowed values are http1.1 and http2"
  type        = string
  default     = "http2"
}

variable iam_certificate_id {
  description = "Specifies IAM certificate id for CloudFront distribution"
  type        = string
  default     = null
}

variable minimum_protocol_version {
  description = <<EOF
    The minimum version of the SSL protocol that you want CloudFront to use for HTTPS connections. 
    One of SSLv3, TLSv1, TLSv1_2016, TLSv1.1_2016 or TLSv1.2_2018. Default: TLSv1. 
    NOTE: If you are using a custom certificate (specified with acm_certificate_arn or iam_certificate_id), 
    and have specified sni-only in ssl_support_method, TLSv1 or later must be specified. 
    If you have specified vip in ssl_support_method, only SSLv3 or TLSv1 can be specified. 
    If you have specified cloudfront_default_certificate, TLSv1 must be specified.
    EOF

  type = string
}

variable price {
  description = "The price class of the CloudFront Distribution.  Valid types are PriceClass_All, PriceClass_100, PriceClass_200"
  type        = string
  default     = "PriceClass_100"
}

variable region {
  description = "Target AWS region"
  type        = string
  default     = "us-east-1"
}

variable restriction_location {
  description = "The ISO 3166-1-alpha-2 codes for which you want CloudFront either to distribute your content (whitelist) or not distribute your content (blacklist)"
  type        = list
  default     = []
}

variable restriction_type {
  description = "The restriction type of your CloudFront distribution geolocation restriction. Options include none, whitelist, blacklist"
  type        = string
  default     = "none"
}

variable ssl_support_method {
  description = "Specifies how you want CloudFront to serve HTTPS requests. One of vip or sni-only."
  type        = string
}

variable tag_name {
  description = "The tagged name"
  type        = string
}

variable webacl {
  description = "The WAF Web ACL"
  type        = string
  default     = ""
}

output "id" {
  value       = module.demo_cf.id
  description = "The identifier for the distribution. For example: EDFDVBD632BHDS5."
}

output "arn" {
  value       = module.demo_cf.arn
  description = "The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID."
}

output "caller_reference" {
  value       = module.demo_cf.caller_reference
  description = "Internal value used by CloudFront to allow future updates to the distribution configuration."
}

output "status" {
  value       = module.demo_cf.status
  description = "The current status of the distribution. Deployed if the distribution's information is fully propagated throughout the Amazon CloudFront system."
}

output "active_trusted_signers" {
  value       = module.demo_cf.active_trusted_signers
  description = "The key pair IDs that CloudFront is aware of for each trusted signer, if the distribution is set up to serve private content with signed URLs."
}

output "domain_name" {
  value       = module.demo_cf.domain_name
  description = "The domain name corresponding to the distribution. For example: d604721fxaaqy9.cloudfront.net."
}

output "name" {
  value       = module.demo_cf.domain_name
  description = "The domain name corresponding to the distribution. For example: d604721fxaaqy9.cloudfront.net."
}

output "last_modified_time" {
  value       = module.demo_cf.last_modified_time
  description = "The date and time the distribution was last modified."
}

output "in_progress_validation_batches" {
  value       = module.demo_cf.in_progress_validation_batches
  description = "The number of invalidation batches currently in progress."
}

output "etag" {
  value       = module.demo_cf.etag
  description = "The current version of the distribution's information. For example: E2QWRUHAPOMQZL."
}

output "hosted_zone_id" {
  value       = module.demo_cf.hosted_zone_id
  description = "The CloudFront Route 53 zone ID that can be used to route an Alias Resource Record Set to. This attribute is simply an alias for the zone ID Z2FDTNDATAQYW2."
}

terraform {
  backend "s3" {
    bucket  = "jmgreg31"
    key     = "cloudfront/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}

provider "aws" {
  version = ">= 2.28.0"
  region  = var.region
}

module demo_cf {
  source                         = "git::https://github.com/jmgreg31/terraform-aws-cloudfront.git?ref=v4.2.1"
  create_cf                      = var.create_cf
  acm_certificate_arn            = var.acm_certificate_arn
  additional_tags                = var.additional_tags
  alias                          = var.alias
  cloudfront_default_certificate = var.cloudfront_default_certificate
  comment                        = var.comment
  dynamic_custom_error_response  = var.dynamic_custom_error_response
  dynamic_default_cache_behavior = var.dynamic_default_cache_behavior
  enable                         = var.enable
  enable_ipv6                    = var.enable_ipv6
  http_version                   = var.http_version
  iam_certificate_id             = var.iam_certificate_id
  minimum_protocol_version       = var.minimum_protocol_version
  dynamic_ordered_cache_behavior = var.dynamic_ordered_cache_behavior
  dynamic_custom_origin_config   = var.dynamic_custom_origin_config
  dynamic_s3_origin_config       = var.dynamic_s3_origin_config
  dynamic_origin_group           = var.dynamic_origin_group
  price                          = var.price
  region                         = var.region
  restriction_type               = var.restriction_type
  ssl_support_method             = var.ssl_support_method
  tag_name                       = var.tag_name
  webacl                         = var.webacl
}
