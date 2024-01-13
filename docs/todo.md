# TODO
1. Refactoring: Use state of art design. Use Design Patterns
2. Add Tests: Implement CICD, (Docker and Deployment)
3. Add Airflow: Orchestrate Job using Airflow

Initial Outline:

1. Setup various source for kafka like:
   - A docker image producing data to websocket. 
   - An API based app in python that is continuously generating data. 
   - An existing API like weather API, Twitter API etc 
