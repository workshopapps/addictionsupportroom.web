
FROM node:16.18.1 as builder-step

WORKDIR /frontend

COPY package*.json /frontend/

RUN npm install 

COPY . /frontend/

RUN npm run build

EXPOSE 3000

FROM nginx:alpine

COPY --from=builder-step /frontend/build /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
