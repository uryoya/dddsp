#! /bin/bash
python3 app.py 9001 'chino.org' > dsp1.log 2>&1 &
python3 app.py 9002 'cocoa.com' > dsp2.log 2>&1 &
python3 app.py 9003 'rize.com' > dsp3.log 2>&1 &
python3 app.py 9004 'chia.co.jp' > dsp4.log 2>&1 &
python3 app.py 9005 'sharo.net' > dsp5.log 2>&1 &
