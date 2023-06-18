default:
	g++ src/*.cpp -o stbipy/bin/stb_image.dll -Iinclude -shared -static -static-libstdc++ -static-libgcc