一、依赖安装

pip install opencv-python    (即cv2)

pip install tflearn
然后根据依赖缺失安装其余依赖


#******************以下方式仅限pycharm运行环境，在Terminal内运行指令**************
pip freeze > requirements.txt    #第一步

pip install -r requirements.txt    #第二步

运行程序，根据缺失安装剩余依赖
#*******************************************************************************
二、配置信息

webcam.py文件第31行  vc = cv2.VideoCapture(1)
括号内数为调用的摄像头选项，0为本地摄像头，按需要修改


三、启动方式

运行webcam.py即可

摄像头启动后，保持80>cm距离以便识别


四、测试用例

识别效果仅供娱乐