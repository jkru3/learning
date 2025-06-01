# 2025/05/31

- uses LXC containers (linux containers), which provides the core container runtime
- LXD adds management, networking, and user experience improvements
- LXCFS enhances process isolation by virtualizing system information

better than VMs because it doesn't need hypervisor and it's own OS for each application
hypervisor is software that creates and manages virtual machines (VMs) by abstracting and sharing the physical hardware resources of a host system

*virtual machines (hosts) run docker containers*
you provision a VM for hundreds or thousands of containers

you can just run docker images `docker run -it ubuntu bas` and then play around with it! this lets you try things out without having to build every time! Note: -it means input -> text

> "It's like having an unlimited supply of clean whiteboards"

unlike VMs, containers are not supposed to run OS, only run an application

## three levels of scale
- docker compose
- docker swarm
- kubernetes

data written to a db persists even after a container stops and is destroyed because the volume is mounted to it

images for google stored at gcr.io

---