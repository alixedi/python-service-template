# python-service-template

This is a template for a Python Kubenetes service with batteries included e.g.:

1. Flask
2. Kubernetes
3. Pytest
4. Circle CI
5. Settings
6. Alchemy
7. Caching
8. Secrets
9. CLI (replaces Makefile, uses python-fire perhaps)
10. Logging
11. Monitoring
12. Feature flags
13. QA
14. Deployment 
15. Jobs (Using kubernetes jobs for heartbeat and having a model and monitoring setup)
16. Templates e.g. using Yasha?

...

9/1/2019

* I am feeling that we should probably include flask-sqlalchemy as a dependency. I just read the code for it and it does a bunch of things that we are not.
* That said, it is probably worth givine it a real go without flask-sqlalchemy. Trusting my instincts that we probably don't need 90% of functionality.
* 