# Use NGINX as the base image
FROM --platform=linux/amd64 nginx

# Set working directory to NGINX HTML directory
WORKDIR /usr/share/nginx/html/

# Copy files from the local 'server' directory to the container
COPY ./server/ .

# Install necessary packages including Node.js and node-http-server
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g node-http-server && \
    apt-get clean

# Expose port 8080
EXPOSE 8080

# Optional: Add a CMD command to start node-http-server if needed
 CMD ["node-http-server","." ,"--port", "8080"]
