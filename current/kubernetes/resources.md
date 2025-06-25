Install and set up the kubectl tool: https://kubernetes.io/docs/tasks/tools/

Install Minikube: https://minikube.sigs.k8s.io/docs/start/

Install VirtualBox: https://www.virtualbox.org/wiki/Downloads

https://www.virtualbox.org/wiki/Linux_Downloads

Minikube Tutorial: https://kubernetes.io/docs/tutorials/hello-minikube/

If the minikube installation has been done on the macOS, then to access the URL on the local browser, we need to do a few steps to get the service URL to work. Those steps are covered on this documentation page: https://minikube.sigs.k8s.io/docs/handbook/accessing/#using-minikube-service-with-tunnel

---

Kubeadm makes bootstrapping a Kubernetes cluster significantly easier compared to doing it manually, but "easy" is relative depending on your experience and requirements.

**What kubeadm does well:**

- Automates most of the complex setup tasks like generating certificates, configuring etcd, and setting up the control plane components
- Provides a standardized, repeatable process that follows Kubernetes best practices
- Handles the tricky parts of cluster initialization, node joining, and component configuration
- Creates a production-ready cluster foundation rather than just a development setup

**The straightforward parts:**

- Basic cluster initialization is literally just `kubeadm init` followed by `kubeadm join` on worker nodes
- Clear, well-documented workflow with predictable steps
- Built-in validation and preflight checks catch common issues early

**Where complexity creeps in:**

- You still need to handle networking (installing a CNI plugin like Weave Net, Calico, or Flannel)
- Certificate management and rotation requires understanding
- Load balancer setup for high availability control planes
- Storage configuration and persistent volume setup
- Security hardening and RBAC configuration