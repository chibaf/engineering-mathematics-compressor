# encoding: utf-8
import soundfile as sf
import numpy as np

x, Fs = sf.read("speech.wav")   # 音声データとサンプリング周波数の読み込み
Len = len(x)                    # 信号の長さ

####################
#  パラメータ設定  #
####################
Th = 0.2                        # しきい値
a  = 0.1                        # コンプレッサの傾き
ymax = a+(1-a)*Th               # yの最大値調整
####################
#  フィルタリング  #
####################
y = np.zeros(Len)               # 出力信号の初期化
for n in range(0, Len):         # メインループ
    if np.abs(x[n])<=Th :       # 出力 y(n)の計算
        y[n] = x[n]/ymax
    else:
        y[n] = np.sign(x[n]) * ( a*np.abs(x[n])+(1-a)*Th )/ymax

# 16ビットのwavファイルとして書き出す
sf.write("output.wav", y, Fs, format="WAV", subtype="PCM_16") 

