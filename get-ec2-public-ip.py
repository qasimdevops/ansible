#!/usr/bin/python3
import boto3
import json

def get_ec2_instacnes():
    session = boto3.Session()

    ec2= session.resource('ec2')

    instances = ec2.instances.all()

    inventory = {'_meta': {'hostvars':{}}, 'all':{'children': ['ungrouped']},'ungrouped':{'hosts':[]}}

    for instance in instances:
        if instance.state['Name']=='running':
            inventory['ungrouped']['hosts'].append(instance.public_ip_address)
            inventory['_meta']['hostvars'][instance.public_ip_address] = {
                    'ansible_host': instance.public_ip_address,
                    'ansible_user': 'ansible',
                    'ansible_ssh_private_key_file': '/home/ansible/.ssh/id_rsa'

                    }
    return inventory
if __name__ == '__main__':
    inventory=get_ec2_instacnes()
    print(json.dumps(inventory))
