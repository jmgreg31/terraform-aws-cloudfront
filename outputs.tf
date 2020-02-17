output "id" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.id
  description = "The identifier for the distribution. For example: EDFDVBD632BHDS5."
}

output "arn" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.arn
  description = "The ARN (Amazon Resource Name) for the distribution. For example: arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5, where 123456789012 is your AWS account ID."
}

output "caller_reference" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.caller_reference
  description = "Internal value used by CloudFront to allow future updates to the distribution configuration."
}

output "status" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.status
  description = "The current status of the distribution. Deployed if the distribution's information is fully propagated throughout the Amazon CloudFront system."
}

output "active_trusted_signers" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.active_trusted_signers
  description = "The key pair IDs that CloudFront is aware of for each trusted signer, if the distribution is set up to serve private content with signed URLs."
}

output "domain_name" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.domain_name
  description = "The domain name corresponding to the distribution. For example: d604721fxaaqy9.cloudfront.net."
}

output "name" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.domain_name
  description = "The domain name corresponding to the distribution. For example: d604721fxaaqy9.cloudfront.net."
}

output "last_modified_time" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.last_modified_time
  description = "The date and time the distribution was last modified."
}

output "in_progress_validation_batches" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.in_progress_validation_batches
  description = "The number of invalidation batches currently in progress."
}

output "etag" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.etag
  description = "The current version of the distribution's information. For example: E2QWRUHAPOMQZL."
}

output "hosted_zone_id" {
  value       = aws_cloudfront_distribution.cloudfront_distribution.*.hosted_zone_id
  description = "The CloudFront Route 53 zone ID that can be used to route an Alias Resource Record Set to. This attribute is simply an alias for the zone ID Z2FDTNDATAQYW2."
}
