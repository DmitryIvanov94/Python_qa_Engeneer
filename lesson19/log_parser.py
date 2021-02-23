# -*- coding: utf-8 -*-
from collections import Counter
from operator import itemgetter
import argparse
import os
import re
import sys
import json


def get_args():
    arg_parser = argparse.ArgumentParser(description='Process access.log')
    arg_parser.add_argument('-f', '--file', action='store',
                            help='Path to logfile')
    arg_parser.add_argument('-d', '--directory', action='store',
                            help='Path to directory with logfiles')
    return arg_parser.parse_args()


def get_requests_statistics(log_file):
    requests = {
        "total": 0,
        "GET": 0,
        "POST": 0,
        "PUT": 0,
        "DELETE": 0,
        "HEAD": 0,
        "OPTIONS": 0,
        "PATCH": 0,
        "CONNECT": 0,
        "TRACE": 0
    }

    requests_list = []
    ip_list = []

    try:
        with open(log_file) as log:
            for index, line in enumerate(log.readlines()):

                method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD|OPTIONS|"
                                   r"PATCH|CONNECT|TRACE)", line).groups()[0]
                ip = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                request_duration = re.search(r'(\d)*$', line)
                url = re.search(r'(/\D*) HTTP', line)
                status_code = re.search(r'(\d{3}) ', line)

                # Количество запросов по типу:
                requests[method] += 1

                # Общее количество выполненных запросов:
                requests["total"] += 1
                # if requests["total"] > 100:
                #     break

                if (method and ip and request_duration and url and
                    status_code) \
                        is not None:
                    requests_list.append(
                        [
                            ip.group(0),
                            request_duration.group(0),
                            method,
                            url.group(1),
                            status_code.group(1)
                        ]
                    )
                    ip_list.append(ip.group(0))

    except (AttributeError, FileNotFoundError):
        if args.directory:
            sys.exit('Directory with log file not found')
        else:
            sys.exit('Log file not found, check argument "--file=filename"')

    # Топ 10 IP адресов, с которых были сделаны запросы
    top_requests = list(sorted(Counter(ip_list).items(),
                               key=lambda x: x[1], reverse=True))[:9]

    # Топ 10 самых долгих запросов
    top_duration = sorted(requests_list, key=itemgetter(1), reverse=True)[:9]

    # Топ 10 запросов, которые завершились клиентской ошибкой
    top_client_error = [x for x in requests_list if x[4].startswith('4')][:9]

    # Топ 10 запросов, которые завершились ошибкой со стороны сервера
    top_server_error = [x for x in requests_list if x[4].startswith('5')][:9]

    requests_statistics = {
        'requests_count': requests,
        'top_requests': top_requests,
        'top_duration': top_duration,
        'top_client_error': top_client_error,
        'top_server_error': top_server_error
    }
    return requests_statistics


def write_requests_statistics(log_file, statistics_file):
    with open(statistics_file, 'w+') as result:
        json.dump(get_requests_statistics(log_file), result, indent=2)


if __name__ == '__main__':

    args = get_args()

    # Выбор файла или директории
    if args.directory:
        if os.path.exists(args.directory):
            files = os.listdir(args.directory)
            for file in files:
                f_name = file.split('.')[0]
                if file.endswith('.log'):
                    os.chdir(args.directory)
                    write_requests_statistics(file,
                                              'log_statistics_{}.json'
                                              .format(f_name))
        else:
            sys.exit('not found directory {}'.format(args.directory))

    else:
        f_name = args.file.split('.')[0]
        write_requests_statistics(args.file,
                                  'log_statistics_{}.json'.format(f_name))
