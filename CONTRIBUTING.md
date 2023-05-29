# Contributing

Contributions are open and welcome!  Please follow the guidelines below.

## Guidelines

This repo leverages GitHub Actions to help facilitate CICD workflows.  In the context of contributions, the CI workflow is initiated with a Pull Request to the `master` branch.

- Update the [VERSION](https://github.com/jmgreg31/terraform-aws-cloudfront/blob/master/VERSION) numbers to the new version that this Pull Request would represent. The versioning scheme used is [SemVer](http://semver.org/).
- Update `CHANGELOG.md` with the details of the change.  Please follow the format below:

    ```sh
    ## UNRELEASED (<MONTH><YEAR>)
    ```

- If applicable, Apply updates to `/example/*` files to test the proposed feature/fix.
- If applicable, Update `README.md` documentation with any applicable changes.

## Testing

To help ensure the validity of changes, and that the examples provided are accurate, the example folder will also serve as the integration testing space.  These are executed as part of the `Terraform - Staging` GitHub Action when a PR is submitted.  The action will take care of modifying the example/main.tf to a relative path source, to ensure the propsed changes are being accurately tested.  Any additional troubleshooting can be done by viewing the GitHub Action logs.
