cd ../lv_micropython/ports/unix/
make USER_C_MODULES=../../../user_c_module clean
# echo -n "Copy Micropython to path directory  ->"
#cp -v ./build-standard/micropython `which micropython`
#ls -l `which micropython`