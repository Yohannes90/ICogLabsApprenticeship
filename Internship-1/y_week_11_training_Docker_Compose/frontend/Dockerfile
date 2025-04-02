# Use official node runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy everything
COPY . .

# Install dependecies
RUN npm install

# Expose port 5173 for the Vite react app
EXPOSE 5173

# Run the react app
CMD ["npm", "run", "dev"]
