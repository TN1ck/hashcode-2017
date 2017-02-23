#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Google Hash Code 2016 - Qualification
#
# © 2017 Team "TU_DUDES"
#
# Version: 0.1
#

"""Google Hash Code 2017"""

import sys
import numpy as np


class Video(object):
    """A video to be cached"""

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return 'size({})'.format(self.size)

    def __repr__(self):
        return self.__str__()

class Endpoint(object):

    def __init__(self, latency_to_datacenter, cache_servers_with_latency):
        self.latency_to_datacenter = latency_to_datacenter
        self.cache_servers_with_latency = cache_servers_with_latency

    def __str__(self):
        return 'latency({}) caches({})'\
            .format(self.latency_to_datacenter, len(self.cache_servers_with_latency))

    def __repr__(self):
        return self.__str__()

class CacheServer(object):

    def __init__(self, size):
        self.size = size

class Request(object):

    def __init__(self, video_id, endpoint_id, number_of_requests):
        self.video_id = video_id
        self.endpoint_id = endpoint_id
        self.number_of_requests = number_of_requests

    def __str__(self):
        return 'video({}) endpoint({}) requests({})'\
            .format(self.video_id, self.endpoint_id, self.number_of_requests)

    def __repr__(self):
        return self.__str__()

def read_file(file_path):
    """Read input file"""
    with open(file_path, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
        header = lines[0]
        [videos, endpoints, requests, cache_servers, cache_server_capacity] = [int(x) for x in header.split(' ')]
        print('videos {}\n endpoints {} requests {} cache_servers {} cache_server_capacity {}'.format(
            videos, endpoints, requests, cache_servers, cache_server_capacity
        ))

        video_sizes = lines[1]
        video_list = [Video(int(x)) for x in video_sizes.split(' ')]

        endpoint_list = []
        # keeps track of the last index, which is needed for the video parsing
        current_index = 2
        for i in range(endpoints):
            # we start from the second line
            current_endpoint = lines[current_index]
            [latency_to_datacenter, number_of_connected_caches] = [int(x) for x in current_endpoint.split(' ')]
            current_index += 1
            connected_caches = []
            for connected_cache_line in lines[current_index:(current_index + number_of_connected_caches)]:
                [cache_id, latency] = [int(x) for x in connected_cache_line.split(' ')]
                connected_caches.append({
                    'cache_id': cache_id,
                    'latency': latency
                })
                current_index += 1
            endpoint_list.append(Endpoint(latency_to_datacenter, connected_caches))

        request_list = []
        for request_line in lines[current_index:]:
            [video_id, endpoint_id, number_of_requests] = [int(x) for x in request_line.split(' ')]
            request_list.append(Request(video_id, endpoint_id, number_of_requests))

        cache_servers = [CacheServer(cache_server_capacity) for _ in range(cache_servers)]

        return {
            'videos': video_list,
            'endpoints': endpoint_list,
            'requests': request_list,
            'cache_server_capacity': cache_server_capacity,
            'cache_servers': cache_servers
        }

def write_file(pizza, filename):
    """Write output file."""
    with open(filename, 'w') as file_out:
        file_out.write('{}\n'.format(len(pizza.slices)))
        for cur_slice in pizza.slices:
            [start_row, end_row, start_col, end_col] = cur_slice
            file_out.write('{} {} {} {}\n'.format(start_row, start_col, end_row-1, end_col-1))


def main():
    """Main function."""

    if len(sys.argv) < 3:
        sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])

    # read data
    pizza = read_file(sys.argv[1])
    # write output file
    write_file(pizza, sys.argv[2])


if __name__ == '__main__':
    print('HASHCODE - TU_DUDES')
    print('running python {}'.format(sys.version_info.major))
    # main()
    result = read_file('kittens.in')
    print(result)

