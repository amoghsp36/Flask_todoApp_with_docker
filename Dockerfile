FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# 4 layers are cached so the changes in code can be built much quicker
COPY . .

EXPOSE 8080

CMD [ "python3","todos.py" ]


# WORKDIR /app

# COPY . .

# RUN pip install -r requirements.txt

# EXPOSE 8080

# CMD [ "python3", "todos.py" ]

# after the initial build of the docker image the image layers are cached and the next time we build it,docker looks at the cache
# and retrieves the image layers

