#!/usr/bin/env python
#
# Copyright (C) 2007 British Broadcasting Corporation and Kamaelia Contributors(1)
#     All Rights Reserved.
#
# You may only modify and redistribute this under the terms of any of the
# following licenses(2): Mozilla Public License, V1.1, GNU General
# Public License, V2.0, GNU Lesser General Public License, V2.1
#
# (1) Kamaelia Contributors are listed in the AUTHORS file and at
#     http://kamaelia.sourceforge.net/AUTHORS - please extend this file,
#     not this notice.
# (2) Reproduced in the COPYING file, and at:
#     http://kamaelia.sourceforge.net/COPYING
# Under section 3.5 of the MPL, we are using this text since we deem the MPL
# notice inappropriate for this file. As per MPL/GPL/LGPL removal of this
# notice is prohibited.
#
# Please contact us via: kamaelia-list-owner@lists.sourceforge.net
# to discuss alternative licensing.
# -------------------------------------------------------------------------
"""
Running an Axon system in a separate thread
===========================================

The background class makes it easy to run an Axon system in a separate
thread (in effect: in the background).

This simplifies integration of Axon/Kamaelia code into other python code.



Example Usage
-------------

At its simplest, you could run a Kamaelia task independently in the background
- such as a simple network connection, that dumps received data into a thread
safe queue, after de-chunking it into lines of text. To do this:

1. We implement a simple component to collect the data::

    from Axon.background import background
    from Axon.Component import component

    class Receiver(component):
        def __init__(self, queue):
            super(Bucket,self).__init__()
            self.q = queue
            
        def main(self):
            while 1:
                while self.dataReady("inbox"):
                    self.q.put(self.recv("inbox"))
                self.pause()
                yield 1
    
2. Then we create a background object and call its start() method::

    from Axon.background import background
    
    background().start()

3. Finally, we create and activate our Kamaelia pipeline of components,
   including the receiver component we've just written, passing it a thread-safe
   queue to put the data into::
    
    from Kamaelia.Chassis.Pipeline import Pipeline 
    from Kamaelia.Internet.TCPClient import TCPClient
    from Kamaelia.Visualisation.PhysicsGraph import chunks_to_lines
    from Queue import Queue

    queue = Queue()

    Pipeline(
        TCPClient("my.server.com", 1234),
        chunks_to_lines(),
        Receiver(queue)
    ).activate()

We can now fetch items of data, from the queue when they arrive::

    received_line = queue.get()



Behavour
--------

Create one of these and start it running by calling its start() method.
    
After that, any components you activate will default to using this
scheduler.

Only one instance can be used within a given python interpreter.

The background thread is set as a "daemon" thread. This means that if your
program exits, this background thread will be killed too. If it were not a
daemon, then it would prevent the python interpreter terminating until the
components running in it had all terminated too.
"""


from Scheduler import scheduler
from Component import component
import threading

import CoordinatingAssistantTracker as cat

class background(threading.Thread):
    """\
    A python thread which runs the Axon Scheduler. Takes the same arguments
    at creation that Axon.Scheduler.scheduler.run.runThreads accepts.
    
    Create one of these and start it running by calling its start() method.
    
    After that, any components you activate will default to using this
    scheduler.
    
    Only one instance can be used within a given python interpreter.
    """
    lock = threading.Lock()
    def __init__(self,slowmo=0,zap=False):
        if not background.lock.acquire(False):
            raise "only one scheduler for now can be run!"
        self.slowmo = slowmo
        threading.Thread.__init__(self)
        self.setDaemon(True) # Die when the caller dies
        self.zap = zap
        
    """\
    The internal body code of the thread. Call start() to begin execution.
    """
    def run(self):
        if self.zap:
            X = scheduler()
            scheduler.run = X
            cat.coordinatingassistanttracker.basecat.zap()
        scheduler.run.waitForOne()
        scheduler.run.runThreads(slowmo = self.slowmo)
        background.lock.release()

if __name__ == "__main__":
    from Kamaelia.UI.Pygame.MagnaDoodle import MagnaDoodle
    import time

    background = background().start()
    
    MagnaDoodle().activate()
    while 1:
        time.sleep(1)
        print "."
