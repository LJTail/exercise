from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        rootSwitch = self.addSwitch( 's1' )
        rootleftSwitch = self.addSwitch( 's2' )
        rootrightSwitch = self.addSwitch( 's3' )
        left1Switch = self.addSwitch( 's4' )
        left2Switch = self.addSwitch( 's5' )
        right2Switch = self.addSwitch('s6')
        right1Switch = self.addSwitch( 's7' )
        left1Host1 = self.addHost( 'h1' )
        left1Host2 = self.addHost( 'h2' )
        left2Host1 = self.addHost( 'h3' )
        left2Host2 = self.addHost( 'h4' )
        right2Host2 = self.addHost( 'h5' )
        right2Host1 = self.addHost( 'h6' )
        right1Host2 = self.addHost( 'h7' )
        right1Host1 = self.addHost( 'h8' )

        # Add links
        self.addLink( rootleftSwitch, rootSwitch)
        self.addLink( rootSwitch, rootrightSwitch)
        self.addLink( left1Switch, rootleftSwitch)
        self.addLink( rootleftSwitch, left2Switch)
        self.addLink( right2Switch, rootrightSwitch)
        self.addLink( rootrightSwitch, right1Switch)
        self.addLink( left1Host1, left1Switch)
        self.addLink( left1Switch, left1Host2)
        self.addLink( left2Host1, left2Switch)
        self.addLink( left2Switch, left2Host2)
        self.addLink( right2Host2, right2Switch)
        self.addLink( right2Switch, right2Host1)
        self.addLink( right1Host2, right1Switch)
        self.addLink( right1Switch, right1Host1)

topos = { 'mytopo': ( lambda: MyTopo() ) }
