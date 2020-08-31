# data-science
Exercises from `Data Science from Scratch` First Editiion (2015) by Joel Grus.  
However, there is a second edition of the book where all the examples are updated to require at least Python 3.6. `https://github.com/joelgrus/data-science-from-scratch`

The initial checkin of the code is from 2016.  That was the first attempt and I think there was a second attempt during the intervening years between then and now.  It is a good time as any to finally go through this book and learn something.  So hopefully, the third time is a charm!

## Running Graphical Applications in WSL2
Reference: https://medium.com/@shaoyenyu/make-matplotlib-works-correctly-with-x-server-in-wsl2-9d9928b4e36a

- Download XLaunch: https://sourceforge.net/projects/vcxsrv/
It’s important to check the “Disable access control” to allow connection from WSL2
TODO: Figure out how to configure Windows Defender so PUBLIC connections from WSL2 / Ubuntu can connect to XServer running on Windows

Add the following to .bashrc
- `export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0`
- `export LIBGL_ALWAYS_INDIRECT=1`