import logging
import os
import time

from pyats import aetest
from pyats.topology import loader

from genie.testbed import load
from ats.log.utils import banner
from genie.utils.diff import Diff
from genie.libs.sdk.apis.iosxe.bgp.get import get_bgp_session_count
log = logging.getLogger(__name__)
testbed = loader.load('testbed.yml')
device1 = testbed.devices[ 'CiscoL3-3' ]

###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################
class common_setup(aetest.CommonSetup):
    @aetest.subsection
    def connectdevices(self):
        log.info("Connecting to  devices.....")
        result1 = device1.connect()

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

class pre_testcase1(aetest.Testcase):
    @ aetest.test
    def bgp_summary(self):
        ##################CiscoL3-3
        log.info("retreiving bgp summary information...")
        bgpsummarydevice1 = device1.execute("show ip bgp summary")
        indexnw = bgpsummarydevice1.find("network entries")
        if indexnw == -1:
           log.info("no network entries")
           nw = 0
        else:
           nw = bgpsummarydevice1[(indexnw-2)]
        log.info("number of network entries for CiscoL3-3 is %s" %(nw))
        log.info("bgp summary %s" %bgpsummarydevice1)
        f = open("doc1.txt", "w")
        df = open("pre_doc.txt","w")
        f.write("Command 1: show ip bgp summary"+'\n')
        f.write('\n' + "Parsed output:" + '\n' + "network entries:"+ str(nw)+'\n')
        f.write('\n'+"===================="+'\n')
        df.write("Command 1: show ip bgp summary"+'\n')
        df.write('\n' + bgpsummarydevice1 + '\n')
        df.write('\n' + "Parsed output:" + '\n' + "network entries:"+ str(nw)+'\n')
        df.write('\n'+"===================="+'\n')
        f.close()
        df.close()

class pre_testcase2(aetest.Testcase):
    @ aetest.test
    def bgp_neighbors(self):
        ##################CiscoL3-3
        log.info("reteiving bgp neighbors info......")
        bgpneighborsdevice1 = device1.execute("show ip bgp neighbors")
        countnb = bgpneighborsdevice1.count("BGP neighbor is")
        indexst = bgpneighborsdevice1.find("BGP state =")
        if indexst == -1:
           log.info("Bgp state is unknown")
           status = "unknown"
        else:
           indexend = bgpneighborsdevice1.index(",",(indexst+12))
           status = bgpneighborsdevice1[(indexst+12):(indexend)]
        log.info("no of neighbors: %s" %countnb)
        log.info("Status of CiscoL3-3 is %s" %status)
        f = open("doc1.txt", "a")
        df = open("pre_doc.txt","a")
        f.write('\n'+ "Command 2: show ip bgp neighbors"+ '\n')
        f.write('\n' + "Parsed output:" +'\n' + "Number of neighbors:"+ str(countnb)+'\n')
        f.write('\n' +"BGP Neighbor state is :"+ status + '\n')
        f.write('\n'+"===================="+'\n')
        df.write('\n'+ "Command 2: show ip bgp neighbors"+ '\n')
        df.write('\n' + bgpneighborsdevice1 +'\n')
        df.write('\n' + "Parsed output:" +'\n' + "Number of neighbors:"+ str(countnb)+'\n')
        df.write('\n' +"BGP Neighbor state is :"+ status + '\n')
        df.write('\n'+"===================="+'\n')
        f.close()
        df.close()

class pre_testcase3(aetest.Testcase):
    @ aetest.test
    def bgp_routes(self):
        ##################CiscoL3-3
        log.info("reteiving bgp routes info......")
        bgproutesdevice1 = device1.execute("show ip route bgp")
        countrt = bgproutesdevice1.count("via")
        log.info("No of routes for CiscoL3-3: %s" %countrt)
        f = open("doc1.txt", "a")
        df = open("pre_doc.txt","a")
        f.write('\n' + "Command 3: show ip route bgp" +'\n')
        f.write('\n'+"Parsed output:" + '\n' +"No of BGP routes: "+str(countrt) + '\n')
        f.write('\n'+"=========EOF========"+'\n')
        df.write('\n' + "Command 3: show ip route bgp" +'\n')
        df.write('\n' + bgproutesdevice1 + '\n')
        df.write('\n'+"Parsed output:" + '\n' +"No of BGP routes: "+str(countrt) + '\n')
        df.write('\n'+"=========EOF========"+'\n')
        f.close()
        df.close()

class Interfacedown_testcase(aetest.Testcase):
    @ aetest.test
    def interface_down(self):
        bgpsummarydevice1 = device1.configure("interface FastEthernet 0/1\n"
                                              "shutdown")
        log.info("interface 0/1 is shutdown")
        time.sleep(60)

class Removeneighbor_testcase(aetest.Testcase):
    @ aetest.test
    def remove_neighbor(self):
        bgpsummarydevice1 = device1.configure("router bgp 65000\n"
                                              "no neighbor 10.0.0.2 remote-as 65001")
        log.info("neighbor is removed")
        time.sleep(60)

class Interfaceup_testcase(aetest.Testcase):
    @ aetest.test
    def interface_up(self):
        bgpsummarydevice1 = device1.configure("interface FastEthernet 0/1\n"
                                              "no shutdown")
        log.info("interface 0/1 is up")
        time.sleep(60)

class post_testcase1(aetest.Testcase):
    @ aetest.test
    def bgp_summary(self):
        ##################CiscoL3-3
        log.info("retreiving bgp summary information...")
        bgpsummarydevice1 = device1.execute("show ip bgp summary")
        indexnw = bgpsummarydevice1.find("network entries")
        if indexnw == -1:
           log.info("no network entries")
           nw = 0
        else:
           nw = bgpsummarydevice1[(indexnw-2)]
        log.info("number of network entries for CiscoL3-3 is %s" %(nw))
        log.info("bgp summary %s" %bgpsummarydevice1)
        f = open("doc2.txt", "w")
        df = open("post_doc.txt","w")
        f.write("Command 1: show ip bgp summary"+'\n')
        f.write('\n' + "Parsed output:" + '\n' + "network entries:"+ str(nw)+'\n')
        f.write('\n'+"===================="+'\n')
        df.write("Command 1: show ip bgp summary"+'\n')
        df.write('\n' + bgpsummarydevice1 + '\n')
        df.write('\n' + "Parsed output:" + '\n' + "network entries:"+ str(nw)+'\n')
        df.write('\n'+"===================="+'\n')
        f.close()
        df.close()

class post_testcase2(aetest.Testcase):
    @ aetest.test
    def bgp_neighbors(self):
        ##################CiscoL3-3
        log.info("reteiving bgp neighbors info......")
        bgpneighborsdevice1 = device1.execute("show ip bgp neighbors")
        countnb = bgpneighborsdevice1.count("BGP neighbor is")
        indexst = bgpneighborsdevice1.find("BGP state =")
        if indexst == -1:
           log.info("Bgp state is unknown")
           status = "no neighbor"
        else:
           indexend = bgpneighborsdevice1.index(",",(indexst+12))
           status = bgpneighborsdevice1[(indexst+12):(indexend)]
        log.info("no of neighbors: %s" %countnb)
        log.info("Status of CiscoL3-3 is %s" %status)
        f = open("doc2.txt", "a")
        df = open("post_doc.txt","a")
        f.write('\n'+ "Command 2: show ip bgp neighbors"+ '\n')
        f.write('\n' + "Parsed output:" +'\n' + "Number of neighbors:"+ str(countnb)+'\n')
        f.write('\n' +"BGP Neighbor state is :"+ status + '\n')
        f.write('\n'+"===================="+'\n')
        df.write('\n'+ "Command 2: show ip bgp neighbors"+ '\n')
        df.write('\n' + bgpneighborsdevice1 +'\n')
        df.write('\n' + "Parsed output:" +'\n' + "Number of neighbors:"+ str(countnb)+'\n')
        df.write('\n' +"BGP Neighbor state is :"+ status + '\n')
        df.write('\n'+"===================="+'\n')
        f.close()
        df.close()

class post_testcase3(aetest.Testcase):
    @ aetest.test
    def bgp_routes(self):
        ##################CiscoL3-3
        log.info("reteiving bgp routes info......")
        bgproutesdevice1 = device1.execute("show ip route bgp")
        countrt = bgproutesdevice1.count("via")
        log.info("No of routes for CiscoL3-3: %s" %countrt)
        f = open("doc2.txt", "a")
        df = open("post_doc.txt","a")
        f.write('\n' + "Command 3: show ip route bgp" +'\n')
        f.write('\n'+"Parsed output:" + '\n' +"No of BGP routes: "+str(countrt) + '\n')
        f.write('\n'+"=========EOF========"+'\n')
        df.write('\n' + "Command 3: show ip route bgp" +'\n')
        df.write('\n' + bgproutesdevice1 + '\n')
        df.write('\n'+"Parsed output:" + '\n' +"No of BGP routes: "+str(countrt) + '\n')
        df.write('\n'+"=========EOF========"+'\n')
        f.close()
        df.close()

class Addneighbor_testcase(aetest.Testcase):
    @ aetest.test
    def add_neighbor(self):
        bgpsummarydevice1 = device1.configure("router bgp 65000\n"
                                              "neighbor 10.0.0.2 remote-as 65001")
        log.info("neighbor is added")

class compareprepost(aetest.Testcase):
    @ aetest.test
    def compare_Doc1_Doc2(self):
        doc1 = set(line.strip() for line in open("doc1.txt"))
        doc2 = set(line.strip() for line in open("doc2.txt"))
        f = open("out.txt","w")
        for line in doc1:
            if line not in doc2:
                f.write('[pre:Doc1]' + line+'\n')
        for line in doc2:
            if line not in doc1:
                f.write('[post:Doc2]' + line+'\n')
        f.close()

#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

class common_cleanup(aetest.CommonCleanup):
    @aetest.subsection
    def clean_everything(self):
        log.info("Aetest Common Cleanup ")
        device1.disconnect()

if __name__ == '__main__': # pragma: no cover
    logging.getLogger(__name__).setLevel(logging.ERROR)
    logging.getLogger('pyats.aetest').setLevel(logging.ERROR)
    aetest.main()
