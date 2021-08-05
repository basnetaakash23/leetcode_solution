def gasStation(gas, cost):
    if(sum(gas)-sum(cost) < 0):
        return -1

    start_index = 0
    gas_tank = 0

    for i in range(len(gas)):
        gas_tank += gas[i]-cost[i]

        if(gas_tank < 0):
            start_index = i+1
            gas_tank = 0

        print("i",i)

    return start_index

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(gasStation(gas,cost))
gas = [2,3,4]
cost = [3,4,3]

print(gasStation(gas,cost))