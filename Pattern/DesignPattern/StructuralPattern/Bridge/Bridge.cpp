#include <iostream>
using namespace std;

class Implementor
{
public:
 virtual ~Implementor() {}
 virtual void action() = 0;
};

class ConcreateImplementorA : public Implementor
{
public:
  ~ ConcreateImplementorA (){}
  
  void action()
  {
    cout << "Create by ConcreateImplementorA" << endl;
  }
};

class ConcreateImplementorB : public Implementor 
{
public:
  ~ConcreateImplementorB (){}
  
  void action()
  {
    cout << "Create by ConcreateImplementorB" << endl;
  }
};

class Abstraction
{
public:
    virtual ~Abstraction () {}
    virtual void operation () = 0;
};

class Bridge : public Abstraction
{
public:
  ~Bridge () {}
  Bridge(Implementor * impl) : implementor(impl){};
  
  void operation()
  {
    implementor->action();
  }

private:
  Implementor *implementor;
};

int main()
{
 Implementor *ia = new ConcreateImplementorA;
 Implementor *ib = new ConcreateImplementorB;
 
 Abstraction *abstraction1 = new Bridge(ia);
 abstraction1->operation();
 Abstraction *abstraction2 = new Bridge(ib);
 abstraction2->operation();

 delete ia;
 delete ib;
 delete abstraction1;
 delete abstraction2;

 return 0;
}