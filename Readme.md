# How to use this repository

## Purpose

This code shows a very simple example how to setup GitHub Actions workflow so that your code is automatically tested when pushed into a branch in repository. Once a code is committed and pushed the workflow performs a set of commands to lint and test the code.

### Makefile

The repository contains `makefile` that defines various steps in the overall process - installation, linting and test. It is a lot easier to execute `make install` compared to `pip install --upgrade pip && pip install -r requirements` all the time. It also simplifies the final `github-actions-demo.yml` config file and makes it more readable. The makefile is not necessary in case you want to execute python commands, but make the process a lot more convenient.

### Sample modules

`math_functions.py` and `test_math_functions/pz` define simple functions and respective tests to illustrate the whole concept of Continous Integration. Once a code is changed or added a respective test should be created to reflect it (or start with the test and write the code to PASS the test - even better.)

### .github/workflows directory

As per the instructions on GitHub page, this is the directory that defines respective action to be performed. `github-actions-demo.yml` configures the workflow. In a nutshell, here are the steps to be performed:

-   the workflow gets trigerred on push to `main` and `chapter-1` branches or on pull request from these branches
-   `ubuntu-latest` is the GitHub environment to run the workflow on (more in [GitHub documentation](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners]))
-   `actions/checkout@v2` will checkout the code from our branch for use
-   `actions/setup-python@v1` prepares respective Python environment we will work with (in our case 3.8.12)
-   next section defines the necessary installation steps to install required libraries (`pylint, coverage, pytest`)

### Workflow execution and results

Upon a commit to `main` branch of the repository a workflow will be trigerred with all defined steps being executed. You can check the status of the worklow in `Actions` tab under `GitHub Actions Demo`. If all goes well and you end up with a successful run, your code has been automatically tested with passing tests.
