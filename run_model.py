import subprocess

def get_sentiment(blob):
  print(blob)
  with open('./blob.txt','w') as f:
      f.write(blob)
  args = ['java','-cp','./stanford-corenlp-full-2018-10-05/*','edu.stanford.nlp.sentiment.SentimentPipeline','-file','blob.txt']
  process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out, err = process.communicate()
  out = out.decode("utf-8")
  out_sentiment = out.rstrip().rsplit('\n',1)[-1].lstrip()
  if out_sentiment == 'Positive':
      return 1
  else:
      return 0

# print(get_sentiment("good good good blob"))
