"""A validation solution.
Requires:
- pip3 install namedlist
"""
from namedlist import namedlist
import csv

"""DATA STRUCTURES"""

Slot = namedlist('Slot', ['row', 'slot'])
Server = namedlist('Server', ['length', 'power'])
Allocation = namedlist('Allocation', ['row', 'slot', 'pool'])
Row = namedlist('Row', ['pools', 'blocks'])
Datacenter = namedlist('Datacenter', ['pools', 'rows'])
Block = namedlist('Block', ['slot', 'length', 'free', 'servers'])

"""INPUT"""

with open('/Users/javier/git/hashcode-training/retos/comprobador HC2015/in.example') as f:
    input_reader = csv.reader(f, delimiter=' ')

    (ROWS, SLOTS, UNAVAILABLE, POOLS, MSERVERS) = (int(x) for x  in next(input_reader))

    def create_slot(source):
        (row, slot) = (int(x) for x in next(source))
        return Slot(row=row, slot=slot)

    def create_servers(source):
        (length, power) = (int(x) for x in next(source))
        return Server(length=length, power=power)

    unavailable = [create_slot(input_reader) for i in range(UNAVAILABLE)]
    servers = [create_servers(input_reader) for i in range(MSERVERS)]

"""POSSIBLE OUTPUT"""

with open('/Users/javier/git/hashcode-training/retos/comprobador HC2015/out.example') as f:
    input_reader = csv.reader(f, delimiter=' ')

    def create_allocation(source):
        line = next(source)
        if len(line) == 3:
            (row, slot, pool) = (int(x) for x in line)
            return Allocation(row=row, slot=slot, pool=pool)
        return None

    allocations = [create_allocation(input_reader) for i in range(MSERVERS)]

"""VALIDATION LOGIC"""

datacenter = Datacenter(pools=[0]*POOLS,
    rows=[Row(pools=[0]*POOLS, blocks=[Block(slot=0, length=SLOTS, free=SLOTS, servers={})]) for _ in range(ROWS)])

def remove_slot(datacenter, slot):
    row = datacenter.rows[slot.row]
    in_slot = lambda b: b[1].slot <= slot.slot and (b[1].slot + b[1].length - 1) >= slot.slot
    (index, block) = next(filter(in_slot, enumerate(row.blocks)))
    result = row[0:index]
    block_left = Block(slot=block.slot,
                       length=slot.slot - block.slot,
                       free=slot.slot - block.slot,
                       servers={})
    if block_left.free > 0:
        result.append(block_left)
    block_right = Block(slot=slot.slot+1,
                        length=block.length - slot.slot + block.slot - 1,
                        free=block.length - slot.slot + block.slot - 1,
                        servers={})
    if block_right.free > 0:
        result.append(block_right)
    if index+1 < len(row):
        result.extend(row[index+1:])
    row.blocks = result

for slot in unavailable:
    remove_slot(datacenter, slot)

"""ADD SERVERS (this should be replaced by a core)"""

def is_allocated(x):
    not x[1] is None

def add_server(datacenter, server, allocation, id):
    datacenter.pools[allocation.pool] = datacenter.pools[allocation.pool] + server.power
    row = datacenter.rows[allocation.row]
    row.pools[allocation.pool] = row.pools[allocation.pool] + server.power
    block = next(filter(lambda b: b.slot <= allocation.slot and (b.slot + b.length - 1)>= allocation.slot, row.blocks))
    block.free = block.free - server.length
    block.servers[id] = allocation.pool

for server, allocation, id in filter(lambda x: not x[1] is None, zip(servers, allocations, range(len(servers)))):
    add_server(datacenter, server, allocation, id)

"""Guaranteed capacity computation (if we arrive here, we can compute the points of the solution)"""

pool_row_unavailable_capacity = lambda pool, row: datacenter.pools[pool] - datacenter.rows[row].pools[pool]
pool_guaranteed_capacity = lambda pool: min(pool_row_unavailable_capacity(pool, row) for row in range(ROWS))
guaranteed_capacity = min(pool_guaranteed_capacity(pool) for pool in range(POOLS))

print(guaranteed_capacity)
