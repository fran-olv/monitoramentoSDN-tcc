#!/usr/bin/env python3
import sys

from probe_hdrs import *
from scapy.sendrecv import sendp
from scapy.all import get_if_hwaddr

def main():

    probe_pkt = Ether(dst='ff:ff:ff:ff:ff:ff', src=get_if_hwaddr('eth0')) / \
                Probe(hop_cnt=0) / \
                ProbeFwd(egress_spec=4) / \
                ProbeFwd(egress_spec=1) / \
                ProbeFwd(egress_spec=1)

    try:
        execucao = 0  # Inicializando o contador
        while execucao < 52:  # Executar 50 vezes
            sendp(probe_pkt, iface='eth0')
            time.sleep(1)
            execucao += 1  # Incrementando o contador a cada iteração
    except KeyboardInterrupt:  # Capturar interrupção do teclado
            sys.exit()



if __name__ == '__main__':
    main()

