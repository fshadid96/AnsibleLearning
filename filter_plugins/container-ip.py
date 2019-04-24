#!/usr/bin/pythoin
import json

class FilterModule(object):
	def filters(self):
		return { 'ip_addr': self.ip_addr }


	def ip_addr(self, json_file):
		ips = []
		details = json.dumps(json_file) 
		clean_details = json.loads(details) 
		for container in clean_details["results"]:
			ips.append(container["ansible_facts"]["docker_container"]["NetworkSettings"]["Networks"]["bridge"]["IPAddress"])

		return ips
