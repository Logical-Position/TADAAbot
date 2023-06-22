# Git Strategy

This is modeled off the strategy described in [this article](https://nvie.com/posts/a-successful-git-branching-model/). The loose idea has since been modeled by GitHub in a method they simply call [flow](https://docs.github.com/en/get-started/quickstart/github-flow#following-github-flow).

This quote from GitHub is very useful in almost any context, even coding by yourself:

> **Tip:** Make a separate branch for each set of unrelated changes. This makes it easier for reviewers to give feedback. It also makes it easier for you and future collaborators to understand the changes and to revert or build on them. Additionally, if there is a delay in one set of changes, your other changes aren't also delayed.

To further this, please remember:

<aside>
⚠️ Work should never be performed directly on a ********main branch********. Create the appropriate type of ****************************support branch**************************** to make your changes.

</aside>

## Main Branches

`prod`

**********************Buds the initial `dev` branch**

************************************Consumes `release` and `hotfix` merges**

**********************PROTECTED.********************** This branch will require merge approval.

> always reflects a *production-ready* state
> 

`dev`

**Buds `release` and `feature` branches**

**Consumes `feature` and `hotfix` merges**

> always reflects a state with the latest delivered development changes for the next release
> 

## Support Branches

`release`

**Branches from `dev`**

**Merges into `dev`**

> Release branches support preparation of a new production release. They allow for last-minute dotting of i’s and crossing t’s. Furthermore, they allow for minor bug fixes and preparing meta-data for a release (version number, build dates, etc.). By doing all of this work on a release branch, the `develop` branch is cleared to receive features for the next big release.
> 

`feature`

**************************************Branches from `dev`**

**************************Merges into `dev`**

> Feature branches (or sometimes called topic branches) are used to develop new features for the upcoming or a distant future release.
> 

`hotfix`

****************************************Branches from `prod`**

************************************Merges into `prod` and `dev`**

> Hotfix branches are very much like release branches in that they are also meant to prepare for a new production release, albeit unplanned.
> 

## Merging Branches

There are two important practices to follow when merging branches:

1. Use the `--no-ff` flag to prevent a fast-forward and preserve history. Without this, the commits will be squashed and will not appear to branch when visualizing the git history.
2. Delete the branch afterwards.

## Commit Messages

When writing a commit message, start it with a label following the Conventional Commits guide. Frequently used labels are:

- **build**: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- **ci**: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- **docs**: Documentation only changes
- **feat**: A new feature
- **fix**: A bug fix
- **perf**: A code change that improves performance
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **test**: Adding missing tests or correcting existing tests

## Resources

- A Successful Branching Model, https://nvie.com/posts/a-successful-git-branching-model/
- Angular Contributing Conventions, Commit Message Types; https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#type
- Conventional Commits, https://www.conventionalcommits.org/en/v1.0.0/
- GitHub Flow, https://docs.github.com/en/get-started/quickstart/github-flow#following-github-flow