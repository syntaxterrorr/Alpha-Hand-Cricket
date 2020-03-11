# Alpha-Hand-Cricket
A hand cricket game bot using reinforcement learning. Final year project for B.E. (Engineering).

Fortnightly reports: https://docs.google.com/spreadsheets/d/1TMdjrsPuM0FtMCsIjYVejufDfuTNtKeGaQPBF9INE4A/edit?usp=sharing

White book: https://drive.google.com/file/d/1-QFvDTL7rCVm590t0Uq06CQhM2Txg6S0/view?usp=sharing

### Database Setup
1. Create database
```
$ mysql -u <username> -p 
mysql> CREATE DATABASE alpha_hand_cricket
```
2. Import database schema
```
$ mysql -u <username> -p alpha_hand_cricket < sql/ddl.sql`
```
3. To include sample data (optional)
```
$ mysql -u <username> -p alpha_hand_cricket < sql/sample_dml.sql`
```
### Play Game
```
$ python alpha_hand_cricket.py
```
### MediaPipe
1. Installation link: https://mediapipe.readthedocs.io/en/latest/install.html (If installing on Debian and Ubuntu, preferably run setup_opencv.sh to automatically build OpenCV from source and modify MediaPipe’s OpenCV config.
2. Run hand tracking model on CPU
```
$ bazel build -c opt --define MEDIAPIPE_DISABLE_GPU=1 mediapipe/examples/desktop/hand_tracking:hand_tracking_cpu
$ GLOG_logtostderr=1 bazel-bin/mediapipe/examples/desktop/hand_tracking/hand_tracking_cpu --calculator_graph_config_file=mediapipe/graphs/hand_tracking/hand_tracking_desktop_live.pbtxt
```
3. Run hand tracking model on GPU (Only Linux)
```
$ bazel build -c opt --copt -DMESA_EGL_NO_X11_HEADERS mediapipe/examples/desktop/hand_tracking:hand_tracking_gpu
$ GLOG_logtostderr=1 bazel-bin/mediapipe/examples/desktop/hand_tracking/hand_tracking_gpu --calculator_graph_config_file=mediapipe/graphs/hand_tracking/hand_tracking_mobile.pbtxt
```
