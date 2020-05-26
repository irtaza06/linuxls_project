# Udacity-Capstone-project


* Creat a Djano blog app following the tutorials on [youtube]([https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p])
* First manually
  * Build a docker image of the Django app served on apace2 webserver 
  * Push docker image to [dockerhub]([https://hub.docker.com/repository/docker/irtaza06/linuxls])
* Make a Jenkins pipeline which creates a EKS k8s cluster
* Make a pipeline which has following stages
  * Lint Django-Project
  * Lint Dockerfile
  * Build Docker Image
  * Push Docker Image
  * Create blue replication controller
  * Create green replication controller
  * Create bg-service/Loadbalancer
  * Update service/redirect to green
  * Remove Image Locally
Note: eksctl is used to provision a k8s cluster which under the hood uses a cloudformation script. 
