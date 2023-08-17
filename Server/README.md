# Sensor Sync Hub - Server

Welcome to the Sensor Sync Hub server! This project demonstrates a gRPC service for streaming sensor values from ESP32 devices to a microservice application. It provides functionalities to stream sensor values, retrieve registered values for specific devices, and list connected devices.

## Table of Contents

- [Getting Started](#getting-started)
  - [Configuration](#configuration)
  - [Running the Service](#running-the-service)
- [Generating Proto Files](#generating-proto-files)
- [Contributing](#contributing)

## Getting Started

To get started with the SensorStreamService project, follow the steps below:

### Configuration

Before running the service, make sure to configure the following environment variables in a `.env` file or by directly setting them in your environment:

```env
# MQTT Broker Configuration
MQTT_BROKER_HOST=your_mosquitto_broker_host
MQTT_BROKER_PORT=1883

# PostgreSQL Database Configuration
DB_HOST=your_postgresql_host
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

Replace `your_mosquitto_broker_host`, `your_postgresql_host`, `your_database_name`, `your_database_user`, and `your_database_password` with your actual configuration details.

### Running the Service

Make sure you have Docker and Docker Compose installed on your system.

Navigate to the root directory of the project.

Run the following command to start the service along with the necessary dependencies (Mosquitto broker and PostgreSQL database):

```bash
docker-compose up -d
```

**Optional:** Using VS Code DevContainers

If you're using Visual Studio Code, you can take advantage of DevContainers for a consistent development environment. Simply open the project in VS Code and the DevContainer configuration will set up the required environment automatically.

The service should now be up and running. You can create gRPC clients to interact with the service.

## Generating Proto Files

The gRPC server and client code can be generated from the `server.proto` file located in the `server/` directory. To generate the code, you can use the Protocol Buffers compiler (`protoc`). Here's an example command for generating Python code:

```bash
protoc -I=server/ --python_out=client/ --grpc_python_out=client/ server/server.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. data-manager.proto
```

Replace `client/` with the appropriate output directory for your chosen programming language.

## Contributing

Contributions to the SensorStreamService project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and ensure they are properly tested.

4. Commit your changes and create a pull request.

5. Your pull request will be reviewed, and once approved, it will be merged into the main repository.

Thank you for contributing to this project!
