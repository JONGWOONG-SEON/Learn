#include <iostream>
#include <string>

using namespace std;

class Product
{
public:
  void makeA( const string &part )
  {
    partA = part;
  }
  void makeB( const string &part )
  {
    partB = part;
  }
  void makeC ( const string &part )
  {
    partC = part;
  }
  string get()
  {
    return (partA + " " + partB + " " + partC);
  }

private:
  string partA;
  string partB;
  string partC;
};

class Builder
{
public:
  virtual ~Builder() {}

  Product get()
  {
    return product;
  }
  virtual void buildPartA() = 0;
  virtual void buildPartB() = 0;
  virtual void buildPartC() = 0;

protected:
  Product product;
};

class ConcreateBuilderX : public Builder
{
public:
  void buildPartA()
  {
    product.makeA( "A-X" );
  }
  void buildPartB()
  {
    product.makeB( "B-X" );
  }
  void buildPartC()
  {
    product.makeC( "C-X" );
  } 
};

class ConcreateBuilderY : public Builder
{
public:
  void buildPartA()
  {
    product.makeA( "A-Y" );
  }
  void buildPartB()
  {
    product.makeB( "B-Y" );
  }
  void buildPartC()
  {
    product.makeC( "C-Y" );
  } 
};


class Director {
public:
  Director() : builder() {}
  
  ~Director()
  {
    if (builder)
    {
        delete builder;
    }
  }

  void set( Builder *b )
  {
    if (builder)
    {
        delete builder;
    }
    builder = b;
  }
  
  Product get()
  {
    return builder->get();
  }
  
  void construct()
  {
    builder->buildPartA();
    builder->buildPartB();
    builder->buildPartC();
  }

private:
  Builder *builder;

};


int main()
{
  Director director;
  director.set( new ConcreateBuilderX );
  director.construct();
  
  Product product1 = director.get();
  cout << "1st product parts: " << product1.get() << endl;
  
  director.set( new ConcreateBuilderY );
  director.construct();
  
  Product product2 = director.get();
  cout << "2nd product parts: " << product2.get() << endl;
  
  return 0;
};