variable alias {
  description = "Aliases, or CNAMES, for the distribution"
  type        = list
  default     = []
}

variable comment {
  description = "Any comment about the CloudFront Distribution"
  type        = string
  default     = ""
}

variable dynamic_custom_error_response {
  description = "Custom error response to be used in dynamic block"
  type = any
}

variable dynamic_custom_origin_config {
  description = "Configuration for the custom origin config to be used in dynamic block"
  type = any
}

variable dynamic_default_cache_behavior {
  description = "Default Cache Behviors to be used in dynamic block"
  type = any
}

variable dynamic_ordered_cache_behavior {
  description = "Ordered Cache Behaviors to be used in dynamic block"
  type = any
}

variable dynamic_origin_group {
  description = "Origin Group to be used in dynamic block"
  type = any
}

variable dynamic_s3_origin_config {
  description = "Configuration for the s3 origin config to be used in dynamic block"
  type = list(map(string))
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

variable ssl_certificate {
  description = "Specifies IAM certificate id for CloudFront distribution"
  type        = string
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

terraform {
  backend "s3" {
    bucket  = "my-bucket"
    key     = "cloudfront/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}

module spyderco_cf {
  source                         = "git::https://github.com/jmgreg31/terraform_aws_cloudfront.git?ref=v3.0.0"
  alias                          = var.alias
  comment                        = var.comment
  dynamic_custom_error_response  = var.dynamic_custom_error_response
  dynamic_default_cache_behavior = var.dynamic_default_cache_behavior
  enable                         = var.enable
  enable_ipv6                    = var.enable_ipv6
  http_version                   = var.http_version
  minimum_protocol_version       = var.minimum_protocol_version
  dynamic_ordered_cache_behavior = var.dynamic_ordered_cache_behavior
  dynamic_custom_origin_config   = var.dynamic_custom_origin_config
  dynamic_s3_origin_config       = var.dynamic_s3_origin_config
  dynamic_origin_group           = var.dynamic_origin_group
  price                          = var.price
  region                         = var.region
  restriction_type               = var.restriction_type
  ssl_certificate                = var.ssl_certificate
  ssl_support_method             = var.ssl_support_method
  tag_name                       = var.tag_name
  webacl                         = var.webacl
}
