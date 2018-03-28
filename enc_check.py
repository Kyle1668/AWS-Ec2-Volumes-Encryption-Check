import os
import json
import subprocess

def get_json(command):
	process = subprocess.Popen(command, stdout=subprocess.PIPE)
	output = process.stdout.read()
	return json.loads(output)


def print_results(data):
	print(json.dumps(data, indent=4))


def get_regions(regions_json_data):
	regions = []

	for region_object in regions_json_data['Regions']:
		regions.append(region_object['RegionName'])
		
	return regions
	

def get_ec2_volumes(regions):
	volumes = []

	for region in regions:
		volumes_in_region = get_json(['aws', 'ec2', 'describe-volumes', '--region', region])
		for volume in volumes_in_region['Volumes']:
			print_results(volume)



def main():
	regions = get_regions(get_json(['aws', 'ec2', 'describe-regions']))
	ec2_volumes = get_ec2_volumes(regions) 


main()

