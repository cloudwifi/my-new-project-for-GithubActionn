FROM node:14

WORKDIR /app

# Copy package files first for better caching
COPY package.json ./
COPY package-lock.json ./

# Optional: REMOVE web-vitals if you don’t use it
RUN npm uninstall web-vitals || true

# Install dependencies
RUN npm install

# Copy rest of the app
COPY . .

# Expose port 8080 for React dev server
EXPOSE 8080

# Start with port override (React uses 3000 by default)
ENV PORT=8080

# Start the frontend app
CMD ["npm", "start"]
