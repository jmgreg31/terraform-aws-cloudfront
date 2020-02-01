alias                    = []
comment                  = "AWS Cloudfront Module"
enable                   = true
enable_ipv6              = true
http_version             = "http1.1"
minimum_protocol_version = "TLSv1.1_2016"
price                    = "PriceClass_100"
profile                  = "Example_Profile"
region                   = "us-east-1"
restriction_type         = "none"
ssl_certificate          = "sslcert"
ssl_support_method       = "sni-only"
tag_name                 = "AWS Cloudfront Module"
webacl                   = "webaclid"

dynamic_s3_origin_config = [
  {
    domain_name            = "domain.s3.amazonaws.com"
    origin_id              = "S3-domain-cert"
    origin_access_identity = "origin-access-identity/cloudfront/1234"
  },
  {
    domain_name            = "domain2.s3.amazonaws.com"
    origin_id              = "S3-domain2-cert"
    origin_access_identity = "origin-access-identity/cloudfront/1234"
    origin_path            = ""
  }
]

dynamic_custom_origin_config = [
  {
    domain_name              = "mydomain.google.com"
    origin_id                = "mydomainorigin.google.com"
    http_port                = 80
    https_port               = 443
    origin_keepalive_timeout = 5
    origin_read_timeout      = 30
    origin_protocol_policy   = "https-only"
    origin_ssl_protocols     = ["TLSv1.2", "TLSv1.1"]
    custom_header            = [
      {
        name                 = "Test"
        value                = "Test-Header"
      },
      {
        name                 = "Test2"
        value                = "Test2-Header"
      }
    ]
  },
  {
    domain_name              = "mydomain2.google.com"
    origin_id                = "mydomain2origin.google.com"
    origin_path              = ""
    http_port                = 80
    https_port               = 443
    origin_keepalive_timeout = 5
    origin_read_timeout      = 30
    origin_protocol_policy   = "https-only"
    origin_ssl_protocols     = ["TLSv1.2", "TLSv1.1"]
  }
]

dynamic_origin_group = [
  {
    origin_id    = "OriginGroup-1-S3-cert"
    status_codes = [403, 404, 500, 502, 503, 504]
    member       = [
      {
        origin_id = "S3-cert-east"
      },
      {
        origin_id = "S3-cert-west"
      }
    ]
  }
]

dynamic_default_cache_behavior = [
  {
    allowed_methods             = ["GET", "HEAD", "OPTIONS", "POST", "PUT", "DELETE", "PATCH"]
    cached_methods              = ["GET", "HEAD"]
    target_origin_id            = "mydomainorigin.google.com"
    compress                    = false
    query_string                = true
    cookies_forward             = "all"
    headers                     = ["*"]
    viewer_protocol_policy      = "redirect-to-https"
    min_ttl                     = 0
    default_ttl                 = 0
    max_ttl                     = 0
    lambda_function_association = [
      {
        event_type = "viewer-request"
        lambda_arn = "YOUR LAMBDA ARN"
        include_body = true
      }
    ]
  }
]

dynamic_ordered_cache_behavior = [
  {
    path_pattern           = "/cafe/"
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "mydomain2origin.google.com"
    compress               = false
    query_string           = true
    cookies_forward        = "all"
    headers                = []
    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 0
    max_ttl                = 0
  }
]

dynamic_custom_error_response = [
  {
    error_caching_min_ttl = 1
    error_code            = 400
    response_code         = null
    response_page_path    = ""
  },
  {
    error_caching_min_ttl = 1
    error_code            = 403
    response_code         = null
    response_page_path    = ""
  },
  {
    error_caching_min_ttl = 1
    error_code            = 404
    response_code         = null
    response_page_path    = ""
  },
  {
    error_caching_min_ttl = 1
    error_code            = 405
    response_code         = null
    response_page_path    = ""
  },
  {
    error_caching_min_ttl = 1
    error_code            = 414
    response_code         = null
    response_page_path    = ""
  },
  {
    error_caching_min_ttl = 1
    error_code            = 416
    response_code         = null
    response_page_path    = ""
  },
  {
    error_caching_min_ttl = 1
    error_code            = 500
    response_code         = null
    response_page_path    = ""
  },
  {
    error_caching_min_ttl = 1
    error_code            = 501
    response_code         = null
    response_page_path    = ""
  },
  {
    error_caching_min_ttl = 1
    error_code            = 502
    response_code         = null
    response_page_path    = ""
  },
  {
    error_caching_min_ttl = 1
    error_code            = 503
    response_code         = null
    response_page_path    = ""
  },
  {
    error_caching_min_ttl = 1
    error_code            = 504
    response_code         = null
    response_page_path    = ""
  }
]