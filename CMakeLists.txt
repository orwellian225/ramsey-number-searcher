cmake_minimum_required(VERSION 3.16)

project(RNS DESCRIPTION "Ramsey Number Searcher - a tool to search for Ramsey Numbers" LANGUAGES CXX)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
add_subdirectory(lib/fmt)

add_executable(rns src/main.cpp)
target_include_directories(rns PUBLIC include PUBLIC lib/fmt/include)
target_link_directories(rns PRIVATE src lib/fmt/src)
target_link_libraries(rns fmt)