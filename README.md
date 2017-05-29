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
es_notifier.configure(job_name='ERMnet1', es_client=Elasticsearch())

model.fit_generator(epochs=...,
                        generator=...,
                        steps_per_epoch=...,
                        validation_data=...,
                        validation_steps=...,
                        verbose=...,
                        callbacks=[es_notifier])
```