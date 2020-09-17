#include <kunai/kunai.hpp>
#include <kunai/path.hpp>
#include <iostream>

int main() {
  std::string mpath = path::join(path::getCwd(), "../../test/test.cpp");
  std::cout << mpath << "\n";
  return 0;
}