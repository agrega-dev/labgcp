# Pasos para despliegue en Cloud Run

git clone https://github.com/agrega-dev/labgcp.git

#cambiar directorio a drectorio de labgcp

#cambiar la siguiente linea con el dato de projectID

export PROJECT_ID=projecdID

export DOCKER_IMG=gcr.io/$PROJECT_ID/labgcp


#copiar Dockerfile a directorio de proyecto

gcloud builds submit --tag $DOCKER_IMG

#gcloud container images list

#docker pull $DOCKER_IMG

Despliegue de container a Cloud run

gcloud run deploy labgcp --image $DOCKER_IMG  --platform managed --allow-unauthenticated
