

def transform(event):

    ## Event Type Should Prefox Schema
    event['_metadata']['event_type'] = '%s.%s' % (event['_metadata']['schema'],
                                                  event['_metadata']['event_type'])

    return event