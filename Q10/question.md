Audit this workflow. Report exactly which of the six findings below are present — no more, no fewer. Some patterns in the file look dangerous but are in fact safe, and some safe-looking ones are not.

Finding codes
W1  Untrusted pull-request code runs in a privileged context
W2  A third-party action is not pinned to a full commit SHA
W3  Workflow-level permissions are broader than any job needs
W4  A secret is written to the build log
W5  A production deploy has no environment approval gate
W6  Attacker-controlled event data is interpolated into a shell command
Rules the audit applies
Actions under the actions/ namespace are first-party and may be referenced by major tag. Third-party actions must be pinned to a full 40-character commit SHA.
A secret is "written to the build log" only if its value can appear in step output. Passing a secret through env: to a script that does not print it is acceptable.
Interpolating ${{ … }} attacker-controlled event data directly into a shell command is script injection. Passing the same value through env: and referencing the shell variable is safe.
Workflow-level permissions are too broad if no job in the file needs the extra scopes.
A production deploy needs an environment: to attach approval protection.
.github/workflows/ci.yml
name: CI and release

on:
  pull_request_target:
    branches: [main]
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  pr-preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - uses: deploy-tools/setup-action@v3
      - name: Install and build
        run: npm ci && npm run build
      - name: Label the build
        run: |
          echo "Building $PR_TITLE" >> notes.txt
        env:
          PR_TITLE: ${{ github.event.pull_request.title }}
      - name: Upload preview
        uses: actions/upload-artifact@v4
        with:
          name: preview
          path: dist/

  unit-tests:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    strategy:
      fail-fast: false
      matrix:
        node: [20, 22]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm ci && npm test

  deploy-prod:
    needs: [unit-tests]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: production
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: deploy-tools/deploy-action@59c72a23093f37b0daf0af3a4a625f118351da38
        with:
          project: storefront
      - name: Show configuration
        run: echo "registry token is ${{ secrets.REGISTRY_TOKEN }}"
      - name: Deploy
        run: ./scripts/deploy.sh --env production
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
Answer both parts
The finding codes present, comma-separated in ascending order (e.g. W1,W3,W5).
The id of the single job an untrusted outside contributor can abuse to run their own code in a privileged context.
Answer as codes|job-id