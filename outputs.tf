output "name" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.domain_name
  description = "The domain name of the CloudFront distribution"
}
