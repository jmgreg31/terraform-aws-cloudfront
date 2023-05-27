# Contributing

Contributions are open and welcome!  Please follow the guidelines below.

## Pull Request Process

Submit a PR to the `master` branch

1. Update `README.md` documentation with any applicable changes.
2. Update `CHANGELOG.md` with the details of the change.  Please follow the format below:

    ```sh
    ## UNRELEASED (<MONTH><YEAR>)
    ```

3. Update the [VERSION](https://github.com/jmgreg31/terraform-aws-cloudfront/blob/master/VERSION) numbers to the new version that this Pull Request would represent. The versioning scheme used is [SemVer](http://semver.org/).

## Testing

To help ensure the validity of changes, and that the examples provided are accurate, the example folder will also serve as the testing space.  Due to limitations of Travis CI and encrypted variables (see [HERE](https://docs.travis-ci.com/user/pull-requests/#pull-requests-and-security-restrictions)), all PR's to `master` will be from the `staging` branch and must be submitted by a repo maintainer.  Should the tests fail, the contributer will make changes and submit updates back to the `staging` branch.
