resource "aws_cloudfront_distribution" "cloudfront_distribution" {
  aliases             = var.alias
  comment             = var.comment
  default_root_object = var.default_root_object
  enabled             = var.enable
  http_version        = var.http_version
  is_ipv6_enabled     = var.enable_ipv6
  price_class         = var.price
  retain_on_delete    = var.retain_on_delete
  wait_for_deployment = var.wait_for_deployment
  web_acl_id          = var.webacl

  dynamic "origin" {
    for_each = [for i in var.dynamic_s3_origin_config : {
      name          = i.domain_name
      id            = i.origin_id
      identity      = i.origin_access_identity
      path          = lookup(i, "origin_path", null)
      custom_header = lookup(i, "custom_header", null)
    }]

    content {
      domain_name = origin.value.name
      origin_id   = origin.value.id
      origin_path = origin.value.path
      dynamic "custom_header" {
        for_each = origin.value.custom_header == null ? [] : [for i in origin.value.custom_header : {
          name  = i.name
          value = i.value
        }]
        content {
          name  = custom_header.value.name
          value = custom_header.value.value
        }
      }
      s3_origin_config {
        origin_access_identity = origin.value.identity
      }
    }
  }

  dynamic "origin" {
    for_each = [for i in var.dynamic_custom_origin_config : {
      name                     = i.domain_name
      id                       = i.origin_id
      path                     = lookup(i, "origin_path", null)
      http_port                = i.http_port
      https_port               = i.https_port
      origin_keepalive_timeout = i.origin_keepalive_timeout
      origin_read_timeout      = i.origin_read_timeout
      origin_protocol_policy   = i.origin_protocol_policy
      origin_ssl_protocols     = i.origin_ssl_protocols
      custom_header            = lookup(i, "custom_header", null)
    }]
    content {
      domain_name = origin.value.name
      origin_id   = origin.value.id
      origin_path = origin.value.path
      dynamic "custom_header" {
        for_each = origin.value.custom_header == null ? [] : [for i in origin.value.custom_header : {
          name  = i.name
          value = i.value
        }]
        content {
          name  = custom_header.value.name
          value = custom_header.value.value
        }
      }
      custom_origin_config {
        http_port                = origin.value.http_port
        https_port               = origin.value.https_port
        origin_keepalive_timeout = origin.value.origin_keepalive_timeout
        origin_read_timeout      = origin.value.origin_read_timeout
        origin_protocol_policy   = origin.value.origin_protocol_policy
        origin_ssl_protocols     = origin.value.origin_ssl_protocols
      }
    }
  }

  dynamic "origin_group" {
    for_each = [for i in var.dynamic_origin_group : {
      id           = i.origin_id
      status_codes = i.status_codes
      member1      = lookup(i, "member", null)
    }]
    content {
      origin_id = origin_group.value.id
      failover_criteria {
        status_codes = origin_group.value.status_codes
      }
      dynamic "member" {
        for_each = origin_group.value.member == null ? [] : [for i in origin_group.value.member : {
          id = i.origin_id
        }]
        content {
          origin_id = member.value.id
        }
      }
    }
  }

  dynamic "default_cache_behavior" {
    for_each = [for i in var.dynamic_default_cache_behavior : {
      allowed_methods             = i.allowed_methods
      cached_methods              = i.cached_methods
      target_origin_id            = i.target_origin_id
      compress                    = i.compress
      query_string                = i.query_string
      cookies_forward             = i.cookies_forward
      headers                     = i.headers
      viewer_protocol_policy      = i.viewer_protocol_policy
      min_ttl                     = i.min_ttl
      default_ttl                 = i.default_ttl
      max_ttl                     = i.max_ttl
      lambda_function_association = lookup(i, "lambda_function_association", null)
    }]
    content {
      allowed_methods  = default_cache_behavior.value.allowed_methods
      cached_methods   = default_cache_behavior.value.cached_methods
      target_origin_id = default_cache_behavior.value.target_origin_id
      compress         = default_cache_behavior.value.compress

      forwarded_values {
        query_string = default_cache_behavior.value.query_string
        cookies {
          forward = default_cache_behavior.value.cookies_forward
        }
        headers = default_cache_behavior.value.headers
      }

      dynamic "lambda_function_association" {
        for_each = default_cache_behavior.value.lambda_function_association == null ? [] : [for i in default_cache_behavior.value.lambda_function_association : {
          event_type   = i.event_type
          lambda_arn   = i.lambda_arn
          include_body = i.include_body
        }]
        content {
          event_type   = lambda_function_association.value.event_type
          lambda_arn   = lambda_function_association.value.lambda_arn
          include_body = lambda_function_association.value.include_body
        }
      }

      viewer_protocol_policy = default_cache_behavior.value.viewer_protocol_policy
      min_ttl                = default_cache_behavior.value.min_ttl
      default_ttl            = default_cache_behavior.value.default_ttl
      max_ttl                = default_cache_behavior.value.max_ttl
    }
  }

  dynamic "ordered_cache_behavior" {
    for_each = [for i in var.dynamic_ordered_cache_behavior : {
      path_pattern                = i.path_pattern
      allowed_methods             = i.allowed_methods
      cached_methods              = i.cached_methods
      target_origin_id            = i.target_origin_id
      compress                    = i.compress
      query_string                = i.query_string
      cookies_forward             = i.cookies_forward
      headers                     = i.headers
      viewer_protocol_policy      = i.viewer_protocol_policy
      min_ttl                     = i.min_ttl
      default_ttl                 = i.default_ttl
      max_ttl                     = i.max_ttl
      lambda_function_association = lookup(i, "lambda_function_association", null)
    }]
    content {
      path_pattern     = ordered_cache_behavior.value.path_pattern
      allowed_methods  = ordered_cache_behavior.value.allowed_methods
      cached_methods   = ordered_cache_behavior.value.cached_methods
      target_origin_id = ordered_cache_behavior.value.target_origin_id
      compress         = ordered_cache_behavior.value.compress

      forwarded_values {
        query_string = ordered_cache_behavior.value.query_string
        cookies {
          forward = ordered_cache_behavior.value.cookies_forward
        }
        headers = ordered_cache_behavior.value.headers
      }

      dynamic "lambda_function_association" {
        for_each = ordered_cache_behavior.value.lambda_function_association == null ? [] : [for i in ordered_cache_behavior.value.lambda_function_association : {
          event_type   = i.event_type
          lambda_arn   = i.lambda_arn
          include_body = i.include_body
        }]
        content {
          event_type   = lambda_function_association.value.event_type
          lambda_arn   = lambda_function_association.value.lambda_arn
          include_body = lambda_function_association.value.include_body
        }
      }

      viewer_protocol_policy = ordered_cache_behavior.value.viewer_protocol_policy
      min_ttl                = ordered_cache_behavior.value.min_ttl
      default_ttl            = ordered_cache_behavior.value.default_ttl
      max_ttl                = ordered_cache_behavior.value.max_ttl
    }
  }

  dynamic "custom_error_response" {
    for_each = [for i in var.dynamic_custom_error_response : {
      error_caching_min_ttl = i.error_caching_min_ttl
      error_code            = i.error_code
      response_code         = i.response_code
      response_page_path    = i.response_page_path
    }]

    content {
      error_caching_min_ttl = custom_error_response.value.error_caching_min_ttl
      error_code            = custom_error_response.value.error_code
      response_code         = custom_error_response.value.response_code
      response_page_path    = custom_error_response.value.response_page_path
    }
  }

  dynamic "logging_config" {
    for_each = [for i in var.dynamic_logging_config : {
      bucket          = i.bucket
      include_cookies = i.include_cookies
      prefix          = i.prefix
    }]

    content {
      bucket          = logging_config.value.bucket
      include_cookies = logging_config.value.include_cookies
      prefix          = logging_config.value.prefix
    }
  }

  tags = {
    Name = var.tag_name
  }

  restrictions {
    geo_restriction {
      locations        = var.restriction_location
      restriction_type = var.restriction_type
    }
  }

  viewer_certificate {
    iam_certificate_id       = var.ssl_certificate
    minimum_protocol_version = var.minimum_protocol_version
    ssl_support_method       = var.ssl_support_method
  }
}