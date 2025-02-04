## 디자인 패턴 (Design Patterns)

소프트웨어 디자인 패턴은 객체 지향 설계 환경에서 반복적으로 발생하는 문제들에 대한  
일반적인 재사용 가능한 해결책입니다.  
디자인 패턴은 직접 소스 코드로 변환될 수 있는 완성된 설계가 아니라,  
문제를 해결하는 방법에 대한 **템플릿(template)** 역할을 합니다.  

디자인 패턴은 목적에 따라 다음 세 가지로 분류할 수 있습니다.  
- **생성 패턴(Creational Patterns)**: 객체의 인스턴스화 과정을 추상화함  
- **구조 패턴(Structural Patterns)**: 클래스와 객체가 더 큰 구조를 형성하는 방법을 정의함  
- **행동 패턴(Behavioral Patterns)**: 객체 간의 책임 할당 및 상호작용을 정의함  

---

### **📌 생성 패턴 (Creational Patterns)**  
- **[추상 팩토리(Abstract Factory)]**: 연관된 제품 객체들의 패밀리를 생성  
- **[빌더(Builder)]**: 복합 객체의 생성 방법을 정의  
- **[팩토리 메서드(Factory Method)]**: 인스턴스화할 객체의 하위 클래스를 결정  
- **[프로토타입(Prototype)]**: 생성할 객체의 클래스를 결정  
- **[싱글턴(Singleton)]**: 클래스의 유일한 인스턴스를 제공  

---

### **📌 구조 패턴 (Structural Patterns)**  
- **[어댑터(Adapter)]**: 객체의 인터페이스 변환  
- **[브리지(Bridge)]**: 객체의 구현을 분리  
- **[컴포지트(Composite)]**: 객체의 구조 및 구성  
- **[데코레이터(Decorator)]**: 서브클래싱 없이 객체의 기능 확장  
- **[퍼사드(Façade)]**: 서브시스템에 대한 단순한 인터페이스 제공  
- **[플라이웨이트(Flyweight)]**: 객체의 저장 비용 절감  
- **[프록시(Proxy)]**: 객체의 접근 및 위치 관리  

---

### **📌 행동 패턴 (Behavioral Patterns)**  
- **[책임 연쇄(Chain of Responsibility)]**: 요청을 처리할 객체 결정  
- **[커맨드(Command)]**: 요청의 실행 시점과 방법 정의  
- **[인터프리터(Interpreter)]**: 언어의 문법과 해석 방법 정의  
- **[이터레이터(Iterator)]**: 컬렉션의 요소 순회 방법 정의  
- **[미디에이터(Mediator)]**: 객체 간의 상호작용 조정  
- **[메멘토(Memento)]**: 객체 외부에 저장되는 정보 및 시점 정의  
- **[옵서버(Observer)]**: 객체 간의 종속 관계 유지  
- **[상태(State)]**: 객체의 상태 변화 관리  
- **[전략(Strategy)]**: 알고리즘 선택 및 변경 가능  
- **[템플릿 메서드(Template Method)]**: 알고리즘의 단계 정의  
- **[방문자(Visitor)]**: 클래스 변경 없이 새로운 연산 추가 


### References

* [Design Patterns by The "Gang of Four"]
* [Head First: Design Patterns]
* [Wikipedia]

[Design Patterns by The "Gang of Four"]: https://en.wikipedia.org/wiki/Design_Patterns
[Head First: Design Patterns]: http://www.headfirstlabs.com/books/hfdp/ 
[Wikipedia]: https://en.wikipedia.org/wiki/Software_design_pattern

[추상 팩토리(Abstract Factory)]: https://github.com/JONGWOONG-SEON/Learn/tree/master/Pattern/DesignPattern/CreationalPattern/AbstarctFactory
[어댑터(Adapter)]: https://github.com/JONGWOONG-SEON/Learn/tree/master/Pattern/DesignPattern/StructuralPattern/Adapter
[책임 연쇄(Chain of Responsibility)]: https://github.com/JONGWOONG-SEON/Learn/tree/master/Pattern/DesignPattern/BehavioralPattern/ChainofResponsibility
[빌더(Builder)]: https://github.com/JONGWOONG-SEON/Learn/tree/master/Pattern/DesignPattern/CreationalPattern/Builder
[브리지(Bridge)]:https://github.com/JONGWOONG-SEON/Learn/tree/master/Pattern/DesignPattern/StructuralPattern/Bridge
[커맨드(Command)]:https://github.com/JONGWOONG-SEON/Learn/tree/master/Pattern/DesignPattern/BehavioralPattern/Command