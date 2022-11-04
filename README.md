<h1 align="center">
  Consent Building Block (Govstack)
</h1>

<p align="center">
  [![CircleCI](https://circleci.com/gh/GovStackWorkingGroup/bb-consent.svg?style=svg)](https://circleci.com/gh/GovStackWorkingGroup/bb-consent)
  <a href="../commits/" title="Last Commit"><img src="https://img.shields.io/github/last-commit/GovStackWorkingGroup/bb-consent?style=flat"></a>
  <a href="../issues" title="Open Issues"><img src="https://img.shields.io/github/issues/GovStackWorkingGroup/bb-consent?style=flat"></a>
  <a href="./LICENSE" title="License"><img src="https://img.shields.io/badge/License-Apache%202.0-green.svg?style=flat"></a>
</p>

<!--TODO: Update the TOC-->
<p align="center">
  <a href="#about">About</a> •
  <a href="#release-status">Release Status</a> •
  <a href="#core-team">Core Team</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#consent-specs-in-gitbook">Specification in Gitbook</a> •
  <a href="#repo-structure">Repo structure</a> •
</p>

## About

Consent BB defines the principles, functions and architecture of an information system that enables services for individuals to approve the use of her/his personal data and for information system operators that process personal data of individuals to know the will of the individual and legitimately process such personal data.

It is a process-oriented GovStack BB facilitating auditable bilateral agreement within a multi-agent environment, that integrates with most other BBs.

This repository contains the deliverables from Consent BB team, as part of the Govstack project.

## Core Team

* Ain Aaviksoo ([ain.aaviksoo@guardtime.com](ain.aaviksoo@guardtime.com))
* Benjamin Balder Bach ([balder@overtag.dk](balder@overtag.dk)) 
* Philippe Page ([philippe.page@humancolossus.org](philippe.page@humancolossus.org))
* Lal Chandran ([lal@igrant.io](lal@igrant.io))

Working Group Representative: Ramkumar ([psramkumar2@gmail.com](psramkumar2@gmail.com))

## Release Status

All diagrams and API specifications contained here are subject to ongoing changes by an internal GovStack Working Group, following this roadmap:

* Wave 2, Internal Review (July 14th, 2022)
* Release certification (30 September 2022)
* Limited publication (Deadline TBA)
* Community-wide publication (~August 2022)

## Contributing

Feel free to improve the plugin and send us a pull request. If you found any problems, please create an issue in this repo.

## Consent specs in Gitbook

Govstack specs are published at [Gitbook - Govstack Global](https://docs.govstack.global/).

Note that pushes to the `main` branch will automatically trigger a Gitbook build
and deployment from the `/spec` directory.

## Repo Structure

```sh
README.md
/spec # the markdown files which are used to build the specification in GitBook
/api # the openapi specification
/test # the test plan and tests
  plan.md
/examples # examples for deploying, configuring, and testing applications which implement the behaviors specified by this building block
  /application-a
    README.md # instructions for deployment/testing
    docker-compose.yaml # example deployment file
      db
      web
      adaptor
      security-server
    Caddyfile # example config for "adaptor"
    Dockerfile # dockerfile to build "adaptor"
  /application-b
  /application-c
```
