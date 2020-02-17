# Contributing

Contributions are open and welcome!  Please follow the guidelines below.

## Pull Request Process

Submit a PR to the `staging` branch

1. Update the README.md with details of changes.
2. Update the CHANGELOG.md with the details of the change.  Please follow the format below:
    ```sh
    ## UNRELEASED (<MONTH><YEAR>)
    ```
3. Update the [VERSION](https://github.com/jmgreg31/terraform-aws-cloudfront/blob/master/VERSION) numbers to the new version that this Pull Request would represent. The versioning scheme used is [SemVer](http://semver.org/).
4. Update the [EXAMPLE](https://github.com/jmgreg31/terraform-aws-cloudfront/blob/master/example) terraform to reflect your changes.  Please make sure the [SOURCE](https://github.com/jmgreg31/terraform-aws-cloudfront/blob/master/example/main.tf#L142) is `git::https://github.com/jmgreg31/terraform-aws-cloudfront.git?ref=staging`

## Testing

To help ensure the validity of changes, and that the examples provided are accurate, the example folder will also serve as the testing space.  Due to limitations of Travis CI and encrypted variables (see [HERE](https://docs.travis-ci.com/user/pull-requests/#pull-requests-and-security-restrictions)), all PR's to `master` will be from the `staging` branch and must be submitted by a repo maintainer.  Should the tests fail, the contributer will make changes and submit updates back to the `staging` branch.