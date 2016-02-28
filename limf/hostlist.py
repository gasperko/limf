import urllib
import json

def retrieve_online_host_list():
    try:
        url = "https://raw.githubusercontent.com/lich/limf/master/host_list.json"
        return json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    except urllib.error.URLError:
        print("Check your internet connection.")
        exit()

def retrieve_local_host_list(local_list_path):
    try:
        with open(local_list_path) as host_file:
            return json.load(host_file)
    except FileNotFoundError:
        print("Could not find the given local host list: {0}".format(local_list_path))
    except json.decoder.JSONDecodeError:
        print("The host list is not valid. Please check it.")
    exit()

def generate_host_string(clone_list, host_string=None):
    host_string = host_string or 'Select hosting: '
    for i in range(0, len(clone_list)):
        if i == len(clone_list)-1:
            host_string += '{} - {}'.format(str(i), clone_list[i][2])
        else:
            host_string += '{} - {}, '.format(str(i), clone_list[i][2])
    return host_string
