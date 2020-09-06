#!/usr/bin/python
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo

class fatTreeTopo(Topo):

    "Fat Tree Topology"

    def __init__(self):
        "Create Fat tree Topology"
        Topo.__init__(self)
       
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
        h4 = self.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
        
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch)
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch)
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch)   
        s4 = self.addSwitch('s4', cls=OVSKernelSwitch)
       
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(s1, s4)
        self.addLink(s1, s3)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
       
topos = { 'mytopo': (lambda: fatTreeTopo() ) }           