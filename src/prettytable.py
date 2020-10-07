from prettytable import PrettyTable

def clean_instances(data):
    pretty = PrettyTable()
    pretty.field_names = ['Name', 'TTL']
    instances = data['instances']
    for instance in instances:
        name = ''
        ttl = ''
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                name = tag['Value']
            if tag['Key'] == 'TTL':
                ttl = tag['Value']
        pretty.add_row([name, ttl])
    
    return pretty
