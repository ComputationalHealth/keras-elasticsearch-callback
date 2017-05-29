import datetime
from elasticsearch import Elasticsearch
import keras
import uuid

class ElasticCallback(keras.callbacks.Callback):
	# Configure job name and ES client
	def configure(self, job_name=None, es_client=Elasticsearch()):
		self.job_name = job_name
		self.es = es_client

	def on_train_begin(self, logs={}):
		# Set epoch to -1 to track on batch list
		self.cur_epoch = -1
		self.guid = uuid.uuid4().hex # Create a unique job ID
		
		if self.job_name == None: # Set name to job ID if not configured
			self.job_name = self.guid

		if self.es == None: # Create ES client if not configured
			self.es = Elasticsearch()

	# Log batch data to Elasticsearch
	def on_batch_end(self, batch, logs={}):
		json = { 'job_id':self.guid,
				 'job_name':self.job_name,
				 'epoch':self.cur_epoch+1,
				 'batch':batch,
				 'loss':float(logs.get('loss')),
				 'acc':float(logs.get('acc')),
				 'timestamp':datetime.datetime.now().isoformat()
			   }
		self.es.index(index="keras-monitor", doc_type='batch', body=json)

	# Log epoch data to Elasticsearch
	def on_epoch_end(self, epoch, logs={}):
		self.cur_epoch = epoch
		json = { 'job_id':self.guid,
				 'job_name':self.job_name,
				 'epoch':epoch,
				 'loss':float(logs.get('loss')),
				 'acc':float(logs.get('acc')),
				 'val_loss':float(logs.get('val_loss')),
				 'val_acc':float(logs.get('val_acc')),
				 'timestamp':datetime.datetime.now().isoformat()
			   }
		self.es.index(index="keras-monitor", doc_type='epoch', body=json)