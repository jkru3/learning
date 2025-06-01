# 05/30/2025
control plane is the single source of truth for kubernetes cluster and ensure a desired state
- kube-apiserver
- etcd
- kube-scheduler
- kube-controller-manager
- cloud-controller-manager 

**Borg** was a predecessor to Kubernetes and still used by Google (written in C++)
Kubernetes is written in GO

---
# 05/31/2025
control plane
1. etcd (kv store based on et-see-dee framework)
    - distributed k/v store used by kubernetes to manage the cluster
    - stores all cluster info
    - *stored on master*
2. API server
    - frontend for kubernetes
    - *held by the master*
    - cli
3. scheduler
    - distributes work or containers across multiple nodes
    - looks for newly created contrainers and assigns them
    - *held by the master*
4. controller
    - brain behind orchestration
    - noticing and responding when nodes go down
    - makes decisions on when containers should be spun up
    - *held by the master*
5. container runtime
    - underlying software used to run containers
6. kubelet
    - agent that runs on each node in the cluster
    - *held by workers* 

**kubectl** (kube control)
- kubernetes cli used to control and manage kubernetes apps on a cluster to get cluster related info, to get status of nodes, etc. 
- `kubectl run`: deploy applicatin on cluster
- `kubectl cluster-info`
- `kubeclt get nodes`

nodes is a machine, virtual or physical (used to be known as minions)
need more than one nodes. This is a **cluster**
then you have a **cluster master** (another node)

uses containerD
nerdctl for containerd
crictl for the Kubernetes Container Runtime Interface (only used for debugging)

applications < pods < nodes < clusters
replicasets < deployments

deployments allow rollbacks

## replication controller vs replica set
replication controller is older tech, being replaced by replica set

# 2025/06/01
services
1. NodePorts
    - internal APIs that other services consume
2. ClusterIP
3. LoadBalancer

typical kubernetes file structure looks like:
```bash
my-app/
├── README.md
├── Makefile                          # Common deployment commands
├── docker-compose.yml                # Local development
│
├── k8s/                             # Main Kubernetes manifests
│   ├── namespace.yaml
│   │
│   ├── frontend/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── ingress.yaml
│   │   └── configmap.yaml
│   │
│   ├── api/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── configmap.yaml
│   │   └── hpa.yaml                 # Horizontal Pod Autoscaler
│   │
│   ├── worker/
│   │   ├── deployment.yaml
│   │   └── configmap.yaml
│   │
│   ├── database/
│   │   ├── statefulset.yaml
│   │   ├── service.yaml
│   │   ├── pvc.yaml                 # Persistent Volume Claim
│   │   └── secret.yaml
│   │
│   ├── redis/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── configmap.yaml
│   │
│   ├── monitoring/
│   │   ├── prometheus/
│   │   │   ├── deployment.yaml
│   │   │   ├── service.yaml
│   │   │   └── configmap.yaml
│   │   └── grafana/
│   │       ├── deployment.yaml
│   │       ├── service.yaml
│   │       └── configmap.yaml
│   │
│   ├── jobs/
│   │   ├── db-migration-job.yaml
│   │   └── backup-cronjob.yaml
│   │
│   └── rbac/
│       ├── serviceaccount.yaml
│       ├── role.yaml
│       └── rolebinding.yaml
│
├── environments/                    # Environment-specific configs
│   ├── base/
│   │   ├── kustomization.yaml
│   │   └── common-configmap.yaml
│   │
│   ├── development/
│   │   ├── kustomization.yaml
│   │   ├── ingress-dev.yaml
│   │   └── patches/
│   │       ├── frontend-dev.yaml
│   │       └── api-dev.yaml
│   │
│   ├── staging/
│   │   ├── kustomization.yaml
│   │   ├── ingress-staging.yaml
│   │   └── patches/
│   │       ├── frontend-staging.yaml
│   │       └── api-staging.yaml
│   │
│   └── production/
│       ├── kustomization.yaml
│       ├── ingress-prod.yaml
│       ├── sealed-secrets.yaml      # Encrypted secrets
│       └── patches/
│           ├── frontend-prod.yaml
│           ├── api-prod.yaml
│           └── resource-limits.yaml
│
├── helm/                           # Alternative: Helm charts
│   ├── Chart.yaml
│   ├── values.yaml
│   ├── values-dev.yaml
│   ├── values-staging.yaml
│   ├── values-prod.yaml
│   └── templates/
│       ├── frontend/
│       ├── api/
│       ├── database/
│       └── _helpers.tpl
│
├── scripts/                        # Deployment and utility scripts
│   ├── deploy.sh
│   ├── rollback.sh
│   ├── port-forward.sh
│   └── logs.sh
│
├── secrets/                        # Secret management
│   ├── sealed-secrets/
│   ├── .env.example
│   └── generate-secrets.sh
│
├── monitoring/                     # Monitoring configs
│   ├── alerts/
│   │   └── app-alerts.yaml
│   ├── dashboards/
│   │   └── app-dashboard.json
│   └── service-monitors/
│       └── app-servicemonitor.yaml
│
├── docs/                          # Documentation
│   ├── deployment.md
│   ├── troubleshooting.md
│   └── architecture.md
│
└── .github/                       # CI/CD workflows
    └── workflows/
        ├── deploy-dev.yml
        ├── deploy-staging.yml
        └── deploy-prod.yml
```

kubernetes has **contexts** for each kubernetes project that you switch between