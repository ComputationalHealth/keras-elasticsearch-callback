# keras-elasticsearch-callback
Elasticsearch Callback for Keras

1. Copy escallback.py script into the directory with your Keras-based application
2. Make sure the elasticsearch-py library is installed
```shell
pip install elasticsearch
```
3. Reference the new script and configure
```python
from elasticsearch import Elasticsearch

from escallback import ElasticCallback

es_notifier = ElasticCallback()
es_notifier.configure(job_name='YOURJOBNAME', es_client=Elasticsearch())

model.fit_generator(epochs=...,
		generator=...,
		steps_per_epoch=...,
		validation_data=...,
		validation_steps=...,
		verbose=...,
		callbacks=[es_notifier])
```
4. Load the visualizations and dashboard located in the /kibana folder into your Kibana installation. If you need a quick ELK (Elasticsearch-Logstash-Kibana) stack in Docker:
```shell
docker run -p 5601:5601 -p 9200:9200 -p 5044:5044 -it --name elk sebp/elk
```

![Keras Monitoring Dashboard in Kibana](http://www.wadeschulz.com/wp-content/uploads/2017/05/image.png "Monitoring Dashboard")