# Use an official Node.js runtime as a parent image
FROM node:16.18.0 as build

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the rest of the application code to the container
COPY . .

# Build the application
RUN npm run build

# Use an official Nginx runtime as a parent image
FROM nginx:1.21-alpine

# Copy the build output to the Nginx document root
COPY --from=build /app/dist/laundromat-fe /usr/share/nginx/html

#Copy nginx configuration
COPY --from=build /app/nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]