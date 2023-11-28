@method=GET @endpoint=/config/policy/{policyId}/

Feature: A data controller can perform basic CRUDL operations on Policies

  Note: The Consent BB is not currently aware of users and permissions.
  Therefore, all tests should contain stub implementations for users and access.

@unit @positive
Scenario: A data controller of an Organization can read a Policy.

  This generic scenario implements UC-C-PIC-A-003.

  Given an organization admin user with access to read configuration
  And an Example Policy for Test Organization exists
  When The User fetches Example Policy for Test Organization
  Then Example Policy for Test Organization is returned
