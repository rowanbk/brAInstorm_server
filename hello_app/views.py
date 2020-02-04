from datetime import datetime
from flask import Flask, render_template, jsonify, request
from flask_cors import cross_origin
from . import app
import subprocess

@app.route("/")
def get_link():
    return jsonify({"response": "Hello from CORS Flask App"})

@app.route("/api/get_sentiment", methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def get_sentiment():
  req_data = request.get_json()
  with open('./json.txt','w') as f:
    f.write(str(req_data))
  #blob = req_data['blob']
  #with open('./blob.txt','w') as f:
    #f.write(blob)
  #args = ['java','-cp','./stanford-corenlp-full-2018-10-05/*','edu.stanford.nlp.sentiment.SentimentPipeline','-file','blob.txt']
  #process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  #out, err = process.communicate()
  #out = out.decode("utf-8")
  #out_sentiment = out.rstrip().rsplit('\n',1)[-1].lstrip()
  out_sentiment = 'Positive'
  if out_sentiment == 'Positive':
      sentiment = 1
  else:
      sentiment = 0

  return jsonify({"sentiment": sentiment})
