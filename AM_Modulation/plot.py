import os
from PyLTSpice import RawRead

from matplotlib import pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))
LTR = RawRead("AM変調と包絡線検波回路.raw")
target_traces = ["V(source)", "V(modulated)", "V(rectified)", "V(output)"]

print(LTR.get_trace_names())
print(LTR.get_raw_property())

x = LTR.get_trace('time')  # Gets the time axis
# trace_names = [name for name in LTR.get_trace_names() if name != 'time']
trace_names = target_traces

# plt.figure()
# plt.tight_layout()
fig, sub_plts = plt.subplots(len(trace_names), 1, sharex=True)
for trace_name in trace_names  :
    trace = LTR.get_trace(trace_name)
    steps = LTR.get_steps()
    index = trace_names.index(trace_name)
    # plt.subplot(len(trace_names), 1, trace_names.index(trace_name)+1, sharex=True)
    for step in range(len(steps)):
        if len(steps) > 1:
            plt.plot(x.get_wave(step), trace.get_wave(step), label=steps[step])
        else:
            # plt.plot(x.get_wave(step), trace.get_wave(step))
            sub_plts[index].plot(x.get_wave(step), trace.get_wave(step))
    sub_plts[index].set_title(trace_name)
plt.subplots_adjust(hspace=0.5)
plt.show(block=True)