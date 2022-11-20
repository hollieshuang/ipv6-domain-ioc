import datetime
import sys
import pandas as pd
from tqdm import tqdm

chunk_size = 10000000
ioc_file = "/home/xxx/dns/domain_xxx.txt"
dns_file = "/home/xxx/dns/xxxxxx_xxxx.log"
ret_file_prefix = "/home/xxx/tmp/ioc"
dns_file = "/home/xxx/dns/unboundBF/unbound_" + sys.argv[1]
ret_file_prefix = "/home/xxx/dns/unboundBF/tmp/ioc" + sys.argv[2]
print({dns_file},{ret_file_prefix})
print(datetime.datetime.now())

ioc_set = set(pd.read_csv(ioc_file, header=None, usecols=[0])[0].tolist())


def domain_is_ioc(domain):
    if isinstance(domain, str):
        levels = domain.strip(".").split(".")
        for i in range(0, len(levels) - 1):
            sub_domain = ".".join(levels[i:])
            if sub_domain in ioc_set:
                return True
    return False


offset = 0
print(datetime.datetime.now())
with tqdm() as pbar:
    reader = pd.read_csv(dns_file, delimiter=" ", header=None, usecols=[0, 1, 2, 5, 6], chunksize=chunk_size)
    for df in reader:
        pbar.update(chunk_size)
        offset += chunk_size
        df = df[df[6].apply(domain_is_ioc)].rename(columns={0: "month", 1: "day", 2: "time", 5: "ip", 6: "domain"})
        df.to_csv(f"{ret_file_prefix}_{offset}.csv", index=False, header=False)

print(datetime.datetime.now())
