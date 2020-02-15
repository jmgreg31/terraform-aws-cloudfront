# Contributing

Contributions are open and welcome!  Please follow the guidelines below.

## Pull Request Process

1. Update the README.md with details of changes.
2. Update the CHANGELOG.md with the details of the change.  Please follow the format below:
    ```sh
    ## UNRELEASED (<MONTH><YEAR>)
    ```
3. Update the [VERSION](https://github.com/jmgreg31/terraform-aws-cloudfront/blob/master/VERSION) numbers to the new version that this Pull Request would represent. The versioning scheme used is [SemVer](http://semver.org/).
4. Ensure your PR is being properly tested.  Additional description below.

## Testing

To help ensure the validity of changes, and that the examples provided are accurate, the example folder will also serve as the testing space.  Please update the [SOURCE](https://github.com/jmgreg31/terraform-aws-cloudfront/blob/master/example/main.tf#L142) of the module to the location of the code you wish to merge.  For example, if you created a branch from the main repo and named it `testing`, the source would be updated to `source = git::https://github.com/jmgreg31/terraform_aws_cloudfront.git?ref=testing` 