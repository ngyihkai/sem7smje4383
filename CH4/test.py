(base) imetnyk@imetnyk-System-Product-Name:~/Downloads$ anaconda navigator
usage: anaconda [-h] [--disable-ssl-warnings] [--show-traceback] [-v] [-q]
                [-V] [-t TOKEN] [-s SITE]
                ...
anaconda: error: argument : invalid choice: 'navigator' (choose from 'auth', 'label', 'channel', 'config', 'copy', 'download', 'groups', 'login', 'logout', 'move', 'notebook', 'package', 'remove', 'search', 'show', 'upload', 'whoami')
(base) imetnyk@imetnyk-System-Product-Name:~/Downloads$ anaconda-navigator
ldd --version

. ~/anaconda3/etc/profile.d/conda.sh
conda activate
conda create --name CloudComPy39 python=3.9
# --- erase previous env if existing
conda activate CloudComPy39
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install qt numpy psutil boost xerces-c pcl gdal cgal cmake pdal opencv ffmpeg mysql "qhull=2019.1" matplotlib "eigen=3.3.9" tbb openmp

^C
(base) imetnyk@imetnyk-System-Product-Name:~/Downloads$ . ~/anaconda3/etc/profile.d/conda.sh
(base) imetnyk@imetnyk-System-Product-Name:~/Downloads$ conda activate
(base) imetnyk@imetnyk-System-Product-Name:~/Downloads$ conda create --name CloudComPy39 python=3.9
Collecting package metadata (current_repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.9.2
  latest version: 4.10.3

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /home/imetnyk/anaconda3/envs/CloudComPy39

  added / updated specs:
    - python=3.9


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    _openmp_mutex-4.5          |            1_gnu          22 KB
    ca-certificates-2021.10.26 |       h06a4308_2         115 KB
    certifi-2021.10.8          |   py39h06a4308_0         151 KB
    ld_impl_linux-64-2.35.1    |       h7274673_9         586 KB
    libgcc-ng-9.3.0            |      h5101ec6_17         4.8 MB
    libgomp-9.3.0              |      h5101ec6_17         311 KB
    libstdcxx-ng-9.3.0         |      hd4cf53a_17         3.1 MB
    ncurses-6.3                |       h7f8727e_2         782 KB
    openssl-1.1.1l             |       h7f8727e_0         2.5 MB
    pip-21.2.4                 |   py39h06a4308_0         1.8 MB
    python-3.9.7               |       h12debd9_1        18.6 MB
    readline-8.1               |       h27cfd23_0         362 KB
    setuptools-58.0.4          |   py39h06a4308_0         790 KB
    sqlite-3.36.0              |       hc218d9a_0         990 KB
    tk-8.6.11                  |       h1ccaba5_0         3.0 MB
    tzdata-2021e               |       hda174b7_0         112 KB
    wheel-0.37.0               |     pyhd3eb1b0_1          33 KB
    ------------------------------------------------------------
                                           Total:        37.9 MB

The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-4.5-1_gnu
  ca-certificates    pkgs/main/linux-64::ca-certificates-2021.10.26-h06a4308_2
  certifi            pkgs/main/linux-64::certifi-2021.10.8-py39h06a4308_0
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.35.1-h7274673_9
  libffi             pkgs/main/linux-64::libffi-3.3-he6710b0_2
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-9.3.0-h5101ec6_17
  libgomp            pkgs/main/linux-64::libgomp-9.3.0-h5101ec6_17
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-9.3.0-hd4cf53a_17
  ncurses            pkgs/main/linux-64::ncurses-6.3-h7f8727e_2
  openssl            pkgs/main/linux-64::openssl-1.1.1l-h7f8727e_0
  pip                pkgs/main/linux-64::pip-21.2.4-py39h06a4308_0
  python             pkgs/main/linux-64::python-3.9.7-h12debd9_1
  readline           pkgs/main/linux-64::readline-8.1-h27cfd23_0
  setuptools         pkgs/main/linux-64::setuptools-58.0.4-py39h06a4308_0
  sqlite             pkgs/main/linux-64::sqlite-3.36.0-hc218d9a_0
  tk                 pkgs/main/linux-64::tk-8.6.11-h1ccaba5_0
  tzdata             pkgs/main/noarch::tzdata-2021e-hda174b7_0
  wheel              pkgs/main/noarch::wheel-0.37.0-pyhd3eb1b0_1
  xz                 pkgs/main/linux-64::xz-5.2.5-h7b6447c_0
  zlib               pkgs/main/linux-64::zlib-1.2.11-h7b6447c_3


Proceed ([y]/n)? y
conda install qt numpy psutil boost xerces-c pcl gdal cgal cmake pdal opencv ffmyeg mysql "qhull=2019.1" matplotlib "eigen=3.3.9" tbb openmp
Proceed ([y]/n)? y


Downloading and Extracting Packages
readline-8.1         | 362 KB    | ##################################### | 100% 
tk-8.6.11            | 3.0 MB    | ##################################### | 100% 
python-3.9.7         | 18.6 MB   | ##################################### | 100% 
libgomp-9.3.0        | 311 KB    | ##################################### | 100% 
setuptools-58.0.4    | 790 KB    | ##################################### | 100% 
libstdcxx-ng-9.3.0   | 3.1 MB    | ##################################### | 100% 
_openmp_mutex-4.5    | 22 KB     | ##################################### | 100% 
sqlite-3.36.0        | 990 KB    | ##################################### | 100% 
ncurses-6.3          | 782 KB    | ##################################### | 100% 
certifi-2021.10.8    | 151 KB    | ##################################### | 100% 
ca-certificates-2021 | 115 KB    | ##################################### | 100% 
openssl-1.1.1l       | 2.5 MB    | ##################################### | 100% 
tzdata-2021e         | 112 KB    | ##################################### | 100% 
libgcc-ng-9.3.0      | 4.8 MB    | ##################################### | 100% 
pip-21.2.4           | 1.8 MB    | ##################################### | 100% 
wheel-0.37.0         | 33 KB     | ##################################### | 100% 
ld_impl_linux-64-2.3 | 586 KB    | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate CloudComPy39
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) imetnyk@imetnyk-System-Product-Name:~/Downloads$ conda activate CloudComPy39
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ . ~/anaconda3/etc/profile.d/conda.sh
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ conda activate CloudComPy39
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=~/anaconda3/envs/CloudComPy39/lib:${LD_LIBRARY_PATH}
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=<path install>/lib/cloudcompare:${LD_LIBRARY_PATH}
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=<path install>/lib/cloudcompare/plugins:${LD_LIBRARY_PATH}
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=~/anaconda3/envs/CloudComPy39/lib:${LD_LIBRARY_PATH}
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=<path install>/lib/cloudcompare:${LD_LIBRARY_PATH}
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=<path install>/lib/cloudcompare/plugins:${LD_LIBRARY_PATH}
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ <path install>/bin/CloudCompare
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=<path install>/lib/cloudcompare:${LD_LIBRARY_PATH}
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/lib/cloudcompare:${LD_LIBRARY_PATH}
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=<path install>/lib/cloudcompare/plugins:${LD_LIBRARY_PATH}
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=export LD_LIBRARY_PATH=<path install>/lib/cloudcompare/plugins:${LD_LIBRARY_PATH}/lib/cloudcompare/plugins:${LD_LIBRARY_PATH}
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=<path install>/lib/cloudcompare/plugins:${LD_LIBRARY_PATH}
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ export LD_LIBRARY_PATH=/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/lib/cloudcompare/plugins:${LD_LIBRARY_PATH}
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ ~Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: ~Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ cd Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: cd: Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ cd
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~$ /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~$ cd Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: cd: Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: Not a directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~$ cd Downloads
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads$ cd CloudComPy_Conda39_Linux64_20211018
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018$ cd CloudComPy_Conda39_Linux64_20211018
bash: cd: CloudComPy_Conda39_Linux64_20211018: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018$ cd installConda39
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39$ cd bin
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin$ cd CloudCompare
bash: cd: CloudCompare: Not a directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin$ cd  <path install>/doc/PythonAPI_test
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin$ cd  /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test
bash: cd: /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin$ cd Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test
bash: cd: Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin$ cd 
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~$ cd /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test
bash: cd: /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~$ ctest

Command 'ctest' not found, but can be installed with:

sudo snap install cmake  # version 3.22.0, or
sudo apt  install cmake  # version 3.16.3-1ubuntu1

See 'snap info cmake' for additional versions.

(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~$ export LD_LIBRARY_PATH=<path install>/lib/cloudcompare/plugins:${LD_LIBRARY_PATH}
bash: path: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~$ export LD_LIBRARY_PATH=/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/lib/cloudcompare/plugins:${LD_LIBRARY_PATH}
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~$ /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: /Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~$ cd Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare
bash: cd: Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/bin/CloudCompare: Not a directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~$ cd Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ ctest

Command 'ctest' not found, but can be installed with:

sudo snap install cmake  # version 3.22.0, or
sudo apt  install cmake  # version 3.16.3-1ubuntu1

See 'snap info cmake' for additional versions.

(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ sudo snap install cmake  # version 3.22.0, or
[sudo] password for imetnyk: 
error: This revision of snap "cmake" was published using classic confinement
       and thus may perform arbitrary system changes outside of the security
       sandbox that snaps are usually confined to, which may put your system
       at risk.

       If you understand and want to proceed repeat the command including
       --classic.
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ sudo snap install cmake  # version 3.22.0
error: This revision of snap "cmake" was published using classic confinement
       and thus may perform arbitrary system changes outside of the security
       sandbox that snaps are usually confined to, which may put your system
       at risk.

       If you understand and want to proceed repeat the command including
       --classic.
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ sudo snap install cmake  # version 3.22.0 --classic
error: This revision of snap "cmake" was published using classic confinement
       and thus may perform arbitrary system changes outside of the security
       sandbox that snaps are usually confined to, which may put your system
       at risk.

       If you understand and want to proceed repeat the command including
       --classic.
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ sudo apt  install cmake  # version 3.16.3-1ubuntu1
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  chromium-codecs-ffmpeg-extra gstreamer1.0-vaapi
  libgstreamer-plugins-bad1.0-0 libllvm11 libva-wayland2
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  cmake-data gcc gcc-9 libasan5 libatomic1 libc-dev-bin libc6-dev
  libcrypt-dev libgcc-9-dev libitm1 libjsoncpp1 liblsan0 libquadmath0
  librhash0 libtsan0 libubsan1 linux-libc-dev make manpages-dev
Suggested packages:
  cmake-doc ninja-build gcc-multilib autoconf automake libtool flex bison
  gcc-doc gcc-9-multilib gcc-9-doc gcc-9-locales glibc-doc make-doc
The following NEW packages will be installed:
  cmake cmake-data gcc gcc-9 libasan5 libatomic1 libc-dev-bin libc6-dev
  libcrypt-dev libgcc-9-dev libitm1 libjsoncpp1 liblsan0 libquadmath0
  librhash0 libtsan0 libubsan1 linux-libc-dev make manpages-dev
0 upgraded, 20 newly installed, 0 to remove and 4 not upgraded.
Need to get 26.5 MB/26.5 MB of archives.
After this operation, 122 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://my.archive.ubuntu.com/ubuntu focal/main amd64 cmake-data all 3.16.3-1ubuntu1 [1,612 kB]
Get:2 http://my.archive.ubuntu.com/ubuntu focal/main amd64 libjsoncpp1 amd64 1.7.4-3.1ubuntu2 [75.6 kB]
Get:3 http://my.archive.ubuntu.com/ubuntu focal/main amd64 librhash0 amd64 1.3.9-1 [113 kB]
Get:4 http://my.archive.ubuntu.com/ubuntu focal/main amd64 cmake amd64 3.16.3-1ubuntu1 [3,669 kB]
Get:5 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 libitm1 amd64 10.3.0-1ubuntu1~20.04 [26.2 kB]
Get:6 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 libasan5 amd64 9.3.0-17ubuntu1~20.04 [394 kB]
Get:7 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 liblsan0 amd64 10.3.0-1ubuntu1~20.04 [835 kB]
Get:8 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 libtsan0 amd64 10.3.0-1ubuntu1~20.04 [2,009 kB]
Get:9 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 libubsan1 amd64 10.3.0-1ubuntu1~20.04 [784 kB]
Get:10 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 libquadmath0 amd64 10.3.0-1ubuntu1~20.04 [146 kB]
Get:11 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 libgcc-9-dev amd64 9.3.0-17ubuntu1~20.04 [2,360 kB]
Get:12 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 gcc-9 amd64 9.3.0-17ubuntu1~20.04 [8,241 kB]
Get:13 http://my.archive.ubuntu.com/ubuntu focal/main amd64 gcc amd64 4:9.3.0-1ubuntu2 [5,208 B]
Get:14 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 libc-dev-bin amd64 2.31-0ubuntu9.2 [71.8 kB]
Ign:15 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 linux-libc-dev amd64 5.4.0-89.100
Get:16 http://my.archive.ubuntu.com/ubuntu focal/main amd64 libcrypt-dev amd64 1:4.4.10-10ubuntu4 [104 kB]
Get:17 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 libc6-dev amd64 2.31-0ubuntu9.2 [2,520 kB]
Get:18 http://my.archive.ubuntu.com/ubuntu focal/main amd64 make amd64 4.2.1-1.2 [162 kB]
Get:19 http://my.archive.ubuntu.com/ubuntu focal/main amd64 manpages-dev all 5.05-1 [2,266 kB]
Err:15 http://security.ubuntu.com/ubuntu focal-updates/main amd64 linux-libc-dev amd64 5.4.0-89.100
  404  Not Found [IP: 202.79.184.254 80]
Fetched 25.4 MB in 2s (10.5 MB/s)                              
E: Failed to fetch http://security.ubuntu.com/ubuntu/pool/main/l/linux/linux-libc-dev_5.4.0-89.100_amd64.deb  404  Not Found [IP: 202.79.184.254 80]
E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ ctest

Command 'ctest' not found, but can be installed with:

sudo snap install cmake  # version 3.22.0, or
sudo apt  install cmake  # version 3.16.3-1ubuntu1

See 'snap info cmake' for additional versions.

(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ sudo apt-get update
Hit:1 http://my.archive.ubuntu.com/ubuntu focal InRelease
Get:2 http://my.archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]    
Get:3 http://my.archive.ubuntu.com/ubuntu focal-backports InRelease [101 kB]  
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,811 B]       
Get:5 https://linux.teamviewer.com/deb stable InRelease [11.9 kB]             
Get:6 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]     
Get:7 http://ppa.launchpad.net/opencpn/opencpn/ubuntu focal InRelease [23.8 kB]
Get:8 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [1,344 kB]
Get:9 http://my.archive.ubuntu.com/ubuntu focal-updates/main i386 Packages [563 kB]
Get:10 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,072 B]
Get:11 http://my.archive.ubuntu.com/ubuntu focal-updates/main Translation-en [276 kB]
Get:12 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 DEP-11 Metadata [279 kB]
Get:13 http://my.archive.ubuntu.com/ubuntu focal-updates/main DEP-11 48x48 Icons [60.8 kB]
Get:14 http://my.archive.ubuntu.com/ubuntu focal-updates/main DEP-11 64x64 Icons [98.3 kB]
Get:15 https://linux.teamviewer.com/deb stable/main i386 Packages [11.7 kB]   
Get:16 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 c-n-f Metadata [14.5 kB]
Get:17 http://my.archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [569 kB]
Get:18 https://linux.teamviewer.com/deb stable/main amd64 Packages [11.9 kB]  
Get:19 http://my.archive.ubuntu.com/ubuntu focal-updates/restricted i386 Packages [21.7 kB]
Get:20 http://my.archive.ubuntu.com/ubuntu focal-updates/restricted Translation-en [81.6 kB]
Get:21 http://my.archive.ubuntu.com/ubuntu focal-updates/restricted amd64 c-n-f Metadata [528 B]
Get:22 http://my.archive.ubuntu.com/ubuntu focal-updates/universe i386 Packages [647 kB]
Get:23 http://my.archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [876 kB]
Get:24 http://my.archive.ubuntu.com/ubuntu focal-updates/universe Translation-en [190 kB]
Get:25 http://my.archive.ubuntu.com/ubuntu focal-updates/universe amd64 DEP-11 Metadata [357 kB]
Get:26 http://my.archive.ubuntu.com/ubuntu focal-updates/universe DEP-11 48x48 Icons [217 kB]
Get:27 http://my.archive.ubuntu.com/ubuntu focal-updates/universe DEP-11 64x64 Icons [385 kB]
Get:28 http://my.archive.ubuntu.com/ubuntu focal-updates/universe amd64 c-n-f Metadata [19.5 kB]
Get:29 http://my.archive.ubuntu.com/ubuntu focal-updates/multiverse i386 Packages [8,204 B]
Get:30 http://my.archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [24.5 kB]
Get:31 http://my.archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 DEP-11 Metadata [940 B]
Get:32 http://my.archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 c-n-f Metadata [616 B]
Get:33 http://my.archive.ubuntu.com/ubuntu focal-backports/universe amd64 Packages [6,588 B]
Get:34 http://my.archive.ubuntu.com/ubuntu focal-backports/universe i386 Packages [5,536 B]
Get:35 http://my.archive.ubuntu.com/ubuntu focal-backports/universe Translation-en [3,292 B]
Get:36 http://my.archive.ubuntu.com/ubuntu focal-backports/universe amd64 DEP-11 Metadata [10.4 kB]
Get:37 http://my.archive.ubuntu.com/ubuntu focal-backports/universe DEP-11 64x64 Icons [5,607 B]
Get:38 http://my.archive.ubuntu.com/ubuntu focal-backports/universe amd64 c-n-f Metadata [580 B]
Get:39 http://ppa.launchpad.net/opencpn/opencpn/ubuntu focal/main amd64 Packages [2,192 B]
Get:40 http://security.ubuntu.com/ubuntu focal-security/main i386 Packages [306 kB]
Get:41 http://ppa.launchpad.net/opencpn/opencpn/ubuntu focal/main Translation-en [944 B]
Get:42 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [987 kB]
Get:43 http://security.ubuntu.com/ubuntu focal-security/main Translation-en [184 kB]
Get:44 http://security.ubuntu.com/ubuntu focal-security/main amd64 DEP-11 Metadata [29.0 kB]
Get:45 http://security.ubuntu.com/ubuntu focal-security/main amd64 c-n-f Metadata [8,880 B]
Get:46 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [526 kB]
Get:47 http://security.ubuntu.com/ubuntu focal-security/restricted i386 Packages [20.4 kB]
Get:48 http://security.ubuntu.com/ubuntu focal-security/restricted Translation-en [75.4 kB]
Get:49 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 c-n-f Metadata [528 B]
Get:50 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [653 kB]
Get:51 http://security.ubuntu.com/ubuntu focal-security/universe i386 Packages [515 kB]
Get:52 http://security.ubuntu.com/ubuntu focal-security/universe Translation-en [107 kB]
Get:53 http://security.ubuntu.com/ubuntu focal-security/universe amd64 DEP-11 Metadata [63.6 kB]
Get:54 http://security.ubuntu.com/ubuntu focal-security/universe amd64 c-n-f Metadata [12.9 kB]
Get:55 http://security.ubuntu.com/ubuntu focal-security/multiverse i386 Packages [7,212 B]
Get:56 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [21.9 kB]
Get:57 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 DEP-11 Metadata [2,464 B]
Get:58 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 c-n-f Metadata [540 B]
Fetched 9,980 kB in 3s (3,974 kB/s)                             
Reading package lists... Done
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ ctest

Command 'ctest' not found, but can be installed with:

sudo snap install cmake  # version 3.22.0, or
sudo apt  install cmake  # version 3.16.3-1ubuntu1

See 'snap info cmake' for additional versions.

(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ sudo apt  install cmake  # version 3.16.3-1ubuntu1
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  chromium-codecs-ffmpeg-extra gstreamer1.0-vaapi
  libgstreamer-plugins-bad1.0-0 libllvm11 libva-wayland2
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  cmake-data gcc gcc-9 libasan5 libatomic1 libc-dev-bin libc6-dev
  libcrypt-dev libgcc-9-dev libitm1 libjsoncpp1 liblsan0 libquadmath0
  librhash0 libtsan0 libubsan1 linux-libc-dev make manpages-dev
Suggested packages:
  cmake-doc ninja-build gcc-multilib autoconf automake libtool flex bison
  gcc-doc gcc-9-multilib gcc-9-doc gcc-9-locales glibc-doc make-doc
The following NEW packages will be installed:
  cmake cmake-data gcc gcc-9 libasan5 libatomic1 libc-dev-bin libc6-dev
  libcrypt-dev libgcc-9-dev libitm1 libjsoncpp1 liblsan0 libquadmath0
  librhash0 libtsan0 libubsan1 linux-libc-dev make manpages-dev
0 upgraded, 20 newly installed, 0 to remove and 73 not upgraded.
Need to get 1,123 kB/26.5 MB of archives.
After this operation, 122 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://my.archive.ubuntu.com/ubuntu focal-updates/main amd64 linux-libc-dev amd64 5.4.0-90.101 [1,123 kB]
Fetched 1,123 kB in 0s (4,772 kB/s)       
Selecting previously unselected package cmake-data.
(Reading database ... 190398 files and directories currently installed.)
Preparing to unpack .../00-cmake-data_3.16.3-1ubuntu1_all.deb ...
Unpacking cmake-data (3.16.3-1ubuntu1) ...
Selecting previously unselected package libjsoncpp1:amd64.
Preparing to unpack .../01-libjsoncpp1_1.7.4-3.1ubuntu2_amd64.deb ...
Unpacking libjsoncpp1:amd64 (1.7.4-3.1ubuntu2) ...
Selecting previously unselected package librhash0:amd64.
Preparing to unpack .../02-librhash0_1.3.9-1_amd64.deb ...
Unpacking librhash0:amd64 (1.3.9-1) ...
Selecting previously unselected package cmake.
Preparing to unpack .../03-cmake_3.16.3-1ubuntu1_amd64.deb ...
Unpacking cmake (3.16.3-1ubuntu1) ...
Selecting previously unselected package libitm1:amd64.
Preparing to unpack .../04-libitm1_10.3.0-1ubuntu1~20.04_amd64.deb ...
Unpacking libitm1:amd64 (10.3.0-1ubuntu1~20.04) ...
Selecting previously unselected package libatomic1:amd64.
Preparing to unpack .../05-libatomic1_10.3.0-1ubuntu1~20.04_amd64.deb ...
Unpacking libatomic1:amd64 (10.3.0-1ubuntu1~20.04) ...
Selecting previously unselected package libasan5:amd64.
Preparing to unpack .../06-libasan5_9.3.0-17ubuntu1~20.04_amd64.deb ...
Unpacking libasan5:amd64 (9.3.0-17ubuntu1~20.04) ...
Selecting previously unselected package liblsan0:amd64.
Preparing to unpack .../07-liblsan0_10.3.0-1ubuntu1~20.04_amd64.deb ...
Unpacking liblsan0:amd64 (10.3.0-1ubuntu1~20.04) ...
Selecting previously unselected package libtsan0:amd64.
Preparing to unpack .../08-libtsan0_10.3.0-1ubuntu1~20.04_amd64.deb ...
Unpacking libtsan0:amd64 (10.3.0-1ubuntu1~20.04) ...
Selecting previously unselected package libubsan1:amd64.
Preparing to unpack .../09-libubsan1_10.3.0-1ubuntu1~20.04_amd64.deb ...
Unpacking libubsan1:amd64 (10.3.0-1ubuntu1~20.04) ...
Selecting previously unselected package libquadmath0:amd64.
Preparing to unpack .../10-libquadmath0_10.3.0-1ubuntu1~20.04_amd64.deb ...
Unpacking libquadmath0:amd64 (10.3.0-1ubuntu1~20.04) ...
Selecting previously unselected package libgcc-9-dev:amd64.
Preparing to unpack .../11-libgcc-9-dev_9.3.0-17ubuntu1~20.04_amd64.deb ...
Unpacking libgcc-9-dev:amd64 (9.3.0-17ubuntu1~20.04) ...
Selecting previously unselected package gcc-9.
Preparing to unpack .../12-gcc-9_9.3.0-17ubuntu1~20.04_amd64.deb ...
Unpacking gcc-9 (9.3.0-17ubuntu1~20.04) ...
Selecting previously unselected package gcc.
Preparing to unpack .../13-gcc_4%3a9.3.0-1ubuntu2_amd64.deb ...
Unpacking gcc (4:9.3.0-1ubuntu2) ...
Selecting previously unselected package libc-dev-bin.
Preparing to unpack .../14-libc-dev-bin_2.31-0ubuntu9.2_amd64.deb ...
Unpacking libc-dev-bin (2.31-0ubuntu9.2) ...
Selecting previously unselected package linux-libc-dev:amd64.
Preparing to unpack .../15-linux-libc-dev_5.4.0-90.101_amd64.deb ...
Unpacking linux-libc-dev:amd64 (5.4.0-90.101) ...
Selecting previously unselected package libcrypt-dev:amd64.
Preparing to unpack .../16-libcrypt-dev_1%3a4.4.10-10ubuntu4_amd64.deb ...
Unpacking libcrypt-dev:amd64 (1:4.4.10-10ubuntu4) ...
Selecting previously unselected package libc6-dev:amd64.
Preparing to unpack .../17-libc6-dev_2.31-0ubuntu9.2_amd64.deb ...
Unpacking libc6-dev:amd64 (2.31-0ubuntu9.2) ...
Selecting previously unselected package make.
Preparing to unpack .../18-make_4.2.1-1.2_amd64.deb ...
Unpacking make (4.2.1-1.2) ...
Selecting previously unselected package manpages-dev.
Preparing to unpack .../19-manpages-dev_5.05-1_all.deb ...
Unpacking manpages-dev (5.05-1) ...
Setting up manpages-dev (5.05-1) ...
Setting up linux-libc-dev:amd64 (5.4.0-90.101) ...
Setting up libasan5:amd64 (9.3.0-17ubuntu1~20.04) ...
Setting up make (4.2.1-1.2) ...
Setting up libquadmath0:amd64 (10.3.0-1ubuntu1~20.04) ...
Setting up libatomic1:amd64 (10.3.0-1ubuntu1~20.04) ...
Setting up libubsan1:amd64 (10.3.0-1ubuntu1~20.04) ...
Setting up librhash0:amd64 (1.3.9-1) ...
Setting up libcrypt-dev:amd64 (1:4.4.10-10ubuntu4) ...
Setting up cmake-data (3.16.3-1ubuntu1) ...
Setting up libc-dev-bin (2.31-0ubuntu9.2) ...
Setting up liblsan0:amd64 (10.3.0-1ubuntu1~20.04) ...
Setting up libitm1:amd64 (10.3.0-1ubuntu1~20.04) ...
Setting up libjsoncpp1:amd64 (1.7.4-3.1ubuntu2) ...
Setting up libtsan0:amd64 (10.3.0-1ubuntu1~20.04) ...
Setting up libgcc-9-dev:amd64 (9.3.0-17ubuntu1~20.04) ...
Setting up cmake (3.16.3-1ubuntu1) ...
Setting up libc6-dev:amd64 (2.31-0ubuntu9.2) ...
Setting up gcc-9 (9.3.0-17ubuntu1~20.04) ...
Setting up gcc (4:9.3.0-1ubuntu2) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.2) ...
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ ctest
Test project /home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test
      Start  1: PYCC_test001
 1/25 Test  #1: PYCC_test001 .....................***Failed    0.02 sec
      Start  2: PYCC_test002
 2/25 Test  #2: PYCC_test002 .....................***Failed    0.02 sec
      Start  3: PYCC_test003
 3/25 Test  #3: PYCC_test003 .....................***Failed    0.02 sec
      Start  4: PYCC_test004
 4/25 Test  #4: PYCC_test004 .....................***Failed    0.02 sec
      Start  5: PYCC_test005
 5/25 Test  #5: PYCC_test005 .....................***Failed    0.02 sec
      Start  6: PYCC_test006
 6/25 Test  #6: PYCC_test006 .....................***Failed    0.02 sec
      Start  7: PYCC_test007
 7/25 Test  #7: PYCC_test007 .....................***Failed    0.02 sec
      Start  8: PYCC_test008
 8/25 Test  #8: PYCC_test008 .....................***Failed    0.02 sec
      Start  9: PYCC_test009
 9/25 Test  #9: PYCC_test009 .....................***Failed    0.02 sec
      Start 10: PYCC_test010
10/25 Test #10: PYCC_test010 .....................***Failed    0.02 sec
      Start 11: PYCC_test011
11/25 Test #11: PYCC_test011 .....................***Failed    0.02 sec
      Start 12: PYCC_test012
12/25 Test #12: PYCC_test012 .....................***Failed    0.02 sec
      Start 13: PYCC_test013
13/25 Test #13: PYCC_test013 .....................***Failed    0.02 sec
      Start 14: PYCC_test014
14/25 Test #14: PYCC_test014 .....................***Failed    0.02 sec
      Start 15: PYCC_test015
15/25 Test #15: PYCC_test015 .....................***Failed    0.02 sec
      Start 16: PYCC_test016
16/25 Test #16: PYCC_test016 .....................***Failed    0.02 sec
      Start 17: PYCC_test017
17/25 Test #17: PYCC_test017 .....................***Failed    0.02 sec
      Start 18: PYCC_test018
18/25 Test #18: PYCC_test018 .....................***Failed    0.02 sec
      Start 19: PYCC_test019
19/25 Test #19: PYCC_test019 .....................***Failed    0.02 sec
      Start 20: PYCC_test020
20/25 Test #20: PYCC_test020 .....................***Failed    0.02 sec
      Start 21: PYCC_test021
21/25 Test #21: PYCC_test021 .....................***Failed    0.02 sec
      Start 22: PYCC_test022
22/25 Test #22: PYCC_test022 .....................***Failed    0.02 sec
      Start 23: PYCC_test023
23/25 Test #23: PYCC_test023 .....................***Failed    0.02 sec
      Start 24: PYCC_test024
24/25 Test #24: PYCC_test024 .....................***Failed    0.02 sec
      Start 25: PYCC_test025
25/25 Test #25: PYCC_test025 .....................***Failed    0.02 sec

0% tests passed, 25 tests failed out of 25

Total Test time (real) =   0.44 sec

The following tests FAILED:
	  1 - PYCC_test001 (Failed)
	  2 - PYCC_test002 (Failed)
	  3 - PYCC_test003 (Failed)
	  4 - PYCC_test004 (Failed)
	  5 - PYCC_test005 (Failed)
	  6 - PYCC_test006 (Failed)
	  7 - PYCC_test007 (Failed)
	  8 - PYCC_test008 (Failed)
	  9 - PYCC_test009 (Failed)
	 10 - PYCC_test010 (Failed)
	 11 - PYCC_test011 (Failed)
	 12 - PYCC_test012 (Failed)
	 13 - PYCC_test013 (Failed)
	 14 - PYCC_test014 (Failed)
	 15 - PYCC_test015 (Failed)
	 16 - PYCC_test016 (Failed)
	 17 - PYCC_test017 (Failed)
	 18 - PYCC_test018 (Failed)
	 19 - PYCC_test019 (Failed)
	 20 - PYCC_test020 (Failed)
	 21 - PYCC_test021 (Failed)
	 22 - PYCC_test022 (Failed)
	 23 - PYCC_test023 (Failed)
	 24 - PYCC_test024 (Failed)
	 25 - PYCC_test025 (Failed)
Errors while running CTest
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ envPyCC.bat
envPyCC.bat: command not found
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ . envPyCC
bash: envPyCC: No such file or directory
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ python3 test001.py
Traceback (most recent call last):
  File "/home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test/test001.py", line 24, in <module>
    from gendata import getSampleCloud, dataDir, isCoordEqual
  File "/home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test/gendata.py", line 3, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ python3 test002.py
Traceback (most recent call last):
  File "/home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test/test002.py", line 24, in <module>
    from gendata import getSampleCloud, dataDir
  File "/home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test/gendata.py", line 3, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ pip3 install numpy
Collecting numpy
  Downloading numpy-1.21.4-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (15.7 MB)
     |████████████████████████████████| 15.7 MB 13.8 MB/s 
Installing collected packages: numpy
Successfully installed numpy-1.21.4
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ python3 test002.py
Traceback (most recent call last):
  File "/home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test/test002.py", line 24, in <module>
    from gendata import getSampleCloud, dataDir
  File "/home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test/gendata.py", line 6, in <module>
    import cloudComPy as cc
ModuleNotFoundError: No module named 'cloudComPy'
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ python3 test001.py
Traceback (most recent call last):
  File "/home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test/test001.py", line 24, in <module>
    from gendata import getSampleCloud, dataDir, isCoordEqual
  File "/home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test/gendata.py", line 6, in <module>
    import cloudComPy as cc
ModuleNotFoundError: No module named 'cloudComPy'
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ pip3 install cloudComPy
ERROR: Could not find a version that satisfies the requirement cloudComPy (from versions: none)
ERROR: No matching distribution found for cloudComPy
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ sudo apt-get intall qtbase5-dev python3 libpython3-dev python3-numpy cmake
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ ctest
Test project /home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test
      Start  1: PYCC_test001
 1/25 Test  #1: PYCC_test001 .....................***Failed    0.21 sec
      Start  2: PYCC_test002
 2/25 Test  #2: PYCC_test002 .....................***Failed    0.17 sec
      Start  3: PYCC_test003
 3/25 Test  #3: PYCC_test003 .....................***Failed    0.17 sec
      Start  4: PYCC_test004
 4/25 Test  #4: PYCC_test004 .....................***Failed    0.17 sec
      Start  5: PYCC_test005
 5/25 Test  #5: PYCC_test005 .....................***Failed    0.02 sec
      Start  6: PYCC_test006
 6/25 Test  #6: PYCC_test006 .....................***Failed    0.17 sec
      Start  7: PYCC_test007
 7/25 Test  #7: PYCC_test007 .....................***Failed    0.18 sec
      Start  8: PYCC_test008
 8/25 Test  #8: PYCC_test008 .....................***Failed    0.20 sec
      Start  9: PYCC_test009
 9/25 Test  #9: PYCC_test009 .....................***Failed    0.19 sec
      Start 10: PYCC_test010
10/25 Test #10: PYCC_test010 .....................***Failed    0.18 sec
      Start 11: PYCC_test011
11/25 Test #11: PYCC_test011 .....................***Failed    0.18 sec
      Start 12: PYCC_test012
12/25 Test #12: PYCC_test012 .....................***Failed    0.19 sec
      Start 13: PYCC_test013
13/25 Test #13: PYCC_test013 .....................***Failed    0.18 sec
      Start 14: PYCC_test014
14/25 Test #14: PYCC_test014 .....................***Failed    0.20 sec
      Start 15: PYCC_test015
15/25 Test #15: PYCC_test015 .....................***Failed    0.20 sec
      Start 16: PYCC_test016
16/25 Test #16: PYCC_test016 .....................***Failed    0.16 sec
      Start 17: PYCC_test017
17/25 Test #17: PYCC_test017 .....................***Failed    0.19 sec
      Start 18: PYCC_test018
18/25 Test #18: PYCC_test018 .....................***Failed    0.18 sec
      Start 19: PYCC_test019
19/25 Test #19: PYCC_test019 .....................***Failed    0.17 sec
      Start 20: PYCC_test020
20/25 Test #20: PYCC_test020 .....................***Failed    0.17 sec
      Start 21: PYCC_test021
21/25 Test #21: PYCC_test021 .....................***Failed    0.17 sec
      Start 22: PYCC_test022
22/25 Test #22: PYCC_test022 .....................***Failed    0.17 sec
      Start 23: PYCC_test023
23/25 Test #23: PYCC_test023 .....................***Failed    0.19 sec
      Start 24: PYCC_test024
24/25 Test #24: PYCC_test024 .....................***Failed    0.18 sec
      Start 25: PYCC_test025
25/25 Test #25: PYCC_test025 .....................***Failed    0.18 sec

0% tests passed, 25 tests failed out of 25

Total Test time (real) =   4.36 sec

The following tests FAILED:
	  1 - PYCC_test001 (Failed)
	  2 - PYCC_test002 (Failed)
	  3 - PYCC_test003 (Failed)
	  4 - PYCC_test004 (Failed)
	  5 - PYCC_test005 (Failed)
	  6 - PYCC_test006 (Failed)
	  7 - PYCC_test007 (Failed)
	  8 - PYCC_test008 (Failed)
	  9 - PYCC_test009 (Failed)
	 10 - PYCC_test010 (Failed)
	 11 - PYCC_test011 (Failed)
	 12 - PYCC_test012 (Failed)
	 13 - PYCC_test013 (Failed)
	 14 - PYCC_test014 (Failed)
	 15 - PYCC_test015 (Failed)
	 16 - PYCC_test016 (Failed)
	 17 - PYCC_test017 (Failed)
	 18 - PYCC_test018 (Failed)
	 19 - PYCC_test019 (Failed)
	 20 - PYCC_test020 (Failed)
	 21 - PYCC_test021 (Failed)
	 22 - PYCC_test022 (Failed)
	 23 - PYCC_test023 (Failed)
	 24 - PYCC_test024 (Failed)
	 25 - PYCC_test025 (Failed)
Errors while running CTest
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ ctest
Test project /home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test
      Start  1: PYCC_test001
 1/25 Test  #1: PYCC_test001 .....................***Failed    0.20 sec
      Start  2: PYCC_test002
 2/25 Test  #2: PYCC_test002 .....................***Failed    0.18 sec
      Start  3: PYCC_test003
 3/25 Test  #3: PYCC_test003 .....................***Failed    0.16 sec
      Start  4: PYCC_test004
 4/25 Test  #4: PYCC_test004 .....................***Failed    0.19 sec
      Start  5: PYCC_test005
 5/25 Test  #5: PYCC_test005 .....................***Failed    0.02 sec
      Start  6: PYCC_test006
 6/25 Test  #6: PYCC_test006 .....................***Failed    0.18 sec
      Start  7: PYCC_test007
 7/25 Test  #7: PYCC_test007 .....................***Failed    0.18 sec
      Start  8: PYCC_test008
 8/25 Test  #8: PYCC_test008 .....................***Failed    0.16 sec
      Start  9: PYCC_test009
 9/25 Test  #9: PYCC_test009 .....................***Failed    0.19 sec
      Start 10: PYCC_test010
10/25 Test #10: PYCC_test010 .....................***Failed    0.17 sec
      Start 11: PYCC_test011
11/25 Test #11: PYCC_test011 .....................***Failed    0.18 sec
      Start 12: PYCC_test012
12/25 Test #12: PYCC_test012 .....................***Failed    0.16 sec
      Start 13: PYCC_test013
13/25 Test #13: PYCC_test013 .....................***Failed    0.18 sec
      Start 14: PYCC_test014
14/25 Test #14: PYCC_test014 .....................***Failed    0.17 sec
      Start 15: PYCC_test015
15/25 Test #15: PYCC_test015 .....................***Failed    0.19 sec
      Start 16: PYCC_test016
16/25 Test #16: PYCC_test016 .....................***Failed    0.18 sec
      Start 17: PYCC_test017
17/25 Test #17: PYCC_test017 .....................***Failed    0.18 sec
      Start 18: PYCC_test018
18/25 Test #18: PYCC_test018 .....................***Failed    0.17 sec
      Start 19: PYCC_test019
19/25 Test #19: PYCC_test019 .....................***Failed    0.19 sec
      Start 20: PYCC_test020
20/25 Test #20: PYCC_test020 .....................***Failed    0.18 sec
      Start 21: PYCC_test021
21/25 Test #21: PYCC_test021 .....................***Failed    0.17 sec
      Start 22: PYCC_test022
22/25 Test #22: PYCC_test022 .....................***Failed    0.16 sec
      Start 23: PYCC_test023
23/25 Test #23: PYCC_test023 .....................***Failed    0.16 sec
      Start 24: PYCC_test024
24/25 Test #24: PYCC_test024 .....................***Failed    0.18 sec
      Start 25: PYCC_test025
25/25 Test #25: PYCC_test025 .....................***Failed    0.18 sec

0% tests passed, 25 tests failed out of 25

Total Test time (real) =   4.27 sec

The following tests FAILED:
	  1 - PYCC_test001 (Failed)
	  2 - PYCC_test002 (Failed)
	  3 - PYCC_test003 (Failed)
	  4 - PYCC_test004 (Failed)
	  5 - PYCC_test005 (Failed)
	  6 - PYCC_test006 (Failed)
	  7 - PYCC_test007 (Failed)
	  8 - PYCC_test008 (Failed)
	  9 - PYCC_test009 (Failed)
	 10 - PYCC_test010 (Failed)
	 11 - PYCC_test011 (Failed)
	 12 - PYCC_test012 (Failed)
	 13 - PYCC_test013 (Failed)
	 14 - PYCC_test014 (Failed)
	 15 - PYCC_test015 (Failed)
	 16 - PYCC_test016 (Failed)
	 17 - PYCC_test017 (Failed)
	 18 - PYCC_test018 (Failed)
	 19 - PYCC_test019 (Failed)
	 20 - PYCC_test020 (Failed)
	 21 - PYCC_test021 (Failed)
	 22 - PYCC_test022 (Failed)
	 23 - PYCC_test023 (Failed)
	 24 - PYCC_test024 (Failed)
	 25 - PYCC_test025 (Failed)
Errors while running CTest
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ ctest
Test project /home/imetnyk/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test
      Start  1: PYCC_test001
 1/25 Test  #1: PYCC_test001 .....................***Failed    0.17 sec
      Start  2: PYCC_test002
 2/25 Test  #2: PYCC_test002 .....................***Failed    0.20 sec
      Start  3: PYCC_test003
 3/25 Test  #3: PYCC_test003 .....................***Failed    0.17 sec
      Start  4: PYCC_test004
 4/25 Test  #4: PYCC_test004 .....................***Failed    0.18 sec
      Start  5: PYCC_test005
 5/25 Test  #5: PYCC_test005 .....................***Failed    0.02 sec
      Start  6: PYCC_test006
 6/25 Test  #6: PYCC_test006 .....................***Failed    0.18 sec
      Start  7: PYCC_test007
 7/25 Test  #7: PYCC_test007 .....................***Failed    0.17 sec
      Start  8: PYCC_test008
 8/25 Test  #8: PYCC_test008 .....................***Failed    0.19 sec
      Start  9: PYCC_test009
 9/25 Test  #9: PYCC_test009 .....................***Failed    0.18 sec
      Start 10: PYCC_test010
10/25 Test #10: PYCC_test010 .....................***Failed    0.18 sec
      Start 11: PYCC_test011
11/25 Test #11: PYCC_test011 .....................***Failed    0.19 sec
      Start 12: PYCC_test012
12/25 Test #12: PYCC_test012 .....................***Failed    0.18 sec
      Start 13: PYCC_test013
13/25 Test #13: PYCC_test013 .....................***Failed    0.18 sec
      Start 14: PYCC_test014
14/25 Test #14: PYCC_test014 .....................***Failed    0.18 sec
      Start 15: PYCC_test015
15/25 Test #15: PYCC_test015 .....................***Failed    0.16 sec
      Start 16: PYCC_test016
16/25 Test #16: PYCC_test016 .....................***Failed    0.18 sec
      Start 17: PYCC_test017
17/25 Test #17: PYCC_test017 .....................***Failed    0.18 sec
      Start 18: PYCC_test018
18/25 Test #18: PYCC_test018 .....................***Failed    0.17 sec
      Start 19: PYCC_test019
19/25 Test #19: PYCC_test019 .....................***Failed    0.16 sec
      Start 20: PYCC_test020
20/25 Test #20: PYCC_test020 .....................***Failed    0.17 sec
      Start 21: PYCC_test021
21/25 Test #21: PYCC_test021 .....................***Failed    0.18 sec
      Start 22: PYCC_test022
22/25 Test #22: PYCC_test022 .....................***Failed    0.16 sec
      Start 23: PYCC_test023
23/25 Test #23: PYCC_test023 .....................***Failed    0.17 sec
      Start 24: PYCC_test024
24/25 Test #24: PYCC_test024 .....................***Failed    0.19 sec
      Start 25: PYCC_test025
25/25 Test #25: PYCC_test025 .....................***Failed    0.20 sec

0% tests passed, 25 tests failed out of 25

Total Test time (real) =   4.30 sec

The following tests FAILED:
	  1 - PYCC_test001 (Failed)
	  2 - PYCC_test002 (Failed)
	  3 - PYCC_test003 (Failed)
	  4 - PYCC_test004 (Failed)
	  5 - PYCC_test005 (Failed)
	  6 - PYCC_test006 (Failed)
	  7 - PYCC_test007 (Failed)
	  8 - PYCC_test008 (Failed)
	  9 - PYCC_test009 (Failed)
	 10 - PYCC_test010 (Failed)
	 11 - PYCC_test011 (Failed)
	 12 - PYCC_test012 (Failed)
	 13 - PYCC_test013 (Failed)
	 14 - PYCC_test014 (Failed)
	 15 - PYCC_test015 (Failed)
	 16 - PYCC_test016 (Failed)
	 17 - PYCC_test017 (Failed)
	 18 - PYCC_test018 (Failed)
	 19 - PYCC_test019 (Failed)
	 20 - PYCC_test020 (Failed)
	 21 - PYCC_test021 (Failed)
	 22 - PYCC_test022 (Failed)
	 23 - PYCC_test023 (Failed)
	 24 - PYCC_test024 (Failed)
	 25 - PYCC_test025 (Failed)
Errors while running CTest
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ conda config --add channels conda-forge
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ conda config --set channel_priority strict
(CloudComPy39) imetnyk@imetnyk-System-Product-Name:~/Downloads/CloudComPy_Conda39_Linux64_20211018/installConda39/doc/PythonAPI_test$ conda install qt numpy psutil boost xerces-c pcl gdal cgal cmake pdal opencv ffmpeg mysql "qhull=2019.1" matplotlib "eigen=3.3.9"
Collecting package metadata (current_repodata.json): done
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
Collecting package metadata (repodata.json): done
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.9.2
  latest version: 4.10.3

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: /home/imetnyk/anaconda3/envs/CloudComPy39

  added / updated specs:
    - boost
    - cgal
    - cmake
    - eigen=3.3.9
    - ffmpeg
    - gdal
    - matplotlib
    - mysql
    - numpy
    - opencv
    - pcl
    - pdal
    - psutil
    - qhull=2019.1
    - qt
    - xerces-c


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    _libgcc_mutex-0.1          |      conda_forge           3 KB  conda-forge
    _openmp_mutex-4.5          |            1_gnu          22 KB  conda-forge
    alsa-lib-1.2.3             |       h516909a_0         560 KB  conda-forge
    aom-3.2.0                  |       h9c3ff4c_2         5.4 MB  conda-forge
    boost-1.72.0               |   py39ha90915f_1         342 KB  conda-forge
    boost-cpp-1.72.0           |       h312852a_5        16.3 MB  conda-forge
    brotli-1.0.9               |       h7f98852_6          18 KB  conda-forge
    brotli-bin-1.0.9           |       h7f98852_6          19 KB  conda-forge
    bzip2-1.0.8                |       h7f98852_4         484 KB  conda-forge
    c-ares-1.18.1              |       h7f98852_0         113 KB  conda-forge
    ca-certificates-2021.10.8  |       ha878542_0         139 KB  conda-forge
    cairo-1.16.0               |    h6cf1ce9_1008         1.5 MB  conda-forge
    certifi-2021.10.8          |   py39hf3d152e_1         145 KB  conda-forge
    cfitsio-3.470              |       hb418390_7         1.3 MB  conda-forge
    cgal-5.0.1                 |   py39hde0f152_3         8.2 MB  conda-forge
    cgal-cpp-5.0.1             |       h747953b_1         5.7 MB  conda-forge
    cmake-3.21.3               |       h8897547_0        15.2 MB  conda-forge
    curl-7.80.0                |       h2574ce0_0         153 KB  conda-forge
    cycler-0.11.0              |     pyhd8ed1ab_0          10 KB  conda-forge
    cyrus-sasl-2.1.27          |       h230043b_4         228 KB  conda-forge
    dbus-1.13.6                |       h48d8840_2         572 KB  conda-forge
    draco-1.4.3                |       h4bd325d_1         1.3 MB  conda-forge
    eigen-3.3.9                |       h4bd325d_1         970 KB  conda-forge
    expat-2.4.1                |       h9c3ff4c_0         182 KB  conda-forge
    ffmpeg-4.4.1               |       h6987444_0        10.0 MB  conda-forge
    flann-1.9.1                |    hfe772e8_1009        39.9 MB  conda-forge
    fontconfig-2.13.1          |    hba837de_1005         357 KB  conda-forge
    fonttools-4.28.1           |   py39h3811e60_0         1.5 MB  conda-forge
    freeglut-3.2.1             |       h9c3ff4c_2         161 KB  conda-forge
    freetype-2.10.4            |       h0708190_1         890 KB  conda-forge
    freexl-1.0.6               |       h7f98852_0          48 KB  conda-forge
    gdal-3.3.2                 |   py39h85a7741_0         1.8 MB  conda-forge
    geos-3.9.1                 |       h9c3ff4c_2         1.1 MB  conda-forge
    geotiff-1.6.0              |       h4f31c25_6         299 KB  conda-forge
    gettext-0.19.8.1           |    h0b5b191_1005         3.6 MB  conda-forge
    giflib-5.2.1               |       h36c2ea0_2          77 KB  conda-forge
    glib-2.68.4                |       h9c3ff4c_0         447 KB  conda-forge
    glib-tools-2.68.4          |       h9c3ff4c_0          86 KB  conda-forge
    gmp-6.2.1                  |       h58526e2_0         806 KB  conda-forge
    gnutls-3.6.13              |       h85f3911_1         2.0 MB  conda-forge
    graphite2-1.3.13           |    h58526e2_1001         102 KB  conda-forge
    gst-plugins-base-1.18.5    |       hf529b03_0         2.6 MB  conda-forge
    gstreamer-1.18.5           |       h76c114f_0         2.0 MB  conda-forge
    harfbuzz-3.0.0             |       h83ec7ef_1         2.0 MB  conda-forge
    hdf4-4.2.15                |       h10796ff_3         950 KB  conda-forge
    hdf5-1.12.1                |nompi_h2750804_101         3.5 MB  conda-forge
    icu-68.2                   |       h9c3ff4c_0        13.1 MB  conda-forge
    jasper-2.0.33              |       ha77e612_0         1.1 MB  conda-forge
    jbig-2.1                   |    h7f98852_2003          43 KB  conda-forge
    jpeg-9d                    |       h36c2ea0_0         264 KB  conda-forge
    json-c-0.15                |       h98cffda_0         274 KB  conda-forge
    jsoncpp-1.9.4              |       h4bd325d_3         262 KB  conda-forge
    kealib-1.4.14              |       h87e4c3c_3         186 KB  conda-forge
    kiwisolver-1.3.2           |   py39h1a9c180_1          80 KB  conda-forge
    krb5-1.19.2                |       hcc1bbae_3         1.4 MB  conda-forge
    lame-3.100                 |    h7f98852_1001         496 KB  conda-forge
    laszip-3.4.3               |       h9c3ff4c_2         185 KB  conda-forge
    laz-perf-3.0.0             |       h4bd325d_0         182 KB  conda-forge
    lcms2-2.12                 |       hddcbb42_0         443 KB  conda-forge
    ld_impl_linux-64-2.36.1    |       hea4e1c9_2         667 KB  conda-forge
    lerc-3.0                   |       h9c3ff4c_0         216 KB  conda-forge
    libblas-3.9.0              |12_linux64_openblas          12 KB  conda-forge
    libbrotlicommon-1.0.9      |       h7f98852_6          65 KB  conda-forge
    libbrotlidec-1.0.9         |       h7f98852_6          33 KB  conda-forge
    libbrotlienc-1.0.9         |       h7f98852_6         286 KB  conda-forge
    libcblas-3.9.0             |12_linux64_openblas          12 KB  conda-forge
    libclang-11.1.0            |default_ha53f305_1        19.2 MB  conda-forge
    libcurl-7.80.0             |       h2574ce0_0         337 KB  conda-forge
    libdap4-3.20.6             |       hd7c4107_2        11.3 MB  conda-forge
    libdeflate-1.8             |       h7f98852_0          67 KB  conda-forge
    libdrm-2.4.108             |       h7f98852_0         284 KB  conda-forge
    libedit-3.1.20191231       |       he28a2e2_2         121 KB  conda-forge
    libev-4.33                 |       h516909a_1         104 KB  conda-forge
    libevent-2.1.10            |       h9b69904_4         1.1 MB  conda-forge
    libffi-3.3                 |       h58526e2_2          51 KB  conda-forge
    libgcc-ng-11.2.0           |      h1d223b6_11         887 KB  conda-forge
    libgdal-3.3.2              |       h6214c1d_0        13.3 MB  conda-forge
    libgfortran-ng-11.2.0      |      h69a702a_11          19 KB  conda-forge
    libgfortran5-11.2.0        |      h5c6108e_11         1.7 MB  conda-forge
    libglib-2.68.4             |       h3e27bee_0         3.0 MB  conda-forge
    libglu-9.0.0               |    he1b5a44_1001         413 KB  conda-forge
    libgomp-11.2.0             |      h1d223b6_11         427 KB  conda-forge
    libiconv-1.16              |       h516909a_0         1.4 MB  conda-forge
    libkml-1.3.0               |    hd79254b_1012         640 KB  conda-forge
    liblapack-3.9.0            |12_linux64_openblas          12 KB  conda-forge
    liblapacke-3.9.0           |12_linux64_openblas          12 KB  conda-forge
    libllvm11-11.1.0           |       hf817b99_2        29.1 MB  conda-forge
    libnetcdf-4.8.1            |nompi_hb3fd0d9_101         1.5 MB  conda-forge
    libnghttp2-1.43.0          |       h812cca2_1         790 KB  conda-forge
    libnsl-2.0.0               |       h7f98852_0          31 KB  conda-forge
    libntlm-1.4                |    h7f98852_1002          32 KB  conda-forge
    libogg-1.3.4               |       h7f98852_1         206 KB  conda-forge
    libopenblas-0.3.18         |pthreads_h8fe5266_0         9.6 MB  conda-forge
    libopencv-4.5.3            |   py39ha7f30a5_5        34.5 MB  conda-forge
    libopus-1.3.1              |       h7f98852_1         255 KB  conda-forge
    libpciaccess-0.16          |       h516909a_0          37 KB  conda-forge
    libpng-1.6.37              |       h21135ba_2         306 KB  conda-forge
    libpq-13.3                 |       hd57d9b9_3         2.7 MB  conda-forge
    libprotobuf-3.18.1         |       h780b84a_0         2.6 MB  conda-forge
    librttopo-1.1.0            |       h1185371_6         235 KB  conda-forge
    libspatialite-5.0.1        |       h8694cbe_6         4.4 MB  conda-forge
    libssh2-1.10.0             |       ha56f1ee_2         233 KB  conda-forge
    libstdcxx-ng-11.2.0        |      he4da1e4_11         4.2 MB  conda-forge
    libtiff-4.3.0              |       h6f004c6_2         614 KB  conda-forge
    libuuid-2.32.1             |    h7f98852_1000          28 KB  conda-forge
    libuv-1.42.0               |       h7f98852_0         1.0 MB  conda-forge
    libva-2.13.0               |       h7f98852_0         165 KB  conda-forge
    libvorbis-1.3.7            |       h9c3ff4c_0         280 KB  conda-forge
    libvpx-1.11.0              |       h9c3ff4c_3         1.1 MB  conda-forge
    libwebp-base-1.2.1         |       h7f98852_0         845 KB  conda-forge
    libxcb-1.13                |    h7f98852_1004         391 KB  conda-forge
    libxkbcommon-1.0.3         |       he3ba5ed_0         581 KB  conda-forge
    libxml2-2.9.12             |       h72842e0_0         772 KB  conda-forge
    libzip-1.8.0               |       h4de3113_1         126 KB  conda-forge
    libzlib-1.2.11             |    h36c2ea0_1013          59 KB  conda-forge
    lz4-c-1.9.3                |       h9c3ff4c_1         179 KB  conda-forge
    matplotlib-3.5.0           |   py39hf3d152e_0           6 KB  conda-forge
    matplotlib-base-3.5.0      |   py39h2fa2bec_0         7.4 MB  conda-forge
    mesalib-18.3.1             |       h590aaf7_0        11.4 MB  conda-forge
    mpfr-4.1.0                 |       h9202a9a_1         2.6 MB  conda-forge
    munkres-1.1.4              |     pyh9f0ad1d_0          12 KB  conda-forge
    mysql-8.0.27               |       ha770c72_0         387 KB  conda-forge
    mysql-client-8.0.27        |       hf09c6a7_0        27.5 MB  conda-forge
    mysql-common-8.0.27        |       ha770c72_0         1.8 MB  conda-forge
    mysql-devel-8.0.27         |       ha770c72_0         2.3 MB  conda-forge
    mysql-libs-8.0.27          |       hfa10184_0         1.9 MB  conda-forge
    mysql-server-8.0.27        |       h1069331_0        19.6 MB  conda-forge
    ncurses-6.2                |       h58526e2_4         985 KB  conda-forge
    nettle-3.6                 |       he412f7d_0         6.5 MB  conda-forge
    nitro-2.7.dev6             |       h9c3ff4c_4         967 KB  conda-forge
    nspr-4.32                  |       h9c3ff4c_1         233 KB  conda-forge
    nss-3.72                   |       hb5efdd6_0         2.1 MB  conda-forge
    numpy-1.21.4               |   py39hdbf815f_0         6.2 MB  conda-forge
    olefile-0.46               |     pyh9f0ad1d_1          32 KB  conda-forge
    opencv-4.5.3               |   py39hf3d152e_5          22 KB  conda-forge
    openh264-2.1.1             |       h780b84a_0         1.5 MB  conda-forge
    openjpeg-2.4.0             |       hb52868f_1         444 KB  conda-forge
    openssl-1.1.1l             |       h7f98852_0         2.1 MB  conda-forge
    packaging-21.3             |     pyhd8ed1ab_0          36 KB  conda-forge
    pcl-1.11.1                 |       h05311af_1        20.3 MB  conda-forge
    pcre-8.45                  |       h9c3ff4c_0         253 KB  conda-forge
    pdal-2.3.0                 |       h006714b_7         5.2 MB  conda-forge
    pillow-8.4.0               |   py39ha612740_0         706 KB  conda-forge
    pip-21.3.1                 |     pyhd8ed1ab_0         1.2 MB  conda-forge
    pixman-0.40.0              |       h36c2ea0_0         627 KB  conda-forge
    pkg-config-0.29.2          |    h36c2ea0_1008         120 KB  conda-forge
    pkgconfig-1.5.5            |   py39hf3d152e_1          13 KB  conda-forge
    poppler-21.03.0            |       h93df280_0        15.9 MB  conda-forge
    poppler-data-0.4.11        |       hd8ed1ab_0         3.6 MB  conda-forge
    postgresql-13.3            |       h2510834_3         5.3 MB  conda-forge
    proj-8.0.1                 |       h277dcde_0         3.1 MB  conda-forge
    psutil-5.8.0               |   py39h3811e60_2         343 KB  conda-forge
    pthread-stubs-0.4          |    h36c2ea0_1001           5 KB  conda-forge
    py-opencv-4.5.3            |   py39hef51801_5         1.1 MB  conda-forge
    pyparsing-3.0.6            |     pyhd8ed1ab_0          79 KB  conda-forge
    pyqt-5.12.3                |   py39hf3d152e_8          22 KB  conda-forge
    pyqt-impl-5.12.3           |   py39hde8b62d_8         5.9 MB  conda-forge
    pyqt5-sip-4.19.18          |   py39he80948d_8         311 KB  conda-forge
    pyqtchart-5.12             |   py39h0fcd23e_8         257 KB  conda-forge
    pyqtwebengine-5.12.1       |   py39h0fcd23e_8         174 KB  conda-forge
    python-3.9.7               |h49503c6_0_cpython        27.6 MB  conda-forge
    python-dateutil-2.8.2      |     pyhd8ed1ab_0         240 KB  conda-forge
    python_abi-3.9             |           2_cp39           4 KB  conda-forge
    qhull-2019.1               |       hc9558a2_0         2.3 MB  conda-forge
    qt-5.12.9                  |       hda022c4_4        99.5 MB  conda-forge
    readline-8.1               |       h46c0cb4_0         295 KB  conda-forge
    rhash-1.4.1                |       h7f98852_0         192 KB  conda-forge
    setuptools-59.1.1          |   py39hf3d152e_0         1.0 MB  conda-forge
    six-1.16.0                 |     pyh6c4a22f_0          14 KB  conda-forge
    sqlite-3.36.0              |       h9cd32fc_2         1.4 MB  conda-forge
    svt-av1-0.8.7              |       h9c3ff4c_1         2.8 MB  conda-forge
    tiledb-2.3.4               |       he87e0bf_0         4.1 MB  conda-forge
    tk-8.6.11                  |       h27826a3_1         3.3 MB  conda-forge
    tornado-6.1                |   py39h3811e60_2         646 KB  conda-forge
    tzcode-2021e               |       h7f98852_0          69 KB  conda-forge
    tzdata-2021e               |       he74cb21_0         121 KB  conda-forge
    wheel-0.37.0               |     pyhd8ed1ab_1          31 KB  conda-forge
    x264-1!161.3030            |       h7f98852_1         2.5 MB  conda-forge
    x265-3.5                   |       h4bd325d_1         6.7 MB  conda-forge
    xerces-c-3.2.3             |       h9d8b166_3         1.8 MB  conda-forge
    xorg-fixesproto-5.0        |    h7f98852_1002           9 KB  conda-forge
    xorg-inputproto-2.3.2      |    h7f98852_1002          19 KB  conda-forge
    xorg-kbproto-1.0.7         |    h7f98852_1002          27 KB  conda-forge
    xorg-libice-1.0.10         |       h7f98852_0          58 KB  conda-forge
    xorg-libsm-1.2.3           |    hd9c2040_1000          26 KB  conda-forge
    xorg-libx11-1.7.2          |       h7f98852_0         941 KB  conda-forge
    xorg-libxau-1.0.9          |       h7f98852_0          13 KB  conda-forge
    xorg-libxdmcp-1.1.3        |       h7f98852_0          19 KB  conda-forge
    xorg-libxext-1.3.4         |       h7f98852_1          54 KB  conda-forge
    xorg-libxfixes-5.0.3       |    h7f98852_1004          18 KB  conda-forge
    xorg-libxi-1.7.10          |       h7f98852_0          46 KB  conda-forge
    xorg-libxrender-0.9.10     |    h7f98852_1003          32 KB  conda-forge
    xorg-renderproto-0.11.1    |    h7f98852_1002           9 KB  conda-forge
    xorg-xextproto-7.3.0       |    h7f98852_1002          28 KB  conda-forge
    xorg-xproto-7.0.31         |    h7f98852_1007          73 KB  conda-forge
    xz-5.2.5                   |       h516909a_1         343 KB  conda-forge
    zlib-1.2.11                |    h36c2ea0_1013          86 KB  conda-forge
    zstd-1.5.0                 |       ha95c52a_0         490 KB  conda-forge
    ------------------------------------------------------------
                                           Total:       620.6 MB

The following NEW packages will be INSTALLED:

  alsa-lib           conda-forge/linux-64::alsa-lib-1.2.3-h516909a_0
  aom                conda-forge/linux-64::aom-3.2.0-h9c3ff4c_2
  boost              conda-forge/linux-64::boost-1.72.0-py39ha90915f_1
  boost-cpp          conda-forge/linux-64::boost-cpp-1.72.0-h312852a_5
  brotli             conda-forge/linux-64::brotli-1.0.9-h7f98852_6
  brotli-bin         conda-forge/linux-64::brotli-bin-1.0.9-h7f98852_6
  bzip2              conda-forge/linux-64::bzip2-1.0.8-h7f98852_4
  c-ares             conda-forge/linux-64::c-ares-1.18.1-h7f98852_0
  cairo              conda-forge/linux-64::cairo-1.16.0-h6cf1ce9_1008
  cfitsio            conda-forge/linux-64::cfitsio-3.470-hb418390_7
  cgal               conda-forge/linux-64::cgal-5.0.1-py39hde0f152_3
  cgal-cpp           conda-forge/linux-64::cgal-cpp-5.0.1-h747953b_1
  cmake              conda-forge/linux-64::cmake-3.21.3-h8897547_0
  curl               conda-forge/linux-64::curl-7.80.0-h2574ce0_0
  cycler             conda-forge/noarch::cycler-0.11.0-pyhd8ed1ab_0
  cyrus-sasl         conda-forge/linux-64::cyrus-sasl-2.1.27-h230043b_4
  dbus               conda-forge/linux-64::dbus-1.13.6-h48d8840_2
  draco              conda-forge/linux-64::draco-1.4.3-h4bd325d_1
  eigen              conda-forge/linux-64::eigen-3.3.9-h4bd325d_1
  expat              conda-forge/linux-64::expat-2.4.1-h9c3ff4c_0
  ffmpeg             conda-forge/linux-64::ffmpeg-4.4.1-h6987444_0
  flann              conda-forge/linux-64::flann-1.9.1-hfe772e8_1009
  fontconfig         conda-forge/linux-64::fontconfig-2.13.1-hba837de_1005
  fonttools          conda-forge/linux-64::fonttools-4.28.1-py39h3811e60_0
  freeglut           conda-forge/linux-64::freeglut-3.2.1-h9c3ff4c_2
  freetype           conda-forge/linux-64::freetype-2.10.4-h0708190_1
  freexl             conda-forge/linux-64::freexl-1.0.6-h7f98852_0
  gdal               conda-forge/linux-64::gdal-3.3.2-py39h85a7741_0
  geos               conda-forge/linux-64::geos-3.9.1-h9c3ff4c_2
  geotiff            conda-forge/linux-64::geotiff-1.6.0-h4f31c25_6
  gettext            conda-forge/linux-64::gettext-0.19.8.1-h0b5b191_1005
  giflib             conda-forge/linux-64::giflib-5.2.1-h36c2ea0_2
  glib               conda-forge/linux-64::glib-2.68.4-h9c3ff4c_0
  glib-tools         conda-forge/linux-64::glib-tools-2.68.4-h9c3ff4c_0
  gmp                conda-forge/linux-64::gmp-6.2.1-h58526e2_0
  gnutls             conda-forge/linux-64::gnutls-3.6.13-h85f3911_1
  graphite2          conda-forge/linux-64::graphite2-1.3.13-h58526e2_1001
  gst-plugins-base   conda-forge/linux-64::gst-plugins-base-1.18.5-hf529b03_0
  gstreamer          conda-forge/linux-64::gstreamer-1.18.5-h76c114f_0
  harfbuzz           conda-forge/linux-64::harfbuzz-3.0.0-h83ec7ef_1
  hdf4               conda-forge/linux-64::hdf4-4.2.15-h10796ff_3
  hdf5               conda-forge/linux-64::hdf5-1.12.1-nompi_h2750804_101
  icu                conda-forge/linux-64::icu-68.2-h9c3ff4c_0
  jasper             conda-forge/linux-64::jasper-2.0.33-ha77e612_0
  jbig               conda-forge/linux-64::jbig-2.1-h7f98852_2003
  jpeg               conda-forge/linux-64::jpeg-9d-h36c2ea0_0
  json-c             conda-forge/linux-64::json-c-0.15-h98cffda_0
  jsoncpp            conda-forge/linux-64::jsoncpp-1.9.4-h4bd325d_3
  kealib             conda-forge/linux-64::kealib-1.4.14-h87e4c3c_3
  kiwisolver         conda-forge/linux-64::kiwisolver-1.3.2-py39h1a9c180_1
  krb5               conda-forge/linux-64::krb5-1.19.2-hcc1bbae_3
  lame               conda-forge/linux-64::lame-3.100-h7f98852_1001
  laszip             conda-forge/linux-64::laszip-3.4.3-h9c3ff4c_2
  laz-perf           conda-forge/linux-64::laz-perf-3.0.0-h4bd325d_0
  lcms2              conda-forge/linux-64::lcms2-2.12-hddcbb42_0
  lerc               conda-forge/linux-64::lerc-3.0-h9c3ff4c_0
  libblas            conda-forge/linux-64::libblas-3.9.0-12_linux64_openblas
  libbrotlicommon    conda-forge/linux-64::libbrotlicommon-1.0.9-h7f98852_6
  libbrotlidec       conda-forge/linux-64::libbrotlidec-1.0.9-h7f98852_6
  libbrotlienc       conda-forge/linux-64::libbrotlienc-1.0.9-h7f98852_6
  libcblas           conda-forge/linux-64::libcblas-3.9.0-12_linux64_openblas
  libclang           conda-forge/linux-64::libclang-11.1.0-default_ha53f305_1
  libcurl            conda-forge/linux-64::libcurl-7.80.0-h2574ce0_0
  libdap4            conda-forge/linux-64::libdap4-3.20.6-hd7c4107_2
  libdeflate         conda-forge/linux-64::libdeflate-1.8-h7f98852_0
  libdrm             conda-forge/linux-64::libdrm-2.4.108-h7f98852_0
  libedit            conda-forge/linux-64::libedit-3.1.20191231-he28a2e2_2
  libev              conda-forge/linux-64::libev-4.33-h516909a_1
  libevent           conda-forge/linux-64::libevent-2.1.10-h9b69904_4
  libgdal            conda-forge/linux-64::libgdal-3.3.2-h6214c1d_0
  libgfortran-ng     conda-forge/linux-64::libgfortran-ng-11.2.0-h69a702a_11
  libgfortran5       conda-forge/linux-64::libgfortran5-11.2.0-h5c6108e_11
  libglib            conda-forge/linux-64::libglib-2.68.4-h3e27bee_0
  libglu             conda-forge/linux-64::libglu-9.0.0-he1b5a44_1001
  libiconv           conda-forge/linux-64::libiconv-1.16-h516909a_0
  libkml             conda-forge/linux-64::libkml-1.3.0-hd79254b_1012
  liblapack          conda-forge/linux-64::liblapack-3.9.0-12_linux64_openblas
  liblapacke         conda-forge/linux-64::liblapacke-3.9.0-12_linux64_openblas
  libllvm11          conda-forge/linux-64::libllvm11-11.1.0-hf817b99_2
  libnetcdf          conda-forge/linux-64::libnetcdf-4.8.1-nompi_hb3fd0d9_101
  libnghttp2         conda-forge/linux-64::libnghttp2-1.43.0-h812cca2_1
  libnsl             conda-forge/linux-64::libnsl-2.0.0-h7f98852_0
  libntlm            conda-forge/linux-64::libntlm-1.4-h7f98852_1002
  libogg             conda-forge/linux-64::libogg-1.3.4-h7f98852_1
  libopenblas        conda-forge/linux-64::libopenblas-0.3.18-pthreads_h8fe5266_0
  libopencv          conda-forge/linux-64::libopencv-4.5.3-py39ha7f30a5_5
  libopus            conda-forge/linux-64::libopus-1.3.1-h7f98852_1
  libpciaccess       conda-forge/linux-64::libpciaccess-0.16-h516909a_0
  libpng             conda-forge/linux-64::libpng-1.6.37-h21135ba_2
  libpq              conda-forge/linux-64::libpq-13.3-hd57d9b9_3
  libprotobuf        conda-forge/linux-64::libprotobuf-3.18.1-h780b84a_0
  librttopo          conda-forge/linux-64::librttopo-1.1.0-h1185371_6
  libspatialite      conda-forge/linux-64::libspatialite-5.0.1-h8694cbe_6
  libssh2            conda-forge/linux-64::libssh2-1.10.0-ha56f1ee_2
  libtiff            conda-forge/linux-64::libtiff-4.3.0-h6f004c6_2
  libuuid            conda-forge/linux-64::libuuid-2.32.1-h7f98852_1000
  libuv              conda-forge/linux-64::libuv-1.42.0-h7f98852_0
  libva              conda-forge/linux-64::libva-2.13.0-h7f98852_0
  libvorbis          conda-forge/linux-64::libvorbis-1.3.7-h9c3ff4c_0
  libvpx             conda-forge/linux-64::libvpx-1.11.0-h9c3ff4c_3
  libwebp-base       conda-forge/linux-64::libwebp-base-1.2.1-h7f98852_0
  libxcb             conda-forge/linux-64::libxcb-1.13-h7f98852_1004
  libxkbcommon       conda-forge/linux-64::libxkbcommon-1.0.3-he3ba5ed_0
  libxml2            conda-forge/linux-64::libxml2-2.9.12-h72842e0_0
  libzip             conda-forge/linux-64::libzip-1.8.0-h4de3113_1
  libzlib            conda-forge/linux-64::libzlib-1.2.11-h36c2ea0_1013
  lz4-c              conda-forge/linux-64::lz4-c-1.9.3-h9c3ff4c_1
  matplotlib         conda-forge/linux-64::matplotlib-3.5.0-py39hf3d152e_0
  matplotlib-base    conda-forge/linux-64::matplotlib-base-3.5.0-py39h2fa2bec_0
  mesalib            conda-forge/linux-64::mesalib-18.3.1-h590aaf7_0
  mpfr               conda-forge/linux-64::mpfr-4.1.0-h9202a9a_1
  munkres            conda-forge/noarch::munkres-1.1.4-pyh9f0ad1d_0
  mysql              conda-forge/linux-64::mysql-8.0.27-ha770c72_0
  mysql-client       conda-forge/linux-64::mysql-client-8.0.27-hf09c6a7_0
  mysql-common       conda-forge/linux-64::mysql-common-8.0.27-ha770c72_0
  mysql-devel        conda-forge/linux-64::mysql-devel-8.0.27-ha770c72_0
  mysql-libs         conda-forge/linux-64::mysql-libs-8.0.27-hfa10184_0
  mysql-server       conda-forge/linux-64::mysql-server-8.0.27-h1069331_0
  nettle             conda-forge/linux-64::nettle-3.6-he412f7d_0
  nitro              conda-forge/linux-64::nitro-2.7.dev6-h9c3ff4c_4
  nspr               conda-forge/linux-64::nspr-4.32-h9c3ff4c_1
  nss                conda-forge/linux-64::nss-3.72-hb5efdd6_0
  numpy              conda-forge/linux-64::numpy-1.21.4-py39hdbf815f_0
  olefile            conda-forge/noarch::olefile-0.46-pyh9f0ad1d_1
  opencv             conda-forge/linux-64::opencv-4.5.3-py39hf3d152e_5
  openh264           conda-forge/linux-64::openh264-2.1.1-h780b84a_0
  openjpeg           conda-forge/linux-64::openjpeg-2.4.0-hb52868f_1
  packaging          conda-forge/noarch::packaging-21.3-pyhd8ed1ab_0
  pcl                conda-forge/linux-64::pcl-1.11.1-h05311af_1
  pcre               conda-forge/linux-64::pcre-8.45-h9c3ff4c_0
  pdal               conda-forge/linux-64::pdal-2.3.0-h006714b_7
  pillow             conda-forge/linux-64::pillow-8.4.0-py39ha612740_0
  pixman             conda-forge/linux-64::pixman-0.40.0-h36c2ea0_0
  pkg-config         conda-forge/linux-64::pkg-config-0.29.2-h36c2ea0_1008
  pkgconfig          conda-forge/linux-64::pkgconfig-1.5.5-py39hf3d152e_1
  poppler            conda-forge/linux-64::poppler-21.03.0-h93df280_0
  poppler-data       conda-forge/noarch::poppler-data-0.4.11-hd8ed1ab_0
  postgresql         conda-forge/linux-64::postgresql-13.3-h2510834_3
  proj               conda-forge/linux-64::proj-8.0.1-h277dcde_0
  psutil             conda-forge/linux-64::psutil-5.8.0-py39h3811e60_2
  pthread-stubs      conda-forge/linux-64::pthread-stubs-0.4-h36c2ea0_1001
  py-opencv          conda-forge/linux-64::py-opencv-4.5.3-py39hef51801_5
  pyparsing          conda-forge/noarch::pyparsing-3.0.6-pyhd8ed1ab_0
  pyqt               conda-forge/linux-64::pyqt-5.12.3-py39hf3d152e_8
  pyqt-impl          conda-forge/linux-64::pyqt-impl-5.12.3-py39hde8b62d_8
  pyqt5-sip          conda-forge/linux-64::pyqt5-sip-4.19.18-py39he80948d_8
  pyqtchart          conda-forge/linux-64::pyqtchart-5.12-py39h0fcd23e_8
  pyqtwebengine      conda-forge/linux-64::pyqtwebengine-5.12.1-py39h0fcd23e_8
  python-dateutil    conda-forge/noarch::python-dateutil-2.8.2-pyhd8ed1ab_0
  python_abi         conda-forge/linux-64::python_abi-3.9-2_cp39
  qhull              conda-forge/linux-64::qhull-2019.1-hc9558a2_0
  qt                 conda-forge/linux-64::qt-5.12.9-hda022c4_4
  rhash              conda-forge/linux-64::rhash-1.4.1-h7f98852_0
  six                conda-forge/noarch::six-1.16.0-pyh6c4a22f_0
  svt-av1            conda-forge/linux-64::svt-av1-0.8.7-h9c3ff4c_1
  tiledb             conda-forge/linux-64::tiledb-2.3.4-he87e0bf_0
  tornado            conda-forge/linux-64::tornado-6.1-py39h3811e60_2
  tzcode             conda-forge/linux-64::tzcode-2021e-h7f98852_0
  x264               conda-forge/linux-64::x264-1!161.3030-h7f98852_1
  x265               conda-forge/linux-64::x265-3.5-h4bd325d_1
  xerces-c           conda-forge/linux-64::xerces-c-3.2.3-h9d8b166_3
  xorg-fixesproto    conda-forge/linux-64::xorg-fixesproto-5.0-h7f98852_1002
  xorg-inputproto    conda-forge/linux-64::xorg-inputproto-2.3.2-h7f98852_1002
  xorg-kbproto       conda-forge/linux-64::xorg-kbproto-1.0.7-h7f98852_1002
  xorg-libice        conda-forge/linux-64::xorg-libice-1.0.10-h7f98852_0
  xorg-libsm         conda-forge/linux-64::xorg-libsm-1.2.3-hd9c2040_1000
  xorg-libx11        conda-forge/linux-64::xorg-libx11-1.7.2-h7f98852_0
  xorg-libxau        conda-forge/linux-64::xorg-libxau-1.0.9-h7f98852_0
  xorg-libxdmcp      conda-forge/linux-64::xorg-libxdmcp-1.1.3-h7f98852_0
  xorg-libxext       conda-forge/linux-64::xorg-libxext-1.3.4-h7f98852_1
  xorg-libxfixes     conda-forge/linux-64::xorg-libxfixes-5.0.3-h7f98852_1004
  xorg-libxi         conda-forge/linux-64::xorg-libxi-1.7.10-h7f98852_0
  xorg-libxrender    conda-forge/linux-64::xorg-libxrender-0.9.10-h7f98852_1003
  xorg-renderproto   conda-forge/linux-64::xorg-renderproto-0.11.1-h7f98852_1002
  xorg-xextproto     conda-forge/linux-64::xorg-xextproto-7.3.0-h7f98852_1002
  xorg-xproto        conda-forge/linux-64::xorg-xproto-7.0.31-h7f98852_1007
  zstd               conda-forge/linux-64::zstd-1.5.0-ha95c52a_0

The following packages will be UPDATED:

  certifi            pkgs/main::certifi-2021.10.8-py39h06a~ --> conda-forge::certifi-2021.10.8-py39hf3d152e_1
  ld_impl_linux-64   pkgs/main::ld_impl_linux-64-2.35.1-h7~ --> conda-forge::ld_impl_linux-64-2.36.1-hea4e1c9_2
  libgcc-ng          pkgs/main::libgcc-ng-9.3.0-h5101ec6_17 --> conda-forge::libgcc-ng-11.2.0-h1d223b6_11
  libgomp              pkgs/main::libgomp-9.3.0-h5101ec6_17 --> conda-forge::libgomp-11.2.0-h1d223b6_11
  libstdcxx-ng       pkgs/main::libstdcxx-ng-9.3.0-hd4cf53~ --> conda-forge::libstdcxx-ng-11.2.0-he4da1e4_11
  pip                pkgs/main/linux-64::pip-21.2.4-py39h0~ --> conda-forge/noarch::pip-21.3.1-pyhd8ed1ab_0
  setuptools         pkgs/main::setuptools-58.0.4-py39h06a~ --> conda-forge::setuptools-59.1.1-py39hf3d152e_0
  sqlite                pkgs/main::sqlite-3.36.0-hc218d9a_0 --> conda-forge::sqlite-3.36.0-h9cd32fc_2
  tk                        pkgs/main::tk-8.6.11-h1ccaba5_0 --> conda-forge::tk-8.6.11-h27826a3_1
  xz                         pkgs/main::xz-5.2.5-h7b6447c_0 --> conda-forge::xz-5.2.5-h516909a_1
  zlib                    pkgs/main::zlib-1.2.11-h7b6447c_3 --> conda-forge::zlib-1.2.11-h36c2ea0_1013

The following packages will be SUPERSEDED by a higher-priority channel:

  _libgcc_mutex           pkgs/main::_libgcc_mutex-0.1-main --> conda-forge::_libgcc_mutex-0.1-conda_forge
  _openmp_mutex                                   pkgs/main --> conda-forge
  ca-certificates    pkgs/main::ca-certificates-2021.10.26~ --> conda-forge::ca-certificates-2021.10.8-ha878542_0
  libffi                   pkgs/main::libffi-3.3-he6710b0_2 --> conda-forge::libffi-3.3-h58526e2_2
  ncurses                 pkgs/main::ncurses-6.3-h7f8727e_2 --> conda-forge::ncurses-6.2-h58526e2_4
  openssl              pkgs/main::openssl-1.1.1l-h7f8727e_0 --> conda-forge::openssl-1.1.1l-h7f98852_0
  python                 pkgs/main::python-3.9.7-h12debd9_1 --> conda-forge::python-3.9.7-h49503c6_0_cpython
  readline               pkgs/main::readline-8.1-h27cfd23_0 --> conda-forge::readline-8.1-h46c0cb4_0
  tzdata                 pkgs/main::tzdata-2021e-hda174b7_0 --> conda-forge::tzdata-2021e-he74cb21_0
  wheel                pkgs/main::wheel-0.37.0-pyhd3eb1b0_1 --> conda-forge::wheel-0.37.0-pyhd8ed1ab_1


Proceed ([y]/n)? y


Downloading and Extracting Packages
xorg-libice-1.0.10   | 58 KB     | ######################################################################################################################################################################## | 100% 
libgomp-11.2.0       | 427 KB    | ######################################################################################################################################################################## | 100% 
openh264-2.1.1       | 1.5 MB    | ######################################################################################################################################################################## | 100% 
glib-tools-2.68.4    | 86 KB     | ######################################################################################################################################################################## | 100% 
expat-2.4.1          | 182 KB    | ######################################################################################################################################################################## | 100% 
ffmpeg-4.4.1         | 10.0 MB   | ######################################################################################################################################################################## | 100% 
jsoncpp-1.9.4        | 262 KB    | ######################################################################################################################################################################## | 100% 
python-3.9.7         | 27.6 MB   | ######################################################################################################################################################################## | 100% 
pkgconfig-1.5.5      | 13 KB     | ######################################################################################################################################################################## | 100% 
pyqt5-sip-4.19.18    | 311 KB    | ######################################################################################################################################################################## | 100% 
tzdata-2021e         | 121 KB    | ######################################################################################################################################################################## | 100% 
python-dateutil-2.8. | 240 KB    | ######################################################################################################################################################################## | 100% 
zstd-1.5.0           | 490 KB    | ######################################################################################################################################################################## | 100% 
cmake-3.21.3         | 15.2 MB   | ######################################################################################################################################################################## | 100% 
fonttools-4.28.1     | 1.5 MB    | ######################################################################################################################################################################## | 100% 
_openmp_mutex-4.5    | 22 KB     | ######################################################################################################################################################################## | 100% 
boost-1.72.0         | 342 KB    | ######################################################################################################################################################################## | 100% 
pip-21.3.1           | 1.2 MB    | ######################################################################################################################################################################## | 100% 
c-ares-1.18.1        | 113 KB    | ######################################################################################################################################################################## | 100% 
pcl-1.11.1           | 20.3 MB   | ######################################################################################################################################################################## | 100% 
tk-8.6.11            | 3.3 MB    | ######################################################################################################################################################################## | 100% 
libblas-3.9.0        | 12 KB     | ######################################################################################################################################################################## | 100% 
libcurl-7.80.0       | 337 KB    | ######################################################################################################################################################################## | 100% 
libxkbcommon-1.0.3   | 581 KB    | ######################################################################################################################################################################## | 100% 
libpq-13.3           | 2.7 MB    | ######################################################################################################################################################################## | 100% 
qhull-2019.1         | 2.3 MB    | ######################################################################################################################################################################## | 100% 
libwebp-base-1.2.1   | 845 KB    | ######################################################################################################################################################################## | 100% 
libva-2.13.0         | 165 KB    | ######################################################################################################################################################################## | 100% 
ld_impl_linux-64-2.3 | 667 KB    | ######################################################################################################################################################################## | 100% 
libglu-9.0.0         | 413 KB    | ######################################################################################################################################################################## | 100% 
x264-1!161.3030      | 2.5 MB    | ######################################################################################################################################################################## | 100% 
xz-5.2.5             | 343 KB    | ######################################################################################################################################################################## | 100% 
six-1.16.0           | 14 KB     | ######################################################################################################################################################################## | 100% 
lcms2-2.12           | 443 KB    | ######################################################################################################################################################################## | 100% 
nitro-2.7.dev6       | 967 KB    | ######################################################################################################################################################################## | 100% 
libxcb-1.13          | 391 KB    | ######################################################################################################################################################################## | 100% 
libnghttp2-1.43.0    | 790 KB    | ######################################################################################################################################################################## | 100% 
laz-perf-3.0.0       | 182 KB    | ######################################################################################################################################################################## | 100% 
liblapacke-3.9.0     | 12 KB     | ######################################################################################################################################################################## | 100% 
libgcc-ng-11.2.0     | 887 KB    | ######################################################################################################################################################################## | 100% 
fontconfig-2.13.1    | 357 KB    | ######################################################################################################################################################################## | 100% 
svt-av1-0.8.7        | 2.8 MB    | ######################################################################################################################################################################## | 100% 
xorg-xextproto-7.3.0 | 28 KB     | ######################################################################################################################################################################## | 100% 
libssh2-1.10.0       | 233 KB    | ######################################################################################################################################################################## | 100% 
cycler-0.11.0        | 10 KB     | ######################################################################################################################################################################## | 100% 
xorg-libx11-1.7.2    | 941 KB    | ######################################################################################################################################################################## | 100% 
jasper-2.0.33        | 1.1 MB    | ######################################################################################################################################################################## | 100% 
librttopo-1.1.0      | 235 KB    | ######################################################################################################################################################################## | 100% 
ncurses-6.2          | 985 KB    | ######################################################################################################################################################################## | 100% 
libbrotlidec-1.0.9   | 33 KB     | ######################################################################################################################################################################## | 100% 
libffi-3.3           | 51 KB     | ######################################################################################################################################################################## | 100% 
libprotobuf-3.18.1   | 2.6 MB    | ######################################################################################################################################################################## | 100% 
mysql-common-8.0.27  | 1.8 MB    | ######################################################################################################################################################################## | 100% 
libvpx-1.11.0        | 1.1 MB    | ######################################################################################################################################################################## | 100% 
packaging-21.3       | 36 KB     | ######################################################################################################################################################################## | 100% 
boost-cpp-1.72.0     | 16.3 MB   | ######################################################################################################################################################################## | 100% 
brotli-bin-1.0.9     | 19 KB     | ######################################################################################################################################################################## | 100% 
libedit-3.1.20191231 | 121 KB    | ######################################################################################################################################################################## | 100% 
matplotlib-base-3.5. | 7.4 MB    | ######################################################################################################################################################################## | 100% 
jbig-2.1             | 43 KB     | ######################################################################################################################################################################## | 100% 
hdf5-1.12.1          | 3.5 MB    | ######################################################################################################################################################################## | 100% 
pyparsing-3.0.6      | 79 KB     | ######################################################################################################################################################################## | 100% 
libgfortran-ng-11.2. | 19 KB     | ######################################################################################################################################################################## | 100% 
ca-certificates-2021 | 139 KB    | ######################################################################################################################################################################## | 100% 
libzip-1.8.0         | 126 KB    | ######################################################################################################################################################################## | 100% 
sqlite-3.36.0        | 1.4 MB    | ######################################################################################################################################################################## | 100% 
eigen-3.3.9          | 970 KB    | ######################################################################################################################################################################## | 100% 
xorg-xproto-7.0.31   | 73 KB     | ######################################################################################################################################################################## | 100% 
pyqtwebengine-5.12.1 | 174 KB    | ######################################################################################################################################################################## | 100% 
libuv-1.42.0         | 1.0 MB    | ######################################################################################################################################################################## | 100% 
aom-3.2.0            | 5.4 MB    | ######################################################################################################################################################################## | 100% 
libspatialite-5.0.1  | 4.4 MB    | ######################################################################################################################################################################## | 100% 
libgfortran5-11.2.0  | 1.7 MB    | ######################################################################################################################################################################## | 100% 
pcre-8.45            | 253 KB    | ######################################################################################################################################################################## | 100% 
kiwisolver-1.3.2     | 80 KB     | ######################################################################################################################################################################## | 100% 
opencv-4.5.3         | 22 KB     | ######################################################################################################################################################################## | 100% 
x265-3.5             | 6.7 MB    | ######################################################################################################################################################################## | 100% 
xorg-libxrender-0.9. | 32 KB     | ######################################################################################################################################################################## | 100% 
pyqtchart-5.12       | 257 KB    | ######################################################################################################################################################################## | 100% 
mysql-devel-8.0.27   | 2.3 MB    | ######################################################################################################################################################################## | 100% 
libopencv-4.5.3      | 34.5 MB   | ######################################################################################################################################################################## | 100% 
geos-3.9.1           | 1.1 MB    | ######################################################################################################################################################################## | 100% 
libcblas-3.9.0       | 12 KB     | ######################################################################################################################################################################## | 100% 
freetype-2.10.4      | 890 KB    | ######################################################################################################################################################################## | 100% 
xorg-libxi-1.7.10    | 46 KB     | ######################################################################################################################################################################## | 100% 
xorg-libxau-1.0.9    | 13 KB     | ######################################################################################################################################################################## | 100% 
gnutls-3.6.13        | 2.0 MB    | ######################################################################################################################################################################## | 100% 
glib-2.68.4          | 447 KB    | ######################################################################################################################################################################## | 100% 
numpy-1.21.4         | 6.2 MB    | ######################################################################################################################################################################## | 100% 
kealib-1.4.14        | 186 KB    | ######################################################################################################################################################################## | 100% 
zlib-1.2.11          | 86 KB     | ######################################################################################################################################################################## | 100% 
hdf4-4.2.15          | 950 KB    | ######################################################################################################################################################################## | 100% 
xorg-libxfixes-5.0.3 | 18 KB     | ######################################################################################################################################################################## | 100% 
gmp-6.2.1            | 806 KB    | ######################################################################################################################################################################## | 100% 
mysql-server-8.0.27  | 19.6 MB   | ######################################################################################################################################################################## | 100% 
flann-1.9.1          | 39.9 MB   | ######################################################################################################################################################################## | 100% 
nss-3.72             | 2.1 MB    | ######################################################################################################################################################################## | 100% 
libstdcxx-ng-11.2.0  | 4.2 MB    | ######################################################################################################################################################################## | 100% 
pdal-2.3.0           | 5.2 MB    | ######################################################################################################################################################################## | 100% 
pthread-stubs-0.4    | 5 KB      | ######################################################################################################################################################################## | 100% 
matplotlib-3.5.0     | 6 KB      | ######################################################################################################################################################################## | 100% 
mysql-8.0.27         | 387 KB    | ######################################################################################################################################################################## | 100% 
pyqt-5.12.3          | 22 KB     | ######################################################################################################################################################################## | 100% 
libvorbis-1.3.7      | 280 KB    | ######################################################################################################################################################################## | 100% 
_libgcc_mutex-0.1    | 3 KB      | ######################################################################################################################################################################## | 100% 
draco-1.4.3          | 1.3 MB    | ######################################################################################################################################################################## | 100% 
liblapack-3.9.0      | 12 KB     | ######################################################################################################################################################################## | 100% 
tiledb-2.3.4         | 4.1 MB    | ######################################################################################################################################################################## | 100% 
libtiff-4.3.0        | 614 KB    | ######################################################################################################################################################################## | 100% 
pillow-8.4.0         | 706 KB    | ######################################################################################################################################################################## | 100% 
libglib-2.68.4       | 3.0 MB    | ######################################################################################################################################################################## | 100% 
wheel-0.37.0         | 31 KB     | ######################################################################################################################################################################## | 100% 
libllvm11-11.1.0     | 29.1 MB   | ######################################################################################################################################################################## | 100% 
openssl-1.1.1l       | 2.1 MB    | ######################################################################################################################################################################## | 100% 
libntlm-1.4          | 32 KB     | ######################################################################################################################################################################## | 100% 
gettext-0.19.8.1     | 3.6 MB    | ######################################################################################################################################################################## | 100% 
giflib-5.2.1         | 77 KB     | ######################################################################################################################################################################## | 100% 
nettle-3.6           | 6.5 MB    | ######################################################################################################################################################################## | 100% 
cgal-cpp-5.0.1       | 5.7 MB    | ######################################################################################################################################################################## | 100% 
openjpeg-2.4.0       | 444 KB    | ######################################################################################################################################################################## | 100% 
psutil-5.8.0         | 343 KB    | ######################################################################################################################################################################## | 100% 
proj-8.0.1           | 3.1 MB    | ######################################################################################################################################################################## | 100% 
lerc-3.0             | 216 KB    | ######################################################################################################################################################################## | 100% 
krb5-1.19.2          | 1.4 MB    | ######################################################################################################################################################################## | 100% 
libzlib-1.2.11       | 59 KB     | ######################################################################################################################################################################## | 100% 
libbrotlienc-1.0.9   | 286 KB    | ######################################################################################################################################################################## | 100% 
xorg-libxdmcp-1.1.3  | 19 KB     | ######################################################################################################################################################################## | 100% 
cgal-5.0.1           | 8.2 MB    | ######################################################################################################################################################################## | 100% 
xorg-renderproto-0.1 | 9 KB      | ######################################################################################################################################################################## | 100% 
geotiff-1.6.0        | 299 KB    | ######################################################################################################################################################################## | 100% 
poppler-data-0.4.11  | 3.6 MB    | ######################################################################################################################################################################## | 100% 
libnsl-2.0.0         | 31 KB     | ######################################################################################################################################################################## | 100% 
libkml-1.3.0         | 640 KB    | ######################################################################################################################################################################## | 100% 
cairo-1.16.0         | 1.5 MB    | ######################################################################################################################################################################## | 100% 
olefile-0.46         | 32 KB     | ######################################################################################################################################################################## | 100% 
lz4-c-1.9.3          | 179 KB    | ######################################################################################################################################################################## | 100% 
mysql-client-8.0.27  | 27.5 MB   | ######################################################################################################################################################################## | 100% 
gst-plugins-base-1.1 | 2.6 MB    | ######################################################################################################################################################################## | 100% 
cfitsio-3.470        | 1.3 MB    | ######################################################################################################################################################################## | 100% 
xerces-c-3.2.3       | 1.8 MB    | ######################################################################################################################################################################## | 100% 
xorg-fixesproto-5.0  | 9 KB      | ######################################################################################################################################################################## | 100% 
xorg-libsm-1.2.3     | 26 KB     | ######################################################################################################################################################################## | 100% 
tzcode-2021e         | 69 KB     | ######################################################################################################################################################################## | 100% 
libuuid-2.32.1       | 28 KB     | ######################################################################################################################################################################## | 100% 
alsa-lib-1.2.3       | 560 KB    | ######################################################################################################################################################################## | 100% 
mesalib-18.3.1       | 11.4 MB   | ######################################################################################################################################################################## | 100% 
harfbuzz-3.0.0       | 2.0 MB    | ######################################################################################################################################################################## | 100% 
json-c-0.15          | 274 KB    | ######################################################################################################################################################################## | 100% 
xorg-libxext-1.3.4   | 54 KB     | ######################################################################################################################################################################## | 100% 
mysql-libs-8.0.27    | 1.9 MB    | ######################################################################################################################################################################## | 100% 
certifi-2021.10.8    | 145 KB    | ######################################################################################################################################################################## | 100% 
setuptools-59.1.1    | 1.0 MB    | ######################################################################################################################################################################## | 100% 
icu-68.2             | 13.1 MB   | ######################################################################################################################################################################## | 100% 
rhash-1.4.1          | 192 KB    | ######################################################################################################################################################################## | 100% 
freeglut-3.2.1       | 161 KB    | ######################################################################################################################################################################## | 100% 
cyrus-sasl-2.1.27    | 228 KB    | ######################################################################################################################################################################## | 100% 
curl-7.80.0          | 153 KB    | ######################################################################################################################################################################## | 100% 
xorg-kbproto-1.0.7   | 27 KB     | ######################################################################################################################################################################## | 100% 
libpng-1.6.37        | 306 KB    | ######################################################################################################################################################################## | 100% 
libdap4-3.20.6       | 11.3 MB   | ######################################################################################################################################################################## | 100% 
dbus-1.13.6          | 572 KB    | ######################################################################################################################################################################## | 100% 
py-opencv-4.5.3      | 1.1 MB    | ######################################################################################################################################################################## | 100% 
libdeflate-1.8       | 67 KB     | ######################################################################################################################################################################## | 100% 
libxml2-2.9.12       | 772 KB    | ######################################################################################################################################################################## | 100% 
libclang-11.1.0      | 19.2 MB   | ######################################################################################################################################################################## | 100% 
libgdal-3.3.2        | 13.3 MB   | ######################################################################################################################################################################## | 100% 
laszip-3.4.3         | 185 KB    | ######################################################################################################################################################################## | 100% 
pyqt-impl-5.12.3     | 5.9 MB    | ######################################################################################################################################################################## | 100% 
nspr-4.32            | 233 KB    | ######################################################################################################################################################################## | 100% 
munkres-1.1.4        | 12 KB     | ######################################################################################################################################################################## | 100% 
pixman-0.40.0        | 627 KB    | ######################################################################################################################################################################## | 100% 
gdal-3.3.2           | 1.8 MB    | ######################################################################################################################################################################## | 100% 
gstreamer-1.18.5     | 2.0 MB    | ######################################################################################################################################################################## | 100% 
libiconv-1.16        | 1.4 MB    | ######################################################################################################################################################################## | 100% 
postgresql-13.3      | 5.3 MB    | ######################################################################################################################################################################## | 100% 
libopenblas-0.3.18   | 9.6 MB    | ######################################################################################################################################################################## | 100% 
libev-4.33           | 104 KB    | ######################################################################################################################################################################## | 100% 
lame-3.100           | 496 KB    | ######################################################################################################################################################################## | 100% 
pkg-config-0.29.2    | 120 KB    | ######################################################################################################################################################################## | 100% 
mpfr-4.1.0           | 2.6 MB    | ######################################################################################################################################################################## | 100% 
libogg-1.3.4         | 206 KB    | ######################################################################################################################################################################## | 100% 
libpciaccess-0.16    | 37 KB     | ######################################################################################################################################################################## | 100% 
xorg-inputproto-2.3. | 19 KB     | ######################################################################################################################################################################## | 100% 
readline-8.1         | 295 KB    | ######################################################################################################################################################################## | 100% 
freexl-1.0.6         | 48 KB     | ######################################################################################################################################################################## | 100% 
libdrm-2.4.108       | 284 KB    | ######################################################################################################################################################################## | 100% 
graphite2-1.3.13     | 102 KB    | ######################################################################################################################################################################## | 100% 
qt-5.12.9            | 99.5 MB   | ######################################################################################################################################################################## | 100% 
libbrotlicommon-1.0. | 65 KB     | ######################################################################################################################################################################## | 100% 
bzip2-1.0.8          | 484 KB    | ######################################################################################################################################################################## | 100% 
jpeg-9d              | 264 KB    | ######################################################################################################################################################################## | 100% 
libnetcdf-4.8.1      | 1.5 MB    | ######################################################################################################################################################################## | 100% 
python_abi-3.9       | 4 KB      | ######################################################################################################################################################################## | 100% 
poppler-21.03.0      | 15.9 MB   | ######################################################################################################################################################################## | 100% 
libopus-1.3.1        | 255 KB    | ######################################################################################################################################################################## | 100% 
libevent-2.1.10      | 1.1 MB    | ######################################################################################################################################################################## | 100% 
brotli-1.0.9         | 18 KB     | ######################################################################################################################################################################## | 100% 
tornado-6.1          | 646 KB    | ######################################################################################################################################################################## | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
