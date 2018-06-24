# sample_roads

Converting osm to wbt

```
cd /resources/osm_importer
python importer.py --input=myMap.osm --output=myMap.wbt
```
Create/modify wbt file and run the following steps:

  1- export node/edges: 
  ```
  python exporter.py --input=~/dev/worlds/myMap.wbt -- output=~/dev/worlds/myMap_net/
  ```
  2- create network: 
  
  ```
  bin/netconvert --node-files=/Users/kimiahs/dev/worlds/test_my_world_net/sumo.nod.xml --edge-files=~/dev/worlds/myMap_net/sumo.edg.xml --output-file=~/dev/worlds/myMap_net/sumo.net.xml
   ```
   
   3- test/edit network:
   ```
   bin/netedit -s ~/dev/worlds/myMap_net/sumo.net.xml -n ~/dev/worlds/myMap_net/sumo.nod.xml -e ~/dev/worlds/myMap_net/sumo.edg.xml 
   ```
   
   4- generate trips:
   ```
   python tools/randomTrips.py -n ~/dev/worlds/myMap_net/sumo.net.xml -o ~/dev/worlds/myMap_net/sumo.trip.xml
   ```
   
   5- generate routes:
   ```
   bin/duarouter --trip-files ~/dev/worlds/myMap_net/sumo.trip.xml --net-file ~/dev/worlds/myMap_net/sumo.net.xml --output-file ~/dev/worlds/myMap_net/sumo.rou.xml --ignore-errors true
   ```
   
   6- configure wb simulator with arguments in sumosupervisor : --max-num-vehicles=30 , this is equivalent to running sumo with argumenet of --max-num-vehicles:
   ```
    bin/sumo-gui -n ~/dev/worlds/myMap_net/sumo.net.xml -r ~/dev/worlds/myMap_net/sumo.rou.xml --max-num-vehicles 30
   ```
