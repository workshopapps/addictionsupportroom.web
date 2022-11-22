
FROM node:11.1.0-alpine as build

WORKDIR /frontend

COPY package*.json /frontend/

RUN npm install -g

COPY ./ /frontend/

RUN npm run build

FROM nginx:1.15.8-alpine

COPY --from=build /app/build /usr/share/nginx/html
COPY --from=build /app/nginx/nginx.conf /etc/nginx/nginx.conf

EXPOSE 3000

# ENTRYPOINT [ "nginx", "-g", "daemon off;" ]