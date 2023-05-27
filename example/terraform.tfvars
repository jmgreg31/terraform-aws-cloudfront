create_cf                = true
alias                    = []
comment                  = "AWS Cloudfront Module"
enable                   = true
enable_ipv6              = true
http_version             = "http1.1"
minimum_protocol_version = "TLSv1.1_2016"
price                    = "PriceClass_100"
region                   = "us-east-1"
restriction_type         = "none"
iam_certificate_id       = "sslcert"
ssl_support_method       = "sni-only"
tag_name                 = "AWS Cloudfront Module"
additional_tags = {
  Test1 = "Test1"
}
webacl = "webaclid"

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
    custom_header = [
      {
        name  = "Test"
        value = "Test-Header"
      },
      {
        name  = "Test2"
        value = "Test2-Header"
      }
    ]
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
    custom_header = [
      {
        name  = "Test"
        value = "Test-Header"
      },
      {
        name  = "Test2"
        value = "Test2-Header"
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
    member = [
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
    allowed_methods        = ["GET", "HEAD", "OPTIONS", "POST", "PUT", "DELETE", "PATCH"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "mydomainorigin.google.com"
    compress               = false
    query_string           = true
    cookies_forward        = "all"
    headers                = ["*"]
    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 0
    max_ttl                = 0
    lambda_function_association = [
      {
        event_type   = "viewer-request"
        lambda_arn   = "arn:aws:lambda:us-east-1:123456789012:function:my-function"
        include_body = true
      }
    ]
    function_association = [
      {
        event_type   = "viewer-request"
        function_arn = "arn:aws:cloudfront::123456789012:function/my-cf-function"
      }
    ]
  }
]

dynamic_ordered_cache_behavior = [
  {
    path_pattern           = "/test1/"
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
    lambda_function_association = [
      {
        event_type   = "viewer-request"
        lambda_arn   = "arn:aws:lambda:us-east-1:123456789012:function:my-function"
        include_body = true
      },
      {
        event_type   = "viewer-response"
        lambda_arn   = "arn:aws:lambda:us-east-1:123456789012:function:my-function2"
        include_body = true
      }
    ]
  },
  {
    path_pattern           = "/test2/"
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "S3-domain-cert"
    compress               = false
    query_string           = true
    cookies_forward        = "all"
    headers                = []
    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 0
    max_ttl                = 0
    response_headers_policy_id = "60669652-455b-4ae9-85a4-c4c02393f86c"
  }
]

dynamic_custom_error_response = [
  {
    error_code = 400
  },
  {
    error_caching_min_ttl = 10
    error_code            = 403
  },
  {
    error_caching_min_ttl = 1
    error_code            = 404
    response_code         = 200
    response_page_path    = "/error/200.html"
  },
  {
    error_code         = 405
    response_code      = null
    response_page_path = ""
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
