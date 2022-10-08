import sys


with open(
    'sites.txt',
    'r',
    encoding='UTF-8'
) as sitesfile:
    sites = [site.strip() for site in sitesfile.readlines()]


HOST = '/private/etc/hosts'
REDIRECT = '127.0.0.1'


def block_websites():
    with open(
        HOST,
        'r+',
        encoding='UTF-8'
    ) as hostfile:
        hosts = hostfile.read()
        for site in sites:
            if site not in hosts:
                hostfile.write(
                    (
                        f'{REDIRECT}\t{site}\n'
                        f'{REDIRECT}\twww.{site}\n'
                    )
                )
    print(f'{len(sites)} websites blocked')


def unblock_websites():
    with open(
        HOST,
        'r+',
        encoding='UTF-8'
    ) as hostfile:
        hosts = hostfile.readlines()
        hostfile.seek(0)
        for host in hosts:
            if not any(site in host for site in sites):
                hostfile.write(host)
        hostfile.truncate()
    print(f'{len(sites)} websites unblocked')


if __name__ == '__main__':
    args = sys.argv
    if args[1] == 'block':
        block_websites()
    else:
        unblock_websites()
