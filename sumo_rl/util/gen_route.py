import os
import sys

v4 =  '''<flow id="flow_ns_c" route="route_ns" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_nw_c" route="route_nw" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ne_c" route="route_ne" begin="bb" end="ee" vehsPerHour="400" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_sw_c" route="route_sw" begin="bb" end="ee" vehsPerHour="400" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_sn_c" route="route_sn" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_se_c" route="route_se" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>

    <flow id="flow_en_c" route="route_en" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ew_c" route="route_ew" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_es_c" route="route_es" begin="bb" end="ee" vehsPerHour="400" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_wn_c" route="route_wn" begin="bb" end="ee" vehsPerHour="400" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_we_c" route="route_we" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ws_c" route="route_ws" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>'''


h4 = v4

v =  '''<flow id="flow_ns_c" route="route_ns" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_nw_c" route="route_nw" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ne_c" route="route_ne" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_sw_c" route="route_sw" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_sn_c" route="route_sn" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_se_c" route="route_se" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>

    <flow id="flow_en_c" route="route_en" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ew_c" route="route_ew" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_es_c" route="route_es" begin="bb" end="ee" vehsPerHour="600" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_wn_c" route="route_wn" begin="bb" end="ee" vehsPerHour="600" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_we_c" route="route_we" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ws_c" route="route_ws" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>'''

h =  '''<flow id="flow_ns_c" route="route_ns" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_nw_c" route="route_nw" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ne_c" route="route_ne" begin="bb" end="ee" vehsPerHour="400" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_sw_c" route="route_sw" begin="bb" end="ee" vehsPerHour="400" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_sn_c" route="route_sn" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_se_c" route="route_se" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>

    <flow id="flow_en_c" route="route_en" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ew_c" route="route_ew" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_es_c" route="route_es" begin="bb" end="ee" vehsPerHour="400" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_wn_c" route="route_wn" begin="bb" end="ee" vehsPerHour="400" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_we_c" route="route_we" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ws_c" route="route_ws" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>'''


v2 =  '''<flow id="flow_ns_c" route="route_ns" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_nw_c" route="route_nw" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ne_c" route="route_ne" begin="bb" end="ee" vehsPerHour="600" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_sw_c" route="route_sw" begin="bb" end="ee" vehsPerHour="600" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_sn_c" route="route_sn" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_se_c" route="route_se" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>

    <flow id="flow_en_c" route="route_en" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ew_c" route="route_ew" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_es_c" route="route_es" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_wn_c" route="route_wn" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_we_c" route="route_we" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ws_c" route="route_ws" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>'''

h2 =  '''<flow id="flow_ns_c" route="route_ns" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_nw_c" route="route_nw" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ne_c" route="route_ne" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_sw_c" route="route_sw" begin="bb" end="ee" vehsPerHour="200" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_sn_c" route="route_sn" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_se_c" route="route_se" begin="bb" end="ee" vehsPerHour="100" departSpeed="max" departPos="base" departLane="best"/>

    <flow id="flow_en_c" route="route_en" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ew_c" route="route_ew" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_es_c" route="route_es" begin="bb" end="ee" vehsPerHour="600" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_wn_c" route="route_wn" begin="bb" end="ee" vehsPerHour="600" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_we_c" route="route_we" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>
    <flow id="flow_ws_c" route="route_ws" begin="bb" end="ee" vehsPerHour="300" departSpeed="max" departPos="base" departLane="best"/>'''

def get_context(begin, end, c):
    if c % 2 == 0:
        s = v
    else:
        s = h
    s = s.replace('c', str(c)).replace('bb', str(begin)).replace('ee', str(end))
    return s

def write_route_file(file, end, step):
    with open(file, 'w+') as f:
        f.write('''<routes>
                <route id="route_ns" edges="3 2"/>
                <route id="route_nw" edges="3 8"/>
                <route id="route_ne" edges="3 6"/>
                <route id="route_we" edges="7 6"/>
                <route id="route_wn" edges="7 4"/>
                <route id="route_ws" edges="7 2"/>
                <route id="route_ew" edges="5 8"/>
                <route id="route_en" edges="5 4"/>
                <route id="route_es" edges="5 2"/>
                <route id="route_sn" edges="1 4"/>
                <route id="route_se" edges="1 6"/>
                <route id="route_sw" edges="1 8"/>''')

        c = 0
        for i in range(0, end, step):
            f.write(get_context(i, i+step, c))
            c += 1
        
        f.write('''</routes>''')

if __name__ == '__main__':
    write_route_file('nets/kilis-deneme_1.rou.xml', 100000, 2000)
