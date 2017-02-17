import transform_mysql

def transform(event):
    module_name = 'transform_' + event['_metadata']['input_label'].lower().replace(' ', '_').replace('-', '_')
    if module_name in globals():
        class_instance = globals()[module_name]
        return class_instance.transform(event)

    else:
        raise Exception('Missing %s' % module_name)