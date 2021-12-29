# Documentation

These are the guide on how to set up gcloud and kubectl component and connect to

## Setting Up

Prerequisite:

1. install kubectx
2. install kubectl
3. install gcloud

## To authenticate with gcloud

Go to console and go to Kubernetes Engine console and click on the connect button which will pop up a command to be copied into your clipboard to run into your terminal.

enter the terminal(any terminal of your choice, cmd,windows shell,linux) and run them

```
gcloud auth login
```

```
gcloud config set project project-xxxx
```

```
gcloud container clusters get-credentials kubeflow-cluster --region asia-southeast1 --project project-xxxx
```

```
kubectx
```

```
kubectx gke_project-xxxx_asia-southeast1_kubeflow-cluster
```

```
k get pods -A
```

### Test run a sample pod

```
k run nginx -n default --image=nginx
# to clean up
k delete pod -n default nginx
```

## Installing kubeflow

Head to kubeflow website and download the binary

Kubeflow website - `https://www.kubeflow.org/docs/started/installing-kubeflow/`

```
gcloud components install kubectl kustomize kpt anthoscli beta
```

WIP

Installing via kustomize

python packages

1. tfx - python sdk, `pip install tfx`
2. tensorflow 2 or above


