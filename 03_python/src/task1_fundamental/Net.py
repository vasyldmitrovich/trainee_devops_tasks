import requests
import http.client
import urllib.request
import aiohttp
import asyncio
import socket
import httpx
from flask import Flask, jsonify
from fastapi import FastAPI
import pycurl
from io import BytesIO

print("Working with network")


# Function to demonstrate various network requests
def main():
    print("=== Using requests library ===")
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print("GET Request (requests):", response.json())

    print("\n=== Using http.client ===")
    connection = http.client.HTTPSConnection('jsonplaceholder.typicode.com')
    connection.request('GET', '/posts/1')
    response = connection.getresponse()
    print("GET Request (http.client):", response.read().decode())
    connection.close()

    print("\n=== Using urllib ===")
    response = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts/1')
    data = response.read().decode()
    print("GET Request (urllib):", data)

    print("\n=== Using aiohttp (asynchronous) ===")

    async def fetch_data_aiohttp():
        async with aiohttp.ClientSession() as session:
            async with session.get('https://jsonplaceholder.typicode.com/posts/1') as response:
                data = await response.json()
                print("GET Request (aiohttp):", data)

    asyncio.run(fetch_data_aiohttp())

    print("\n=== Using socket for low-level TCP connection ===")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('jsonplaceholder.typicode.com', 80))
    sock.sendall(b'GET /posts/1 HTTP/1.1\r\nHost: jsonplaceholder.typicode.com\r\n\r\n')
    response = sock.recv(4096)
    print("GET Request (socket):", response.decode())
    sock.close()

    print("\n=== Using httpx (asynchronous) ===")

    async def fetch_data_httpx():
        async with httpx.AsyncClient() as client:
            response = await client.get('https://jsonplaceholder.typicode.com/posts/1')
            print("GET Request (httpx):", response.json())

    asyncio.run(fetch_data_httpx())

    print("\n=== Using Flask to create a simple web server ===")
    app = Flask(__name__)

    @app.route('/posts/1', methods=['GET'])
    def get_post_flask():
        return jsonify({"userId": 1, "id": 1, "title": "sample title", "body": "sample body"})

    # To run the Flask server, uncomment the line below
    # app.run(debug=True)

    print("\n=== Using FastAPI to create an async web server ===")
    fastapi_app = FastAPI()

    @fastapi_app.get('/posts/1')
    async def get_post_fastapi():
        return {"userId": 1, "id": 1, "title": "sample title", "body": "sample body"}

    # To run the FastAPI server, uncomment the line below
    # uvicorn.run(fastapi_app, host="127.0.0.1", port=8000)

    print("\n=== Using pycurl for sending requests ===")
    buffer = BytesIO()
    curl = pycurl.Curl()
    curl.setopt(curl.URL, 'https://jsonplaceholder.typicode.com/posts/1')
    curl.setopt(curl.WRITEDATA, buffer)
    curl.perform()
    curl.close()

    body = buffer.getvalue().decode('utf-8')
    print("GET Request (pycurl):", body)

    print("\n=== Using requests for POST request ===")
    data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
    print("POST Request (requests):", response.json())


if __name__ == "__main__":
    main()
