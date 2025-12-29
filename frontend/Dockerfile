#build stage
FROM node:lts-alpine AS build-stage
WORKDIR /app
COPY . .
RUN npm install
ENV VITE_API_BASE_URL=http://localhost/backend
RUN npm run build
# production stage
FROM nginx:stable-alpine AS production-stage
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]