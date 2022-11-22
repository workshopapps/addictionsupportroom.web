
FROM node:16.10.0 as build

WORKDIR /frontend

COPY package*.json /frontend

RUN npm install 

COPY . /frontend

RUN npm run build

EXPOSE 3000

COPY --from=builder /frontend/build /usr/share/nginx/html

COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
