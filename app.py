import redis
import time
import streamlit as st
import yaml

with open("config.yml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)
    
# connect to Redis
redis_conn = redis.Redis(config['host'], config['port'])

# define function to retrieve value from Redis
def get_redis_value(key):
    return redis_conn.get(key)

# define function to display label and value in Streamlit
def display_redis_value(label, value):
    st.write(f"{label}: {value}")

# main function
def main():
    # set up Streamlit app
    st.title("Redis Value Display")

    # define key to retrieve from Redis
    key = "my_key"

    # continuously refresh value from Redis and display in Streamlit
    while True:
        # retrieve value from Redis
        value = get_redis_value(key)

        # display label and value in Streamlit
        display_redis_value("My Label", value)

        # wait for 100ms before refreshing
        time.sleep(0.1)

if __name__ == "__main__":
    main()
