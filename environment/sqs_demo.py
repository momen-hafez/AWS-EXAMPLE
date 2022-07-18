import boto3
#sqs = boto3.resource('sqs')
#queue = sqs.create_queue(QueueName = 'test' , Attributes = {'DelaySeconds': '5'})
#print(queue.url)
#print(queue.attributes.get('DelaySeconds'))
# Get the service resource
#------------------------ Printing the Queue Content -----------------
#sqs = boto3.resource('sqs')

# Get the queue. This returns an SQS.Queue instance
#queue = sqs.get_queue_by_name(QueueName='test')

# You can now access identifiers and attributes
#print(queue.url)
#print(queue.attributes.get('DelaySeconds'))

# Print out each queue name, which is part of its ARN
#for queue in sqs.queues.all():
#    print(queue.url)
#------------------------------------------------------------------------
# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

response = queue.send_message(MessageBody = 'boto3' , MessageAttributes = {
    'Author' : {
        'StringValue' : 'Momen',
        'DataType': 'String'
    }
})
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')
        if author_name:
            author_text = ' ({0})'.format(author_name)

    # Print out the body and author (if set)
    print('Hello, {0}!{1}'.format(message.body, author_text))

    # Let the queue know that the message is processed
    message.delete()
print(response.get('Failed'))