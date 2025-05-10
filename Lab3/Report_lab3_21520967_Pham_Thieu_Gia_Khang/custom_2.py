from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo

class Lab3_Topo(Topo):
    def build(self):
        # Add hosts
        hosts = [self.addHost(f'h{i}') for i in range(1, 17)]

        # Add switches
        switches = [self.addSwitch(f's{i}') for i in range(1, 5)]

        # Link switches in chain
        for i in range(len(switches) - 1):
            self.addLink(switches[i], switches[i + 1])

        # Link hosts to switches (4 hosts per switch)
        for i, host in enumerate(hosts):
            self.addLink(host, switches[i // 4])

def run():
    topo = Lab3_Topo()
    net = Mininet(topo=topo, controller=None)
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
