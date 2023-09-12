FROM node:18.16-alpine AS build

WORKDIR /app/client

COPY ./ ./

RUN npm install -g serve 

FROM nginx:1.23.2-alpine

COPY --from=build /app/client/ /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]