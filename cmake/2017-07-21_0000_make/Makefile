

# iEdit: $(patsubst %.cpp,%.o,$(wildcard *.cpp))
# 	g++ $^ -o $@ 
# 
# %.o: %.cpp
# 	g++ -c -MD $<
# 
# include $(wildcard *.d) 

source_dirs := . Editor TextLine $(STD_PLUS_DIR)/include

search_wildcards := $(addsuffix /*.cpp,$(source_dirs)) 

iEdit: $(notdir $(patsubst %.cpp,%.o,$(wildcard $(search_wildcards))))
	i686-w64-mingw32-g++ -std=c++1y $^ -o $@ 

VPATH := $(source_dirs)
 
%.o: %.cpp
	i686-w64-mingw32-g++ -std=c++1y -c -MD $(addprefix -I,$(source_dirs)) $<

include $(wildcard *.d) 


.PHONY : clean
clean :
	rm *.exe *.d *.o