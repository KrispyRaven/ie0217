TARGET = menu.exe

#C0mipilador
CXX = g++

#opciones de compilado
CXXFLAGS = -Wall 

#Archivos fuente
SOURCES = main.cpp student.cpp


OBJECTS = $(SOURCES:.cpp=.exe)

%.exe: %.cpp

	$(CXX) $(CXXFLAGS) -c $< -o $@

$(TARGET): $(OBJECTS)

	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJECTS)


all: $(TARGET) run clean

run: 
	./$(TARGET)



.PHONY: clean	



clean:
	del $(TARGET) $(OBJECTS)