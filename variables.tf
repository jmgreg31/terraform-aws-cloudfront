variable enabled {
  description = "Set to false to prevent the module from creating any resources"
  type        = bool
  default     = true
}

variable acm_certificate_arn {
  description = "The ARN of the AWS Certificate Manager certificate that you wish to use with this distribution"
  type        = string
  default     = null
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

variable default_root_object {
  description = "The object that you want CloudFront to return (for example, index.html) when an end user requests the root URL"
  type        = string
  default     = ""
}

variable dynamic_custom_error_response {
  description = "Custom error response to be used in dynamic block"
  type        = any
  default     = []
}

variable dynamic_custom_origin_config {
  description = "Configuration for the custom origin config to be used in dynamic block"
  type        = any
  default     = []
}

variable dynamic_default_cache_behavior {
  description = "Default Cache Behviors to be used in dynamic block"
  type        = any
}

variable dynamic_ordered_cache_behavior {
  description = "Ordered Cache Behaviors to be used in dynamic block"
  type        = any
  default     = []
}

variable dynamic_origin_group {
  description = "Origin Group to be used in dynamic block"
  type        = any
  default     = []
}

variable dynamic_logging_config {
  description = <<EOF
    This is the logging configuration for the Cloudfront Distribution.  It is not required.
    If you choose to use this configuration, be sure you have the correct IAM and Bucket ACL
    rules.  Your tfvars file should follow this syntax:

    logging_config = [{
    bucket = "<your-bucket>"
    include_cookies = <true or false>
    prefix = "<your-bucket-prefix>"
    }]

    EOF

  type    = any
  default = []
}

variable dynamic_s3_origin_config {
  description = "Configuration for the s3 origin config to be used in dynamic block"
  type        = list(map(string))
  default     = []
}

variable enable {
  description = "Whether the distribution is enabled to accept end user requests for content"
  type        = bool
  default     = true
}

variable enable_ipv6 {
  description = "Whether the IPv6 is enabled for the distribution"
  type        = bool
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

variable retain_on_delete {
  description = "Disables the distribution instead of deleting it when destroying the resource through Terraform. If this is set, the distribution needs to be deleted manually afterwards."
  type        = bool
  default     = false
}

variable ssl_support_method {
  description = "Specifies how you want CloudFront to serve HTTPS requests. One of vip or sni-only."
  type        = string
}

variable tag_name {
  description = "The tagged name"
  type        = string
  default     = ""
}

variable additional_tags {
  description = "A mapping of additional tags to attach"
  type        = map(string)
  default     = {}
}

variable wait_for_deployment {
  description = "If enabled, the resource will wait for the distribution status to change from InProgress to Deployed. Setting this tofalse will skip the process."
  type        = bool
  default     = true
}

variable webacl {
  description = "The WAF Web ACL"
  type        = string
  default     = ""
}

// variable origin_group_member {
//   type = any
// }
