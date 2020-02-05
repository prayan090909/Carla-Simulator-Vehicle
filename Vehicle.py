

from __future__ import print_function


# ==============================================================================
# -- find carla module ---------------------------------------------------------
# ==============================================================================


import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass


# ==============================================================================
# -- imports -------------------------------------------------------------------
# ==============================================================================


import carla

from carla import ColorConverter as cc

import argparse
import collections
import datetime
import logging
import math
import random
import re
import weakref
import time

actor_list = []

try:
    client = carla.Client("localhost",2000)
    client.set_timeout(2.0)
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
    bp = random.choice(blueprint_library.filter('vehicle.bmw.*'))
    print(bp)

    spawn_point = random.choice(world.get_map().get_spawn_points())
    vehicle = world.spawn_actor(bp,spawn_point)

    vehicle.apply_control(carla.VehicleControl(throttle=1.0,steer=0.0))
    actor_list.append(vehicle)
    time.sleep(10)
    
    
    
finally:
    for actor in actor_list:
        actor.destroy()
    print("All cleaned Up")

