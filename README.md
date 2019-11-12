# dlib

Projects using dlib

For all the time I've practiced Computer Vision (hardly one and a half year), I've had the most fun working with dlib.
Installing it on my pc was a real pain, and I credit it for making me realise the importance of virtual environments. Dlib has a lot of dependencies, and it's fairly tough to get down with all. But going through this 'tough time installing' is definitely worth it. Dlib has a lot of state-of-the-art implementations including my favorite, facial landmarks detection.

I usually work with Python3 on my Mac, so, getting forward to installing dlib on MacOS:

----------------------------------------------------------------------------------------------------------------------------

Dlib has the following prerequisites: Boost, Boost.Python, CMake, XQuartz Windows Manager. These packages can be installed using HomeBrew (preferable) on MacOS.

- Update Brew
$ brew update

- Install CMake, Boost, and Boost.Python
$ brew install cmake
$ brew install boost
$ brew install boost-python --with-python3

- Download and install XQuartz Window Manager from the link: https://www.xquartz.org/

- As I mentioned earlier, I'll be creating a separate virtual environment for my dlib projects (I use the conda environment)
$ conda create -n env_dlib python=3.7
$ conda activate env_dlib

- Installing necessary libraries inside the environment
$ pip install opencv-contrib-python
$ pip install numpy
$ pip install scipy
$ pip install scikit-image

$ pip install dlib

- Test your dlib installation
$ python3
>>> import dlib
>>>

----------------------------------------------------------------------------------------------------------------------------






