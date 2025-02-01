#include <iostream>

using namespace std;

class Animal
{
public:
  virtual void walk(){
    cout << "Animal Walk" << endl;
  }
};

class Fish
{
public:
  virtual void swim(){
    cout << "Fish Swmming" << endl;
  }
};

class FishAdpater : public Animal, private Fish
{
public:
  virtual void walk()
  {
  swim();  
  }
};

void makeWalk(Animal& animal){
    animal.walk();
}

int main()
{
    FishAdpater adapter;
    
    makeWalk(adapter);

    return 0;
}