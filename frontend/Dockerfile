# Step 1: Build React App
FROM node:18 AS builder

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./

RUN npm install

COPY . .

# Enable legacy OpenSSL provider
ENV NODE_OPTIONS=--openssl-legacy-provider

RUN npm run build

# Step 2: Serve with Nginx
FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
