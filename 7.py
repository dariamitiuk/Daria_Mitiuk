import ipaddress
def ip(s):
    return '"' + str(ipaddress.ip_address(int(s))) + '"'

if __name__ == '__main__':
    print("ip(2149583361) -> ", ip(2149583361))
    print("ip(32) -> ", ip(32))
    print("ip(0) -> ", ip(0))