#!/bin/bash

# Run Docker container with Spark
docker run -it your-spark-app scala <<EOF
:require /opt/spark/jars/your-file.jar
// Your Scala code here
println("Running Scala code with custom JAR")
EOF
