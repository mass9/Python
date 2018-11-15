import argparse,dns.resolver

def lookup(name):
    for qtype in 'A','AAA','CNAME','MX','NS':
        answer = dns.resolver.query(name, qtype,raise_on_no_answer = False)
        if answer.rrset is not None:
            print(answer.rrset)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Resolve the name useing DNS')
    parser.add_argument('name',help='name that you wnat to look up in DNS')
    lookup(parser.parse_args().name)
