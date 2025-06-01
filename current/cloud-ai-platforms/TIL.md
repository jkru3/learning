# 05/31/2025
TPUs are made by google and currently not consumer facing

**typical ML workflow**
you do this after defining your prediction task
1. ingest the data
2. analyze it
3. transform it
4. create + train model
6. evaluate model for efficiency and optimization
7. deploy and make predictions

## Vertex AI
Vertex AI is Google Cloud's comprehensive, managed platform for machine learning (ML). It provides a high-level abstraction of tools to handle the entire ML lifecycle. When you use Vertex AI Pipelines, you're leveraging a managed service that runs on Kubeflow Pipelines technology under the hood.

Kubeflow Pipelines is an open-source system for orchestrating ML workflows. These workflows consist of steps (like data processing or model training) that run as containers. When executed on Google Cloud, these steps typically run on GKE (Google Kubernetes Engine).

GKE is Google's managed Kubernetes service. It simplifies running containerized applications by abstracting away the complexities of managing Kubernetes clusters yourself. This means you don't have to worry about the underlying infrastructure, like maintaining the Kubernetes control plane or individual server nodes.

Cloud ML Engine was a part of Cloud AI and is a predecessor to Vertex AI. Cloud AI is still around, but Vertex AI has taken it’s use cases

## GOOGLE Vizier

GCP's general purpose black-box optimization service. Define parameters for *any* system. Performs the intelligent search and optimization
- A/B testing
- engineering simulations
- search algorithms
    - Bayesian optimization

## Google Compute Engine
- provides the hardware for the applications to run on
- are the hosts for docker containers
---