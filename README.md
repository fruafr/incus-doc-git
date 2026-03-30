# incus-doc-git

Combines [Incus](https://linuxcontainers.org/incus/docs/main/) documentation from [its git repo](https://github.com/lxc/incus) in a single file ready for AI consumption.

The combined file is [incus-doc-git.txt](./incus-doc-git.txt).

## Introduction

Incus is a truly free open-source command-line container and virtual machine manager. 

It provides a unified experience for running and managing :
- full Linux systems inside containers (shares the host kernel).
- full Linux or non-Linux systems in virtual machines (UEFI or not). 
- OCI container images (similar to Docker or Podman).

Incus supports container and virtual-machine images for a large number of Linux distributions (official Ubuntu images and images provided by the community).

It scales from one instance on a single machine to a cluster in a full data center rack, making it suitable for running workloads both for development and in production.

Incus allows you to easily set up a system that feels like a small private cloud. You can run any type of workload in an efficient way while keeping your resources optimized.

## Purpose of this repo

- To contain a cleaned copy of [the documentation of incus found in its git repo](https://github.com/lxc/incus/tree/main/doc) in the [/doc](./doc) folder
- To contain a [single file combining the documentation](./incus-doc-git.txt) for AI consumption.

## Official sources of documentation
- [Incus - Documentation (on linuxcontainers)](https://linuxcontainers.org/incus/doc/main)
- [Incus - Github](https://github.com/lxc/incus)
  - [doc/explanation](https://github.com/lxc/incus/tree/main/doc/explanation)
  - [doc/howto](https://github.com/lxc/incus/tree/main/doc/howto)
  - [doc/reference](https://github.com/lxc/incus/tree/main/doc/reference)

## Note
- Date of extraction : Check the [extraction-date.txt](./extraction-date.txt) file.
- The content of the [doc/incus](./doc/incus) folder was extracted automatically from the git doc folder (with cleaning).
- Generation scripts found in the [scripts](./scripts) folder. The complete extraction cycle is controlled by [scripts/refresh.sh](./scripts/refresh.sh)
