from mininet.topo import Topo


class MyTopo(Topo):

    def __init__(self):

        Topo.__init__(self)

        #hosts definition
        Host1 = self.addHost('h1')
        Host2 = self.addHost('h2')
        Host3 = self.addHost('h3')
        Host4 = self.addHost('h4')
        Host5 = self.addHost('h5')
        Host6 = self.addHost('h6')
        Host7 = self.addHost('h7')
        Host8 = self.addHost('h8')
        Host9 = self.addHost('h9')
        Host10 = self.addHost('h10')
        Host11 = self.addHost('h11')
        Host12 = self.addHost('h12')
        Host13 = self.addHost('h13')
        Host14 = self.addHost('h14')
        Host15 = self.addHost('h15')
        
        #switch definition
        Switch1 = self.addSwitch('S1')
        Switch2 = self.addSwitch('S2')
        Switch3 = self.addSwitch('S3')
        Switch4 = self.addSwitch('S4')
        Switch5 = self.addSwitch('S5')
        Switch6 = self.addSwitch('S6')
        Switch7 = self.addSwitch('S7')
        Switch8 = self.addSwitch('S8')
        Switch9 = self.addSwitch('S9')
        Switch10 = self.addSwitch('S10')

        #links definition
        self.addLink(Host1, Switch1)
        self.addLink(Host2, Switch1)
        self.addLink(Host3, Switch2)
        self.addLink(Host4, Switch10)
        self.addLink(Host5, Switch10)
        self.addLink(Host6, Switch9)
        self.addLink(Host7, Switch6)
        self.addLink(Host8, Switch6)
        self.addLink(Host9, Switch7)
        self.addLink(Host10, Switch8)
        self.addLink(Host11, Switch8)
        self.addLink(Host12, Switch4)
        self.addLink(Host13, Switch4)
        self.addLink(Host14, Switch4)
        self.addLink(Host15, Switch5)

        self.addLink(Switch1, Switch2)
        self.addLink(Switch2, Switch3)
        self.addLink(Switch3, Switch4)
        self.addLink(Switch4, Switch5)
        self.addLink(Switch4, Switch6)
        self.addLink(Switch6, Switch7)
        self.addLink(Switch6, Switch9)
        self.addLink(Switch7, Switch8)
        self.addLink(Switch9, Switch10)

topos = { 'mytopo': (lambda: MyTopo()) }

