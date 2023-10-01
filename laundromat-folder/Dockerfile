FROM node:16.15.0-alpine AS build

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to /app
COPY package*.json ./

# Install dependencies
RUN npm ci --production

# Copy the rest of the application code to /app
COPY . .

# Build the application
RUN npm run build

# Use a smaller base image for the final image
FROM node:16.15.0-alpine

# Set the working directory to /app
WORKDIR /app

# Create a non-root user named "nest"
RUN addgroup -S nest && adduser -S nest -G nest

# Copy only the necessary files from the build image
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package.json ./package.json

# Change the ownership of the /app directory to the non-root user
RUN chown -R nest:nest /app

# Expose port 3000
EXPOSE 3000

# Switch to the non-root user
USER nest

# Run the application
CMD ["npm", "run", "start:prod"]