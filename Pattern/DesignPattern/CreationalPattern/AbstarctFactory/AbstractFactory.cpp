#include <iostream>

class ProductA
{
public:
    virtual ~ProductA() {}
    
    virtual const char* getName() = 0;
};

class ConcreateProductAX : public ProductA
{
public:
  ~ConcreateProductAX() {}
  
  const char* getName()
  {
    return "A-X";
  }
};

class ConcreateProductAY : public ProductA
{
public:
  ~ConcreateProductAY() {}
  
  const char* getName()
  {
    return "A-Y";
  }
};



class ProductB
{
public:
  virtual ~ProductB() {}
  
  virtual const char* getName() = 0;
};

class ConcreateProductBX : public ProductB
{
public:
  ~ConcreateProductBX () {}
  
  const char* getName()
  {
    return "B-X";
  }
};

class ConcreateProductBY : public ProductB
{
public:
  ~ConcreateProductBY () {}
  
  const char* getName()
  {
    return "B-Y";
  }
};

class AbstractFactory
{
public:
  virtual ~AbstractFactory() {}
  
  virtual ProductA *createProductA() = 0;
  virtual ProductB *createProductB() = 0;
};

class ConcreateFactoryX : public AbstractFactory
{
public:
  ~ConcreateFactoryX() {}
  
  ProductA *createProductA()
  {
    return new ConcreateProductAX();
  }

  ProductB *createProductB()
  {
    return new ConcreateProductBX();
  }
};

class ConcreateFactoryY : public AbstractFactory
{
public:
  ~ConcreateFactoryY() {}
  
  ProductA *createProductA()
  {
    return new ConcreateProductAY();
  }
  
  ProductB *createProductB()
  {
    return new ConcreateProductBY();
  }
};

int main()
{
  ConcreateFactoryX *factoryX = new ConcreateFactoryX();
  ConcreateFactoryY *factoryY = new ConcreateFactoryY();

  ProductA *p1 = factoryX -> createProductA();
  std::cout << "Product: " << p1->getName() << std::endl;

  ProductB *p2 = factoryX -> createProductB();
  std::cout << "Product: " << p2->getName() << std::endl;

  delete p1;
  delete p2;

  delete factoryX;
  delete factoryY;

  return 0;
}