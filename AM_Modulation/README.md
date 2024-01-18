# 包絡線検波(envelope detector)

搬送波（10kHz）を変調信号（V(souce)，100Hz，DC成分含む）でAM変調した波形（V(mosulated)）を包絡線検波で変調信号を復元するシミュレーションです．

包絡線検波部の素子はAnalog Devicesが公開している資料と同じ値にしました．
https://wiki.analog.com/university/courses/electronics/electronics-lab-envelope-detector

同資料の回路のままではDC成分が残るので，ハイパスフィルタで切っています．
