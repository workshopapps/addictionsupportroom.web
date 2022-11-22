
FROM node:16.10.0 as build

WORKDIR /frontend

COPY package*.json /frontend

RUN npm install 

COPY . /frontend

RUN npm run build

EXPOSE 3000

