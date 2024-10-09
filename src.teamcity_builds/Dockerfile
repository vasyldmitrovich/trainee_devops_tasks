# Dockerfile for Spark application with a custom JAR
FROM bde2020/spark-master:3.1.1-hadoop3.2

LABEL authors="vbazhan"

# Copy the JAR file into the container
COPY my-file.jar /opt/spark/jars/

# Set up the entry point to launch Spark shell with the custom JAR
ENTRYPOINT ["/spark/bin/spark-shell", "--jars", "/opt/spark/jars/my-file.jar"]
