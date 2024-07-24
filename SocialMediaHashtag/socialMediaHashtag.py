import time
import streamlit as st
import boto3
import json
from datetime import datetime 
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


# Initialize AWS clients
# Initialize AWS clients
try:
   AWS_ACCESS_KEY_ID = 'id'
   AWS_SECRET_ACCESS_KEY = 'key'

   session = boto3.Session(
       aws_access_key_id='',
       aws_secret_access_key='',
       region_name='us-east-1'
   )
   dynamodb = session.client('dynamodb')
   lambda_client = session.client('lambda')

except  (NoCredentialsError, PartialCredentialsError) as e:
   print("AWS credentials not found. Please configure your AWS credentials.")
   
# Streamlit App
st.title("InstaBook")

# Input fields for post text and hashtags
post_text = st.text_area("Compose your post")
hashtags = st.text_input("Hashtags (comma separated)")

if st.button("Publish"):
    if post_text and hashtags:
        hashtags_list = hashtags.split(',')
        post_data = {
            'text': post_text,
            'hashtags': hashtags_list,
                }
        try:
            # Invoke AWS Lambda to process and store the post
            response = lambda_client.invoke(
                FunctionName='testlamda',
                InvocationType='Event',
                Payload=json.dumps(post_data)
            )
            st.success("Post published successfully!")
        except Exception as e:
            st.error(f"Failed to publish post: {e}")
    else:
        st.error("Please enter both post text and hashtags.")

def fetch_trending_hashtags():
    try:
        # Call your Lambda function to fetch trending hashtags
        response = lambda_client.invoke(
            FunctionName='testhashtagcounter',
            InvocationType='RequestResponse'
        )
        trending_hashtags = json.loads(response['Payload'].read())
        return trending_hashtags
    except Exception as e:
        st.error(f"Failed to fetch trending hashtags: {e}")
        return []

st.sidebar.title("Trending Hashtags")
while True:
    st.sidebar.empty()
    trending_hashtags = fetch_trending_hashtags()
    json_string = json.dumps(trending_hashtags)
    data = json.loads(json_string)['body']
    hashtag_counts = json.loads(data)
    for hashtag, count in hashtag_counts:
        st.sidebar.write(f"{hashtag} : {count}")
    time.sleep(60)
