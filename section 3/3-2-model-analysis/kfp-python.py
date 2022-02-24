import kfp
import json



# Here we create a kfp client and connect to the Kubeflow host exposing the KFP API. Kubeflow Pipeline API endpoint the url needs to be the global route to the istio-ingress gateway service on your cluster with a path to pipelines “/pipeline”. An example url is “https://istio-ingressgateway.domainname.com/pipeline”
client = kfp.Client(“Insert your Kubeflow host”) #http://localhost:3000 kubectl port-forward svc/ml-pipeline-ui 3000:80 --namespace kubeflow




newExperiment = client.create_experiment(name=”Insert Experiment Name”, namespace=”Insert namespace to run this experiment”)