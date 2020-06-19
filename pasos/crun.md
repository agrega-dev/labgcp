git clone https://github.com/agrega-dev/labgcp.git

export PROJECT_ID=xxxxx

export DOCKER_IMG=gcr.io/$PROJECT_ID/labgcp

cambiar directorio

gcloud builds submit --tag $DOCKER_IMG

gcloud container images list

docker pull $DOCKER_IMG

Despliegue
gcloud run deploy labgcp --image $DOCKER_IMG  --platform managed --allow-unauthenticated

