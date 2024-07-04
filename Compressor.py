# encoding: utf-8
import soundfile as sf
import numpy as np

x, Fs = sf.read("speech.wav")   # �����f�[�^�ƃT���v�����O���g���̓ǂݍ���
Len = len(x)                    # �M���̒���

####################
#  �p�����[�^�ݒ�  #
####################
Th = 0.2                        # �������l
a  = 0.1                        # �R���v���b�T�̌X��
ymax = a+(1-a)*Th               # y�̍ő�l����
####################
#  �t�B���^�����O  #
####################
y = np.zeros(Len)               # �o�͐M���̏�����
for n in range(0, Len):         # ���C�����[�v
    if np.abs(x[n])<=Th :       # �o�� y(n)�̌v�Z
        y[n] = x[n]/ymax
    else:
        y[n] = np.sign(x[n]) * ( a*np.abs(x[n])+(1-a)*Th )/ymax

# 16�r�b�g��wav�t�@�C���Ƃ��ď����o��
sf.write("output.wav", y, Fs, format="WAV", subtype="PCM_16") 

