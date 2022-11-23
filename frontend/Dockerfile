
FROM node:16.18.1 as builder-step

WORKDIR /frontend

COPY package*.json /frontend/

RUN npm install 

COPY . /frontend/

RUN npm run build

EXPOSE 3000