TARGET = menu.exe

#C0mipilador
CXX = g++

#opciones de compilado
CXXFLAGS = -Wall 

#Archivos fuente
SOURCES = main.cpp function.cpp largadefinicion.cpp definicion.cpp


OBJECTS = $(SOURCES:.cpp=.exe)

%.exe: %.cpp

	$(CXX) $(CXXFLAGS) -c $< -o $@

$(TARGET): $(OBJECTS)

	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJECTS)

.PHONY: clean	

clean:
	del $(TARGET) $(OBJECTS).PHONY: clean all


