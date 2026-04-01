# Maintainer Workflow

This document describes how maintainers review contributions and manage the FRAME‑online repository.

## 1. Responsibilities

- Review PRs for accuracy, clarity, and consistency  
- Ensure MkDocs builds cleanly  
- Maintain navigation and structure  
- Enforce writing guidelines  
- Manage issues and triage incoming reports  

## 2. Reviewing Pull Requests

1. Confirm the PR scope is clear and focused  
2. Run:

   ```bash
   mkdocs build
   ```

3. Check:
   - No warnings  
   - Navigation integrity  
   - Internal links  
   - File naming conventions  
   - Image placement  

4. Request changes if needed  
5. Approve and merge when ready  

## 3. Issue Triage

- **bug** → verify, label, assign  
- **documentation** → evaluate clarity and scope  
- **enhancement** → assess feasibility and alignment  

## 4. Release Process

The site deploys automatically via GitHub Pages.  
Maintainers ensure the main branch remains stable and buildable.

## 5. Governance

Decisions are made collaboratively among maintainers.  
Consensus is preferred; simple majority applies when needed.