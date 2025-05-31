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

Vertex AI is Google Cloud's comprehensive, managed platform for machine learning (ML). It provides a high-level abstraction of tools to handle the entire ML lifecycle. When you use Vertex AI Pipelines, you're leveraging a managed service that runs on Kubeflow Pipelines technology under the hood.

Kubeflow Pipelines is an open-source system for orchestrating ML workflows. These workflows consist of steps (like data processing or model training) that run as containers. When executed on Google Cloud, these steps typically run on GKE (Google Kubernetes Engine).

GKE is Google's managed Kubernetes service. It simplifies running containerized applications by abstracting away the complexities of managing Kubernetes clusters yourself. This means you don't have to worry about the underlying infrastructure, like maintaining the Kubernetes control plane or individual server nodes.


---