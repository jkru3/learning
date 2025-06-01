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