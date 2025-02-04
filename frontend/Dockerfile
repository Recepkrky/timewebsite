# Use the official Node.js image
FROM node:18

# Set the working directory inside the container
WORKDIR /odev

# Copy package.json and install dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# Copy the rest of the React app files
COPY . .

# Build the React app
RUN npm run build

# Install a simple web server to serve the React build
RUN npm install -g serve

# Expose port 3000
EXPOSE 3000

# Serve the built React app
CMD ["serve", "-s", "build", "-l", "3000"]