import os
import time

trace_files = [
    "rnet_rnet_ti",
    "rnet_mnet_ti",
    "mnet_rnet_ti",
    "mnet_mnet_ti",
    "rnet101_rnet_ti",
    "rnet101_mnet_ti",
    "bert_rnet_ti",
    "bert_mnet_ti",
    "trans_rnet_ti",
    "trans_mnet_ti",
]



#orion, hp is inference - uniform
# depths = [110000, 100000, 150000, 1250000, 400000,
#           110000, 100000, 150000, 1250000, 400000,
#           110000, 100000, 150000, 1250000, 400000,
#           110000, 100000, 150000, 1250000, 400000,
#           110000, 100000, 150000, 1250000, 400000]

# orion, hp is inference, threshold is 0.05
# depths = [320000, 300000, 400000, 2500000, 800000,
#           320000, 300000, 400000, 2500000, 800000,
#           320000, 300000, 400000, 2500000, 800000,
#           320000, 300000, 400000, 2500000, 800000,
#           320000, 300000, 400000, 2500000, 800000]

depths = [
    6,5,10,48,16,
    8,6,13,58,21,
    8,6,13,60,21,
    16,13,27,123,43,
    22,17,36,170,59,
]

limits = [1,1,1,1,1,
          1,1,1,1,1,
          1,1,1,1,1,
          1,1,1,1,1,
          1,1,1,1,1]
updates = [1,1,1,1,1,
           1,1,1,1,1,
           1,1,1,1,1,
           1,1,1,1,1,
           1,1,1,1,1]


# # orion, hp is training
# depths = [
#     1000000, 1000000, 1000000, 40000000, 32000000,
#     1000000, 1000000, 1000000, 40000000, 32000000,
#     1000000, 1000000, 1000000, 40000000, 32000000,
#     1000000, 1000000, 1000000, 40000000, 32000000,
#     1000000, 1000000, 1000000, 40000000, 32000000
# ]
# limits = [
#     135, 120, 235, 250, 250,
#     135, 120, 235, 250, 250,
#     135, 120, 235, 250, 250,
#     135, 120, 235, 250, 250,
#     135, 120, 235, 250, 250
# ]
# updates = [
#     768, 733, 1534, 2669, 1622,
#     768, 733, 1534, 2669, 1622,
#     768, 733, 1534, 2669, 1622,
#     768, 733, 1534, 2669, 1622,
#     768, 733, 1534, 2669, 1622
# ]



print(len(trace_files), len(depths))
assert len(trace_files) == len(depths)
for f,d,l,u in zip(trace_files, depths, limits, updates):
    print(f,d, flush=True)
    file_path = f"eval/inf_inf/poisson/{f}.json"
    os.system(f"python launch_jobs.py {file_path} {d} {l} {u}")
    time.sleep(10)
